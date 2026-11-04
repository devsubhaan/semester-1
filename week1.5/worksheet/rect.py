# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        # raising appropriate exceptions if necessary (see README.md)

        if not isinstance(width, int) or not isinstance(height, int):
            raise(TypeError)
        elif width <=0 or height <= 0:
            raise(ValueError)
        
        self.width = width
        self.height = height

    # Implement methods is_square(), area() & perimeter() here
    # (See README.md for details of what they should do)

    def is_square(self) -> bool:
        """
        Checks if its a square (if height is equal to width)
        """
        if self.height == self.width:
            return True
        return False

    def area(self) -> int:
        """
        Finds the area by multiplying width and height
        """
        return self.height * self.width

    def perimeter(self) -> int:
        """
        Calculates the perimeter by adding 2x the width and heights
        """
        return (2 * self.height) + (2 * self.width)

"""
test = Rectangle(5, 5)
print(test.area())
print(test.is_square())
print(test.perimeter())

test2 = Rectangle(6, 5.2)
print(test2.area())
print(test2.is_square())
print(test2.perimeter())
"""