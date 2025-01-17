import random

print("Guess the number between 1 - 10.")
target = random.randint(1, 10)

while True:
    userChoice = input("Guess the number or Quit(Q): ")
    if(userChoice == "Q"):
        break

    userChoice = int(userChoice)
    if(userChoice == target):
        print("Success: Correct Guess!")
        break
    elif(userChoice > target):
        print("Guess is bigger than the number. Try Again...")
    else:
        print("Guess is smaller than the number. Try Again...")

print("------GAME OVER-----")