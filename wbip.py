#!/usr/bin/python

#Weather by IP address must recieve an IP address as an arguement, gather the zip code for that IP, then gather and display the weather for that zip code.

import urllib

#cityOf should return the zip code associated with the IP address it is passed. 
def locOf( ip ):
  apiCall = "http://api.hostip.info/?ip=" + ip
  connection = urllib.urlopen(apiCall)
  loc = connection.read()
  print loc

locOf( raw_input("input IP to look up: ") )
