#!/usr/bin/python3

# handle user input for the filename
word = input("What is your favorite dinosaur: ")
try:
    word2 = word.lower()
except:
    print(word, "is not a dinosaur!")
    exit()

d = dict()
for c in word2:
    d[c] = d.get(c,0) + 1
print(d)
