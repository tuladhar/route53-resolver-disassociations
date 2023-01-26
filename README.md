# route53-resolver-disassociations
A script to disassociate route53 resolver rules from provided VPC IDs

## Use cases
- Quickly disassociate route53 resolver rules associated to the VPC(s) in bulk.

## Usage

### Step 1. Install Nix: the package manager [from here](https://nixos.org/download.html#download-nix)

### Step 2. Clone the repository
```
git clone https://github.com/tuladhar/route53-resolver-disassociations
```

### Step 3. Start nix-shell

The file `shell.nix` contains Python and related dependecies needed for the script.
```
nix-shell
```

### Step 4. Execute the script
```
python3 src/disassociate.py vpc-061c02becd1630c9c,vpc-0880368327804d479
```

## Example

### Step 1. Export the AWS profile name as environment variable
```
export AWS_PROFILE=XYZ
```

### Step 2. Execute the script with VPC ID(s)
```
[nix-shell:~/route53-resolver-disassociations]$ python src/disassociate.py
Usage: python3 src/disassociate.py [VPC_IDS,VPC_IDS,...]

Example:
    python3 src/disassociate.py vpc-061c02becd1630c9c,vpc-0880368327804d479
```
