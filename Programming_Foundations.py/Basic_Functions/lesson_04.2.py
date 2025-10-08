name = ""
count = 0
while not name and count <= 5:

    name = input("What is your name? ")
    count += 1
    print(count)
    if count > 5:
        exit()
    name = input("What is your name? ")
    if name:
        print(f"The name is given: {name}")
    else:
        print("The name was not given...")
