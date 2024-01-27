"""BMI formula:
BMI = (wheight in pounds / (height in inches x height in inches)) * 703"""
Weight_str = input("Weight in Pounds? ")
Height_str = input('Height in inches? ')
Height = int(Height_str)
Weight = int(Weight_str)
BMI = Weight / (Height * Height) * 703
BMI = round(BMI, 2)
print(f"BMI = {BMI}")