# q1. Conditional Basics
## a. prompt the user for a day of the week, print out weather the day is Monday or not

user_input = input('Please enter a day of the week: ')
if user_input == 'Monday':
    print('is a Monday')
else:
    print('is not Monday')

## b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend

user_input = input('Please enter a day of the week: ')
if user_input == 'Saturday' or user_input == 'Sunday':
    print('is a weekend')
else:
    print('is a weekday')

## c. create variables and make up values for
# the number of hours worked in one week
# the hourly rate
# how much the week's paycheck will be
# write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours

number_of_hours_worked
hourly_rate
weekly_paycheck
if number_of_hours_worked > 40:
    weekly_paychek == 1.5 * hourly_rate * number_of_hours_worked
else:
    weekly_paycheck == hourly_rate * number_of_hours_worked

# q2. Loop Basics
## a. While
# Create an integer variable i with a value of 5.
# Create a while loop that runs so long as i is less than or equal to 15
# Each loop iteration, output the current value of i, then increment i by one.
i = 5
while i <= 15:
    print(i)
    i += 1

# Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.

i = 0
while i in range(0,101):
    print(i)
    i += 2

# Alter your loop to count backwards by 5's from 100 to -10.
i = 100
while i in range(-10,101):
    print(i)
    i = i-5

# Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000.
i = 2
while i in range(2, 1000000):
    print(i)
    i = i**2

# Write a loop that uses print to create the output shown below.
# 100
# 95
# 90
# 85
# 80
# 75
# 70
# 65
# 60
# 55
# 50
# 45
# 40
# 35
# 30
# 25
# 20
# 15
# 10
# 5
i = 100
while i in range(5,101):
    print(i)
    i -= 5

## b. For Loops
# i. Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.
# For example, if the user enters 7, your program should output:
number = input('Please enter a number: ')
for i in range(1,11):
    print(number, 'x', i, '=', int(number) * i)
    i += 1

# ii. Create a for loop that uses print to create the output shown below.
for i in range (1, 10):
    print(str(i)*i)
    i += 1

## c. breank and continue
# i. Prompt the user for an odd number between 1 and 50.
# Use a loop and a break statement to continue prompting the user if they enter invalid input. 