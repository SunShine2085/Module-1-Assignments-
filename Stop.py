import turtle

def octagon(size):
  for i in range(8):
    turtle.forward(size)
    turtle.left(45)

def rectangle(size):
  for i in range(2):
    turtle.forward(size/5)
    turtle.right(90)
    turtle.forward(size*2)
    turtle.right(90)

def forward(size):
  turtle.penup()
  turtle.forward(size*.375)
  turtle.pendown()

def stop(size):
  octagon(size)
  forward(size)
  rectangle(size)

stop(100)
forward(500)
stop(50)
turtle.Screen().exitonclick()