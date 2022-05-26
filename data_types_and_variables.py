type(99.9)
type("False")
type(False)
type('0')
type(0)
type(True)
type('True')
type([{}])
type({'a': []})

# What data type would best represent:
## A term or phrase typed into a search box? -- string
## If a user is logged in? -- boolean
## A discount amount to apply to a user's shopping cart? -- int
## Whether or not a coupon code is valid? -- boolean
## An email address typed into a registration form? -- string
## The price of a product? -- float
## A Matrix? -- list
## The email addresses collected from a registration form? -- list
## Information about applicants to Codeup's data science program? -- dictionary

'1' + 2 # error
6 % 4 # 2
type(6 % 4) # int
type(type(6 % 4)) #class 'type'
'3 + 4 is ' + 3 + 4 # error
0 < 0 # False
'False' == False # False
True == 'True' # False
5 >= -5 # True
True or "42" # True
6 % 5 # 1
5 < 4 and 1 == 1 # False
'codeup' == 'codeup' and 'codeup' == 'Codeup' # False
4 >= 0 and 1 !== '1' # syntax error
6 % 3 == 0 # True
5 % 2 != 0 # True
[1] + 2 # type error
[1] + [2] # [1, 2]
[1] * 2 # [1, 1]
[1] * [2] # type error
[] + [] == [] # True
{} + {} # type error

# You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, they love it),
# and Hercules (1 day, you don't know yet if they're going to like it).
# If price for a movie per day is 3 dollars, how much will you have to pay?

littlemermaid = 3
hercules = 3
brotherbear = 5
totalpay = 3 * littlemermaid + 5 * brotherbear + 1 * hercules
print(totalpay)

# Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook,
# they pay you a different rate per hour.
# Google pays 400 dollars per hour, Amazon 380, and Facebook 350.
# How much will you receive in payment for this week? You worked 10 hours for Facebook,
# 6 hours for Google and 4 hours for Amazon.

google = 400
amazon = 380
facebook = 350
googlehour = 6
facebookhour = 10
amazonhour = 4

totalpay = facebookhour * facebook + googlehour * google + amazonhour * amazon
print(totalpay)

# A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.

classnotfull = True
notconlict_schedule = False
can_be_enrolled = classnotfull and notconlict_schedule
print(can_be_enrolled)

# A product offer can be applied only if people buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products.

itemsmorethan2 = False
notexpired = True
people = itemsmorethan2 and notexpired
premium = notexpired
print(people)
print(premium)

# Create a variable that holds a boolean value for each of the following conditions:
username = 'codeup'
password = 'notstrongpassword'

# the password must be at least 5 characters
at_least_five_characters = len(password) >= 5

# the username must be no more than 20 characters
at_least_20_char = len(password) <= 20

# the password must not be the same as the username
not_the_same = password != username

# bonus neither the username or password can start or end with whitespace
username_no_white_space = username[0] != ' ' and username[-1] != ' '
password_no_white_space = password[0] != ' ' and username[-1] != ' '