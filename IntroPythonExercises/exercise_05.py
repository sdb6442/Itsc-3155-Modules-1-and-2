# Learned set() method to eliminate duplicates in a list
# from url: https://www.geeksforgeeks.org/python-ways-to-remove-duplicates-from-list/
# begins on line 30

# Create lists
list1 = []
list2 = []
list3 = []

# Append inputs to 'First List"
for i in range (0, 5, +1):
    input1 = int(input('Enter a number for the first list: '))
    list1.append(input1)

# Append inputs to 'Second List"
for j in range (0, 5, +1):
    input2 = int(input('Enter a number for the second list: '))
    list2.append(input2)

# Print first two lists
print('First List: ' + str(list1))
print('Second List: ' + str(list2))

# Traverse lists using an inner loop
for k in list1:
    for l in list2:
        if k == l: # compare lists to find matches
            list3.append(k) # add matches to list3 (Common List)

list3 = list(set(list3)) # eliminate duplicates found in list3 using a set() method
print('Common List: ' + str(list3)) # print final list3