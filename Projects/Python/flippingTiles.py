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
   a = (count % 8) * 50 - 200
   b = (count // 8) * 50 - 200
   return a, b

def click(x, y):
   spot = Numbering(x, y)
   mark = state['mark']
   
   # verificar variável error
   if mark is None or mark == spot or tiles[mark] != error:
      state['mark'] = spot
   eles:
      hide[spot] = False
      hide[mark] = False
      state['mark'] = None

def draw():
   clear()
   goto(0, 0)
   stamp()

   for count in range(64):
      if hide[count]:
         x, y = Coordinates(count)
         Square(x, y)

   mark = state['mark']

   if mark is not None and hide[mark]:
