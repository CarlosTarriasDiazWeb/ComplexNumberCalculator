import math

# class that represents a mathematical complex number (z=a+bi : real comp.->a, imaginary comp.->b)
class Complex:
    __slots__ = ['__real', '__img']  # stating the attributes of the class

    # constructor
    def __init__(self, real=0, img=0):
        self.__real = real
        self.__img = img

    # prompts the user to write the real and imaginary part
    def scan(self):
        self.__real = int(input("Input the real part..."))
        self.__img = int(input("Input the imaginary part..."))

    # get the conjugate of the number (imaginary component with sign inverted)
    def calculate_conjugate(self):
        conjugate = Complex()
        conjugate.__real = self.__real
        conjugate.__img = -self.__img

        return conjugate

    #calculates the modulus of the number
    def calculate_modulus(self):
        return math.sqrt((self.__real * self.__real) + (self.__img * self.__img))

    # returns the sum of two complex numbers (overloading add operator)
    def __add__(self, c):
        return Complex(self.__real + c.__real, self.__img + c.__img)
    
    #return the substraction of two complex numbers (overloading substract operator)
    def __sub__(self, c):
        return Complex(self.__real - c.__real, self.__img - c.__img)

    def __mul__(self, c):
        return Complex(self.__real*c.__real - self.__img*c.__img, self.__real*c.__img + self.__img*c.__real)

    # prints the complex number in the format a+bi (overloading stringify function)
    def __str__(self):
        notation_symbol = " + " if self.__img > 0 else ""
        if (self.__real == 0 ):
            return "0"
        elif (self.__img == 0):
            return (f'{str(self.__real)}')
        else:
            return (f'{str(self.__real) + notation_symbol + str(self.__img)}i ')
