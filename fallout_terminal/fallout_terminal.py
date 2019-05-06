"""A  simplified remake of Bethesda's "Fallout" series' Terminal Hacking Minigame"""

import words, random, sys, time

#some global fields
victory = False
attempts_remaining = 4
PASSWORD_LENGTH = 5
sleepytime = .05 #time to wait between printing, for . ~ a e s t h e t i c s ~ .

#get 10 unique random words
TEN_WORDS = []
for i in range(10):
	random_word = random.choice(words.words)
	if random_word not in TEN_WORDS:
		TEN_WORDS.append(random_word)

#the password becomes a random word from the list of 10
PASSWORD = random.choice(TEN_WORDS)

#print the 10 choices in two columns for neatness
def print_choices():
	print("")
	time.sleep(sleepytime)
	for i in range(10):
		print(TEN_WORDS[i] + (" " if i%2==0 else "\n"), end="")
		time.sleep(sleepytime)
	print("")

#returns how many characters in the attempt match the password, and are in the correct place
def likeness(attempt):
	likeness = 0
	try:
		for i in range(PASSWORD_LENGTH):
			if attempt[i] == PASSWORD[i]:
				likeness += 1
	except Exception:
		return 0
	return likeness

#main game loop
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

	#for debug: enter "EXIT" to exit the game
	if user_input == "EXIT":
		sys.exit()

	#if player guessed correctly, player wins and loop ends
	if user_input == PASSWORD:
		victory = True
		break

	#if player's attempt is not one of the choices, ask again
	if (user_input not in TEN_WORDS):
		print("Attempt must be one of the choices. Try again.")
		continue

	#The user guessed an incorrect choice. Print likeness of attempt
	attempt_likeness = likeness(user_input)
	print("LIKENESS:", attempt_likeness)

	attempts_remaining -= 1
#end main game loop

#print endgame results
if victory:
	print("ACCESS GRANTED")
else:
	print("TERMIAL LOCKED\nPLEASE CONTACT AN ADMINISTRATOR")
