# Networked technology in python using sockets


"""
import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       # create an instance of the socket object
mysocket.connect(('data.pr4e.org', 80))
new_cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysocket.send(new_cmd)

while True:
    data = mysocket.recv(512)
    if len(data) < 1:
        break

    print(data.decode(), end='')
mysocket.close()
"""

import urllib.error
import urllib.request
import urllib.parse

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())


