"""
import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")

pic = turtle.Turtle()
pic.pensize(4)
pic.shape('turtle')
pic.color('blue')


pic.up()
dist = 5
for line in range(80):
    pic.stamp()
    pic.forward(dist)
    pic.left(24)
    dist += 2
wn.exitonclick()
"""

import shutil
du = shutil.disk_usage("/")
print(du)
percent = du.free/du.total * 100
print(percent)





