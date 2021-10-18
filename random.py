import random

guess_num = int(input("Enter your guessing number :"))

random_guess = random.choice(range(1, 11))

if guess_num == random_guess:
    print("Hurray !")
else:
    print("Not Matched,", end=" ")
    print("Correct number:", random_guess)
