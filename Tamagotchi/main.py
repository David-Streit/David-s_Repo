import os
import time
from datetime import datetime
import random
import gf
import pf
import hm


# put in this into the terminal to commit changes
"""
git add .
git commit -m "Update meiner Dateien"
git push
"""


# GAME START -----------------------------------------------------------------------------------------------
gf.clear_terminal()


print(f'Welcome to the Tamagotchi game. \n\nPlease enlarge your terminal to max size so that all information can be displayed. \n\nPress "Enter" when ready to start the game.')
input("")  # empty input to continue in the code

gf.loading_bar()

while True:  # main loop to be able to restart the game whithout restarting the program

    # MAIN MENU - checks what the player wants to do - create new pet - continue with an existing pet - or exit the game
    new = gf.main_menu()
    if new == "3":  # checks if the player wants to exit the game
        gf.exit_bar()
        break

    # Checks if the Pet name exists
    while True:
        gf.clear_terminal()
        loginpetname = input("What is your pet Username? ")
        if os.path.exists(loginpetname+".txt"):
            break
        else:
            print("This pet does not exist, try again")
            time.sleep(3)
            gf.clear_terminal()

    # Opens the Data from the pet textfile, so password can be checket later
    opendata = loginpetname + ".txt"
    name, password, hunger, clean, energy, entertainment, last_login = gf.load_pet_data(
        opendata)

    # checks password
    while True:
        passwordgiven = input("Please enter your password: ")

        if password == passwordgiven:
            gf.clear_terminal()
            print("Your password was correct")
            time.sleep(1)
            break
        else:
            print("Your password was not correct, please try again")
            time.sleep(1)
            gf.clear_terminal()

 # calculates time difference for damage
    hours_passed = gf.hours_since(last_login)

    # calculating damage on values
    hunger -= hours_passed * 3
    clean -= hours_passed * 3
    energy -= hours_passed * 3
    entertainment -= hours_passed * 3

    # --> Start in Game Menu loop
    while True:
        # checks after every game loop if the pet is still alive
        alive = gf.still_alive(hunger, clean, energy, entertainment)
        if alive == False:
            break

        gf.clear_terminal()

        # HANGMAN starts in one of three cases - it can only happen once every 2 hours after being logged out.
        # vor jeder Aktion Stunden neu berechnen
        hours_passed = gf.hours_since(last_login)

        # Hangman nur starten, wenn wirklich >= 2 Stunden vergangen sind
        if hours_passed >= 2:
            if random.randint(1, 3) == 1:
                result = hm.hangman(name)
                if result == 0:
                    hunger = 0
                    gf.safe(name, password, hunger,
                            clean, energy, entertainment)
                    break

        # nach Hangman immer neuen Timestamp setzen,
        # damit das Spiel nicht direkt wieder startet
        gf.safe(name, password, hunger, clean, energy, entertainment)

        # Timestamp wieder einlesen (für nächste Schleifenrunde)
        opendata = name + ".txt"
        with open(opendata, "r") as data:
            for line in data:
                if ":" in line:
                    key, value = line.strip().split(":", 1)
                    if key == "Last Timestamp":
                        last_login = value.strip()

        # --> printing current stats - MAIN PET INTERFACE
        print(f'Currently {name} has following stats:\n')
        print(f'--> Saturation: {hunger}')
        print(f'--> Cleanliness: {clean}')
        print(f'--> Energy: {energy}')
        print(f'--> Entertainment: {entertainment}')

        # printing User Interface
        print(r"""
            You have following options:
            
            Health:
                  1. Feed                                |\\_,-~/
                  2. Clean                               / _  _ |    ,--.
                  3. Play                               (  @  @ )   / ,-'
                  4. Sleep                               \ \_T_/-._( (
                  5. Heal                               /        `. \
                                                        |         _  \ 
                                                        \ \ ,  /      |
                                                        || |-_\__    /
                                                        ((_/`(____,-'  
            Menu: 
                  8. Pet settings
                  9. Safe and exit to main menu
                  """)

        # --> decision what action the player wants to do
        decison = input("What do you wanna do? Enter number: ")
        if decison == "1":
            hunger, clean = pf.feed(name, hunger, clean)
        elif decison == "2":
            clean = pf.clean(name, clean)
        elif decison == "3":
            entertainment, clean = pf.play_hide(name, entertainment, clean)
        elif decison == "4":
            energy = pf.sleep(energy, name)
        elif decison == "5":
            print("--Healing is coming soon")
        elif decison == "8":
            decision_deleate = ""
            name, password, decision_deleate = pf.pet_settings(
                name, password, decision_deleate)
            if decision_deleate == "YES":
                break
            gf.safe(name, password, hunger, clean, energy, entertainment)

        elif decison == "9":
            gf.safe(name, password, hunger, clean, energy, entertainment)
            break

    # End screeen
    gf.clear_terminal()

    if decision_deleate == "YES":
        print(f'{name} has been deleated permanently from the game.')
    else:
        if clean > 0 and hunger > 0:
            print(f'''Thanks for playing, please come back soon, {name} will miss you.
                              -> Please come back whitin a Day or {name} may be dead...''')

            # Prints picture
            with open("goodbye.txt", "r", encoding="utf-8") as file:
                content = file.read()
                print(content)
        else:
            print("Your Pet is dead")

        time.sleep(4)
        gf.clear_terminal()
