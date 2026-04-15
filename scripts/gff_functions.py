#!/usr/bin/env python3

fasta_file = "../data/covid_genome/covid.fasta"
# function to read the fasta file
#def read_fasta(fasta_file):
with open(fasta_file, "r") as covid_fasta: # covid_fasta is the file handle
    
    # skip the header line
    header = next(covid_fasta)

    # Empty list to store each line for eventual concatenation
    genome_sequence = []
    # read DNA sequence line by line
    for line in covid_fasta:
        # strip the lines from newline characters
        line = line.strip()
        genome_sequence.extend(line)

    "".join(genome_sequence)
    # return(genome_sequence)
    print(genome_sequence)


