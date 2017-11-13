#Write a function called multiply_strings. Multiply
#strings should have one parameter, a list of strings.
#It should return a modified list according to the
#following changes:
#
# - Every string stored at an even index should be
#   doubled.
# - Every string stored at an index that is a multiple
#   of 3 should be tripled.
# - Every other string should remain unchanged.
#
#These changes should "stack": the string stored at index
#6 should be duplicated six times (2 * 3).
#
#Then, return the new list. You may assume that 0 is a
#multiple of 2 and 3.
#
#Hint: To do this, you need to modify the values of the
#list using their indices, e.g. a_list[1]. If you're not
#using their indices, your answer won't work!


#Write your function here!
def multiply_strings(aListOfStrings):
    for string in range(0,len(aListOfStrings)):
        if string == 0:
            aListOfStrings[string] = aListOfStrings[string] * 6
        elif string == 6:
            aListOfStrings[string] = aListOfStrings[string] * 6
        elif string % 2 == 0:
            aListOfStrings[string] = aListOfStrings[string] * 2
        elif string % 3 == 0:
            aListOfStrings[string] = aListOfStrings[string] * 3
        else:
            continue

    return aListOfStrings


#myList1 = ["Omar","is","the","man","okay","guys","?"]

myList1 = ['ayFV', 'ufUy', 'CvEm', 'blSO', 'vAiZ', 'FCmb', 'FYdP', 'bvlJ', 'lMRM', 'Mkar', 'vslZ', 'WkOC']

print("Original List is:", myList1)
print("New List is:", multiply_strings(myList1))