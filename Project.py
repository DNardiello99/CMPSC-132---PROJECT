#DOMINIC NARDIELLO COMP SCI 132 PROJECT #3
import random

def Number_Guessing_Game():
    print("This is the Number Guessing Game Designed by Dominic Nardiello!")
    print("\nDifficulty Levels:")
    print("1. Easy (Numbers from 1 to 50)")
    print("2. Medium (Numbers from 1 to 100)")
    print("3. Hard (Numbers from 1 to 500)")

    upper = 0
    validity = False

    while not validity:
        level = input("Enter level choice (1, 2, or 3): ")
        if level == "1":
            upper = 50
            validity = True
        if level == "2":
            upper = 100
            validity = True
        if level == "3":
            upper = 500
            validity = True
        else:
            print("ERROR - Please try again, typing only '1' '2' or '3'")
        
    secretnum = random.randint(1,upper)
    attempts = 0

    print(f"\nMy number is selected! (It's between 1 and {upper})")
    print("Let's get started!")

    correct = False
    
    while not correct:
        userinput = input("\n Enter your guess: ")
        try:
            guess = int(userinput)
            validnum = True
        except ValueError:
            print("Try again using only whole numbers!")
            validnum = False
        if validnum:
            if guess < 1 or guess > upper:
                print(f"Out of bounds! Please enter a number between 1 and {upper}")
            else:
                attempts += 1
                if guess > secretnum:
                    print("High!")
                elif guess < secretnum:
                    print("Low!")
                else:
                    print("\nCORRECT!! You have found my number!")
                    print(f"You guessed my number in {attempts} attempts!")
                    correct = True

if __name__ == "__main__":
    Number_Guessing_Game()



