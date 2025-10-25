price = float(input("Please enter the bill amount: "))

tip = price*0.18
sales_tax = price*0.07
total = price + tip + sales_tax

print(f"Price: {price:.2f}")
print(f"Tip: {tip:.2f}")
print(f"Sales Tax: {sales_tax:.2f}")
print(f"Total: {total:.2f}")
