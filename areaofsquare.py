#Write a function that takes in one integer parameter, the
#side length of a square, and finds the area. The function
#should be named findArea, and have one parameter:
#sideLength.

#Write your function here!

def findArea(sideLength):
    #Caluculates the Area of a Square
    area = sideLength ** 2
    return area

#You can modify these lines to test out your function.
testSideLength = 8
print("A square with side length", testSideLength, "has an area of", findArea(testSideLength))