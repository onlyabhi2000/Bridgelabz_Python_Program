import math

class LineComparison:
    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def calculate_length(self):
        return math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)

    def __str__(self):
        return f"Line(({self.x1}, {self.y1}) to ({self.x2}, {self.y2}))"

def compare_lines(line1, line2):
    length1 = line1.calculate_length()
    length2 = line2.calculate_length()

    print(f"Length of line 1: {length1}")
    print(f"Length of line 2: {length2}")

    if length1 == length2:
        print("Both lines are equal.")
    elif length1 > length2:
        print("Line 1 is longer.")
    else:
        print("Line 2 is longer.")


line1 = LineComparison(0, 0, 3, 4)  
line2 = LineComparison(1, 1, 4, 5) 

print(line1)
print(line2)

compare_lines(line1, line2)
