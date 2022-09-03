let
    pkgs = (import (builtins.fetchTarball {
        url = "https://github.com/NixOS/nixpkgs/archive/067d5d5b89133efcda060bba31f9941c6396e3ee.zip";
        sha256 = "0wyrwrw5fr5b1ss2za37cgwk7hzydy184a49wbqrks5vhpjvfkg7";
    }) { });
    stdenv = pkgs.stdenv;
in pkgs.mkShell rec {
    name = "waasu";
    shellHook = ''
        source .bashrc
    '';
    buildInputs = (with pkgs; [
        bashInteractive
        (pkgs.python3.buildEnv.override {
            ignoreCollisions = true;
            extraLibs = with pkgs.python3.pkgs; [
                ipython
                beautifulsoup4
                requests
                lxml
                selenium
                chromedriver
                python39Packages.ipdb
            ];
        })
    ]);
}


