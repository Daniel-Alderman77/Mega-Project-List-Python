# Find PI to the Nth Digit - Enter a number and have the program generate PI up to that many decimal places.
# Keep a limit to how far the program will go.

import sys
from decimal import Decimal, getcontext


# Uses BPP formula as described here http://stackoverflow.com/questions/28284996/python-pi-calculation
def generate_pi(nth):
    print "Now generating PI to " + str(nth) + " digits"

    getcontext().prec = nth + 1

    pi = sum(1 / Decimal(16) ** k *
              (Decimal(4) / (8 * k + 1) -
               Decimal(2) / (8 * k + 4) -
               Decimal(1) / (8 * k + 5) -
               Decimal(1) / (8 * k + 6)) for k in range(100))

    return pi


if len(sys.argv) < 2:
    print "Less than one argument entered"

elif len(sys.argv) > 2:
    print "More than one argument entered"

else:
    print "Valid number of arguments entered"
    nth = int(sys.argv[1])

    pi = generate_pi(nth)

    print "PI to " + str(nth) + " digits = " + str(pi)
