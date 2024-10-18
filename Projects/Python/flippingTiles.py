from random import *
from turtle import *

screen = Screen()
screen.bgcollor("yellow")

def Square(x, y):
   up()
   goto(x, y)
   down()
   colors('white', 'green')
