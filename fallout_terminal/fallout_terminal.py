# A  simplified remake of Bethesda's "Fallout" series' Terminal Hacking minigame

import words
import random
import sys
import time

# some global fields
victory = False
attempts_remaining = 4
PASSWORD_LENGTH = 5
sleepytime = .05  # time to wait between printing, for aesthetics

# get 10 unique random words
TEN_WORDS = []
for i in range(10):
    random_word = random.choice(words.words)
    if random_word not in TEN_WORDS:
        TEN_WORDS.append(random_word)

# the password becomes a random word from the list of 10
PASSWORD = random.choice(TEN_WORDS)


# print the 10 choices in two columns for neatness
def print_choices():
    print("")
    time.sleep(sleepytime)
    for i in range(10):
        print(TEN_WORDS[i] + (" " if i % 2 == 0 else "\n"), end="")
        time.sleep(sleepytime)
    print("")


# The number chars in the attempt that match the password and are in the correct position
def likeness(attempt):
    likeness = 0
    try:
        for i in range(PASSWORD_LENGTH):
            if attempt[i] == PASSWORD[i]:
                likeness += 1
    except Exception:
        return 0
    return likeness


# Start game
print("""
The Fallout(TM) Terminal Hacking Minigame (An Imitation)
Instructions: Guess the password out of the 10 possible choices.
"LIKENESS" is the number of matching letters in the correct position.

---------------------------------------
  ROBCO INDUSTRIES TERMALINK PROTOCOL
---------------------------------------""")
time.sleep(sleepytime)

user_input = ""
while (attempts_remaining > 0):

    print("\nATTEMPTS REMAINING:", attempts_remaining)
    print_choices()
    print("ENTER PASSWORD NOW:\n>>", end="")

    user_input = input().upper()

    # For debug: enter "EXIT" to exit the game
    if user_input == "EXIT":
        sys.exit()

    #  If player guessed correctly, player wins and loop ends
    if user_input == PASSWORD:
        victory = True
        break

    # If player's attempt is not one of the choices, ask again
    if (user_input not in TEN_WORDS):
        print("Attempt must be one of the choices. Try again.")
        continue

    # The user guessed an incorrect choice. Print likeness of attempt
    attempt_likeness = likeness(user_input)
    print("LIKENESS:", attempt_likeness)

    attempts_remaining -= 1
# End main game loop

# Print endgame results
if victory:
    print("ACCESS GRANTED")
else:
    print("TERMIAL LOCKED\nPLEASE CONTACT AN ADMINISTRATOR")
