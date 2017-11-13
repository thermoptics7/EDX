import turtle
myTurtle = turtle.Turtle()
command = ""
#Loop until the user's command is 'end'
while not command == "end":
    #Get the user's command
    command = input("Enter a command (turn, forward, end): ")
    #Check if the command is 'turn'
    if command == "turn":
        #Get the angle if so
        angle = input("Enter the angle: ")
        #Execute the turn
        myTurtle.right(int(angle))
    #Check if the command is 'forward'
    elif command == "forward":
        #Get the distance if so
        distance = input("Enter distance: ")
        #Execute the move
        myTurtle.forward(int(distance))
    #Check if the command is 'shape'
    elif command == "shape":
        #Get the number of sides to draw
        numSides = int(input("Enter the number of sides (3 or more): "))
        #Get the side length to draw
        sideLength = int(input("Enter the length of each side: "))
        #Draw the shape: forward sideLength, rotated 360/numSides, repeat numSides times
        for _ in range(0, numSides):
            myTurtle.forward(sideLength)
            myTurtle.right(360/numSides)
    #Checks if the command is 'end'
    elif command == "end":
        #Skip if so; the loop won't repeat again if command == "end"
        pass
    else:
        print("Invalid command! Please enter 'turn' or 'forward'.")
