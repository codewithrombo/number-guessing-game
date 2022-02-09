import random
from unicodedata import digit

rang = 25

def guessing_game():
    score = 1
    random_number = random.randrange(1, rang)
    while True:
        try:
            player_number = int(input("Choose a number: "))
            if player_number < random_number:
                score += 1
                print("\nYou are below the target number. Try again!\n")
                continue
            elif player_number > random_number:
                score += 1
                print("\nYou are above the target number. Try again!\n")
                continue
            elif player_number == random_number:
                    if score == 1:
                        print("\nYou got it on your first try! You win! :)\n")
                    else:
                        print("\nYou got it in", score, "tries. You win! :)\n")
                    break
        except:
                print("\nInvalid input. Please use a number.\n")
                continue


print("\nHello and welcome to Robert's number guessing game.\n")

while True:
    playing = input("Would you like to play this game? (y/n): ")
    if playing.lower() == "y":
        print("\nAwesome, let's play!\n")
        break
    elif playing.lower() == "n":
        print("\nThanks for stopping by! Have a nice day, bye! :)")
        quit()
    else:
        print("Invalid command, please try again!")

print("In this number guessing game you have to guess randomly generated number up to " + str(rang) + ". You have unlimited tries. Good luck :)\n")
print("Computer generating a number\n")
print("..............................")
print("..............................")
print("..............................\n")


guessing_game()

while True:
    play_again = input("Would you like to play again? (y/n): ")
    if play_again.lower() == "y":
        print("\nStarting over! Good luck! :)\n")
        guessing_game()
    elif play_again.lower() == "n":
        quit("\nGood bye! :)\n")
    else:
        print("\nInvalid input.\n")
        continue
