software_package = int(99)

order = int(input("Please enter the amount of purchased packages: "))

if order < 1:
    print("Are you retarded bruv?")
elif 1 <= order <= 9:
    print(f"Your total is {software_package * order} USD")
elif 10 <= order <= 19:
    print(
        f"Your total is {float(software_package * order * 0.9)} USD with a discount of 10%")
elif 20 <= order <= 49:
    print(
        f"Your total is {float(software_package * order * 0.8)} USD with a discount of 20%")
elif 50 <= order <= 99:
    print(
        f"Your total is {float(software_package * order * 0.7)} USD with a discount of 30%")
elif order >= 100:
    print(
        f"Your total is {float(software_package * order * 0.6)} USD with a maximum discount of 40%")
