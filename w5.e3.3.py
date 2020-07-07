#!/usr/bin/python3

v = input('enter a score: ')
# accept only numbers as input
try:
    v = float(v)
except:
    print('error: enter a number. exiting')
    quit()
# catch out of range values
if v < 0.0:
    print('out of range. too low')
    exit()
elif v > 1.0:
    print('out of range. too high')
    exit()
# print score
elif v >= 0.9:
    print("A")
elif v >= 0.8:
    print("B")
elif v >= 0.7:
    print("C")
elif v >= 0.6:
    print("D")
elif v < 0.6:
    print("F")
#print("Done")
