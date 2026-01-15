import random

print("🙏🙏🙏👏 Welcome to the Number Guess Game 👏🙏🙏🙏")
min_range = 1
max_range = 25
for i in range(1,6):
    print(f"Number Range : {min_range} - {max_range}")
    r_number = random.randint(min_range, max_range)
    print(r_number)
    for i in range(1, 6):
        guess = int(input("Enter the number : "))

        if guess < r_number:
            print("Guess is low")
        elif guess > r_number:
            print("Guess is high")
        else:
            print("🥳🥳🥳 Congratulations! You won the Game 🥳🥳🥳")
            min_range = max_range
            max_range += 25
            break
    else:
        print("😢 Game Over! The number was:", r_number)
        break