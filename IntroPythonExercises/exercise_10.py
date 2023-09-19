# I had trouble figuring this exercise out. Cout separate the characters into sets of 3
# but I could not figure out how to create subsets

# Input a string
input1 = input('Enter a string: ');

# Put string in a list and separate by characters
list = list(input1)
listLength = len(list) # Determine list length to use in if/else statement

# Append new list- if/else statement required to account for the last characters
# without if statement, the last character or 2 will not be added to list if the string
# is not divisible by 3
newList = []
if listLength % 3 == 0: 
    for i in range(0, listLength-1, 3):
        newList.append(list[i] + list[i+1] + list[i+2])
elif listLength % 3 == 2:
    for i in range(0, listLength-2, 3):
        newList.append(list[i] + list[i+1] + list[i+2])
    newList.append(list[listLength-2] + list[listLength-1])
else:
    for i in range(0, listLength-2, 3):
        newList.append(list[i] + list[i+1] + list[i+2])
    newList.append(list[listLength-1])

# Display lists I was able to create
print('String split by individual character:')
print(list)
print('String split by 3 characters at a time:')
print(newList)