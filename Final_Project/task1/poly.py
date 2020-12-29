from OO_complex import *
from math import sqrt

class Polynomial:
    '''Initialize the object'''
    def __init__(self, coefficients):
        self.__coefficients = coefficients
    
    @property
    def coefficients(self):
        '''To view outside the class'''
        return self.__coefficients
    
    def add(self, other):
        '''Sum value between two coefficients to 'poly1' '''
        if len(self.__coefficients) >= len(other.__coefficients):
            poly1 = list(self.__coefficients)
            poly2 = list(other.__coefficients)
        else:
            poly1 = list(other.__coefficients)
            poly2 = list(self.__coefficients)
        index1 = len(poly1) - 1
        index2 = len(poly2) - 1
        while index1 >= 0 and index2 >= 0:
            poly1[index1] += poly2[index2]
            index1 -= 1
            index2 -= 1
        return Polynomial(poly1)

    def val(self, v):
        '''give value to the variable and return the answer'''
        index = len(self.__coefficients) - 1
        value = 0
        for number in self.__coefficients:
            value += number * (v**index)
            index -= 1
        return value

    def mul(self, other):
        '''multiply two coefficients and assigned to 'poly3' '''
        poly1 = list(self.__coefficients)
        poly2 = list(other.__coefficients)
        poly1.reverse()
        poly2.reverse()
        poly3 = [0 for _ in range(len(poly1) + len(poly2) - 1)]
        for p1_index in range(len(poly1)):
            for p2_index in range(len(poly2)):
                poly3[p1_index+p2_index] += poly1[p1_index]*poly2[p2_index]
        poly3.reverse()
        return Polynomial(poly3)
    
    def coeff(self, i):
        '''return the value of coefficients in index i'''
        poly = self.__coefficients
        poly.reverse()
        return poly[i]

    def roots(self):
        '''find the root of coefficient by a formula'''
        if len(self.__coefficients) > 3:
            return "Order too high to solve for roots."
        poly = list(self.__coefficients)
        if len(poly) == 2:
            return float(-(self.__coefficients[1]/self.__coefficients[0]))
        a = self.__coefficients[0]
        b = self.__coefficients[1]
        c = self.__coefficients[2]
        front_ans = (-b)/(2*a)
        if b**2 - 4*a*c < 0:
            back_ans = sqrt(-(b**2 - 4*a*c))/(2*a)
            return [str(Complex(front_ans, back_ans)), str(Complex(front_ans, -back_ans))]
        else:
            back_ans = sqrt(b**2 - 4*a*c)/(2*a)
        if front_ans+back_ans == front_ans-back_ans:
            return float(front_ans+back_ans)
        return [front_ans+back_ans, front_ans-back_ans]

    def __call__(self, v):
        '''navigate to nethod 'val' '''
        return self.val(v)

    def __add__(self, other):
        '''navigate to method 'add' '''
        return self.add(other)

    def __mul__(self, other):
        '''navigate to method 'mul' '''
        return self.mul(other)
    
    def __str__(self):
        '''return the output message'''
        output = ""
        z_pow = len(self.__coefficients) - 1
        for number in self.__coefficients:
            if z_pow == 1:
                output += str(number) + "(z) + "
            elif z_pow == 0:
                output += str(number)
            elif number == 0:
                pass
            else:
                output += str(number) + "(z**" + str(z_pow) + ") + "
            z_pow -= 1
        return output