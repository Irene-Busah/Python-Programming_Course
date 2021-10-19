import turtle

"""

fopen = open('romeo.txt', 'r')
fhand = fopen.readlines()
for line in fhand:
    line = line.capitalize()

    print(line)
"""

"""
line = 'X-DSPAM-Confidence: 0.8475'

post = line.find(':')
#print(post)
piece = line[post + 2]
part = line[20:26]
print(part)


#print(piece)

"""

"""
fopen = open('romeo.txt', 'r')
fhand = fopen.readlines()

for line in fhand:
    ans = line.upper()

    print(ans)
"""

"""
fopen = open('romeo.txt', 'r')
new_list = list()
fhand = fopen.readlines()

for line in fhand:
    words = line.split()
    for word in words:
        if word not in new_list:
            new_list.append(word)
print(new_list)

"""


"""
wn = turtle.Screen()
wn.bgcolor("lightgreen")
pic = turtle.Turtle()
pic.color("blue")
pic.pensize(3)
pic.forward(150)
pic.left(90)
pic.forward(75)
pic.left(90)
pic.forward(150)
pic.left(90)
pic.forward(75)

wn.exitonclick()
"""

wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("blue")
tess.shape("turtle")

dist = 5
tess.up()                     # this is new
for _ in range(30):    # start with size = 5 and grow by 2
    tess.stamp()                # leave an impression on the canvas
    tess.forward(dist)          # move tess along
    tess.right(24)              # and turn her
    dist = dist + 2
wn.exitonclick()
