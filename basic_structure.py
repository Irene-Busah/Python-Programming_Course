# code returns the name of a person and their corresponding emails

"""
def get_emails(people):
    result = []
    for name, email in people:
        result.append("{} , <{}>".format(name,email))
    return result

print(get_emails([("i.busah@alustudent.com", "Irene Busah"), ("m.mburu@alustudent.com","Mary Mburu")]))

"""
"""
def count(strings, letter):
    number = 0
    for string in strings:
        if string == letter:
            number += 1
    return number
print(count("Irene is here", 'e'))
print(count("The Lord's Grace is sufficient for my life!", "s"))
"""

fhand = open('Text_files/text.txt', 'r')
#print(fhand.readlines(57))
#count = 0
for line in fhand:
    #count = count + 1
#print(count)
    line = line.rstrip()
    if line.startswith('From'):
        print(line)

