#Write a function called "steps" that should accept as input
#a number between 1 and 9. It should then return output such
#as the following:
#
#steps(3)
#1111
#	2222
#		3333
#
#steps(6)
#1111
#	2222
#		3333
#			4444
#				5555
#					6666
#
#Specifically, it should start with 1, and show four of each
#number from 1 to the inputted value, each on a separate
#line. The first line should have no tabs in front, but each
#subsequent line should have one more tab than the line
#before it. You may assume that we will not call steps() with
#a value greater than 9.

#Write your function here!
def steps(numberOfSteps):
    for i in range(1, numberOfSteps+1):
        result = ("\t" * (i - 1) + str(i) + str(i) + str(i) + str(i))
        print(result)






#The following two lines will test your code, but are not
#required for grading, so feel free to modify them.
#steps(3)
steps(9)


