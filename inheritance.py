class Rectangle:
    def __init__(self,width,height):
        self._width = width
        self._height = height

    @property
    def area (self):
        return self._width * self._height

class Square(Rectangle):
    def __init__(self,side):
        #call parent class constructor
        super().__init__(side,side)


if __name__ == '__main__':
    rectangle = Rectangle(3,4)
    print("rectangle area: " , rectangle.area)

    square = Square(8)

    print("Square area: " , square.area)