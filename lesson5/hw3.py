"""formula:
BMR = 10 × weight(kg) + 6.25 × height(cm) - 5 × age(y) + 5 (man)
BMR = 10 × weight(kg) + 6.25 × height(cm) - 5 × age(y) - 161 (woman)
input: weight, height, age, gender
output: BMR result
HINT: use input() to collect weight, height, age,
and gender; use gender to identify man or woman,
then provide the expected results according to the
BMR formula."""

weight = int(input("Enter your weight in KG: \n"))
height = int(input("Enter your height in cm: \n"))
age = int(input("Enter your age in years: \n"))
isMale = str(input("Are you male? (y/n)"))

if isMale == "y":
    isMale = True
elif isMale == "n":
    isMale = False
else:
    print("Error")
    quit()


if isMale:
    bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
else:
    bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161

bmr = round(bmr)
print("Your BMR is {:,} calories per day.".format(bmr))
