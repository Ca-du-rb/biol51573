#!/usr/bin/env python3

import argparse 

###-------- function to parse the command-line arguments
def get_args():
    ###------------ accept and parse command line arguments
    # create an argument parser object
    parser = argparse.ArgumentParser(description="This script calculates the number at a given position \
                                    in the Fibonacci sequence")

    # add a positional argument. In this case, it's the position in the Fibonacci sequence
    parser.add_argument("position", help="Position in the Fibonacci sequence", type=int)

    # an optional argument for verbose output or not
    # if 'store_true', this means assign 'True' if the optional argument is specified
    # on the command line, so the default for 'store_true' is actually false (no optional argument specified)
    parser.add_argument("-v", "--verbose", help="Print verbose output", action='store_true')

    # parse (pick apart and interpret) the arguments
    args = parser.parse_args()


###-------- function to calculate the Fibonacci number
def fib():
    # initialize two integers
    a,b = 0,1

    for i in range(int(args.position)):
        a,b = b,a+b

    fibonacci_number = a


###-------- function to print the output
def print_output():
    if args.verbose:
        print(f"The Fibonacci number in position {args.position} is {fibonacci_number}.")
    else:
        print(fibonacci_number)

##-------- define a main() function
def main():


# set the environment for this script
# is this main (i.e., a standalone Python script), or
# is this a Python module (set of functions) being called by another script
if __name__ == '__main__': # if the namespace is main
    main()