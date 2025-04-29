import random

n = random.randint(1, 100)
a = -1
guesses = 0
while(a != n):
    guesses += 1
    a = int(input("Guess the Number between 1 to 100: "))
    if(a < n):
        print("Your guess is too low")
    elif(a > n):
        print("Your guess is too high")

print(f"Congratulations! You guessed the number {n} in {guesses} guesses")
print("Game Over!")