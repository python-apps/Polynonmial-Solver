import cmath as m
a = float(input("Enter the coefficient of x^2 :"))
b = float(input("Enter the coefficient x :"))
c = float(input("Enter the constant :"))
d = ((b**2) - 4*a*c)
if d > 0:
    print("The roots real and distinct")
if d == 0:
    print("The roots are real and equal")
if d < 0:
    print("There are no real roots for the given equation")
e = m.sqrt(d)
root1 = ((-b + e)/(2*a)) 
root2 = ((-b - e)/(2*a))
print("The Roots of the given equation are,",root1,"and",root2)
