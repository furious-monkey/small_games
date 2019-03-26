import random

name = input("What is your name? ")
number = random.randint (1, 100)

print ("Hi" + name + "I am thinking a number between 1 and 100")
guessesTaken = 0


 
while guessesTaken < 5:
	guess = input ("Enter a guess: ")
	guess = int (guess)
	guessesTaken = guessesTaken +1
	if number < guess:
		print ("Too large")
	elif number > guess:
		print ("Too small")
	else:
		break

if guess == number:
	print("Sabbash")
else:
	print("Looser" + "The right number was" + mumber)
		



