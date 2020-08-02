#!/usr/bin/python3

while True :
    password = input("Make up a secure password: ")
    print("You entered: ", password)

    # initialize
    has_capital = False
    has_digit = False

    # check length
    gt_6 = len(password) >= 6
    if gt_6 is True :
        print("Password length check passed")

    # check alphanum exist
    for ch in password :
        if ch in "0123456789" :
            has_digit = True
        if ch in "ABCDEFGHIJKLMNOPQRSTUVWYZ" :
            has_capital = True
    if has_digit is True :
        print("Password number check passed")
    if has_capital is True :
        print("Password capital check passed")

    # tell the user they failed to meet requirements
    if not gt_6 :
        print("Password length should be greater than or equal to 6 characters")

    if not has_capital :
        print("Password must have at least one capital letter")

    if not has_digit :
        print("Password must have at least one number")

    # conditions to ask for a new password
    if not gt_6 or not has_capital or not has_digit:
        continue
    break
print("Great password!")
