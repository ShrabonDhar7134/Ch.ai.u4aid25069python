# Exercise 18: Number Guessing Game (1–1000, smart hints, 15 attempts)

secret_number = 567
max_attempts = 15
attempts = 0

print("WELCOME TO THE NUMBER GUESSING GAME")
print("I have chosen a secret number between 1 and 1000.")
print("You have only 15 attempts to guess the correct number.\n")

while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts += 1

    difference = abs(guess - secret_number)
    remaining = max_attempts - attempts

    if guess == secret_number:
        print("\nCongratulations! You guessed the correct number.")
        print("Secret number:", secret_number)
        print("Attempts used:", attempts)
        break

    elif difference <= 3:
        print("Extremely close! Just a little adjustment needed.")

    elif difference <= 10:
        print("Very close! You are almost there.")

    elif difference <= 25:
        print("Close enough. You are moving in the right direction.")

    elif difference <= 50:
        print("Not too far, but you need a better adjustment.")

    elif guess > secret_number:
        print("Too high! Try a smaller number.")

    else:
        print("Too low! Try a bigger number.")

    print("Attempts remaining:", remaining, "\n")

else:
    print("\nGame Over!")
    print("You have used all 15 attempts.")
    print("The secret number was:", secret_number)
