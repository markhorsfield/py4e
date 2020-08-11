#!/usr/bin/python3

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

#url = 'http://py4e-data.dr-chuck.net/comments_734012.xml'
url = input('Enter location: ')
print('Retrieving', url)

# open user input URL
try:
    uh = urllib.request.urlopen(url)
except:
    print('URL cannot be opened')
    exit()

# read XML
data = uh.read()
print('Retrieved', len(data), 'characters')
#print(data.decode())
tree = ET.fromstring(data)

# count the number of items in the XML tree (total)

iter = 0
sum = 0

comment_counts = tree.findall('.//count')

for c in comment_counts :
    sum += int(c.text)
    iter += 1

print('Count:', iter)
print('Sum:', sum)

# sample output
#
#% ./w5.e13.1.xml.py                                                                                            (develop ?)
#Enter location: http://py4e-data.dr-chuck.net/comments_42.xml
#Retrieving http://py4e-data.dr-chuck.net/comments_42.xml
#Retrieved 4189 characters
#Count: 50
#Sum: 2553
