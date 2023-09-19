# Researched lists at https://stackabuse.com/bytes/how-to-add-a-float-to-a-list-in-python/
# Learned Sum function at https://www.geeksforgeeks.org/sum-function-python/

# Cast user input
num = int(input('Enter a number: '));

# Create a list
list = []
for i in range(1, num+1):  
    listNum = float(input('Enter number: ')) # Collect numbers from input 
    list.append(listNum) # add numbers to list

print('List: ' + str(list)) # print list

list_len = len(list) # determine length of list
Sum = sum(list) # find the sum of the floats in the list

average = Sum/list_len # calculate the average of the list
print("Average: " + str(average))