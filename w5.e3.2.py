#!/usr/bin/python3
h = input('enter hours: ')
r = input('enter rate: ')
try:
    h = float(h)
    r = float(r)
except:
    print('EXIT HARDER, please enter numberic input')
    quit()
# print base_pay
if h > 40 :
    #print("overtime")
    reg = r * h
    opt = (h - 40.0) * (r *0.5)
    p = reg + opt
else:
    #print("regular")
    p = h * r
print("Pay:",p)
