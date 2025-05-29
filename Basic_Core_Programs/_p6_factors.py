
n = int(input("Enter a positive integer"))

if n <= 1:
    print("Enter an integer greater than 1.")
else:
    print(f"Prime factors of {n} are:")
    
    i = 2
    while i * i <= n:
        if n % i == 0:
            print(i)
            n = n // i
        else:
            i += 1

    if n > 1:
        print(n)

