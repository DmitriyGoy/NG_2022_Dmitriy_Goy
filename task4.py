print("Enter the values ​​of the coefficients for the equation: ")
print("a*x^2 + b*x + c = 0")
a = float(input("a =  "))
b = float(input("b =  "))
c = float(input("c =  "))
print("================================================")

discr = (b ** 2 - 4 * a * c)
print("Discriminant = ", discr)
if discr > 0:
    x1 = -b + discr ** 0.5/ 2*a
    x2 = -b - discr ** 0.5/ 2*a
    print(f"x1 = {x1}; x2= {x2}.")
elif discr == 0:
    x = -b / 2 * a
    print(f"x = {x}")
elif discr < 0:
    print("Quadratic equation has no roots.")