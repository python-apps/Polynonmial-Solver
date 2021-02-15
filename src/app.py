import cmath as m

def quadpoly(a,b,c):
    d = ((b**2) - 4*a*c)
    e = m.sqrt(d)
    alpha = ((-b + e)/(2*a)) 
    beta = ((-b - e)/(2*a))
    return str(alpha) , str(beta)
def cubpoly(a,b,c):
    alpha = -b / 3*a
    b1 = b + alpha*a
    c1 = c + alpha*b
    beta , gamma = quadpoly(a,b1,c1)
    return str(alpha) , beta , gamma
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
