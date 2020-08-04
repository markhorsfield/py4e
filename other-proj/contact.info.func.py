#!/usr/bin/python3

"""
requirements:
friends.txt: name and phone number mapping
map_areacodes.txt: areacode to state mapping
"""

def read_file(file) :
    """
    file: a file object
    Starting from the first line, it reads every 2 lines
    and stores them in a tuple. Starting from the second line,
    it reads every 2 lines and stores them in a tuple.
    Returns a tuple.
    """
    first_every2 = ()
    second_every2 = ()
    count = 0
    for line in file :
        stripped_line = line.replace("\n", "")
        # every other line starting with even
        if count % 2 == 0 :
            first_every2 += (stripped_line, )
        # every other line starting with odd
        elif count % 2 == 1 :
            second_every2 += (stripped_line, )
        count += 1
    return (first_every2, second_every2)

def sanitize(some_tuple) :
    """
    some_tuple: a tuple of strings
    Removes all spaces, dashes, and open/closed parenthesis in each string
    Returns a tuple with cleaned up string elements
    """

    clean_str = ()
    for s in some_tuple :
        s = s.replace(" ", "")
        s = s.replace("-", "")
        s = s.replace("(", "")
        s = s.replace(")", "")
        clean_str += (s, )
    return clean_str

def analyze_friends(names, phones, all_areacodes, all_places) :
    """
    names: tuple of friends names
    phones: tuple of phone numbers without special characters
    all_areacodes: tuple of area codes
    all_places: tuple of states
    Prints how many friends you have and every unique state, represeneted
    by phone number
    """
    def get_unique_area_codes():
        """
        Returns a tuple of all unique area codes in phones
        """
        area_codes = ()
        # phones is the parameter to analyze_friends
        for p in phones :
            if p[0:3] not in area_codes :
                area_codes += (p[0:3], )
        return area_codes

    def get_states(some_areacodes) :
        """
        some_areacodes: tuple of area codes
        Returns a tuple of states associated with some_areacodes
        """
        states = ()
        for ac in some_areacodes :
            if ac not in all_areacodes :
                states += ("BAD AREACODE", )
            else :
                # use index to match ac with state
                index = all_areacodes.index(ac)
                states += (all_places[index], )
        return states

    num_friends = len(names)
    unique_area_codes = get_unique_area_codes()
    unique_states = get_states(unique_area_codes)

    print("You have", num_friends, "friends!")
    print("They live in:, ")
    for s in unique_states :
        print(s)

friends_file = open("friends.txt", "r")
map_file = open("map_areacodes.txt", "r")
(names, phones) = read_file(friends_file)
(areacodes, places) = read_file(map_file)
friends_file.close()
map_file.close()

# initial check to print data in raw format
#print(names)
#print(phones)

# check to print cleaned up phone strings
clean_phones = sanitize(phones)
#print(clean_phones)

analyze_friends(names, clean_phones, areacodes, places)
