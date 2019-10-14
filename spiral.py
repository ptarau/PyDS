import turtle

# Set the background color
turtle.bgcolor("orange")

# Create a turtle
t = turtle.Turtle()
t.width(2)
t.speed(10)
t.color("red")

def left_spiral():
  t.up()
  t.home()
  t.down()
  t.clear()
  for x in range(100):
    t.forward(5*x)
    t.left(90)

def right_spiral():
  t.up()
  t.home()
  t.down()
  t.clear()
  for x in range(100):
    t.forward(5*x)
    t.right(90)

def go() :
   left_spiral()
   right_spiral()

go()
