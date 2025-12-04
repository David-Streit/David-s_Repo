Tamagotchi Console Game
Analysis
Problem

In real life it is easy to forget regular tasks like feeding or caring for a pet. There is no direct, visible feedback on what happens if you neglect a pet over time. Our application simulates a digital pet with simple health values (hunger, cleanliness, energy, entertainment) that decrease while the player is away. This lets the user see the consequences of their actions (or inaction) and practice taking care of a pet in a playful and time-based way.

Scenario

A user starts the game in a terminal and is welcomed by a loading bar and a main menu. They can create a new pet by choosing a name and password, or log into an existing pet. The pet's status values are loaded from a save file, reduced based on how many hours have passed since the last login, and then the user interacts with their pet using console input. They can feed, clean, play with, or let the pet sleep through mini-games, and finally save and exit. If they stay away too long or neglect the pet, it can die.

User stories

As a player, I want to create a new pet with a name and password so that my progress is saved between sessions.
gf

As a player, I want to log in to an existing pet so that I can continue caring for it later.

As a player, I want to see my pet's current stats (hunger, cleanliness, energy, entertainment) so that I know which action is needed.

As a player, I want to play interactive mini-games (feed, clean, play, sleep) so that I can improve the pet's stats in a fun way.
pf

As a player, I want the game to remember when I last played and reduce stats accordingly so that the pet really feels "alive over time".

As a player, I want to rename or delete my pet via settings so that I stay in control of my save files.

Use cases
Create Pet

User chooses "Create a new pet" in the main menu.

Application asks for pet name and password and creates a <name>.txt file with initial stats and a timestamp.

gf

Login Existing Pet

User chooses "Continue with an existing one".

Application checks whether <name>.txt exists and validates the password.

Time-based Stat Update

On login, the program reads the last timestamp, computes how many hours passed, and decreases all stats accordingly.

Interact With Pet

User chooses actions (Feed, Clean, Play, Sleep) via numeric input and plays mini-games to change the stats.

Random Hangman Event

After being logged out for at least 2 hours, a random hangman event can trigger, which may end with the pet dying if the word is not guessed.

Pet Settings

User can rename their pet (rename file on disk) or delete it permanently after confirming "YES".

pf

Save and Exit

User saves current stats, updates the timestamp, and leaves the game. A goodbye screen with ASCII art is shown.

Project Requirements

Each app must meet the following three criteria in order to be accepted:

Interactive app (Console input)

Data validation

File processing

1. Interactive app (Console input)

The application is fully interactive and operates via console input and output.

The main menu lets the user choose between creating a new pet, continuing with an existing one, or exiting the game.

After login, the in-game menu allows the user to choose actions such as feeding, cleaning, playing, sleeping, opening pet settings, or saving and exiting.

All mini-games (apple counting, swipe directions, hide and seek, sleep with nightmares, and hangman) are controlled by user input in the console.

Example of an interactive loop in the feed mini-game:

while True:
    guess_input = input("How many apples were there? ")
    try:
        guess = int(guess_input)
        break
    except ValueError:
        print("Please enter a valid number.")
        time.sleep(1)


pf

This interaction pattern appears in different forms throughout the project, ensuring that the user always actively controls the pet via the keyboard.

2. Data validation

The application validates user input at several critical points to ensure the game does not crash and behaves predictably.

Examples:

Pet file existence: when logging in, the program checks if <name>.txt exists. If not, it prints an error and asks again.
main

Password check: password input is compared to the stored password, and the user is kept in a loop until the correct password is entered.

Numeric input validation in the feed mini-game: the input is converted to int inside a try/except block, and invalid input is rejected without crashing the program.
pf

Swipe mini-game: only the correct keys (w, a, s, d) count as valid input for the cleaning mini-game. Anything else is treated as a wrong swipe but handled gracefully.
pf

Delete confirmation: deleting a pet requires typing "YES" explicitly. All other inputs lead back to the menu without deleting the file.
pf

These checks help maintain consistent game logic, prevent invalid states, and give the user clear feedback when inputs are not acceptable.

3. File processing

The project uses multiple files to persist data and to display additional content.

Pet save files

For each pet, a separate <name>.txt file is used to store:

Pet name

Password

Hunger, Clean, Energy, Entertainment values

Last timestamp (for time-based decay)

Reading pet data

The function load_pet_data reads the save file and parses each line into the corresponding variables:

with open(filename, "r") as data:
    for line in data:
        if ":" in line:
            key, value = line.strip().split(":", 1)
            if key == "Petname":
                name = value
            elif key == "Hunger":
                hunger = int(value)
            # ...


gf

Saving pet data

The function safe (save) writes the current stats and a fresh timestamp back into the text file:

with open(dataname, "w") as data:
    data.write(f"Petname:{name}\n")
    data.write(f"Password:{password}\n")
    data.write(f"Hunger:{hunger}\n")
    data.write(f"Clean:{clean}\n")
    data.write(f"Energy:{energy}\n")
    data.write(f"Entertainment:{entertainment}\n")
    data.write(f"Last Timestamp: {timestamp_str}\n")


gf

Goodbye screen

When leaving the game, goodbye.txt is read and printed to show an ASCII art farewell screen.

These file operations allow the game to maintain persistent state between different runs and provide a simple, transparent format that is easy to inspect or back up.

Implementation
Technology

Python 3.x

Environment: any standard Python environment with a terminal (for example VS Code terminal, Git Bash, or system terminal)

No external libraries - only standard modules are used:

os for terminal clearing and file operations

time for delays and timing effects

datetime for timestamps and time differences

random for mini-game randomness and hangman word selection

Repository structure
Tamagotchi/
├── main.py       # Entry point, login flow, main game loop, hangman trigger
├── gf.py         # General game functions (menus, loading bar, time handling, save/load)
├── pf.py         # Pet functions (feed, clean, play, sleep, pet settings)
├── hm.py         # Hangman mini-game and display logic
├── words.py      # Word list (animals and insects) for the hangman event
├── goodbye.txt   # ASCII art shown on exit when the pet is alive
└── README.md     # Project documentation

How to run

Make sure Python 3 is installed on your system.

Open a terminal in the project folder (where main.py is located).

Run the program:

python main.py


or on some systems:

py main.py


Follow the instructions in the console to create or log into a pet and play the game.

Libraries used

All libraries used are from the Python standard library:

os

Clear the terminal screen to create a cleaner game experience.

Check for the existence of pet save files and delete them when requested.

time

Add short delays to make animations (loading bars, mini-game transitions) and messages more readable.

datetime

Store and parse timestamps and calculate how many hours passed between sessions so that stats can decay over time.

random

Choose random numbers and words for the different mini-games and events (apples, hide and seek, swipe directions, nightmares, hangman words).

These modules were chosen because they provide all necessary functionality for console interaction, randomness, and simple file-based persistence without requiring extra installations.