class Circle(object):
    '''
    Circle class representing a circle

    Attributes
    ----------
    radius : float
        radius of the circle
    
    Methods
    -------
    area()
        returns the area of the circle
    perimeter()
        returns the perimeter of the circle
    __str__()
        returns the string representation of the circle
    __eq__(other)
        returns True if the circles have the same radius, False otherwise

    

    '''
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

    def __str__(self):
        return "Circle with radius " + str(self.radius)

    def __eq__(self, other):
        return self.radius == other.radius