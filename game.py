import random
keepPlaying = "y"

while keepPlaying == "y":
    print("The game is starting!")
    hiddenNumber = random.randint(1,100)

    userGuess = 0

    while not userGuess == hiddenNumber:

        userGuess = int(input("Guess a number between 1 and 100, Nighath Aunty: "))

        if userGuess > hiddenNumber:
            print("Too high Chicken Brother!")
            print("")

        elif userGuess < hiddenNumber:
            print("Too low Chicken Brother!")
            print("")

        else:
            print("You got the right number Naggerlicious!!!")
            print("")

    keepPlaying = input("Want to play again (y for yes, n for no)? ")
