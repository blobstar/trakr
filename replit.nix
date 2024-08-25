{pkgs}: {
  deps = [
    pkgs.bfg-repo-cleaner
    pkgs.pkg-config
    pkgs.mysql-client
    pkgs.python3
    pkgs.python3Packages.mysqlclient
  ];
}
