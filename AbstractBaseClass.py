from abc import ABCMeta, abstractmethod
class Shape(metaclass=ABCMeta):
    """
    This class is Abstract Meta or Base class.
    """
    @abstractmethod
    def printArea(self):
        return 0

class Rectangle(Shape):
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.length = 6
        self. width = 7
    def printArea(self):
        return self.length * self.width

class Square(Shape):
    type = "Square"
    sides = 4
    def __init__(self):
        self.one_side = 6
    def printArea(self):
        return self.one_side * self.one_side

rect = Rectangle()
sq = Square()
print(f"So the area of Rectangle, where its length is 6cm and width is 7cm, is : " + str(rect.printArea()))
print(f"So the area of Square, where its one side is 6cm, is : " + str(sq.printArea()))