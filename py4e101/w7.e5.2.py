#!/usr/bin/python3

largest = None
smallest = None

#helpful to debug if needed
#print('Before:', largest)
#print('Before:', smallest)

# validate input is number then convert string to integer
while True :
    sval = input('Enter a number: ')
    if sval == 'done' :
        break
    try:
        ival = int(sval)
    except:
        print('Invalid input')
        continue

#helpful to debug if needed
#for fval in [7, 3, 5.0]:

# find largest
    if largest is None or ival > largest :
        largest = ival
    # print values for each iteration through the loop
#    print('Loop Maximum:', fval, largest)

# find smallest
    if smallest is None or ival < smallest :
        smallest = ival
    # print values for each iteration through the loop
#    print('Loop Minimum:', fval, smallest)

# print the final result
print("Maximum is", largest)
print("Minimum is", smallest)
