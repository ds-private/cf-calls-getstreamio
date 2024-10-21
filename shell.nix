{ pkgs ? import <nixpkgs> {} }:

(pkgs.buildFHSEnv {
  name = "cf-calls-getstreamio";
  targetPkgs = pkgs: (with pkgs; [
    libz
    rye
    python3
    nodejs_20
  ]);
  runScript = "fish";
}).env
