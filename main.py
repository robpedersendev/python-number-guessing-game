import random
import sys


def guessingGame():
    while true:

        try:
            guess = int(
                input(f"Number guesser.\t\t\n {name} choose a number between {start} and {end}. Enter guess? : "))
        except (TypeError, ValueError):
            print("Im sorry, please try again")
            continue
        finally:
            print(f"{name}, your last successful guess was {guess}")

        if guess != number:
            print("\n\nNice try, keep going\n\n")
        elif guess < number:
            print("\n\nThat number is a tad low\n\n")
        elif guess > number:
            print("\n\nThat number is a tad high\n\n")
        else:
            print("\n\nCongrats, you chose the right number!\n\n")
            break


if __name__ == "__main__":
    true = True
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    number = random.randrange(start, end)
    name = input("\t\t\t\t\nHello stranger, whats your name? ")
    guessingGame()