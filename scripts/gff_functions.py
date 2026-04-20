#!/usr/bin/env python3

from collections import defaultdict

# function to open and read the fasta file
def read_fasta(fasta_file):
  # covid_fasta is the file handle
  with open(fasta_file, "r") as covid_fasta: 
      
      # skip the header line
      header = next(covid_fasta)
  
      # Empty list to store each line for eventual concatenation
      genome_sequence = []
      
      # read DNA sequence line by line
      for line in covid_fasta:
          # strip the lines from newline characters
          line = line.strip()
          # add the line to the list
          genome_sequence.extend(line)
          
      # join list elements into a single string
      genome_sequence = ''.join(genome_sequence)
      
  return(genome_sequence)


# function to read and parse covid_genes.gff3
def read_gff(gff_file, genSeq):
  with open(gff_file, "r") as covid_gff:
    # seqs is a dictionary where the keys are the sequence IDs and the items are the sequences
    seqs = defaultdict(str)
    for line in covid_gff:
      # turn each line into a list to access its elements
      # some are separated by whitespace and others by semi-colon
      # hence we turn everything into whitespace before splitting into a list
      line = line.replace(';', ' ').split()
      
      # getting coordinates for genome sequence extraction and its ID
      # convert coordinates to integers
      crdBegin = int(line[3])
      crdEnd = int(line[4])
      seqID = line[8].replace("ID=","")
      seqs[seqID] = genSeq[crdBegin:(crdEnd+1)]
      
  return seqs


# function to write the outputs to the covFile
def write_output(covGene, seqDict):
  with open(covGene, "w") as cov_file:
    # iterate through the dictionary and write to output file
    for ID, SEQ in seqDict.items():
      cov_file.write(f">{ID}\n{SEQ}\n")
