# We've written the function, reverse, below. This function
# takes a string and returns the reverse of it. There are two
# scope errors somewhere in the code. Read through all the
# code below to find and fix the errors, so that the function
# produces the correct output and the result of the function
# is correctly printed. Note that you should not change the
# three lines that are already present in the function, but
# you may add lines before them, or you may change or add to
# the lines outside the function.
#
# Function Name: reverse
# Parameters: word (a string)
# Returns: the reversed string

def reverse(word):
    # You may add code before the following three lines.
    rev = ""
    # Don't change these three lines.
    for i in range(len(word) - 1, -1, -1):
        rev = rev + word[i]
    return rev


# You may change or add to the following lines.
reversedString = reverse("This is kind of like the reverse feature on Snapchat")
print(reversedString)