import random

def roll (sides = 6):
	num_rolled = random.randint(1, sides)
	return num_rolled


def main():
	sides = 6
	rolling = True
	while rolling:
		roll_again = input("Ready to roll? Enter=roll. Q=quit. ")
		if roll_again.lower() != "q":
			num_rolled = roll (sides)
			print("You roller a ", num_rolled)
		else:
			rolling = False

	print ("Thanks for playing")


main()



