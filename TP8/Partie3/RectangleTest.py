from Rectangled import rectangle
import turtle
turtle.delay(0)

A = rectangle(10, 50, 50, 400)
B = rectangle(20, 30, 50, 100)
print("x", A.getX(),"y", A.getY(),"width", A.getWidth(), "Height", A.getHeight())
print("x", B.getX(),"y", B.getY(),"width", B.getWidth(), "Height", B.getHeight())

A.draw(turtle)
B.draw(turtle)
turtle.exitonclick()
