from random import *
from turtle import *

screen = Screen()
screen.bgcollor("yellow")

def Square(x, y):
   up()
   goto(x, y)
   down()
   colors('white', 'green')
   begin_fill()
   for count in range(4):
      forward(50)
      left(90)
   end_fill()

def Numbering(x, y):
   return int((x + 200) // 50 + ((y + 200) // 50) * 8)

# define function
def Coordinates(count):
   return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def click(