# We've started writing a function named whoWon(). It takes in the following variables:
# - team1 (a string)
# - score1 (an integer)
# - team2 (a string)
# - score2 (an integer)
#
# Create two variables. Name the first one 'winner', and give it the value of the winning
# team. Name the second one 'margin', and give it the number of points that the winning
# team won by. If the game was a tie, set the value of 'winner' equal to "It's a tie!",
# and set 'margin' equal to 0.
#
# For example, calling whoWon("Georgia Tech", 30, "Duke", 20) would result in a value of
# "Georgia Tech" for the variable 'winner' and 10 for the variable 'margin'.

def whoWon(team1, score1, team2, score2):
    # Add your code here. When your code is done running, there should exist a variable
    # called winner, with the value of the name of the team with the higher score, and
    # a variable called margin, with the value the number of points the winning team
    # won by.

    if score1 > score2:
        winner = team1
        margin = score1 - score2
    elif score1 == score2:
        winner = "It's a tie!"
        margin = 0
    else:
        winner = team2
        margin = score2 - score1

    return (winner, margin)

# You may modify the variables below to test your code.
testTeam1 = "Georgia Tech"
testScore1 = 26
testTeam2 = "Georgia"
testScore2 = 26

# Don't worry with the code below, it just prints the result!
print("Score:", testTeam1, testScore1, "-", testTeam2, testScore2)
resultTuple = whoWon(testTeam1, testScore1, testTeam2, testScore2)
if not resultTuple[1] == 0:
    print(resultTuple[0], "won by", resultTuple[1], "points.")
else:
    print(resultTuple[0])