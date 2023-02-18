from turtle import *

def renk_konum(renk,x,y):
  penup()
  goto(x,y)
  pendown()
  color(renk)
  begin_fill()

def yildiz():
  renk_konum("black", 80, 25)
  for i in range(5):
    forward(50)
    right(144)
  end_fill()


yildiz()
mainloop()