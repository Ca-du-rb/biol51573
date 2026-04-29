#!/usr/bin/env python3

covidPath = "../data/covid_genome/covid_genes.fasta"

with open(covidPath, "r") as covidFile:
    for line in covidFile:
        # prints the IDs as well and their lengths, but does the job
        # of printing the genome sequences and their lengths too
        print(line)
        print(len(line.strip())) # strings stripped of the newline characters
