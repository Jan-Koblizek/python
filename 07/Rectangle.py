class Rectangle:

    def __init__(self, width, height):
        self._width = width
        self._height = height

    def get_area(self):
        return self._width * self._height

    def set_size(self, width, height):
        self._width = width
        self._height = height


r = Rectangle(16, 14)
print(r.get_area())
