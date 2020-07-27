#!/usr/bin/python3


# create empty list
t1 = list()

# debug only
# skip user input for the filename
#fhandle = open('romeo.txt','r')

# handle user input for the filename
fname = input("Read file: ")
try:
    fhandle = open(fname, 'r')
except:
    print('File cannot be opened', fname)
    exit()

# for each line in file, split on whitespace char, then sort
for line in fhandle:
    # list 'words' is a placeholder only
    words = line.split()
    words.sort()

    # check for word in new line
    for word in words:
        # if word exists in list 't1' then keep going
        if word in t1 :
            continue
        # add new word to list 't1'
        t1.append(word)
        # debug
        #print("iter: ", word)
        #print("list: ",t1)
        # sort the list to match expected output
        t1.sort()
# print the list
print(t1)
