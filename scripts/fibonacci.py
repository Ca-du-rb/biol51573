#!/usr/bin/env python3

import argparse 

###------------ accept and parse command line arguments
# create an argument parser object
parser = argparse.ArgumentParser(description="This script calculates the number at a given position \
                                 in the Fibonacci sequence")

# add a positional argument. In this case, it's the position in the Fibonacci sequence
parser.add_argument("position", help="Position in the Fibonacci sequence", type=int)

# parse (pick apart and interpret) the arguments
args = parser.parse_args()

# initialize two integers
a,b = 0,1

for i in range(int(args.position)):
    a,b = b,a+b

fibonacci_number = a

print(f"The Fibonacci number in position {args.position} is {fibonacci_number}.")