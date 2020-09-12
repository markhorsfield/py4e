#!/usr/bin/python3

import sqlite3

# similar to a fh open used on txt files
conn = sqlite3.connect('emailbyorg.sqlite')
cur = conn.cursor()

# start fresh. delete existing table with name 'Counts' if one exists
cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

# same logic used in the dict to iterate through every line in a file
# count the iterations and keep a sum 

#fname = input('Enter file name: ')
fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    # find the domain name
    org = email.split('@')[1]
    # create new tuple with single element
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    # when org is first seen set count to 1
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    # add 1 to existing count
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))
    # write data to disk                
    conn.commit()

# https://www.sqlite.org/lang_select.html
# retrieve the rows in sorted manner
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
