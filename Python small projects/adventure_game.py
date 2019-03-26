import random
import time

def displayIntro():
    print("You are in a land full of dragons. In front of")
    print("you are two caves. In one cave the dragon is")
    print("friendly and will give you his treasure. In the")
    print("other, the dragon is greedy and hungry and will")
    print("eat you on sight")
    print()

def chooseCave():
    cave = ""
    while cave != "1" and cave != "2":
        print("Which cave will you choose? (1 or 2)")
        cave = input()
    return cave

def checkCave(chosenCave):
    print("You approach the cave...")
    time.sleep(2)
    print("It is dark and spooky...")
    time.sleep(2)
    print("A large dragon jumps out in front of you. He opens his jaws and...")
    print()
    time.sleep(2)

    friendlyCave = random.randint(1,2)

    if chosenCave == str(friendlyCave):
        print("gives you his treasure")
    else:
        print("gobbles you down in one bite")


playAgain = "yes"
while playAgain =="yes" or playAgain == "y":

    displayIntro()

    caveNumber = chooseCave()

    checkCave(caveNumber)

    print("Would you like to play again? (yes or no)")
    playAgain = input()