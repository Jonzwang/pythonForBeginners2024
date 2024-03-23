def payment_calculator(rate, hour):
    #base salary

    payment = hour * rate

    # bonus = 0
    #for hour over 40
    if hour > 40:
        # bonus= (hour - 40) * .25 * rate
        payment += (hour-40) * .25 * rate
    if hour >56:
        # bonus = (56 - 40) * .25 * rate + (hour - 56) * .5 * rate
        # bonus += (hour - 56) * .25 * rate
        payment += (hour - 56) * .25 * rate

    # payment += bonus
    print(f"{payment=}")
    return payment


# payment_calculator(10, 30)
# payment_calculator(10, 45)
# payment_calculator(10, 60)

def payment_for_user():
    name = input("name: ")
    hours = float(input("hours: "))
    rate = float(input("rate: "))
    pay = payment_calculator(rate, hours)
    print(f"The weekly payment total for {name}: ${pay}")

def main():
    total = int(input("emplooyee total: "))
    for n in range(total):
        payment_for_user()

if __name__ == '__main__':
    main()