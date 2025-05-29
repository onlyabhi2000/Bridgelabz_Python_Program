import sys
n1 = int(input("Entee the first number "))
n2 = int(input("Enter the second number"))
try:
    div = n1/n2
    print(div)
# except:
#     print("Something went wrong")
# except Exception as var:
#     print(var)
#     print(var.__class__)

except:
    print(sys.exc_info()[1])
else:
    print("this will be printed only if exception did not occur")
finally:
    print("This should be prited always")


    