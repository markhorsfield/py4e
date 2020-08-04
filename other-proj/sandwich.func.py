#!/usr/bin/python3

def sandwich(kind):
    print("-------")
    print(kind())
    print("-------")

def blt():
    my_blt = " bacon\nlettuce\n tomato"
    return my_blt

def bfast():
    my_ec = " eggegg\ncheese"
    return my_ec

sandwich(blt)
