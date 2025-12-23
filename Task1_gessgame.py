import random
secret_number = random.randint(1, 100)
for attempt in range(1, 11):
    guess = int(input(f"Attempt {attempt}/10 - Guess the number (1 to 100): "))
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Congratulations! You guessed it right in ",attempt," attempts.",sep=" ")
        break
else:
    print("Sorry! You've used all attempts. The number was ",secret_number)
