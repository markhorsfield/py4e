#!/usr/bin/python3

# debug only
# skip user input for the filename
#fhandle = open('mbox-short.txt','r')

# handle user input for the filename
fname = input("Read file: ")
try:
    fhandle = open(fname, 'r')
except:
    print('File cannot be opened', fname)
    exit()

count = 0
iter = 0
for line in fhandle:
    # ignore the unimportant lines
    if not line.startswith("X-DSPAM-Confidence:") : continue
    # remove extra new lines
    line2 = line.rstrip()
    # debug only
    #print(line2)
    # find the delimitor
    ipos = line2.find(':')
    # keep the number - as a string initially
    num = line2[ipos+1:]
    #print(float(num)
    # sum the cumuluative values as float
    count = count + float(num)
    # count the number of iterations
    iter = iter + 1
# debug
#print("lines matched:", iter, "and agg count is", count)
# do math
avg = (count/iter)
# round to 12 places
print("Average spam confidence:", "%0.12f" % avg)
