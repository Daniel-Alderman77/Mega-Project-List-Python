# Prime Factorization - Have the user enter a number and find all Prime Factors (if there are any) and display them.
import sys


def is_prime(user_input):
    print "Checking if integer is prime..."

    return True


def find_factors(user_input):
    print "Finding prime factors..."

if len(sys.argv) < 2:
    print "No input found, please enter an integer as argument"

elif type(sys.argv[1]) != int:
    "Input is not an integer, please enter an integer as argument"

else:
    print "Integer has been entered"

    user_input = int(sys.argv[1])

    is_prime = is_prime(user_input)

    if is_prime:
        print str(user_input) + "is a prime number"

        find_factors(user_input)

    else:
        print str(user_input) + "is not a prime number"
