age = int(input("Enter the age of a person: "))

if age <= 1:
    print("The person is an infant")
elif age > 1 and age < 13:
    print("The person is an child")
elif age >= 13 and age < 20:
    print("The person is a teenager")
elif age >= 20:
    print("The person is an adult")
