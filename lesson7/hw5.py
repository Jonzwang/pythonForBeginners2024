def payment_calculator(rate, hour):
    """
    calculate payment total with flow control to satisfy the special bonus payment policy
        calculate payment using rate and hour, plus, add bonus accordingly
        make payment round to 2 digit precision
        return payment as the result
    Args:
        rate: dollar/hour
        hour: working time

    Returns:
    """
    if hour <= 40:
        payment = rate * hour
    elif 40 < hour <= 56:
        payment = rate * 40 + rate * 1.25 * (hour - 40)
    else:
        payment = rate * 40 + rate * 1.25 * 16 + rate * 1.5 * (hour - 56)
    return payment

# print(payment_calculator(10, 30))
# print(payment_calculator(10, 45))
# print(payment_calculator(10, 60))

def payment_for_user():
    """
    calculate one employee weekly salary from user entry of employee_name, rate and working hour
        ask user to enter employee_name, rate and hour from keyboard
        call function payment_calculator() to get weekly payment total
        print out: The weekly payment total for {employee_name}: ${payment}
    Returns:

    """

    employee_name = input("Hi! Please enter your name:")
    rate = float(input("Please enter payment rate:"))
    hour = float(input("please enter your total working hours:"))

    payment = payment_calculator(rate, hour)
    print(f"The weekly payment total for {employee_name} is: ${payment}")

# payment_for_user()

def main():
    total = int(input("How many employees are there in total?"))
    for employee in range(total):
        payment_for_user()

main()

