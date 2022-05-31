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
## Create an integer variable i with a value of 5.
## Create a while loop that runs so long as i is less than or equal to 15
## Each loop iteration, output the current value of i, then increment i by one.
i = 5
while i <= 15:
    print(i)
    i += 1

## Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.

i = 0
while i in range(0,101):
    print(i)
    i += 2

## Alter your loop to count backwards by 5's from 100 to -10.
i = 100
while i in range(-10,101):
    print(i)
    i = i-5

## Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000.
i = 2
while i in range(2, 1000000):
    print(i)
    i = i**2

## Write a loop that uses print to create the output shown below.
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
## i. Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.
## For example, if the user enters 7, your program should output:
number = input('Please enter a number: ')
for i in range(1,11):
    print(number, 'x', i, '=', int(number) * i)
    i += 1

# num = input('Please enter a number: ')
# num = int(num)
# for i in range(1,11):
#     print(f'{num} * {i} = {num * i}')

## ii. Create a for loop that uses print to create the output shown below.
for i in range (1, 10):
    print(str(i)*i)
    i += 1

## c. breank and continue
## i. Prompt the user for an odd number between 1 and 50.
## Use a loop and a break statement to continue prompting the user if they enter invalid input.
number = input('Please enter an odd number: ')
print('Number to skip is: ', number)
for i in range(1, 50):
    if i == int(number):
        print('Yikes! Skipping number: ', number)
    elif i % 2 == 1 and i != int(number):       
        print(i)
    i  = i + 2

## d. The input function can be used to prompt for input and use that input in your python code.
## Prompt the user to enter a positive number and write a loop that counts from 0 to that number.
number = input('Please enter a positive number: ')
if int(number)> 0:
    for i in range(0,int(number)+1):
        print(i)
else:
    print('Please re-enter a postivie number: ')
    number = input('Please enter a postitive number: ')


# q3. Fizzbuzz
## Write a program that prints the numbers from 1 to 100.

for i in range(1,101):
    print(i)

## For multiples of three print "Fizz" instead of the number
for i in range(1,101):
    if i % 3 == 0:
        print('Fizz')
    else:
        print(i)

## For the multiples of five print "Buzz".
for i in range(1,101):
    if i % 5 == 0:
        print('Buzz')
    else:
        print(i)

## For numbers which are multiples of both three and five print "FizzBuzz".
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    else:
        print(i)


# q4. Display a table of powers
## Prompt the user to enter an integer.
number = input('What number would you lke to go up to? \n')

## Display a table of squares and cubes from 1 to the value entered.
print('Here is your table!\n')
print('number ', 'squared ', 'cubed')
for i in range (1,int(number)+1):
    table_data = [[i, i**2, i**3]]
    for row in table_data:
        print("{: >5} {: >5} {: >5}".format(*row))


# q5. Convert given number grades into letter grades.
## Prompt the user for a numerical grade from 0 to 100.
## Display the corresponding letter grade.
## Prompt the user to continue.
## Assume that the user will enter valid integers for the grades
## The application should only continue if the user agrees to.
## Grade Ranges:
# A : 100 - 88
# B : 87 - 80
# C : 79 - 67
# D : 66 - 60
# F : 59 - 0

number = input('Please enter a number: ')
play = 'y'
while play == 'y':
    if 88 <= int(number) <= 100:
        print('A')
    elif 80 <= int(number) <= 87:
        print('B')
    elif 67 <= int(number) <= 79:
        print('C')
    elif 60 <= int(number) <= 66:
        print('D')
    else:
        print('F')
    play = input('Would you like to continue? (y/n): ')
    if play == 'y':
        play == True
    else:
        break
    number = input('Please enter a number: ')


# q6.Create a list of dictionaries where each dictionary represents a book that you have read.
# Each dictionary in the list should have the keys title, author, and genre. Loop through the list and print out information about each book.
books = [
    {
        "title": "Ace the Data Science Interview",
        "author": "Kevin Huo",
        "genre": "education",
    },
    {
        "title": "naked statistics",
        "author": "Charles Wheelan",
        "genre": "education",
    },
    {
        "title": "The Invisible Life of Addie LaRue",
        "author": "V.E. Schwab",
        "genre": "fantasy",
    },
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "genre": "fiction",
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "genre": "fiction",
    },
      {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "genre": "romance",
    }
]

def print_books(books):
    for book in books:
        print(book['title'], book['author'], book['genre'])

print_books(books)

## a. Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.
entered_genre = input('Please enter a genre: ')
for book in books:
    if book['genre'] == entered_genre:
        print(book['title'])
