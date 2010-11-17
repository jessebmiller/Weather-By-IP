#!/usr/bin/python -tt

#Weather by IP address must recieve an IP address as an arguement, gather the zip code for that IP, then gather and display the weather for that zip code.

import sys
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
  currentConditions = weatherDom.getElementsByTagName('current_conditions')
  return currentConditions[0].firstChild.attributes['data'].value

def main():
  if len(sys.argv) != 2:
    print 'usage: python wbip.py ip-to-check'
    sys.exit(1)

  ip = sys.argv[1]
  print "the current weather conditions at IP:", ip, "are", weatherOf( locOf(ip) )+'.'

  
if __name__ == '__main__':
  main()

