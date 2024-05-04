import turtle

def rectangle(size):
  for i in range(2):
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size/9)
    turtle.right(90)

def triangle(size):
  for i in range(3):
    turtle.forward(size)
    turtle.left(120)


def forward(size):
    turtle.penup()
    turtle.forward(size)
    turtle.pendown()

def backward(size):
    turtle.penup()
    turtle.forward(-(size/4))
    turtle.pendown()

def down(size):
   turtle.penup()
   turtle.right(90)
   turtle.forward(size/9)
   turtle.left(90)
   turtle.pendown()
      


def cake(size):
    triangle(size/2)
    backward(size)
    for i in range(3):
        rectangle(size)
        down(size)



cake(100)
forward(200)
cake(50)
turtle.Screen().exitonclick()
