
# Final Version: 

import random
from colorama import Fore, Style, init

init(autoreset=True)

def choose_difficulty():
    print(f"{Fore.CYAN}Choose difficulty level:")
    print("1. Easy (1–50)")
    print("2. Medium (1–100)")
    print("3. Hard (1–500)")
    while True:
        choice = input("Enter 1, 2 or 3: ")
        if choice == "1":
            return 50
        elif choice == "2":
            return 100
        elif choice == "3":
            return 500
        else:
            print(f"{Fore.RED}Invalid choice! Try again.")

def load_high_score():
    try:
        with open("highscore.txt", "r") as file:
            return int(file.read())
    except:
        return float('inf')

def save_high_score(score):
    with open("highscore.txt", "w") as file:
        file.write(str(score))

def play_game():
    max_val = choose_difficulty()
    number = random.randint(1, max_val)
    guess_count = 0
    print(f"\n{Fore.YELLOW}I'm thinking of a number between 1 and {max_val}... Try to guess it!\n")

    while True:
        try:
            guess = int(input(f"{Fore.LIGHTBLUE_EX}Your guess: "))
            guess_count += 1

            if guess == number:
                print(f"\n{Fore.GREEN}🎉 You got it! The number was {number}.")
                print(f"You found it in {guess_count} guesses.")
                highscore = load_high_score()
                if guess_count < highscore:
                    print(f"{Fore.MAGENTA}🏆 New high score!")
                    save_high_score(guess_count)
                break
            elif guess > number:
                print(f"{Fore.BLUE}⬇️ Too high!")
            else:
                print(f"{Fore.MAGENTA}⬆️ Too low!")

            # Fun hint if close
            if abs(guess - number) <= 5:
                print(f"{Fore.YELLOW}🔥 You're really close!")

        except ValueError:
            print(f"{Fore.RED}⚠️ Please enter a valid number.")

if __name__ == "__main__":
    play_game()




