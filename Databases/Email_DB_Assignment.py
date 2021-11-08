# Creating a database using python to count emails from a text file

import sqlite3

connect = sqlite3.connect('Assignment_DB.sqlite')
cur = connect.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

file_name = input("Enter the name of the text file: ")
if len(file_name) < 1:
    file_name = 'email.txt'
file_handle = open(file_name)
for line in file_handle:
    if not line.startswith("From: "):
        continue
    piece = line.split()
    email = piece[1]
    domain = email.split('@')
    organization = domain[-1]

    cur.execute('SELECT count FROM Counts WHERE org = ? ', (organization,))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (organization,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (organization,))
    connect.commit()

sql = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
for row in cur.execute(sql):
    print(str(row[0]), row[1])
cur.close()

