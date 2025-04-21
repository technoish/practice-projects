import random

computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice (snake, water, gun): ").lower()
youDict = {"snake": -1, "water": 0, "gun": 1}
reverseDict = {-1: "snake", 0: "water", 1: "gun"}
you = youDict[youstr]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("It's a tie!")
else:
    if(computer == -1 and you == 1):
        print("You win!")
    elif(computer == -1 and you == 0):
        print("You lose!")
    elif(computer == 0 and you == -1):
        print("You win!")
    elif(computer == 0 and you == 1):
        print("You lose!")
    elif(computer == 1 and you == -1):
        print("You lose!")
    elif(computer == 1 and you == 0):
        print("You win!")
    else:
        print("Invalid input!")