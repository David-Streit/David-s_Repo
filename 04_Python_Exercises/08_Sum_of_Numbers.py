number = 1
sum = 0

while number >= 0:
    number = int(input(
        "Please enter a positive integer, enter a negative integer to display sum: "))
    if number >= 0:
        sum += number

print(f"The sum of the entered numbers is {sum}")
