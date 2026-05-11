import random
play=True
computer=random.randint(1,3)
print("1:Rock")
print("2:paper")
print("3:Scissors") 
num1=int(input("1,2,3 "))
while play:
    if computer == 1 and num1 == 2:
        print("Ok,you won")
        print("Computer guess",computer)
        play=False
        break