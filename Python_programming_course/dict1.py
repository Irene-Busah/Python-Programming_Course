# reads words from the document and store them as keys

"""
fhand = open('words.txt', 'r')
words_lines = fhand.readlines()
#dict1 = []
for line in words_lines:
    parts = line.split()
    #for part in parts:
        #dict1.append(part)
dict2 = {}
for words in words_lines:
    if words not in dict2:
        dict2[words] = 1
    else:
        dict2[words] += 1

print(dict2)
"""

fopen = input("Enter the document link: ")

fhand = open(fopen)
words_lines = fhand.readlines()
for line in words_lines:
    words = line.split()

new_dict = dict()
for word in words_lines:
    if word not in new_dict:
        new_dict[word] = 1

    else:
        new_dict[word] += 1

    #print(max(new_dict))

print(new_dict)


