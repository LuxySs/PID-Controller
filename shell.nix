{ pkgs ? import <nixpkgs> {} }:
  pkgs.mkShell {
    nativeBuildInputs = with pkgs.buildPackages; [
        python3
        python3Packages.matplotlib
        python3Packages.numpy
        python3Packages.pandas
    ];
}

