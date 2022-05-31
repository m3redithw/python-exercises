# q1. Define a function named is_two.
# It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.
from os import remove


def is_two(input):
    if input == '2' or input ==2:
        return True
    else:
        return False

is_two(3)

# q2. Define a function named is_vowel.
# It should return True if the passed string is a vowel, False otherwise.
def is_vowel(input):
    if input == 'a' or input == 'e' or input == 'i' or input == 'o' or input == 'u':
        return True
    else:
        return False

is_vowel('i')

# q3. Define a function named is_consonant.
# It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.
def is_consonant(input):
    if is_vowel(input) == False:
        return True
    else:
        return False
is_consonant('b')

# q4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.
def is_word(word):
    if is_consonant(word[0]) == True:
        print(word.capitalize())
    else:
        print(word)
is_word('codeup')

# q5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.
def calculate_tip(tip_percentage, bill_total):
    return tip_percentage * bill_total

# q6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.
def apply_discount(original_price, discount):
    return original_price * (1-discount)

# q7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.
def handle_commas(input_str):
    result_str = ''
    for i in range(0,len(input_str)):
        if input_str[i] != ',':
            result_str = result_str + input_str[i]
    return result_str

handle_commas('1,2,3')

# q8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).
def get_letter_grade(number):
    if 88 <= number <= 100:
        print('A')
    elif 80 <= number <= 87:
        print('B')
    elif 67 <= number <= 79:
        print('C')
    elif 60 <= number <= 66:
        print('D')
    else:
        print('F')

get_letter_grade(98)

# q9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.
def remove_vowels(input_str):
    result_str = ''
    for i in range(0, len(input_str)):
        if input_str[i] != 'a' and input_str[i] != 'e' and input_str[i] != 'i' and input_str[i] != 'o' and input_str[i] != 'u':
            result_str = result_str + input_str[i]
    return result_str

remove_vowels('banana')

# q10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores
# for example:
## Name will become name
## First Name will become first_name
## % Completed will become completed

def normalize_name(input_string):
    result_str = ''
    for i in range(0, len(input_string)):
        if input_string[i].islower() == True:
            result_str = result_str + input_string[i]
        elif input_string[i] == ' ':
            result_str = result_str + '_'
        elif input_string[i].isupper() == True:
            result_str = result_str + input_string[i].lower()
    return result_str

normalize_name('Meredith W')

# q11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]
def cumulative_sum(list):
    result_list = []
    num = 0
    for n in range(0, len(list)):
        num = num + int(list[n])
        result_list.append(num)
    return result_list
cumulative_sum([1,2,3,4])

# Bonus1. Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format.
def twelveto24(time):
    result_time = ''
    if time[-2] == 'a':
        result_time = time
    else:
        result_time = str(int(time[:-5])+12) + time[-5:]
    return result_time
twelveto24('10:45pm')

## Bonus write a function that does the opposite.
## 20:14pm --> 8:14pm
## 09:25am --> 09:25am
def totwelve(time):
    result_time = ''
    if time[-2] == 'a':
        result_time = time
    else:
        result_time = str(int(time[:-5])-12) + time[-5:]
    return result_time
totwelve('20:20pm')
