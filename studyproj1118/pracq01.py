import random

secret = random.randint(1, 10)
guess = random.randint(1, 10)

if guess > secret:
    print("Too high")
elif guess < secret:
    print("Too low")
else:
    print("Just right!")
