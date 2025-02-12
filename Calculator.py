# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 14:01:27 2025

@author: computershop.mn
"""
#importing math for the use of mathimatical functions
import math

#function for addition
def add(a, b):
    return a + b

#function for substraction
def subtract(a, b):
    return a - b

#function for multiplying
def multiply(a, b):
    return a * b

#function for deviding
def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

#function for sine calculation
def sine(a):
    return math.sin(math.radians(a))

#fucntion for cosine calculation
def cosine(a):
    return math.cos(math.radians(a))

#function for tangent calculation
def tangent(a):
    return math.tan(math.radians(a))

#function for arcsin calculation, it is inverse of sine
def arcsin(a):
    if -1 <= a <= 1:
        return math.degrees(math.asin(a))
    return "Error: Input not between"

#function for arccos calculation, it is inverse of cos
def arccos(a):
    if -1 <= a <= 1:
        return math.degrees(math.acos(a))
    return "Error: Input not between"

#function for arctan calculation, it is inverse of tangent
def arctan(a):
    return math.degrees(math.atan(a))

#function for square of a number
def square(a):
    return a ** 2

#function for the square root of a number
def square_root(a):
    if a < 0:
        return "Error: Cannot calculate a square root of negative number"
    return math.sqrt(a)



