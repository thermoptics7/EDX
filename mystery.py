#Write a for loop that finds the factorial of mysteryValue and prints it. A
#factorial of x is the multiplication of every number from 1 to x. For
#example, the factorial of 5 = 5 * 4 * 3 * 2 * 1 = 120.

import sys
mysteryValue = int(sys.argv[1])
print("~ testing with mysteryValue = {} ~".format(mysteryValue))

#Don't modify the code above!

#Write your code here. You'll have access to a variable named mysteryValue,
#which will be an integer. When you run your code, we'll test it with
#mysteryValue = 5. When you submit your code, we'll test it with a few
#other numbers.

result = 1
mysteryValue = 5
for i in range(mysteryValue, 0, -1):
    result = result * i
print(result)

