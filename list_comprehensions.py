# 17 list comprehension problems in python


fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)

# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]

# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())
    
# Exercise 1 - rewrite the above example code using list comprehension syntax. Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]
uppercased_fruits =[x.upper() for x in fruits]
print(uppercased_fruits)

# ['MANGO', 'KIWI', 'STRAWBERRY', 'GUAVA', 'PINEAPPLE', 'MANDARIN ORANGE']

# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]
capitalized_fruits =[x.capitalize() for x in fruits]
print(capitalized_fruits)

# ['Mango', 'Kiwi', 'Strawberry', 'Guava', 'Pineapple', 'Mandarin orange']
# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.
def is_vowel(string):
    vowel = 0
    for string in string:
        if string in ('a', 'e', 'i', 'o', 'u'):
            vowel += 1
    return vowel

fruits_with_more_than_two_vowels = [x for x in fruits if is_vowel(x) >= 2]
print(fruits_with_more_than_two_vowels)

# ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']
fruits_with_only_two_vowels = [x for x in fruits if is_vowel(x) == 2]
print(fruits_with_only_two_vowels)

# ['mango', 'kiwi', 'strawberry']

# Exercise 5 - make a list that contains each fruit with more than 5 characters
morethanfive = [x for x in fruits if len(x) > 5]
print(morethanfive)

# ['strawberry', 'pineapple', 'mandarin orange']

# Exercise 6 - make a list that contains each fruit with exactly 5 characters
exactlyfive = [x for x in fruits if len(x) == 5]
print(exactlyfive)

# ['mango', 'guava']

# Exercise 7 - Make a list that contains fruits that have less than 5 characters
lessthanfive = [x for x in fruits if len(x) < 5]
print(lessthanfive)

# ['kiwi']

# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]
charfruit = [(len(x)) for x in fruits]
print(charfruit)

# [5, 4, 10, 5, 9, 15]

# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"
def contain_a(string):
    for x in string:
        if x in('a'):
            return True

fruits_with_letter_a = [x for x in fruits if contain_a(x) == True]
print(fruits_with_letter_a)

# ['mango', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)

# [2, 4, 6, 8, 10, 256, -8, -4, -2]

# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers
odd_numbers = [x for x in numbers if x % 2 == 1]
print(odd_numbers)

# [3, 5, 7, 9, 11, 13, 17, 19, 23, 5, -9]

# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers
positive_numbers = [x for x in numbers if x > 0]
print(positive_numbers)

# [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, 5]

# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers
negative_numbers = [x for x in numbers if x < 0]
print(negative_numbers)

# [-8, -4, -2, -9]

# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals
numerals = [x for x in numbers if x > 9]
print(numerals)

# [10, 11, 13, 17, 19, 23, 256]

# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]
numbers_squared = [x ** 2 for x in numbers]
print(numbers_squared)

# [4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 169, 289, 361, 529, 65536, 64, 16, 4, 25, 81]

# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.
odd_negative_numbers = [x for x in numbers if x % 2 == 1 and x < 0]
print(odd_negative_numbers)

# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five. 
numbers_plus_5 = [x + 5 for x in numbers]
print(numbers_plus_5)

# [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 22, 24, 28, 261, -3, 1, 3, 10, -4]

# BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list. *Hint* you may want to make or find a helper function that determines if a given number is prime or not.
def is_prime(n):
    if n > 1:
        for number in range(2, n):
            if (n % number ==0):
                return False
            else:
                return True

primes = [x for x in numbers if is_prime(x) == True]
print(primes)

# [3, 5, 7, 9, 11, 13, 17, 19, 23, 5]