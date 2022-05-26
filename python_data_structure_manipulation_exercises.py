students = [
    {
        "id": "100001",
        "student": "Ada Lovelace",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 91, 82, 71],
        "pets": [{"species": "horse", "age": 8}],
    },
    {
        "id": "100002",
        "student": "Thomas Bayes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [75, 73, 86, 100],
        "pets": [],
    },
    {
        "id": "100003",
        "student": "Marie Curie",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 89, 69, 65],
        "pets": [{"species": "cat", "age": 0}],
    },
    {
        "id": "100004",
        "student": "Grace Hopper",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [73, 66, 83, 92],
        "pets": [{"species": "dog", "age": 4}, {"species": "cat", "age": 4}],
    },
    {
        "id": "100005",
        "student": "Alan Turing",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [78, 98, 85, 65],
        "pets": [
            {"species": "horse", "age": 6},
            {"species": "horse", "age": 7},
            {"species": "dog", "age": 5},
        ],
    },
    {
        "id": "100006",
        "student": "Rosalind Franklin",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [76, 70, 96, 81],
        "pets": [],
    },
    {
        "id": "100007",
        "student": "Elizabeth Blackwell",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [69, 94, 89, 86],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100008",
        "student": "Rene Descartes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [87, 79, 90, 99],
        "pets": [{"species": "cat", "age": 10}, {"species": "cat", "age": 8}],
    },
    {
        "id": "100009",
        "student": "Ahmed Zewail",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [74, 99, 93, 89],
        "pets": [{"species": "cat", "age": 0}, {"species": "cat", "age": 0}],
    },
    {
        "id": "100010",
        "student": "Chien-Shiung Wu",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [82, 92, 91, 65],
        "pets": [{"species": "cat", "age": 8}],
    },
    {
        "id": "100011",
        "student": "William Sanford Nye",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [70, 92, 65, 99],
        "pets": [{"species": "cat", "age": 8}, {"species": "cat", "age": 5}],
    },
    {
        "id": "100012",
        "student": "Carl Sagan",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [100, 86, 91, 87],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100013",
        "student": "Jane Goodall",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [80, 70, 68, 98],
        "pets": [{"species": "horse", "age": 4}],
    },
    {
        "id": "100014",
        "student": "Richard Feynman",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [73, 99, 86, 98],
        "pets": [{"species": "dog", "age": 6}],
    },
]

# 1. How many students are there?
print(len(students))

# 14


# 2. How many students prefer light coffee? For each type of coffee roast?
def countlight(students):
    count = 0
    for student in students:
        if (student['coffee_preference'] == 'light'):
            count += 1
    return count
print(countlight(students))
# light: 3

def countmedium(students):
    count = 0
    for student in students:
        if (student['coffee_preference'] == 'medium'):
            count += 1
    return count
print(countmedium(students))
# medium: 6

def counthard(students):
    count = 0
    for student in students:
        if (student['coffee_preference'] == 'dark'):
            count += 1
    return count
print(counthard(students))
# dark: 5


# 3. How many types of each pet are there?
# HELP
def counthorse(students):
    count = 0
    for student in students:
        for pet in student['pets']:
            if pet['species'] == 'horse':
                count +=1
    return count
            #print(pet['species'])   
counthorse(students)              
print(counthorse(students))          
# horses: 4

def countdog(students):
    count = 0
    for student in students:
        for pet in student['pets']:
            if pet['species'] == 'dog':
                count +=1
    return count
countdog(students)                       
# dogs: 3

def countcat(students):
    count = 0
    for student in students:
        for pet in student['pets']:
            if pet['species'] == 'cat':
                count +=1
    return count
countcat(students)
# cats: 11


# 4. How many grades does each student have? Do they all have the same number of grades?
len(students[0]['grades']) # 4
len(students[1]['grades']) # 4
len(students[2]['grades']) # 4
# each student has 4 grades

# 5. What is each student's grade average?
# sum(students[0]['grades'])/4 # student 1: 78.5

def avggrades(students):
    for student in students:
        print(sum(student['grades'])/4)

avggrades(students)
# >>> avggrades(students)
# 78.5
# 83.5
# 73.25
# 78.5
# 81.5
# 80.75
# 84.5
# 88.75
# 88.75
# 82.5
# 81.5
# 91.0
# 79.0
# 89.0


# 6. How many pets does each student have?
def countpets(students):
    for student in students:
        print(len(student['pets']))
    
countpets(students)
# >>> countpets(students)
# 1
# 0
# 1
# 2
# 3
# 0
# 1
# 2
# 2
# 1
# 2
# 1
# 1
# 1


# 7. How many students are in web development? data science?
def count(students):
    count = 0
    for student in students:
        if student['course'] == 'data science':
            count +=1
    return count

count(students)
# data science: 7 studnets

def count(students):
    count = 0
    for student in students:
        if student['course'] == 'web development':
            count +=1
    return count

count(students)
# web development: 7 studnets


# {
#         "id": "100004",
#         "student": "Grace Hopper",
#         "coffee_preference": "dark",
#         "course": "data science",
#         "grades": [73, 66, 83, 92],
#         "pets": [{"species": "dog", "age": 4}, {"species": "cat", "age": 4}],
#     }
# 8. What is the average number of pets for students in web development?
def avg_num_of_pet(students):
    sum = 0
    for studnet in students:
        if student['course'] == 'web development':
            sum += len(student['pets'])
    return sum/7
avg_num_of_pet(students)

# average number is 2.0

# 9. What is the average pet age for students in data science?
def avg_num_of_pet(students):
    sum = 0
    for student in students:
        if student['course'] == 'data science':
            sum += len(student['pets'])
    return sum/7
avg_num_of_pet(students)

# average number is 1.286

# 10. What is most frequent coffee preference for data science students?


# 11. What is the least frequent coffee preference for web development students?
# 12. What is the average grade for students with at least 2 pets?
# 13. How many students have 3 pets?
# 14. What is the average grade for students with 0 pets?
# 15. What is the average grade for web development students? data science students?
# 16. What is the average grade range (i.e. highest grade - lowest grade) for dark coffee drinkers?
# 17. What is the average number of pets for medium coffee drinkers?
# 18. What is the most common type of pet for web development students?
# 19. What is the average name length?
# 20. What is the highest pet age for light coffee drinkers?