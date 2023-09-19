# Declare list
list = []

# Loop to collect and add words to list from user input
for i in range (0, 5, +1):
    input1 = input('Enter a word: ')
    list.append(input1)

# Print list of words
print('Words: ' + str(list))

# Declare a new string and loop list to modify string to incorpate words from list
newString = ''
for j in list:
    newString += str(j) + ' '

# Print new string
print('One string: ' + newString)