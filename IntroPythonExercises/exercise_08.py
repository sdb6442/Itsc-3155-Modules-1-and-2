# I learned of the count method provided in python from the following URL:
# https://www.geeksforgeeks.org/find-the-element-that-appears-once/
# I used it on line 19 to count occurances of items in my original list.

# Declare original list and new list to display numbers that appear once
originalList = []
newList = []

# Collect numbers from user
for i in range(1, 11, +1):
    num = int(input('Enter number ' + str(i) + ' : '));
    originalList.append(num) # add numbers to original list

# Display original list
print('Original list: ' + str(originalList))

# Loop original list and count occurances of items in list
for j in originalList:
    if(originalList.count(j) == 1):  # Add items with one occurance to new list
        newList.append(j)

# Display new list
print('Nums that appear once: ' + str(newList))
