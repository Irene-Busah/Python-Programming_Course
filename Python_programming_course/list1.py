#print a list of unique words in alphabetical order from the text file

"""
new_list = []
fopen = open('romeo.txt', 'r')
fhand = fopen.readlines()

for line in fhand:
    words = line.split()
    for word in words:
        if word not in new_list:
            #new_list += word
            new_list.append(word)


print(sorted(new_list))

"""

#prints out who sent the email from a MBOX

fopen = open('../Text_files/text1.txt', 'r')
fhand = fopen.readlines()
count = 0
for line in fhand:
    if line.startswith('From'):
        count = count + 1
        words = line.split()
    else:
        continue

    print(words[1])
print("There are {} lines in the file that starts with From".format(count))
