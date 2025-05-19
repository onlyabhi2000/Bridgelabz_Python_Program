# Write a program ​Distance.java t​hat takes two integer command-line arguments x
# and y and prints the Euclidean distance from the point (x, y) to the origin (0, 0). The
# formulae to calculate distance = sqrt(x*x + y*y). Use Math.power function

import math

def calculate_distance(x,y):
    distnace = math.sqrt(math.pow(x,2) + (math.pow(y,2)))
    return distnace


x = int(input("ENter the value of X"))
y = int(input("ENter the value of Y"))

print("Calculated distance is :")
print(calculate_distance(x,y))