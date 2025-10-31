budget = float(input("Please enter your budget for the month: "))

expense = 1
total_expenses = 0

while expense != 0:
    expense = float(
        input("Please enter an expense (or enter 0 to see total): "))
    total_expenses += expense

if total_expenses <= budget:
    print(
        f"Your total expenses are {total_expenses} and you are within the given budget")
elif total_expenses > budget:
    print(
        f"Your total expenses are {total_expenses} and you are over the given budget")
