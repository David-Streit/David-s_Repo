year = int(input("Please enter a year: "))

if year % 100 == 0 and year % 400 == 0:
    print(f"{year} is a leap year and February has 29 days")
elif year % 4 == 0:
    print(f"{year} is a leap year and February has 29 days")
else:
    print(f"{year} is not a leap year and February has 28 days")
