year = input("Enter a 4-digit year: ")

if year.isdigit() and len(year) == 4:
    year = int(year)
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(str(year) + " is a Leap Year.")
    else:
        print(str(year) + " is not a Leap Year.")
else:
    print("Invalid input! Please enter a valid 4-digit year.")
