import random
import time
import os
from words import word_list
import gf


def hangman(name):
    def get_word():
        word = random.choice(word_list)
        return word.upper()

    def play(word):
        guessed = False
        guessed_letters = []
        guessed_words = []
        tries = 6

        gap = "\n\n"

        # reveal first letter
        first_letter = word[0]
        guessed_letters.append(first_letter)

        word_completion = ""
        for letter in word:
            if letter == first_letter:
                word_completion += first_letter
            else:
                word_completion += "_"

        # clear screen
        os.system('cls' if os.name == 'nt' else 'clear')

        print(f'''Oh no, {name} got kidnaped.
You will have to safe him. Solve this hangman Quiz ''')
        print("-----------------------------------------")
        print("CATEGORY: ANIMALS OR INSECTS")
        print("-----------------------------------------")
        print(display_hangman(tries))
        print(word_completion)
        print(gap)

        while not guessed and tries > 0:
            guess = input("Please guess a letter or word: ").upper()

            os.system('cls' if os.name == 'nt' else 'clear')
            print("CATEGORY: ANIMALS OR INSECTS")
            print("----------------------------")

            # Single letter
            if len(guess) == 1 and guess.isalpha():
                if guess in guessed_letters:
                    print("You already guessed the letter", guess)

                elif guess not in word:
                    print(guess, "is not in the word.")
                    tries -= 1
                    guessed_letters.append(guess)

                    # panic mode hint
                    if tries == 1:
                        print(gap)
                        print("!!! DANGER: LAST TRY !!!")

                        missing_letters = [
                            l for l in word if l not in guessed_letters]

                        if len(word) >= 7:
                            print("This is a long word. I will reveal 2 letters...")

                            if len(missing_letters) >= 2:
                                hint1 = random.choice(missing_letters)
                                missing_letters.remove(hint1)
                                hint2 = random.choice(missing_letters)
                                guessed_letters.extend([hint1, hint2])
                                print("Revealed:", hint1, "and", hint2)

                            elif len(missing_letters) == 1:
                                hint1 = missing_letters[0]
                                guessed_letters.append(hint1)
                                print("Revealed:", hint1)
                        else:
                            print("Here is a hint to help you…")
                            if missing_letters:
                                hint1 = random.choice(missing_letters)
                                guessed_letters.append(hint1)
                                print("Revealed:", hint1)

                        # update board
                        word_completion = "".join(
                            [l if l in guessed_letters else "_" for l in word])

                else:
                    print("Good job,", guess, "is in the word!")
                    guessed_letters.append(guess)
                    word_completion = "".join(
                        [l if l in guessed_letters else "_" for l in word])

                    if "_" not in word_completion:
                        guessed = True

            # Word guess
            elif len(guess) == len(word) and guess.isalpha():
                if guess in guessed_words:
                    print("You already guessed the word", guess)
                elif guess != word:
                    print(guess, "is not the word.")
                    tries -= 1
                    guessed_words.append(guess)
                else:
                    guessed = True
                    word_completion = word

            else:
                print("Not a valid guess.")

            print(display_hangman(tries))
            print(word_completion)
            print(gap)

        if guessed:
            print("Congrats, you guessed the word! You win!")
            return True   # WIN
        else:
            print("Sorry, you ran out of tries. The word was " + word + ".")
            return False  # LOSS

    def display_hangman(tries):
        stages = [
            # final state: head, torso, both arms, and both legs
            r"""
                        --------
                        |      |
                        |    )\_/(
                        |    'o.o'
                        |    =( )=
                        |      U
                        -
                        """,
            # head, torso, both arms, and one leg
            r"""
                        --------
                        |      |
                        |    )\_/(
                        |    'o.o'
                        |    =( )=
                        |
                        -
                        """,
            # head, torso, and both arms
            r"""
                        --------
                        |      |
                        |    )\_/(
                        |    'o.o'
                        |
                        |      
                        -
                        """,
            # head, torso, and one arm
            r"""
                        --------
                        |      |
                        |    )\_
                        |    'o.o
                        |
                        |    
                        -
                        """,
            # head and torso
            r"""
                        --------
                        |      |
                        |    )\
                        |    'o
                        |
                        |    
                        -
                        """,
            # head
            r"""
                        --------
                        |      |
                        |    )\
                        |    
                        |      
                        |    
                        -
                        """,
            # initial empty state
            r"""
                        --------
                        |      |
                        |      
                        |    
                        |      
                        |    
                        -
                        """
        ]
        return stages[tries]

    def main():
        word = get_word()
        result = play(word)

        if result is False:
            return 0   # hunger = 0
    gf.clear_terminal()
    return main()
