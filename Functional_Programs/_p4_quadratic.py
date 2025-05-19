import math
def quadratic(a ,b , c):
    delta = b*b + 4*a*c
    print(f"delta value is : {delta}")
    root1 = (-b + math.sqrt(delta)) / (2 * a)
    root2 = (-b - math.sqrt(delta)) / (2 * a)
    print("Roots are :")
    return root1 , root2


a = int(input("Enteer the value of x :"))
b = int(input("ENter the value of y :"))
c = int(input("ENter the vlaue of c :"))

print(quadratic(a , b, c))


