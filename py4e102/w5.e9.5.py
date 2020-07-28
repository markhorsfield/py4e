#!/usr/bin/python3

import string

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for w in words:
        if w not in counts:
            counts[w] = 1
        else:
            counts[w] += 1

print(counts)
