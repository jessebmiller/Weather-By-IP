#!/usr/bin/python -tt

#Weather by IP address must recieve an IP address as an arguement, gather the zip code for that IP, then gather and display the weather for that zip code.

import re
import sys
import urllib
from xml.dom import minidom

#returns the location associated with the IP address it is passed.
#loc should be in a form that google ig weather api can understand. (city or zip) 
def locOf( ip ):
  apiCall = "http://api.hostip.info/?ip=" + ip
  apiResponse = urllib.urlopen(apiCall)
  hostip = minidom.parse(apiResponse)
  hostipNames = hostip.getElementsByTagName("gml:name")
  loc = hostipNames[1].firstChild.data
  return loc

#returns weather information according to the google ig weather api for the location given as an XML dom object.
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
    
  #verify that the arguement is in fact an IP address
  print sys.argv[1]
  match = re.search( '\d+\.\d+\.\d+\.\d+' , sys.argv[1])   #pull out of the passed arguement an IP like pattern
  if match:                #if that pattern is the passed arguement, assume it is an ip address
    ip = match.group()
    print 'the current weather conditions at IP:', ip, 'are', weatherOf( locOf(ip) )+'.'
  else:
    print 'First arguement must contain the IP address to look up';
  
if __name__ == '__main__':
  main()

