{ pkgs ? import <nixpkgs> {} # import nixpkgs package set
}:
pkgs.mkShell {
    name="dev-env";
    buildInputs = [
        pkgs.python3
        pkgs.python3Packages.ipython
        pkgs.python3Packages.virtualenv
        pkgs.python3Packages.boto3
    ];
    shellHook = ''
        echo "Dev env started!"
    '';
}