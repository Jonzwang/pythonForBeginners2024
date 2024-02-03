"""BMI formula:
BMI = (wheight in pounds / (height in inches x height in inches)) * 703"""
Weight_str = input("Weight in Pounds? ")
Height_str = input('Height in inches? ')

# convert sting to integer
Height = float(Height_str) # take entry for height
Weight = float(Weight_str) # take entry for weight

# print =(type(Weight_str), type(Weight))

#BMI = Weight / (Height * Height) * 703
BMI = Weight / Height ** 2 * 703

BMI = round(BMI, 2)

print(f"BMI = {BMI}")