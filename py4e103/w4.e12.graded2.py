#!/usr/bin/python3

# In this assignment you will write a Python program that
# expands on https://www.py4e.com/code3/urllinks.py.
#
# The program will use urllib to read the HTML from the data files below,
# extract the href= values from the anchor tags,
# scan for a tag that is in a particular position from the top
# and follow that link, repeat the process a number of times,
# and report the last name you find.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# test
# Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
#url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
#repeat = 4
#position = 3

url = 'http://py4e-data.dr-chuck.net/known_by_Jensyn.html'
repeat = 7
position = 18

# repeat 7 times
for i in range(repeat) :
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    # Retrieve all of the anchor tags
    tags = soup('a')
    count = 0
    for tag in tags:
        count += 1
        # stop at position
        if count > position :
            break
        url = tag.get('href', None)
        #print('Name:', tag.contents[0])
        name = tag.contents[0]
print(name)
