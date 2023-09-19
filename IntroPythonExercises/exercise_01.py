# I consulted the github link provided in the course material 
# at https://github.com/akashp1712/awesome-python-cheatsheets/blob/master/Python_for_Java_developers_cheat_sheet.pdf

# Collect grade number as input
num = int(input('Enter a grade from 0-100: '));

# Determine grade value based on input
if num<60:
    print('Your grade is F')
elif num >= 60 and num < 70:
    print('Your grade is D')
elif num >= 70 and num <80 :
    print('Your grade is C')
elif num >= 80 and num <90 :
    print('Your grade is B')
else:
    print('Your grade is A')