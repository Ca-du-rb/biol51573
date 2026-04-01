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

    # parse (pick apart and interpret) the arguments and return in two steps
    args = parser.parse_args()
    return args

    # or, parse the arguments and return in one step
    # return(parser.parse_args())

###-------- function to calculate the Fibonacci number
def fib():
    # initialize two integers
    a,b = 0,1

    for i in range(int(beyonce.position)):
        a,b = b,a+b

    fibonacci_number = a
    return fibonacci_number

###-------- function to print the output
def print_output(fibn):
    if beyonce.verbose:
        print(f"The Fibonacci number in position {beyonce.position} is {fibn}.")
    else:
        print(fibn)

###-------- define a main() function
def main():
    fibnum = fib()
    print_output(fibnum)



###-------- calling get_args happens out here on its own
beyonce = get_args() # arguments passed by args are always global, but here we assigned that output to beyonce

# set the environment for this script
# is this main (i.e., a standalone Python script), or
# is this a Python module (set of functions) being called by another script
if __name__ == '__main__': # if the namespace is main
    main()