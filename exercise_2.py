# Re-orders and prints input string with lowercase letters first and uppercase letters second
# My code is based off of a program I had chatGBT create at https://chat.openai.com/

# Input
input1 = input('Enter a string: ');

# Create 2 strings by joining characters that are either lowercase or uppercase
# determined by for loops of input and if statements
lowerCase = ''.join([char for char in input1 if char.islower()])
upperCase = ''.join([char for char in input1 if char.isupper()])

# New string from lowerCase and upperCase
newString = lowerCase + upperCase

# Pring new string
print(newString)