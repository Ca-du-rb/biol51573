#!/usr/bin/env python3

# For user created modules, bear in mind that they must be in the same directory as
# the main code file

import my_functions

def main():
    input_name = input("Enter a name: ")

    my_functions.greeting(input_name)

# set the environment for this script
# is it main(), or is this module being called by something else?
if __name__ == '__main__':
    main()