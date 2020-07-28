#!/usr/bin/python3

# debug only
# skip user input for the filename
#fh = open('mbox-short.txt','r')

# handle user input for the filename
fname = input("Read file: ")
try:
    fh = open(fname, 'r')
except:
    print('File cannot be opened', fname)
    exit()

import operator

c = 0
mydict = dict()

# for each line in file
for line in fh:
    # split each line into words
    words = line.split()
    # search for first word 'From'
    # compound guardian to ensure greater than 2 words in line and first word is 'From'
    if len(words) < 2 or words[0] != 'From' : continue
    # save email addr in new var 'sender'
    sender = words[1]
    # set default value 0 if key is not found in dictionary
    mydict[sender] = mydict.get(sender,0) + 1

# find the largest number (value) and corresponding email (key)
largest = None
email = None
for k,v in mydict.items():
    # print(k,v)
    if largest is None or v > largest :
        largest = v
        email = k

print(email, largest)
