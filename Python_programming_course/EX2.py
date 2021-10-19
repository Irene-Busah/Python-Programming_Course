import urllib.error
import urllib.request
import xml.etree.ElementTree as ET

# http://py4e-data.dr-chuck.net/comments_1303036.xml
url = input("Enter the url: ")
# if len(url) < 1:
#     url = "http://python-data.dr-chuck.net/comments_200531.xml"
#     print("Retrieving " + url)

xml = urllib.request.urlopen(url).read()
print("Retrieved: " + str(len(xml)) + " characters")

tree = ET.fromstring(xml)

counts = tree.findall('.//count')
print("Count: " + str(len(counts)))

accumulator = 0

for count in counts:
    accumulator += int(count.text)

print("Sum:" + str(accumulator))
