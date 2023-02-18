import time
import turtle
#for body
emo = turtle.Turtle()
emo.up()
emo.goto(0,-100)
emo.down()

emo.begin_fill()
emo.pendown()
emo.fillcolor('yellow')
emo.circle(100)
emo.end_fill()
time.sleep(0.9)

#for mouth
emo.up()
emo.goto(-67,-40)
emo.setheading(-60)
emo.width(7)
emo.down()
emo.circle(80,120)
emo.fillcolor('black')
time.sleep(0.9)
#for eyes

for i in range(-35,105,70):
 emo.up()
 emo.goto(i,35)
 emo.setheading(0)
 emo.down()
 emo.begin_fill()
 emo.circle(10)
 emo.end_fill()
 emo.penup()
 emo.goto(0,-150)
time.sleep(5)

