#!/usr/bin/python3

# debug only
# skip user input for the filename
fh = open('mbox-short.txt','r')

# handle user input for the filename
#fname = input('Enter the file name: ')
#try:
#    fhand = open(fname)
#except:
#    print('File cannot be opened:', fname)
#    exit()

count = 0
mydict = dict()

# for each line in file, split on whitespace character
# search for first word 'From'
for line in fh:
    words = line.split()
    # compound guardian to ensure greater than 2 words in line and first word is 'From'
    if len(words) < 2 or words[0] != 'From' : continue
    # store the hour value in the time of day var
    time = words[5].split(':')[0]
    # set default value 0 if key is not found in dictionary
    mydict[time] = mydict.get(time,0) + 1

# sort based on time (key) and print corresponding count (value)
for k, v in sorted(mydict.items()):
    print(k, v)
