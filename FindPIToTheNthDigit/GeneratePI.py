# Find PI to the Nth Digit - Enter a number and have the program generate PI up to that many decimal places.
# Keep a limit to how far the program will go.

import sys

def GeneratePI(nth):
    print "Now generating PI to " + str(nth) + " digits"

if len(sys.argv) < 2:
    print "Less than one argument entered"

elif len(sys.argv) > 2:
    print "More than one argument entered"

else:
    print "Valid number of arguments entered"
    nth = sys.argv[1]

    GeneratePI(nth)
