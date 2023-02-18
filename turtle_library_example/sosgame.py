import turtle
import time

def kare(a):
 for i in range(4):
     ok.forward(a)
     ok.left(90)


ok=turtle.Turtle()
ok.speed(10)
renkler=['red','blue','purple','gray']
kenar=10
for i in range(40):
    kare(kenar)
    kenar=kenar+ 10
    ok.right(10)
    ok.color(renkler[i%4])

time.sleep(2)