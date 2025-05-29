try:
    age = int(input("Enter your age :"))
    if age<0:
        raise ValueError("invalid age")
    print("your age is :", age)
    
except ValueError as var:
    print(var)

finally:
    print("this will be printed in any condition")

