#!/usr/bin/python

#Weather by IP address must recieve an IP address as an arguement, gather the zip code for that IP, then gather and display the weather for that zip code.

import urllib
from xml.dom import minidom

#should return the location associated with the IP address it is passed.
#loc should be in a form that google ig weather api can understand. (city or zip) 
def locOf( ip ):
  apiCall = "http://api.hostip.info/?ip=" + ip
  connection = urllib.urlopen(apiCall)
  loc = minidom.parse(connection)
  return loc

#should return weather information for the location given as an XML dom object.
def weatherOf( loc ):
  apiCall = "http://www.google.com/ig/api/?weather=" + loc
  connection = urllib.urlopen(apiCall)
  weather = connection.read()
  return weather

ip = raw_input("input IP to look up: ")
loc = locOf( ip )

print loc
