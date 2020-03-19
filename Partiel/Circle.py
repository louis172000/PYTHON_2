from Partiel.Point import Point
from math import *

class Circle:
    def __init__(self, c=None, r=0):
        self.__radius = r
        self.__center = c

    def getRadius(self):
        return self.__radius

    def getCenter(self):
        return self.__center

    def setRadius(self, r1):
        self.__radius = r1

    def setCenter(self, x, y):
        c1 = Point()
        c1.setX(x)
        c1.setY(y)
        self.__center = c1

    def contains(self, p):
        return p.distance(self.__center) <= self.__radius

    def area(self):
        return pi * (self.__radius ** 2)

    def compare(self, c):
        return self.__radius == c.__radius and self.__center.eq(c.__center)

    def perimeter(self):
        return 2 * pi * self.__radius

    def print(self):
        print("Center :")
        self.__center.print()
        print("Radius : ")
        print(self.__radius)

c = Circle(Point(5,4),9)
c.print()
c.setCenter(12,13)
print(c.contains(Point(4,4)))
print(c.area())
print(c.perimeter())
print(c.compare(Circle(Point(5,40),9)))
