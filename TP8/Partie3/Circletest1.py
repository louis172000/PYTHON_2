from Circled import circles
import turtle
turtle.delay(0)
A = circles(10, 50, 100)
B = circles(20, 30, 200)
print("x", A.getX(),"y", A.getY(),"radius", A.getRadius())
print("x", B.getX(),"y", B.getY(),"radius", B.getRadius())

A.draw(turtle)
B.draw(turtle)
turtle.ht()

turtle.exitonclick()
