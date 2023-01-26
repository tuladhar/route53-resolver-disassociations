import boto3
import time, sys, os

resolver = None

def paginate_through_all_resolver_rule_associations(vpc_ids=[], starting_token=None):    
    filters = [{'Name': 'VPCId','Values': vpc_ids}]
    try:
        paginator = resolver.get_paginator('list_resolver_rule_associations')
        response_iterator = paginator.paginate(
            Filters=filters,
            PaginationConfig={
                'MaxItems': 100,
                'PageSize': 100,
                'StartingToken': starting_token
            }
        )
        return response_iterator
    except Exception as e:
      raise Exception("Unexpected error: " + e.__str__())

def get_resolver_rule_associations_by_vpc_ids(vpc_ids=[]):
    associations = []
    next_token = None
    should_paginate = True
    while should_paginate:
        response_iterator = paginate_through_all_resolver_rule_associations(vpc_ids=vpc_ids, starting_token=next_token)
        for response in response_iterator:
            next_token = response.get('NextToken')
            associations += response.get('ResolverRuleAssociations')
        if next_token == None:
            should_paginate = False
            break
    return associations

def show_usage():
    print('Usage: python3 {} [VPC_IDS,VPC_IDS,...]'.format(sys.argv[0]))
    print('')
    print('Example:')
    print('    python3 {} vpc-061c02becd1630c9c,vpc-0880368327804d479'.format(sys.argv[0]))
    sys.exit(1)

def main():
    global resolver

    profile_name = os.environ.get('AWS_PROFILE', False)

    if len(sys.argv) != 2 or not profile_name:
        show_usage()

    session = boto3.Session(profile_name=profile_name)
    resolver = session.client('route53resolver')
    
    vpc_ids = [vpc_id.strip() for vpc_id in sys.argv[1].split(',')]
    print('VPC IDs: {}'.format(vpc_ids))

    associations = get_resolver_rule_associations_by_vpc_ids(vpc_ids)
    print('Total associations: {}'.format(len(associations)))

    for association in associations:
        vpcid, rrid = association.get('VPCId'), association.get('ResolverRuleId')
        print('Disassociating: {}'.format(association))
        try:
            response = resolver.disassociate_resolver_rule(
                VPCId=vpcid,
                ResolverRuleId=rrid
            )
        except Exception as e:
            print('... error: {}'.format(e))

if __name__ == '__main__':
    main()

