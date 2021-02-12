import cmath as m
from numpy.polynomial import polynomial as P
deg = input("Enter the degree of polynomial")
if deg == "quad":
        a = float(input("Enter the coefficient of x^2 :"))
        b = float(input("Enter the coefficient x :"))
        c = float(input("Enter the constant :"))        
        fx = P([c,b,a])
        print("The Roots of the given equation are,"P.root())
