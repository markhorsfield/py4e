#!/usr/bin/python3

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_734010.html')
soup = BeautifulSoup(url, "html.parser")

count = 0
sum = 0

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    sum = sum + int(tag.contents[0])
    count += 1
print("Count", count,"\nSum", sum)
