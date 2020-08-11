#!/usr/bin/python3

import urllib.request, urllib.parse, urllib.error

fh = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()

for line in fh :
    words = line.decode().split()
    for word in words :
        counts[word] = counts.get(word, 0) + 1
print(counts)
