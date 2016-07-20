# Prime Factorization - Have the user enter a number and find all Prime Factors (if there are any) and display them.
import sys


def is_prime(user_input):
    print "Checking if integer is prime..."

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

        if is_prime(user_input):
            print str(user_input) + " is a prime number"

            find_factors(user_input)

        else:
            print str(user_input) + "is not a prime number"

run()
