i = -2
j = 2
while i < j:
    try:
        print(j // i)
        i += 1
    except:
        print("An error occurred!")
print("Done!")