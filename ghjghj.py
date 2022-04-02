from graphics import *
from random import randint
import math

idmage_height = 1000
image_height = 1000;
def main():
    win = GraphWin("Window",image_height,image_height)
    win.setBackground(color_rgb(255, 255, 255))

    for _ in range(0,8):
          figure = drawahexagon(80)
         #figure = rotatePolygon(figure,randint(0,90))
          figure.draw(win)
    win.getMouse()
    win.close


def drawahexagon(length):
    x = randint(0, image_height-length)
    y = randint(0, image_height-length)
    poly = Polygon(Point(x+getRandom(0),y+getRandom(0)),
                   Point(x+length+getRandom(1),y+getRandom(1)),
                   Point(x+(length*1.5)+getRandom(0),y+(length/2)+getRandom(1)),
                   Point(x+length+getRandom(1),y+length+getRandom(1)),
                   Point(x+getRandom(0),y+length+getRandom(1)),
                   Point(x-(length/2)+getRandom(1),y+(length/2)+getRandom(0)))
    poly.setFill(color_rgb(255,0,0))
    return poly


def getRandom(base):
  if base == 0:
    foo = randint(0,5)
  else:
    foo = randint(3,10)
  return foo



main()