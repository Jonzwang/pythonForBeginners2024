"""1. Make function bmi(weight, height) for BMI Calculator (http://www.calculator.net/bmi-calculator.html)
formula: BMI =  mass (kg) / (height(m) × height(m))

input: weight, height
output: result

2. Make function bmr(weight, height, age, gender)   for BMR Calculator (http://www.calculator.net/bmr-calculator.html)
formula:
BMR = 10 × weight(kg) + 6.25 × height(cm) - 5 × age(y) + 5 (man)
BMR = 10 × weight(kg) + 6.25 × height(cm) - 5 × age(y) - 161 (woman)
input: weight, height, age, gender
output: result

3. Make function main() to call BMI and BMR Calculators.
Asking user to enter weight (kg), height (cm), age, gender(male/female)
Get results by calling function bmi(weight, height) and bmr(weight, height, age)
print out result in BMI = f'{bmi_result} kg/m2', BMR = f'{bmr_result} Calories/day'
"""
def bmi(Height, Weight):

    Height /= 100
    BMI = Weight / (Height * Height)
    BMI = round(BMI, 2)
    print(f'BMI = {BMI} kg/m2')

def bmr(weight, height, age, gender):

    bmr = (10 * weight) + (6.25 * height) - (5 * age)

    if gender == "male":
        bmr += 5
    elif gender == "female":
        bmr -= 161
    else:
        print("Error")
        quit()

    print (f'BMR = {round(bmr,0):,} Calories/day')

def main():

    weight = int(input("Enter your weight in KG: \n"))
    height = int(input("Enter your height in cm: \n"))
    age = int(input("Enter your age in years: \n"))
    gender = str(input("What's your gender? (male/female): \n"))

    bmi(Height=height, Weight=weight)
    bmr(weight, height, age, gender)

main()

