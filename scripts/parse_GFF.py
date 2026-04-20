#!/usr/bin/env python3

# Module for parsing arguments from the command line
import argparse

# Module with the functions to read the COVID gene sequences
import gff_functions

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


#------- define a main function
def main():
  # file to store the IDs and sequences
  covid_file = "../data/covid_genome/covid_genes.fasta"
  
  # reading full genome sequence and storing it in genomeSEQ
  genomeSEQ = read_fasta(files[0])
  
  # reading gff file (to get IDs and their respective sub-sequences)
  covidGFF = read_gff(files[1], genomesSEQ)
  
  # writing output to covid_file
  write_output(covid_file, covidGFF)

#------- obtaining file paths with get_args
files = get_args()

# Setting the environment for the script:
if __name__ == '__main__':
    main()
