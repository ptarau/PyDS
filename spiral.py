import turtle

# Set the background color
turtle.bgcolor("orange")

# Create a turle
t = turtle.Turtle()
t.width(2)
t.speed(100)  
t.color("red")

def spirals():
  t.up()
  t.home()
  t.down()
  t.clear()
  for x in range(100):
    t.forward(5*x)
    t.left(90)  
  t.up()
  t.home()
  t.down()
  t.clear()
  for x in range(100):
    t.forward(5*x)
    t.right(90)

def go() :
  for x in range(4) :
    spirals()  