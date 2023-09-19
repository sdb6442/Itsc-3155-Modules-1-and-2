# I'd only made 2D matrixes with Java, so I read how to do it on python at the
# following two URLs and made adjustments accordingly:
# https://stackoverflow.com/questions/6667201/how-to-define-a-two-dimensional-array
# https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/ 

# Get a row number and column number from user
row = int(input('Enter a row number from 1 to 5: '));
column = int(input('Enter a column number from 1 to 5: '));

# Create a 5x5 2D matrix using a for loop
matrix = [[0]*5 for i in range(5)]
matrix[row-1][column-1] = 1  # Assign number 1 to the row and column number provided by user input

# Print matrix
for i in matrix:
    print(i)
