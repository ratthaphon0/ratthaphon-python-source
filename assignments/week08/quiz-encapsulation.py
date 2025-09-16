"""
Write a Python class Rectangle with:

- Private attributes for length and width
- Methods to calculate area (getArea()) and perimeter (getPerimeter())
- A method to check if it's a square (isSquare())
"""


class Rectangle:
    def __init__(self, length=0, width=0):
        self.__length = length
        self.__width = width

    def getArea(self):
        return f"The area of this rectangle is: {self.__length * self.__width}"

    def getPerimeter(self):
        return f"The perimeter of this rectangle is: {2 * (self.__length + self.__width)}"

    def isSquare(self):
        return (
            "Yes, this rectangle is a square."
            if self.__length == self.__width
            else "No, this rectangle is not a square."
        )

    def __str__(self):
        return f"Rectangle(length={self.__length}, width={self.__width})"

# Example usage
if __name__ == "__main__":
    rectangle1 = Rectangle(10, 5)
    print("-"*50)
    print(rectangle1)       
    print(rectangle1.getArea())
    print(rectangle1.getPerimeter())
    print(rectangle1.isSquare())
    
    print()


    rectangle2 = Rectangle(7, 7)
    print(rectangle2)
    print(rectangle2.getArea())
    print(rectangle2.getPerimeter())
    print(rectangle2.isSquare())
    print("-"*50)
