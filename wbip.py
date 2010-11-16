#!/usr/bin/python -tt

#Weather by IP address must recieve an IP address as an arguement, gather the zip code for that IP, then gather and display the weather for that zip code.

import urllib
from xml.dom import minidom

#should return the location associated with the IP address it is passed.
#loc should be in a form that google ig weather api can understand. (city or zip) 
def locOf( ip ):
  apiCall = "http://api.hostip.info/?ip=" + ip
  apiResponse = urllib.urlopen(apiCall)
  hostip = minidom.parse(apiResponse)
  hostipNames = hostip.getElementsByTagName("gml:name")
  loc = hostipNames[1].firstChild.data
  return loc

#should return weather information for the location given as an XML dom object.
def weatherOf( loc ):
  apiCall = "http://www.google.com/ig/api?weather=" + loc
  apiResponse = urllib.urlopen(apiCall)
  weatherDom = minidom.parse(apiResponse)
  weatherDomTags = weatherDom.getElementsByTagName('condition')
  for tag in weatherDomTags:
    print tag.attributes   

ip = "8.8.8.8"
loc = locOf( ip )
weather = weatherOf( loc )

print "\n\n" + loc, weather

#tests
print "\n\nTests:"

#should return Mounain View, CA
if locOf("8.8.8.8") == "Mountain View, CA":
  print "locOf( ip ) PASS"
else:
  print "locOf( ip ) FAIL"

#add white space to give results some room
print "\n\n"
