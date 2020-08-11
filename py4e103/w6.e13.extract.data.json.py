#!/usr/bin/python3

import urllib.request, urllib.parse, urllib.error
import json

#url = 'http://py4e-data.dr-chuck.net/comments_734013.json'
url = input('Enter location: ')
print('Retrieving', url)

# open user input URL
try:
    uh = urllib.request.urlopen(url)
except:
    print('URL cannot be opened')
    exit()

# decode into raw data

data = uh.read().decode('utf-8')
print('Retrieved', len(data), 'characters')

# data is byte string format at this point
#print(type(data))

# convert into json

jdata = json.loads(data)

# info is a two-level nested dictionary 
#print(type(info))
#print(info.items())

# count the number of items in the json data

iter = 0
sum = 0

# need to replace this with json friendly method

for key in jdata['comments'] :
    #print('Value:', key['count'])
    sum += int(key['count'])
    iter += 1

print('Count:', iter)
print('Sum:', sum)


# sample output

# % ./w5.e13.1.json.py                                                                                                   (develop ?)
# Retrieving http://py4e-data.dr-chuck.net/comments_42.json
# Retrieved 2711 characters
# Count: 50
# Sum: 2553