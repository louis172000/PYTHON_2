from Shape import Shape

class circles(Shape):
    def __init__(self, x, y, radius):
        # self.__x = x
        # self.__y = y
        Shape.__init__(self, x, y)
        self.__radius = radius

   #  def getX(self):
   #      return self.__x
#
   #  def getY(self):
   #      return self.__y
#
    def getRadius(self):
        return self.__radius

   #  def setX(self, x):
   #      self.__x = x
#
   #  def setY(self, y):
   #      self.__y = y

    def setRadius(self, radius):
        self.__radius = radius

    def draw(self, turtle):
        turtle.circle(self.__radius)

