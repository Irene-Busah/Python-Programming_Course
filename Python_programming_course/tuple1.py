import string
# prints the ten most common words in the text

file_open = open('../Text_files/romeo.txt', 'r')
contents = dict()
for line in file_open:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in contents:
            contents[word] = 1
        else:
            contents[word] += 1

lists_contents = list()
for key, value in list(contents.items()):
    lists_contents.append((value, key))

lists_contents.sort(reverse=True)
for key, value in lists_contents[:10]:
    print(key, value)
