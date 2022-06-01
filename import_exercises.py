# q1. Import and test 3 of the functions from your functions exercise file. Import each function in a different way:
## b. Create a file named import_exericses.py. Within this file, use from to import the calculate_tip function directly. Call this function with values you choose and print the result.
from function_exercises import calculate_tip
print(calculate_tip(15, 200))

# q2. Read about and use the itertools module from the python standard library to help you solve the following problems:
## How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
import itertools
list(itertools.combinations('abc',1))
# 3

list(itertools.combinations('abc',2))
# 3

list(itertools.combinations('abc',3))
# 1

## How many different combinations are there of 2 letters from "abcd"?
list(itertools.combinations('abcd',2))
# 6

## How many different permutations are there of 2 letters from "abcd"?
list(itertools.permutations('abcd', 2))
print(len(list(itertools.permutations('abcd', 2))))
# 12

# q3. 
import json
fileref = json.load(open('profiles.json'))

## Total number of users
print(len(fileref))
# --- 19

## Number of active users
count = 0
for users in fileref:
    if (users['isActive'] == True):
        count +=1
print(count)
# --- 9

## Number of inactive users
count = 0
for users in fileref:
    if (users['isActive'] != True):
        count +=1
print(count)
# --- 10

## Grand total of balances for all users
total = 0
for users in fileref:
    balance = users['balance'][1:].replace(',','')
    total += float(balance)
print(total)
# --- 52667.02

## Average balance per user
total = 0
for users in fileref:
    balance = users['balance'][1:].replace(',','')
    total += float(balance)
print(total/len(fileref))
# --- 2771.95

## User with the lowest balance
balance = []
for users in fileref:
    balance.append(users['balance'][1:].replace(',',''))
print(min(balance))
# --- 1214.10

## User with the highest balance
balance = []
for users in fileref:
    balance.append(users['balance'][1:].replace(',',''))
print(max(balance))
# --- 3919.53

## Most common favorite fruit
## Least most common favorite fruit
fruits = []
for users in fileref:
    fruits.append(users['favoriteFruit'])
print(sorted(fruits))

countapple = 0
for fruit in fruits:
    if fruit == 'apple':
        countapple +=1
print(countapple)
# apple --> 4

countbanana = 0
for fruit in fruits:
    if fruit == 'banana':
        countbanana +=1
print(countbanana)
# banana --> 6

countstr = 0
for fruit in fruits:
    if fruit == 'strawberry':
        countstr +=1
print(countstr)
# strawberry --> 9

# most common: strawberry
# least common: apple

## Total number of unread messages for all users
unread = []
for user in fileref:
    for s in user['greeting'].split():
        if s.isdigit():
            unread.append(s)
print(unread)

sum = 0
for i in range(0, len(unread)):
    sum += int(unread[i])
print(sum)
# --- 210