# Prime Factorization - Have the user enter a number and find all Prime Factors (if there are any) and display them.
from math import sqrt


def is_prime(user_input):
    print "Checking if integer is prime..."

    if user_input == 2:
        return True

    elif user_input <= 1 or user_input % 2 == 0:
        return False

    else:
        to = sqrt(user_input)

        i = 3

        while i <= to:
            if user_input % i == 0:
                return False
            i += 2

        return True


def find_factors(user_input):
    print "Finding prime factors..."


def run():
    user_input = raw_input("Please enter an integer: ")

    try:
        int(user_input)

    except ValueError:
        print "Input is not an integer, please enter an integer"

    else:
        print "Integer has been entered"

        if is_prime(int(user_input)):
            print str(user_input) + " is a prime number"

            find_factors(int(user_input))

        else:
            print str(user_input) + " is not a prime number"

run()
