n = int(input("Enter a positive integer : "))

if n <= 0:
    print("N must be greater than 0.")
else:
    harmonic = 0.0
    i = 1
    while i <= n:
        harmonic += 1 / i
        i += 1

    print(f"The {n}th Harmonic number is: {harmonic}")
