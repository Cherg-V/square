class Square:
    def __init__(self, side=10):
        self.side = side

    def calculate_area(self):
        return self.side * self.side

    def draw(self):
        for i in range(self.side):
            print(" * " * self.side)


s2 = Square(5)
print(s2.calculate_area())
s2.draw()
