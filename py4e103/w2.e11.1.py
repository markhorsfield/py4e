#!/usr/bin/python3

import re

# run manually
fhandle = open('regex_sum_734008.txt','r')

t1 = list()

# for each line in file, split on whitespace char, then sort
for line in fhandle:
    # list 'words' is a placeholder only
    words = line.split()

    # check for word in new line
    for i in words:
        num_list = re.findall('([0-9]+)', i)
        t1 = t1 + num_list

sum = 0

for element in t1:
    sum = sum + int(element)
print(sum)
#print("the new int is", element, "and the sum is", sum)

# to verify result, run against e11.1.sample.txt and final sum should be 27486
