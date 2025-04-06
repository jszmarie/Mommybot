{ pkgs }: {
  deps = [
    pkgs.python310
    pkgs.python310Packages.discordpy
    pkgs.python310Packages.requests
  ];
}
