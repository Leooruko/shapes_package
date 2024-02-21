class Rectangle:

    '''
    Rectangle class representing a rectangle

    Attributes
    ----------
    length : float
        length of the rectangle
    width : float
        width of the rectangle

    Methods
    -------
    area()
        returns the area of the rectangle
    perimeter()
        returns the perimeter of the rectangle
    __str__()   
        returns the string representation of the rectangle
    __eq__(other)
        returns True if the rectangles have the same length and width, False otherwise
    '''
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)
    def __str__(self) -> str:
        return f"Rectangle with length {self.length} and width {self.width}"
    
    def __eq__(self, __value: object) -> bool:
        return self.length == __value.length