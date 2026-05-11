import random
play=True
computer=random.randint(1,10)
print("Guess the number between 1 to 10")
while play:
    guess=int(input("Enter your number  "))
    if computer > guess:
        print("You are to low")
    elif computer < guess:
        print("You are high")
    elif computer == guess:
        print("That is the right number")
        print("The computer generted number was",computer)
        print("You won")
        play=False
        break