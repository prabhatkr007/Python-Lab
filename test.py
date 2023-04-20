import turtle 
import math

tur = turtle.Turtle()
sw = turtle.Screen()

sw.bgcolor("black")
tur.color("white")

# tur.hideturtle()

tur.speed(0)

def fillcircle(rad,color):
    tur.begin_fill()
    tur.fillcolor(color)
    tur.circle(rad)
    tur.end_fill()

fillcircle(30,"yellow")

def planet(a,b ,rad,cl): 
    for i in range(360):
        tur.up()
        x = a * math.sin(math.radians(45//180- i))
        y = b* math.cos(math.radians(45//180 - i))
        tur.goto(x,y)
        tur.down()
        fillcircle(rad,cl)
        # tur.sleep(0.2)
        fillcircle(rad,"black")
        
        

planet(200,100,30,"red")


x = input()