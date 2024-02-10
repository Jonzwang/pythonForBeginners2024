# 1.create a variable and set it equal to True using a statement containing an "and" Boolean operator
p1 = 1 == 1 and 2 == 2
print(f"{p1=}")
# 2.create a variable and set it equal to False using a statement containing an "and" Boolean operator
p2 = 2 == 1 and 1 == 2
print(f"{p2=}")
# 3.create a variable and set it equal to True using a statement containing an "or" Boolean operator
p3 = 1 == 1 or 2 == 1
print(f"{p3=}")
# 4.create a variable and set it equal to False using a statement containing an "or" Boolean operator
p3 = 1 == 2 or 2 == 1
p3a = 5 == 3 or 2 == 1
p3b = 4 == 5 or 6 == 1
print(f"{p3=}, {p3a=}, {p3b=}")
# 5.create a variable and set it equal to True using a statement containing an "not" Boolean operator
p4 = not (1 == 2 and 1 == 1)
print(f"{p4=}")
# 6.create a variable and set it equal to False using a statement containing an "not"
p5 = not (5 == 5 and 2 == 2)
print(f"{p5=}")

# Boolean operator
var = False or not 5 < 8
print ("False or not 5 < 8 ?", var)

#7. Using var1 and var2 for the following program:
var_1 = not 3 > 1 and 5 != 2 or 6 == 6
var_2 = 4 * 2 != 6 and not 7 % 6 == 1

#7.1 Evaluation order of operations for Boolean operators of var_1 and var_2

print(f"{var_1=}")

print(f"{var_2=}")

#7.2 Change the var_1 and var_2 assignment to have result as followed:

#7.3 make var_1 evaluate to False by changing or removing a single Boolean operator
var_1a = not 3 > 1 and 5 != 2 and 6 == 6
print(f"{var_1=}, {var_1a=}")

#7.4 make var_2 evaluate to True by changing or removing a single Boolean operator
var_2a = 4 * 2 != 6 and 7 % 6 == 1
var_2b = 4 * 2 != 6 or not 7 % 6 == 1
print(f"{var_2=}, {var_2a=}, {var_2b=}")
