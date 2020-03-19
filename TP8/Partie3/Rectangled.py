from Shape import Shape
import turtle
screen = turtle.Screen()
turtle.delay(0)
screen.setup(width=1920, height=1080, startx=0, starty=0)

class rectangle(Shape) :
    def __init__(self, x, y, width, height) :
        Shape.__init__(self, x, y)
        # self.__x = x
        # self.__y = y
        self.__width = width
        self.__height = height

   # def getX(self):
   #     return self.__x

   # def getY(self):
   #     return self.__y

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height

   # def setX(self, x):
   #     self.__x = x

   # def setY(self, y):
   #     self.__y = y

    def setWidth(self, width):
        self.__width = width

    def setHeight(self, Height):
        self.__Height = Height

    def draw(self, turtle):
        turtle.down()
        for i in (0, 1):
            turtle.forward(self.__width)
            turtle.left(90)
            turtle.forward(self.__height)
            turtle.left(90)

#turtle.forward(200)
#screen.exitonclick()
