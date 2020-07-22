#!/usr/bin/python3

fname = input("Read file: ")
#fh = open('words.txt','r')
fhandle = open(fname, 'r')
for i1 in fhandle:
    i2 = i1.rstrip()
    print(i2.upper())
