N = input("Enter a value for N : ")

if N.isdigit():
    N = int(N)
    if 0 <= N < 31:
        print("Powers of 2 up to " + str(N))
        for i in range(N + 1):
            print("2^" + str(i) + " = " + str(2 ** i))
    else:
        print("Please enter a number between 0 and 30.")
else:
    print("Invalid input! Please enter a valid number.")
