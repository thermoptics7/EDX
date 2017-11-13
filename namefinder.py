#Write a function called name_finder which takes two
#arguments: a string containing comma-separated names, and a
#single string of a first and last name separated by a space.
#Your function should return True if either the first or the
#last name from the second string is anywhere in the first
#string. Otherwise, your function should return False.
#
#The first argument will always have the following format:
#"first_1 last_1, first_2 last_2, first_3 last_3". There may
#be more than three names, however.
#
#The second argument will always be two words, a first and
#last name.
#
#Here are some examples:
#name_finder("Joshua Diaddigo, Marguerite Murrell, Jackie
#             Elliott", "Dave Elliott")
#True
#
#name_finder("Joshua Diaddigo, Marguerite Murrell, Jackie
#             Elliott", "Jack Smith")
#False
#
#Hint: The toughest part of this is returning "False" when
#we're searching for a name (like "Jack") that appears in
#another name (like "Jackie"). You'll have to be clever to
#find a way around that! If you're stuck, come back to this
#later: it's possible to do this with what you've learned
#so far, but next lesson we'll cover additional tools that
#can help.
#Write your function here!
def name_finder(studentList, studentName):
    firstName = ""
    lastName = ""
    firstName, lastName = studentName.split(" ")
    #print(firstName)
    #print(lastName)

    if studentList.startswith(firstName + " "):
        return True
    if studentList.endswith(" " + firstName):
        return True
    if studentList.find(" " + firstName + " ") != -1:
        return True
    if studentList.startswith(lastName + " "):
        return True
    if studentList.endswith(" " + lastName):
        return True
    if studentList.find(" " + lastName + " ") != -1:
        return True

    return False

#If you want to try out your code, uncomment the lines below.
#When you submit, however, comment these lines back out. The
#autograder may interpret these lines as an attempt to
#circumvent it if they aren't commented out!
studentList = "Joshua Diaddigo, Marguerite Murrell, Jackie Elliott"
#print(name_finder(studentList, "Jackie Elliott"))
#print(name_finder(studentList, "Dave Elliott"))
#print(name_finder(studentList, "David Joyner"))
print(name_finder(studentList, "Jack Smith"))

#if studentList.find(firstName) >= 0:
        #result = True
    #elif studentList.find(lastName)  >= 0:
        #result = True
    #else:
        #result = False

    #return result

