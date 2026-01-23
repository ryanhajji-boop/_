from math import sqrt

class Rectangle:
    def __init__(self, w,h):
        if (w < 0) or (h < 0):
            raise Exception("triangle cannot have negative height or width")
        else:
            self.width = w
            self.height = h

    def get_area(self):
        return self.width * self.height
    
    def get_diagonal(self):
        diagonal_length_squared = (self.width)**2 + (self.height)**2
        return sqrt(diagonal_length_squared)
    
    # I learned something interesting here, python by itself adds a 0j to the end, incase the number that is square rooted is negative, thus resulting in a complex part to the number. I have gone out of my way to get rid of this by adding .real. alternatively, we can just do the solution below **0.5 which avoids this issue entirely, but thought this was cool to share. 
    
    # OR: ( ((self.width)**2) + ((self.height)**2) )**0.5
    
rect_1 = Rectangle(10,2)

print("The diagonal is", round(rect_1.get_diagonal(),3))