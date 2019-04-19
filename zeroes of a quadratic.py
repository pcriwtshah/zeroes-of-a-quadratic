#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 18:16:40 2019

@author: pashupatishah
"""

# Finding zeroes of a quadratic
# ax^2+bx+c
# x1 = (-b+sqrt(b^2-4ac))/2*a
# x2 = (-b-sqrt(b^2-4ac))/2*a


from numpy import math
a = float(input("Enter coefficients of x^2 : "))
b = float(input("Enter coefficients of x : "))
c = float(input("Enter the constant term : "))

discriminant = math.sqrt(b*b - 4*a*c)
x1 = (-b + discriminant)/2*a
x2 = (-b - discriminant)/2*a

print("The zeroes of quadratics are : ")
print(x1,x2)

# Axis of symmetry
x = 2*a/b
print("The equation of axis of symmetry is: x = ", x )

#Curve facing Up or Down
if a>0:
    print("The curve faces upward")
elif a<0:
    print("The curve faces downward")
else:
    print("This is not a quadratic")

#Vertex
y=a*x*x+b*x+c
print("The vertex of the quadratic is: ","(",x,",",y,")")