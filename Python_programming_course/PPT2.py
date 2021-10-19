import urllib.parse
import urllib.request
import urllib.error
from bs4 import BeautifulSoup

"""
url = input("Enter url: ")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# retrieve all the anchor tags of the url entered
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
"""
import ssl

# Ignore SSL certificate errors

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input("Enter url: ")
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('span')
add = 0
for tag in tags:
    add = add + int(tag.contents[0])
print(add)





