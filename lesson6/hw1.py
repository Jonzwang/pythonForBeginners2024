"""
Write a python program to ask a user name and email address.
1. Use function input() to get name and email
2. Store your input to the variables name and email one by one.
3. Using function print() Print out a concatenated string with user name and email collected from the keyboard, like the example below.

Hi! What is your Name? (Type in your NAME from keyboard)
What is your Email address? (Type in your EMAIL from keyboard)
'Hello [the NAME typed in]!. May I contact you via [the EMAIL typed in]?'
"""
def get_name_and_email():
    name = input("Hi! What is your Name ?")
    email = input("What is your Email address? ")

    message = f"Hello, {name}!. May I contact you via {email}?"
    print(message)

    return message

    # print("Hello, {}!. May I contact you via {}?".format(name.upper(), email.upper()))





value = get_name_and_email()
print(f'{value = }')
def plus(a=1, b=2):
    c = a + b
    return c

result = plus(2,3)
print(f'{result = }')

