#Write two nested for loops that print out a multiplication table. The table 
#should multiply every combination of two numbers from 1-10. Tab characters 
#should seperate each entry. 

#Hint: By default, print() starts a new line after whatever it prints. You
#can override this by adding , end="" to the end of your print statement,
#like this; print("Hi", end=""). That will print "Hi", but it won't start a
#new line afterward.
#
#Anything you put in the quotation marks after 'end' will be used at the end
#of the line: print("Hi", end="%") would print "Hi%". To use a tab character,
#put \t inside the quotation marks: print("Hi", end="\t").

#Your output should look something like this:
# 	1	2	3	4	5	6	...
#	2	4	6	8	10	12	...
#	3	6	9	12	15	18	...
#	...	...	...	...	...	...	...

result = 0
for x in range(1,11):
    for y in range(1,11):
        result = x * y
        print(result, end="\t")
    print()
