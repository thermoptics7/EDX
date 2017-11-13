#Write a function called "quote_this" that accepts two
#arguments: a string representing a quote (not surrounded
#by quotation marks) and a string of a name. The function
#should return a new string with the quote surrounded by
#quotation marks (") followed by a dash and the given
#name. For example:
#
#a = quote_this("You miss 100% of the shots you don't
#take.", "Wayne Gretzky")
#print(a)
#
#Will print:
#"You miss 100% of the shots you don't take." - Wayne
#Gretzky

#If the code were to continue, this:
#
#b = quote_this(a, "Michael Scott")
#print(b)
#
#Would print:
#""You miss 100% of the shots you don't take." - Wayne
#Gretzky" - Michael Scott


#Write your function here!

def quote_this(quote,name):
    return ('"' + quote + '"' + " - " + name)


#The function calls below will test your code, but are
#not required for grading, so feel free to modify them.
#When your function is correctly written, the output
#will be the same as in the example above.

a = quote_this("You miss 100% of the shots you don't take.", "Wayne Gretzky")
print(a)
b = quote_this(a, "Michael Scott")
print(b)
