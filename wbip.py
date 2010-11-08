#!/usr/bin/python

#Weather by IP address must recieve an IP address as an arguement, gather the zip code for that IP, then gather and display the weather for that zip code.

import urllib
from xml.dom import minidom

#cityOf should return the zip code associated with the IP address it is passed. 
def locOf( ip ):
  apiCall = "http://api.hostip.info/?ip=" + ip
  apiResponse = urllib.urlopen(apiCall)
  loc = minidom.parse(apiResponse)
  return loc

def weatherOf( loc ):
  apiCall = "http://www.google.com/ig/api/?weather=" + loc
  apiResponse = urllib.urlopen(apiCall)
  weather = minidom.parse(apiResponse)
  return weather

ip = raw_input("input IP to look up: ")
loc = locOf( ip )

print loc
