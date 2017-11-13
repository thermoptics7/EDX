#Write a function called "num_words" that accepts a string
#as an argument and returns the number of words in the
#string. You can assume all words are separated by a space,
#and that the string has at least one word. You do not need
#to worry about punctuation.
#
#For example:
#
#  num_words("I came. I saw. I conquered.") -> 6
#
#Do not use any loops.


#Write your function here!
def num_words(string):
    wordList = string.split(" ")
    #print(wordList) #only for debug purposes
    wordCount = len(wordList)

    return wordCount



#You may test your function with the lines below. When your
#function works correctly, these lines should print 6, 2,
#and 1.
print(num_words("I came. I saw. I conquered."))
print(num_words("Hello, world!"))
print(num_words("HeyDavidwhyaren'ttherespacesinthissentence"))
