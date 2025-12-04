# in this file you will find every defintion about the gamestructure

import os
import time
from datetime import datetime
import random


from datetime import datetime


def hours_since(timestamp_string: str) -> int:

    # Takes a timestamp string in format '%Y-%m-%d %H:%M:%S' and returns how many whole hours have passed since then.

    # Convert saved timestamp back to datetime
    last = datetime.strptime(timestamp_string, "%Y-%m-%d %H:%M:%S")

    # Get current time
    now = datetime.now()

    # Time difference
    diff = now - last

    # Convert to hours (integer)
    hours = int(diff.total_seconds() // 3600)

    return hours


def main_menu():
    """
    Displays the main menu and handles creating a new pet or continuing with an existing one.
    Returns:
        str: "1" for new pet, "2" for continue, "3" for exit
    """
    while True:
        clear_terminal()  # keep your existing function call
        new = input(f'''MAIN MENU
                      
You have following options:

1. Create a new pet
2. Continue with an existing one.
3. Exit

Input number: ''')

        # Option 1 → create new pet
        if new == "1":
            namenew = input("How do you want to call your new Pet? ")
            print(f'{namenew} is a cute name!')
            passwordnew = input("Enter a password to save your pet: ")

            now = datetime.now()
            timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

            dataname = f"{namenew}.txt"
            with open(dataname, "w") as data:
                data.write(f"Petname:{namenew}\n")
                data.write(f"Password:{passwordnew}\n")
                data.write("Hunger:50\n")
                data.write("Clean:50\n")
                data.write("Energy:50\n")
                data.write("Entertainment:100\n")
                data.write(f"Last Timestamp: {timestamp}\n")

            print("Thank you, please log in now.")
            time.sleep(1)
            return "1"   # Send result back

        # Option 2 → continue existing pet
        elif new == "2":
            print("Alright, please login")
            time.sleep(1)
            return "2"

        # Option 3 → exit
        elif new == "3":
            return "3"

        else:
            print("Your input did not make sense")
            time.sleep(1)
            clear_terminal()  # keep your existing function call


# reads the current text filedata
def load_pet_data(filename):
    name = None
    password = None
    hunger = None
    clean = None
    energy = None
    entertainment = None
    last_login = None

    with open(filename, "r") as data:
        for line in data:
            if ":" in line:
                key, value = line.strip().split(":", 1)

                if key == "Petname":
                    name = value
                elif key == "Password":
                    password = value
                elif key == "Hunger":
                    hunger = int(value)
                elif key == "Clean":
                    clean = int(value)
                elif key == "Energy":
                    energy = int(value)
                elif key == "Entertainment":
                    entertainment = int(value)
                elif key == "Last Timestamp":
                    last_login = value.strip()

    return name, password, hunger, clean, energy, entertainment, last_login


# clears terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


# loading bar for design purpose
def loading_bar():
    loadingbar = "-"
    for i in range(70):
        loadingbar += "-"
        clear_terminal()
        print("Starting game:")
        print(loadingbar)
        time.sleep(0.02)


# checks if the animal is still alive
def still_alive(hunger, clean, energy, entertainment):
    alive = True

    if hunger <= 0 or clean <= 0 or energy <= 0 or entertainment <= 0:
        print("Your PET is dead...")
        time.sleep(2)
        alive = False

    return alive


# safes current pet stat
def safe(name, password, hunger, clean, energy, entertainment):  # SAVE <----------------- correct
    dataname = (f"{name}.txt")

    # 1. Get the current time of the save
    now = datetime.now()
    timestamp_str = now.strftime("%Y-%m-%d %H:%M:%S")

    with open(dataname, "w") as data:
        data.write(f"Petname:{name}\n")
        # Use the correct 'password' variable
        data.write(f"Password:{password}\n")
        data.write(f"Hunger:{hunger}\n")
        data.write(f"Clean:{clean}\n")
        data.write(f"Energy:{energy}\n")
        data.write(f"Entertainment:{entertainment}\n")
        data.write(f"Last Timestamp: {timestamp_str}\n")


def exit_bar():
    loadingbar = "-"
    for i in range(70):
        loadingbar += "-"
        clear_terminal()
        print("Exiting Tamagochi program:")
        print(loadingbar)
        time.sleep(0.02)


# Tells the user to use the main file
clear_terminal()
print("Do not run this file directly, please run main.py instead.")
