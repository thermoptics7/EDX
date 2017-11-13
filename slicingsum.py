#Write a function called "num_changer" that accepts a string
#of digits (0-9). You should make an integer from the digits
#of the even indices and another number from the digits in
#the odd indices. Return the sum of these two numbers. You
#can assume the given string will have a length of at least
#2 digits.
#
#For example, if the string was "123456", you would split
#this into two integers, 135 and 246. Adding them would give
#381. Or if the string was "1357", you would split this into
#15 and 37, then add them to get 52.
#
#Do not use any loops for your solution. Instead of using
#loops, you can use an extra bit of string slicing syntax.
#If you include second colon in a string slice, the number
#that follows it lets you skip characters in the string. For
#example:
#
# "Hello, world!"[1:9] -> This gives "ello, wo".
# "Hello, world!"[1:9:2] -> This gives "el,w". Including :2
#    in the string slice skips every other letter.
# "Hello, world!" [::3] -> This gives "Hl r!". Leaving the
#    first two spots blank tells it to look at the entire
#    string, but putting :3 at the end says to only take
#    every third character (H, l, space, r, and !).
#
#Use this syntax to write this function.


#Write your function here!
def num_changer(digitString):
    evenDigitInt = int(digitString[::2])
    oddDigitInt = int(digitString[1::2])
    sum = evenDigitInt + oddDigitInt
    return sum



#The lines below will test your function, but they aren't
#needed for grading, so feel free to change them. As written
#originally, this should give 381.
#stringInt = "123456"
stringInt = "0123456789"
result = num_changer(stringInt)
print(stringInt + " -> " + str(result))