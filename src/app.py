def quadpoly(a,b,c):
	  d = ((b**2) - 4*a*c)
	  e = m.sqrt(d)
	  alpha = ((-b + e)/(2*a)) 
	  beta = ((-b - e)/(2*a))
	  return alpha,beta
def cubpoly(a,b,c,d):
	  alpha = (-b / a) / 3
	  a1 = a 
	  b1 = b + alpha*a
	  c1 = c + alpha*b
          beta , gamma = quadpoly(a1,b1,b2)
	  return alpha , beta , gamma
deg = input("Enter the degree of polynomial")
if deg == "quad":
	  a = float(input("Enter the coefficient of x^2 :"))
	  b = float(input("Enter the coefficient x :"))
	  c = float(input("Enter the constant :")) 
          alpha , beta = quadpoly(a,b,c)
	  print("The Roots of the given equation are,"+ alpha + " " + beta )
elif deg == "cube":
	  a = float(input("Enter the coefficient of x^3 :"))
	  b = float(input("Enter the coefficient x^2 :"))
	  c = float(input("Enter the coefficient x :"))
	  d = float(input("Enter the constant :")) 
	  alpha , beta , gamma = cubpoly(a,b,c,d)
	  print("The Roots of the given equation are,"+ alpha + " " + beta + " " + gamma )
