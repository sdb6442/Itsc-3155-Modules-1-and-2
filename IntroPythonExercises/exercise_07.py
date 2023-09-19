# I consulted the python cheatsheet to understand how to make a while loop in python at:
# https://github.com/akashp1712/awesome-python-cheatsheets/blob/master/Python_for_Java_developers_cheat_sheet.pdf

# Declare two lists, one for all numbers (allNums) & one for even numbers (evenNums)
allNums = []
evenNums = []

# Loop until user enters 'QUIT'
while True:
    input1 = input('Enter a number or QUIT to quit: '); # collect user input
    if input1 == 'QUIT': # Break when 'QUIT' is entered
        break
    else:
        num = int(input1) # Cast input to integer
        allNums.append(num) # Add number to 'All Nums' list
        if num % 2 == 0: # Add number to 'Even Nums' list
            evenNums.append(num)

# Print lists
print('All Nums: ' + str(allNums))
print('Even Nums: ' + str(evenNums))
