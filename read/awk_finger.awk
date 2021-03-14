BEGIN {
  NetService = "/inet/tcp/0/localhost/finger"
  print "geoptus"
  while ((NetService |& getline) > 0)
    print $0
  close(NetService)
}
