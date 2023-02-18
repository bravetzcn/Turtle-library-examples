from turtle import *
title("turk bayragı")
bgcolor("red")
setup(width=600,height=600)
hideturtle()

def renk_konum(renk,x,y):
  penup()
  goto(x,y)
  pendown()
  color(renk)
  begin_fill()

def ay(cap):
    circle(cap)
    end_fill()

def yildiz():
   renk_konum("white", 80, 50)
   for i in range(5):
     forward(50)
     right(144)
     forward(50)
     right(-72)
   end_fill()

renk_konum("white",-110,-120)
ay(130)
renk_konum("red",-70,-90)
ay(100)
yildiz()
mainloop()