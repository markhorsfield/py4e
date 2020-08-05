#!/usr/bin/python3

def seat_at_tables(group) :
    """
    group: an int
    Given 3 tables of size 6 and 3 tables of size 4,
    return True if the group can be seated so that they
    completely fill any combination of tables.
    Return False if not.
    """
    big_size = 6
    big_count = 3
    small_size = 4
    small_count = 3

    possible = ()

    # nested for loop to check small table capacity first
    # then outer for loop to check big table capacity
    # return a tuple

    for i in range(big_count + 1) :
        for j in range(small_count + 1) :
            possible += (i*big_size + j*small_size, )

    return group in possible

# example of a number that would fit ok, should return True
#print(seat_at_tables(14))

# example of a number that would NOT fit, should return False 
print(seat_at_tables(11))
