import math

class Point:
    def __init__(self, x_init=0, y_init=0):
        self.__x = x_init
        self.__y = y_init

    def print(self):
        print("(", self.__x, ",", self.__y,")")

    def shift(self, dx, dy):
        self.__x += dx
        self.__y += dy

    def distance(self, p):
        return math.sqrt((self.__x - p.__x) ** 2 + (self.__y - p.__y) ** 2)

    def milieu(self, p):
        return Point(((self.__x+p.__x)/2),((self.__y+p.__y)/2))

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def eq(self, other):
        return self.__x == other.__x and self.__y == other.__y


p1 = Point(10, 3)
p1.shift(1,2)
p2 = Point(11, 5)
d = p1.distance(p2)
print(d)
p3 = p1.milieu(p2)
p3.print()
print(p1.eq(p2))


