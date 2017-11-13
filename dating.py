#Write a function called getTodaysDate that returns today's
#date as a string, in the form year/month/day. For example,
#if today is January 15th, 2017, then it would return
#2017/01/15.
#
#Remember, you took care of the string formatting part of
#this exercise in 2.2.9 Coding Exercise 1! Now, you're
#converting it to a function that returns the string.

#Note that the line below will let you access today's date
#using date.today() anywhere in your code.



#Write your function here!

from datetime import date


def getTodaysDate():
    todaysDate = date.today()
    todaysDateAsStringYear = str(todaysDate.year)
    todaysDateAsStringMonth = str(todaysDate.month)
    todaysDateAsStringDay = str(todaysDate.day)

    return todaysDateAsStringYear + "/" + todaysDateAsStringMonth + "/" + todaysDateAsStringDay




#The line below will test your function.
#print(getTodaysDate())
