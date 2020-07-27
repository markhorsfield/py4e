#!/usr/bin/python3

# debug only
# skip user input for the filename
fh = open('mbox-short.txt','r')

# handle user input for the filename
#fname = input("Read file: ")
#try:
#    fh = open(fname, 'r')
#except:
#    print('File cannot be opened', fname)
#    exit()

count = 0

# for each line in file, split on whitespace character
# search for first word 'From'
for line in fh:
    words = line.split()
    # compound guardian to ensure greater than 2 words in line and first word is 'From'
    if len(words) < 2 or words[0] != 'From' : continue
    count = count + 1
    # print the email address which is the second element in the list
    print(words[1])
print("There were", count, "lines in the file with From as the first word" )
