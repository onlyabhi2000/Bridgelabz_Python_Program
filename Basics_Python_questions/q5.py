#  How do you handle exceptions in Python?

try :
    x= 10/0
except Exception as e:
    print("An error occurred: ", e)