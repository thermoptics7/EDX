#Write a function called "after_second" that accepts two
#arguments: a string to search, and a search term. The
#function should return everything in the first string after
#the SECOND occurrence of the search term. You can assume
#there will always be at least two occurrences of the search
#term in the first string.

#For example:
#  after_second("1122334455321", "3") -> 4455321
#
#The search term "3" appears at indices 4 and 5. So, this
#returns everything from the index 6 to the end.
#
#  after_second("heyyoheyhi!", "hey") -> hi!
#
#The search term "hey" appears at indices 0 and 5. The
#search term itself is three characters. So, this returns
#everything from the index 8 to the end.


#Write your function here!

def after_second(searchString,searchTerm):
    searchTermCount = 0
    currentLocation = searchString.find(searchTerm)
    #print("Location of first search term:", currentLocation)

    if currentLocation >= 0:
        currentLocation = searchString.find(searchTerm, currentLocation+len(searchTerm))
        if currentLocation >=0:
            #print("Location of first search term:", currentLocation)
            return searchString[currentLocation+len(searchTerm):]
        else:
            return "There are no second terms found"
    else:
        return "No search terms found"




#Uncomment the lines below to test your code. When your
#function works correctly, these should result in
#"4455321" and "hi!". However, comment these lines out
#before submitting or else the autograder may interpret
#them as an attempt to circumvent the directions.
#print(after_second("1122334455321", "3"))
#print(after_second("heyyoheyhi!", "hey"))
