# Change the socket program socket1.py to prompt the user for the URL
# so it can read any web page. You can use split('/') to break the URL into its component
# parts so you can extract the host name for the socket connect call. Add error checking
# using try and except to handle the condition where the user enters an improperly
# formatted or non-existent URL.

import socket
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter the url: ')
try:
    host = url.split("/")[2]
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, 80))
    new_link = 'GET ' + url + 'HTTP/1.0\r\n\r\n'
    new = new_link.encode()
    sock.send(new)
    while True:
        data = sock.recv(512)
        if len(data) < 1:
            break
        print(data.decode())

except:
    print("Invalid url")

sock.close()
