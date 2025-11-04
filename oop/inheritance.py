class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, length):
        self.length = length
        super().__init__(length, length)
    
    def area(self):
        area = super().area() * 100
        return area

asdf = Square(1)
print(asdf.area())
    