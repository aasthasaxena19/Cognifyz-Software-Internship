import random

def play_game():
    number = random.randint(1, 10)
    attempts = 3

    print("Welcome to Guess the Number Game")
    print("You have 3 attempts")

    while attempts > 0:
        try:
            guess = int(input("Guess a number between 1 and 10: "))
            if guess == number:
                print("🎉 Congratulations! You guessed it right")
                return
            else:
                attempts -= 1
                print(f"Wrong guess. Attempts left: {attempts}")
        except ValueError:
            print("Please enter a valid number")

    print("❌ Game Over! The correct number was:", number)

play_game()
