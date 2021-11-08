#categorizes each email message by the day of the week it was committed.

"""
fopen = open('text1.txt', 'r')
#fhand = fopen.readlines()
count = 0
new_content = dict()
for line in fopen:
    if line.startswith('From'):
        words = line.split()
        if words[0] != 'From':
            continue
        #for words in :
        if words[2] not in new_content:
            #word = fhand[2]
            new_content[words[2]] =  1
        else:
            new_content[words[2]] += 1

print(new_content)
"""

file_open = open('../Text_files/text1.txt', 'r')

file_hand = file_open.readlines()
maximum = 0
maximum_value = " "
new_content = dict()
for line in file_hand:
    if line.startswith('From'):
        words = line.split()
        if words[0] != 'From':
            continue
        if words[1] not in new_content:
            new_content[words[1]] = 1
        else:
            new_content[words[1]] += 1
#prints the max address with that has the highest messages
        for value in new_content:
            if new_content[value] > maximum:
                maximum = new_content[value]
                maximum_value = value
                #maximum = value
#minimum = min(new_content.items())

print(new_content)
print("{} : {}".format(maximum_value, maximum))
#print(minimum)



