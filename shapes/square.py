class Square:
    '''
    Square class representing a square

    Attributes
    ----------
    length : float
        length of the square
    
    methos
    -------
    area()
        returns the area of the square
    perimeter()
        returns the perimeter of the square
    __str__()
        returns the string representation of the square
    __eq__(other)
        returns True if the squares have the same length, False otherwise
    '''
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

    def perimeter(self):
        return 4 * self.length
    
    def __str__(self):
        return f"Square with length {self.length}"
    
    def __eq__(self,other):
        return self.length == other.length
        