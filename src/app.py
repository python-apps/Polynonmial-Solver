import cmath as m

def quadpoly(a,b,c):
    d = ((b**2) - 4*a*c)
    e = m.sqrt(d)
    alpha = ((-b + e)/(2*a)) 
    beta = ((-b - e)/(2*a))
    return alpha , beta
def cubpoly(a,b,c):
    alpha = -b / 3*a
    b1 = b + alpha*a
    c1 = c + alpha*b1
    beta , gamma = quadpoly(a,b1,c1)
    return alpha , beta , gamma
def quartpoly(a,b,c,d):
    alpha = -b / 4*a
    b2 = b + alpha*a
    c2 = c + alpha*b1
    d2 = d + alpha*c2
    beta , gamma , zeta = cubpoly(a,b2,c2,d2)
    return alpha , beta , gamma , zeta
deg = input("Enter the degree of polynomial:")
if deg == "quad":
    a = float(input("Enter the coefficient x^2 :"))
    b = float(input("Enter the coefficient x :"))
    c = float(input("Enter the constant :"))
    alp , be = quadpoly(a,b,c)
    print("The Roots of the given equation are,"+ alp + " " + be)
elif deg == "cubic":
    a3 = float(input("Enter the coefficient of x^3 :"))
    b3 = float(input("Enter the coefficient x^2 :"))
    c3 = float(input("Enter the coefficient x :"))
    d3 = float(input("Enter the constant :"))
    alpha , beta , gamma = cubpoly(a3,b3,c3,d3)
    print("The Roots of the given equation are,"+ alpha + " " + beta + " " + gamma )
elif deg == "quart":
    a4 = float(input("Enter the coefficient of x^4 :"))
    b4 = float(input("Enter the coefficient of x^3 :"))
    c4 = float(input("Enter the coefficient x^2 :"))
    d4 = float(input("Enter the coefficient x :"))
    e4 = float(input("Enter the constant :"))
    alpha , beta , gamma , zeta = quartpoly(a4,b4,c4,d4,e4)
    print("The Roots of the given equation are,"+ alpha + " " + beta + " " + gamma + " " + zeta)
input()
