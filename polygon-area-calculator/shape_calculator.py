from math import sqrt


class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        return "".join(["*" * self.width + "\n" for x in range(self.height)])

    def get_amount_inside(self, other):
        return self.get_area() // other.get_area()

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, new_side):
        self.width = self.height = new_side

    def get_area(self):
        return self.width ** 2

    def get_perimeter(self):
        return 4 * self.width

    def get_diagonal(self):
        return self.width * sqrt(2)

    def __str__(self):
        return f"Square(side={self.width})"