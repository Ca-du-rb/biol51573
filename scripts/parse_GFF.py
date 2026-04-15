#!/usr/bin/env python3

# Module for parsing arguments from the command line
import argparse

## ----- function to parse command-line arguments:
def get_args():
    # create an argument parser object:
    parser = argparse.ArgumentParser(description="This script reads FASTA and GFF files and returns DNA \
                                     sequence information on specific genes")
    
    # add FASTA file name:
    parser.add_argument("FASTA_name", help="Name of the genome FASTA file")

    # add GFF file name:
    parser.add_argument("GFF_name", help="Name of the GFF file")

    # parse the arguments and then return them:
    args = parser.parse_args()
    return args
    # what is returned here is always global











# Setting the environment for the script:
if __name__ == '__main__':
    main()