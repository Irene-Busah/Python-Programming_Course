# Creating a database for collecting emails

import sqlite3

connection = sqlite3.connect('emails.sqlite')
cur = connection.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (email TEXT, count INTEGER)')
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = 'email.txt'
fhandle = open(fname)
for line in fhandle:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts (email, count) VALUES (?,1)', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))
    connection.commit()

sql = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'
for row in cur.execute(sql):
    print(str(row[0]), row[1])
# "email_DB.py"
cur.close()
