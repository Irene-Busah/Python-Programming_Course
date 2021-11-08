# regex

"""
book = " She is 60 years old. She started school at Bibiani Estate F 81."
results = re.findall('[0-9]+', book)
# print(results)
# print(book)


sentence = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
print(re.findall("\S+?@\S+"))
"""

import re

fopen = open("Text_files/textfile.txt", "r")
my_list = list()
for lines in fopen:
    line = lines.rstrip()
    num = re.findall('[0-9]+', line)
    my_list = my_list + num
add = 0
for digit in my_list:
    add += int(digit)

# print(add)

a = '<p>Please click <a href="http://www.dr-chuck.com">here</a></p>'
rec = re.findall('href="(.+)"', a)
print(rec)
