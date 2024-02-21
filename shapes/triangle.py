class Triangle:
    '''
    Triangle class representing a triangle

    Attributes
    ----------
    base : float
        base of the triangle
    height : float
        height of the triangle
    
    Methods
    -------
    area()
        returns the area of the triangle
    __str__()
        returns the string representation of the triangle
    __eq__(other)
        returns True if the triangles have the same base and height, False otherwise
        
    '''
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height
    
    def __str__(self):
        return f'Triangle with base {self.base} and height {self.height}'

    def __eq__(self, other):
        return self.base == other.base and self.height == other.height
                