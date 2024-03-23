from random import choice, randrange


def rps():
     hand = input("please input r(rock), p,(paper), or s(scissors) : ")
     print(hand)
     c_hand = choice(['r','p','s'])
     print(hand, c_hand)
     if hand == c_hand:
         print("tie, try again")
     else:
         if (hand == 'r' and c_hand == 's' or
                 hand == 'p' and c_hand == 'r' or
                 hand == 's' and c_hand == 'p'):
             print("I won")
         else:
             print("computer won")

def guess_the_number():
    the_number = randrange(100)
    while True:
        guess = int(input("enter the number: "))
        if guess == the_number:
            print("correct")
            break
        elif guess > the_number:
            print("your guess is too high")
        else:
            print("your guess is too low")


if __name__ == '__main__':
    # rps()
    guess_the_number()
