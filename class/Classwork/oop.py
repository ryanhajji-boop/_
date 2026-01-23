class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def get_area(self):
        return (self._width) * (self._height)
    
    def get_perimeter(self):
        return (2 * self._width) + (2 * self._height)
    
    def get_diagonal(self):
        return ((self._width)**2 + (self._height)**2)**0.5
    
def test():
    dims = Rectangle(30,40)

    # area
    area = dims.get_area()
    print(area) # output: 1200

    # perimeter
    perim = dims.get_perimeter()
    print(perim) # output: 140

    # diagonal
    diag = dims.get_diagonal()
    print(diag) # output: 50

test()