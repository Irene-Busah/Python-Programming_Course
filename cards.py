import random

"""
for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + "|" + str(right) + "]",  end=" ")
    print()
"""

# guessing game
n = 2
to_be_guessed = int(random.random() * n) + 1
guess = 0
while guess != to_be_guessed:
    guess = int(input("Guess a number: "))
    if guess > 0:
        if guess > to_be_guessed:
            print("Number is too large")
        elif guess < to_be_guessed:
            print("Number is too small")

    else:
        print("Sorry for giving up!")
        break

print("Congratulations! You made it")
