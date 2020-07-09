#!/usr/bin/python3
def computepay(h,r):
    if h > 40 :
        #print("overtime")
        reg = r * h
        opt = (h - 40.0) * (r *0.5)
        p = reg + opt
    else:
        #print("regular")
        p = h * r
    return p

h = input('enter hours: ')
r = input('enter rate: ')
try:
    h = float(h)
    r = float(r)
except:
    print('EXIT HARDER, please enter numberic input')
    quit()

p = computepay(h,r)
print("Pay",p)
