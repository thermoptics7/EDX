# We've started a function, factors(), below. This function should take
# in two integers, create a variable called result, and assign to result the
# value "Factors!" when either of the two numbers is a factor of the other.
#
# HINT: You can do this with just one conditional statement by using the
# logical expressions we learned earlier (and, or, and not). You'll also
# use the modulus operator we learned in Chapter 2.4.

# Function - factors()
# Parameters - num1, num2, both integers
def factors(num1, num2):
    result = ''  # Here we'll create result in advance.

    # Write your code here. In the code you write, you'll have access to
    # two variables: num1 and num2. Remember to check if *either* of the
    # number is a factor of the other.

    #testing to see if num1 is greater than or equal to num2 and then seeing if they factor
    if (num1 >= num2) and (num1 % num2 == 0):
        result = "Factors!"

    elif num2 % num1 == 0:
        result = "Factors!"

    else:
        result = "Not factors :("


    return result


# You can modify the code below to test out your answer.
testNum1 = 23
testNum2 = 23
print(testNum1, "and", testNum2, "are:", factors(testNum1, testNum2))