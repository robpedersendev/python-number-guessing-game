import random
import sys


def guessingGame(number, guess):
    while true:

        try:
            guess = input(
                f"Number guesser.\t\t\n {name} choose a number between "
                f"{start} and {end}. Enter guess? : ")
            guess = int(guess)
            if guess < number:
                print("\n\nThat number is a tad low\n\n")
            elif guess > number:
                print("\n\nThat number is a tad high\n\n")
            else:
                print("\n\nCongrats, you chose the right number!\n\n")
                break

        except (TypeError, ValueError):
            print("Sorry, numbers only please")
            guess = str(f"\'{guess}\' Which is an invalid character")
            continue
        except (UnboundLocalError):
            print("Sorry, numbers only please")
            continue
        finally:
            print(f"{name}, your last successful guess was {guess}")


if __name__ == "__main__":
    true = True
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    number = random.randrange(start, end)  # Selects the winning number
    name = input("\t\t\t\t\nHello stranger, whats your name? ")
    guessingGame()
