class Shape:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

class rectangle(Shape):
    def __init__(self, i, j, k):
        Shape.__init__(self, i, j)
        self.__k = k

    def drawShapes(self, shapes, turtle):
        turtle.ht()






