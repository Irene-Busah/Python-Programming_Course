# prints out the contents of a file line by line in Capital letters
"""
fhand = open('text1.txt', 'r')
for line in fhand:
    line = line.rstrip()
    print(line.upper())
"""

# receives file input from the user to print out specific lines.


count = 0
total = 0
fhand = input("Please enter the name of the file: ")
fname = open(fhand)
fname1 = fname.readlines()
for line in fname1:
    #line = line.rstrip()

    if not line.startswith('X-DSPAM-Confidence: '): continue



    inp = line.find(":")

    number = line[inp + 1:]

    num = float(number)
    total = total + num
    count = count + 1
        #average = (total/count)
        #print(count)
print("Average spam confidence: ", total/count)



