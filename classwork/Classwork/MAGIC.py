import math 

class Vector:
    def __init__(self, x, y):
        self.xcomp = x
        self.ycomp = y
    
    def get_magnitude(self):
        if self.ycomp == 0:
            return self.xcomp
        elif self.xcomp == 0:
            return self.ycomp
        else:
            return ((self.xcomp)**2 + (self.ycomp)**2)**0.5 # does pythagoras to get the magnitude of the vector

    def __str__(self):
        return f"{self.xcomp}i + {self.ycomp}j"
    
    def __add__(self,other):
        return Vector(self.xcomp + other.xcomp, self.ycomp + other.ycomp)
    
    def __sub__(self, other):
        return Vector(self.xcomp - other.xcomp, self.ycomp + other.ycomp)
    
    def __eq__(self, other):
        return self.xcomp == other.xcomp and self.ycomp == other.ycomp\
        
    def __pow__(self, other, modulo=None):
        if modulo is None:
            resultx = self.xcomp ** other.xcomp
            resulty = self.ycomp ** other.ycomp
        else:
            result = pow(self.value, other, modulo)
        return Vector(resultx,resulty)
    
def test_vector():
    vec1 = Vector(3,4)
    vec2 = Vector(4,5)

    print("Testing mangitude function...", end="")
    if vec1.get_magnitude() == 5:
        print("test passed")
    else:
        print("test failed")

    # test addition

    print("testing addition")
    if vec1 + vec2 == Vector(7,9):
        print('test passed')
    else:
        print('test FAILED')

    # test subtraction

    print('testing subtraction')
    if vec1 - vec2 == Vector(-1,-1):
        print(f"test passed {vec1-vec2}")
    else:
        print("test failed")

    # test exponentiation. x of first vector to power of second, same for y.

    print('testing exponentiation')
    if vec1 ** vec2 == Vector(81,1024):
        print(f"test passed {vec1**vec2}")
    else:
        print(f"test failed {vec1**vec2}")

test_vector()

