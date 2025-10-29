day = int(input("Please enter a day (between 1-31): "))
if day < 1 or day > 31:
    print("Please try again")

month = int(input("Please enter a month (between 1-12): "))
if month < 1 or month > 12:
    print("Please try again")

year = int(input("Please enter a year in two-digit form: "))
if 10 >= year >= 99:
    print("Try again")

if day * month == year:
    print("The date is magic")
else:
    print("The date is not magic")
