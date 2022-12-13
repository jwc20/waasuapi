let
    pkgs = (import (builtins.fetchTarball {
        url = "https://github.com/NixOS/nixpkgs/archive/7b9eeb856cbf976482fa8d1cb295ea03fb3e1277.zip";
        sha256 = "19lp4nlv97dz64sm5cb92gfq0gxqdlcrc7ykfvlq9j0w740nkng5";
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
                python39Packages.ipdb
                fake-useragent
                pprintpp
            ];
        })
    ]);
}


