# It's snowing!
#
# Fill in the function we've started below so that it creates
# a variable called result with the value "School isn't
# cancelled." if we're in New Jersey, "School is postponed."
# if we're in North Carolina, and "School is cancelled!" if
# we're in Georgia. If the value of state isn't "Georgia",
# "North Carolina", or "New Jersey", print "idk wear a
# jacket".

# Function name - snowDay()
# Takes one input, a string variable called "state".
def snowDay(state):
    # Write your code here. In the code you write, you'll
    # have access to a variable called state whose value is
    # a string. When your code is done, a variable should
    # exist called result with the value noted above.

    if state == "New Jersey":
        result = "School isn't cancelled."

    elif state == "North Carolina":
        result = "School is postponed."

    elif state == "Georgia":
        result = "School is cancelled!"

    else:
        result = "idk wear a jacket"

    return result


# You can change the variable below to test out your code.
testState = "new jersey"
print(snowDay(testState))