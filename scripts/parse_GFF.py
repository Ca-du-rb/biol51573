#!/usr/bin/env python3

# Module for parsing arguments from the command line
import argparse

# Functions from custom module to read the COVID gene sequences
from gff_functions import read_fasta, read_gff, write_output

## ----- function to parse command-line arguments:
def get_args():
    # create an argument parser object:
    parser = argparse.ArgumentParser(description="This script reads FASTA and GFF files and returns DNA \
                                     sequence information on specific genes")
    
    # Remember to specify the type of the arguments
    # add FASTA file name:
    parser.add_argument("FASTA_name", help="Name of the genome FASTA file", type=str)

    # add GFF file name:
    parser.add_argument("GFF_name", help="Name of the GFF file", type=str)

    # parse the arguments and then return them:
    args = parser.parse_args()
    return args
    # what is returned here is always global


#------- define a main function
def main():
  # file to store the IDs and sequences
  covid_file = "../data/covid_genome/covid_genes.fasta"
  
  # reading full genome sequence and storing it in genomeSEQ
  genomeSEQ = read_fasta(files.FASTA_name)
  
  # reading gff file (to get IDs and their respective sub-sequences)
  covidGFF = read_gff(files.GFF_name, genomeSEQ)
  
  # writing output to covid_file
  write_output(covid_file, covidGFF)


#------- obtaining file paths for the FASTA and GFF files with get_args
files = get_args()

# Setting the environment for the script:
# (If it's run on its own, it's in the main environment)
if __name__ == '__main__':
    main()
