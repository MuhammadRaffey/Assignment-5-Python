import random

numRounds:int = 20

print("Welcome to High-Low Game")
print("------------------------")
rounds:int = 1
score:int = 0

while rounds <= numRounds:
    userNum:int = random.randint(1,100)
    compNum:int = random.randint(1,100)
    print("\nRound", rounds)
    rounds += 1
    print("Your number is", userNum)

    userGuess:str = input("Do you think your number is higher or lower than the computer's? (or type 'quit' to exit): ").strip().lower()
    
    if userGuess == "quit":
        print("You've chosen to quit the game.")
        break

    while userGuess not in ["lower", "higher"]:
        userGuess = input("Please enter either higher or lower (or type 'quit' to exit): ").strip().lower()
        if userGuess == "quit":
            print("You've chosen to quit the game.")
            break

    if userGuess == "quit":
        break

    if userGuess == "lower":
        if userNum < compNum:
            print("You were right!")
            score += 1
        else:
            print("Aww, that's incorrect.")
    elif userGuess == "higher":
        if userNum > compNum:
            print("You were right!")
            score += 1
        else:
            print("Aww, that's incorrect.")

    print(f"Your score is now {score}")

if score == numRounds:
    print("\nWow! You played perfectly!")
elif score >= numRounds // 2:
    print("\nGood job, you played really well!")
else:
    print("\nBetter luck next time!")
