# I learned how to use an endswith() method from the following url:
# https://www.tutorialspoint.com/python/string_endswith.htm#:~:text=The%20python%20string%20endswith(),specified%20suffix%2C%20otherwise%20returns%20false.

#Takes user input
input1 = input('Enter a string: ')
input2 = input('Enter another string: ')

#Measures length of input strings to compare in if-statement
input1_len = len(input1)
input2_len = len(input2)

#Determines shorter input string and assigns it to the 'suffix' variable
# assigns longer string to 'statement' variable
if input1_len > input2_len:
    statement = input1
    suffix = input2
else:
    statement = input2
    suffix = input1

# endswith() method assigns a true value to test if 'statement' ends with the value of 'suffix'
# endswith() assigns a false value to 'test' if 'statement' doesn't end with the value of 'suffix'
test = statement.endswith(suffix)
print(test)