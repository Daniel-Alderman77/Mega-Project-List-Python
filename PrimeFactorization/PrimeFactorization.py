# Prime Factorization - Have the user enter a number and find all Prime Factors (if there are any) and display them.
from math import sqrt


def is_prime(integer):
    print "Checking if integer is prime..."

    if integer == 2:
        return True

    elif integer <= 1 or integer % 2 == 0:
        return False

    else:
        to = sqrt(integer)

        i = 3

        while i <= to:
            if integer % i == 0:
                return False
            i += 2

        return True


def find_factors(user_input):
    print "Finding " + str(user_input) + "'s prime factors..."

    prime_factors = []

    # 2 is the lowest prime number
    i = 2

    while len(prime_factors) == 0:
        if is_prime(int(i)):
            number = user_input / i

            if is_prime(number) and i * number == user_input:
                prime_factors.append(i)
                prime_factors.append(number)

        i += 1

        print prime_factors


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

        else:
            print str(user_input) + " is not a prime number"

            find_factors(int(user_input))

run()
