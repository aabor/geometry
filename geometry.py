class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        '''
        >>> r = Rectangle(2, 3)
        >>> r.area()
        6
        '''
        return self.length * self.width
