height = float(input("Please enter your height (e.g. 175cm = 1.75): "))
weight = float(input("Please enter your weigh (75kg = 75): "))

BMI = weight / height ** 2

if BMI < 18.5:
    print(f"The person is underweight with a BMI of {BMI:.1f}")
elif 18.5 <= BMI <= 25:
    print(f"The person's weight is optimal with a BMI of {BMI:.1f}")
elif BMI > 25:
    print(f"The person is overweight with a BMI of {BMI:.1f}")

# :.1f can be used to limit the decimal places in output
