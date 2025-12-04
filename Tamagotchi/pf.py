# In this file you will find all pet functions
# Please do not run this file directly, please run main.py instead.

import os
import time
from datetime import datetime
import random
import gf


def feed(name, hunger, clean):
    while True:
        gf.clear_terminal()
        number_of_food = random.randint(5, 10)
        print("How many apples are there? Look carefully!")
        time.sleep(2)
        gf.clear_terminal()
        print("🍎 "*number_of_food)
        time.sleep(2)
        gf.clear_terminal()

        while True:
            guess_input = input("How many apples were there? ")
            try:
                guess = int(guess_input)
                break
            except ValueError:
                print("Please enter a valid number.")
                time.sleep(1)

        if guess == number_of_food:
            # First drawing (Already fixed)
            hunger = min(hunger + 50, 100)
            clean = min(clean - 15, 100)
            print(f'Correct, {name} is eating the apples! 🍎🍎🍎')
            print(r'''
                  
            
        |\__/,|   (`\
        |_ _  |.--.) )
        ( T   )     /
        ((🍎_((/((_/        
            
            ''')
            time.sleep(3)
            gf.clear_terminal()

            print(f'{name} has eaten well and is happy!')
            print(r'''
                  

         |\\_,-~/
         / _  _ |    ,--.
        (  @  @ )   / ,-'
        \ \_T_/-._( (
        /        `. \
        |        _  \ |
        \ \ ,  /      |
        || |-_\__   /
        ((_/`(____,-'  
            ''')
            time.sleep(3)

            break
        else:
            print("Wrong! Try again.")
            time.sleep(1)
    return hunger, clean


def clean_pet(name, clean):
    clean = min(clean + 50, 100)

    print(name, "gets cleaned...")
    time.sleep(4)
    print(name, "is now clean!")
    print("The new Cleanliness level is", clean)

    return clean


def play_hide(name, entertainment, clean):
    gf.clear_terminal()
    number_to_guess = random.randint(1, 3)
    print(f'''{name} is hiding behind one of three Trees
    Guess which Tree.''')
    print(r'''
           
       _-_                   _-_                   _-_
    /~~   ~~\             /~~   ~~\             /~~   ~~\
 /~~    ~    ~~\       /~~   ~     ~~\       /~~    ~    ~~\
{  ~     ~  ~   }     {   ~   ~   ~   }     {  ~  ~ ~   ~   }
 \  _- ~   -_  /       \  _-  ~  -_  /       \  _-  ~  -_  /
   ~  \\ //  ~           ~  \\ //  ~           ~  \\ //  ~
       | |                   | |                   | |    
       | |                   | |                   | |     
      // \\                 // \\                 // \\
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
          ''')

    while True:
        guessed_number = int(input("Enter 1, 2 or 3: "))
        if guessed_number == number_to_guess:
            entertainment += 50  # FIX THAT SHIT ------------------------ Variable can be over 100
            clean -= 10
            gf.clear_terminal()
            print(f"Congrats, you've found {name}")
            print(r'''   
              _-_                             
           /~~   ~~\                          
        /~~         ~~\                       
       {               }            Meow!          
        \  _-     -_  /           /            
         ~  \\ //  ~      |\__/,|   (`\
             | |          |_ _  |.--.) )
             | |          ( T   )     /
            // \\         (( _((/((_/
                  
                  ''')
            # value change here----
            time.sleep(3)
            break
        else:
            print("This was not the correct number, try again.")
            time.sleep(2)

    return entertainment, clean


def sleep(energy, name):
    gf.clear_terminal()
    energy = min(energy + 50, 100)

    print(name, "is sleeping now...zzZ")
    print(r'''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣶⣶⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣽⡿⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⠶⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠷⠶⢤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣶⣶⣶⡶⠀⠀⠀⠉⠻⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣾⣿⣟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠙⠻⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⡶⠶⠶⠟⠿⠿⠛⠋⠋⠛⠛⠛⠳⠶⣤⣤⣤⣤⣤⣄⣤⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣶⣴⠶⠿⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠃⠀⠉⠉⠋⣰⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣿⠾⠿⠿⠟⠛⠛⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⣿⣄⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⠻⣦⣀⠀⣼⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠙⢻⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣇⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⠀⣀⣾⡯⠽⡛⠛⠳⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⡆⠀⠀⠀⠀⠀⠀⠀⣀⣀⡀⠀⠀⠀⠀⠀⠀⢿⣶⠴⠶⠛⠛⠛⠉⣼⣾⣿⣿⡋⠉⠉⠻⠂⠈⢿⣦⣀⣠⣤⣤⣤⣄⣀⠀⠀⠀⠀
⠀⠀⠀⢀⣤⣶⣿⣥⣤⡛⠛⠿⠿⠿⠿⠿⠛⠁⠀⠀⣀⣤⡀⠀⠀⠀⠀⠀⠀⢀⣠⣴⡿⠷⠿⣷⣍⠉⠓⠒⠀⠀⠀⠈⢻⡉⠉⠉⠙⡋⠉⠙⠳⣦⠀
⠀⠀⠰⢋⡭⠖⣹⣿⡿⣿⣤⣄⣀⣀⣀⠀⠀⠀⠀⠀⠙⠋⠁⠀⠀⠀⠀⣠⣴⡿⠋⠁⠀⠀⠀⢼⠟⠀⠀⠀⠀⠀⠀⢰⣾⣿⣥⣴⣦⣶⣶⠀⢠⢿⡧
⠀⢠⡖⠋⣀⡼⠛⣽⡿⠻⠉⠉⠉⠉⠙⠻⢶⣦⣄⡀⠀⠀⠀⠀⠀⢀⣴⡿⠋⠀⠀⠀⠀⠀⢀⣦⠀⠀⠀⠀⠀⠀⣴⣿⠏⠀⠀⣠⣴⡿⠏⠀⣼⣾⡇
⠀⠈⢀⣴⠟⠀⢸⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣦⡀⠀⠀⢀⣼⡿⠁⠀⠀⠀⠀⠀⣠⣾⠃⢀⣠⣤⣴⣶⡿⠟⢁⣴⣾⠟⠋⠁⠀⢀⣼⣿⠏⠀
⠀⠀⠘⠛⠀⠀⢸⣧⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣶⡶⢾⡟⠁⠀⠀⣀⣤⡶⠿⠟⠙⠛⠛⠉⠉⠉⠀⣠⣴⡿⠏⠀⠀⢀⣠⣴⣿⡿⠛⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠙⠓⠒⠦⣤⣀⠀⠀⠀⣀⠀⠀⢀⣬⡿⠀⠘⠷⢶⡶⠾⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣐⣦⣲⣿⣿⡿⠛⠋⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠛⠲⠾⠿⠟⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠛⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀
      ''')
    time.sleep(5)
    gf.clear_terminal()

    # 50% chance nightmare
    if random.randint(1, 2) == 2:
        while True:
            try:
                user_input = input(
                    f'''Oh no, your {name} has a nightmare and is scared!
To save him, press 1 to calm him down: '''
                )

                if user_input == "1":
                    print(f"{name} is now calm and sleeping again... zzZ")
                    time.sleep(5)
                    print(name, "has slept and is full of energy!")
                    print(f"The new Sleep level is {energy}")
                    gf.clear_terminal()
                    return energy

                else:
                    raise ValueError("Invalid input")  # force except block

            except ValueError:
                print("You did the wrong input!")
                time.sleep(2)
                gf.clear_terminal()

    # If no nightmare triggered
    print(name, "has slept and is full of energy!")
    print(f"The new Sleep level is {energy}")
    gf.clear_terminal()
    return energy


def clean(name, clean):
    gf.clear_terminal()
    print("Press the correct key to clean your pet!")
    time.sleep(4)

    directions = {
        "←": "a",
        "↑": "w",
        "→": "d",
        "↓": "s"
    }

    score = 0
    while True:
        for _ in range(5):
            gf.clear_terminal()
            arrow, key_needed = random.choice(list(directions.items()))
            print(r'''
                
                        ↑                |\__/,| (`\
                        w                |_ _  |.--.) )
                  ← a       d →          ( T   )     /
                        s               ((  (( / ((_/
                        ↓               
                ''')
            print(f'Swipe: {arrow}')
            user_input = input("Your key: ").strip().lower()

            if user_input == key_needed:
                print("✔ Nice swipe!")
                score += 1
            else:
                print("X Wrong key!")

        if score >= 5:
            print(f'\n{name} is now clean! ✨')
            clean = min(clean + 50, 100)
            time.sleep(4)
            break
        else:
            print(
                f'\n {name} is still dirty... Try again, every swipe has to be correct.')
        time.sleep(6)
        gf.clear_terminal()

    return clean


def pet_settings(name, password, decision_deleate):
    while True:
        gf.clear_terminal()
        decision = input(
            f' Pet settings of {name}\n\n\n1. Change Name\n2. Deleate Pet\n3. Exit Pet settings\n\nEnter 1 or 2 or 3: ')

        if decision == "1":
            gf.clear_terminal()
            old_file = f"{name}.txt"
            name = input("How do you want to call your Pet?")
            new_file = f"{name}.txt"
            os.rename(old_file, new_file)
            try:
                gf.clear_terminal()
                if input("Enter your password: ") == password:
                    gf.clear_terminal()

                    print(
                        f'Pet name change was sucessfull. \nIn future you will have to login with {name}')

            except:
                gf.clear_terminal()
                print("Your password was wrong. ")
                time.sleep(3)

        elif decision == "2":
            gf.clear_terminal()
            decision_deleate = input(
                f'''Are you sure you want to deleate your Pet {name} ? This process can't be undone \n\nType "YES" or "NO" ''')
            if decision_deleate == "YES":
                gf.clear_terminal()
                print(f"Your Pet is now getting deleated. {decision_deleate}")
                time.sleep(5)
                data_to_deleate = name + ".txt"
                if os.path.exists(data_to_deleate) and data_to_deleate.endswith(".txt"):
                    os.remove(data_to_deleate)
                    break
            else:
                print("Your input was wrong, you will get back to Menu.")
                time.sleep(5)
                break

        elif decision == "3":
            break

    return name, password, decision_deleate
