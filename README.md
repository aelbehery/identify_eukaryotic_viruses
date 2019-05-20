# identify_eukaryotic_viruses

## Description

This is a pipeline to identify eukaryotic virus genome bins according to [Roux et al (2016)](https://doi.org/10.1038/nature19366).
## Dependencies

 1. [Prodigal](https://github.com/hyattpd/Prodigal)
 2. [Blast+](ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/)
 3. Python 2.7

## Installation
There is no need for installation; just copy the scripts to your desired folder and make sure they have executable permissions.

## Data preparation

 1. Download virus genomes with known host information from the NCBI's [Viral Genome Browser](https://www.ncbi.nlm.nih.gov/genomes/GenomesGroup.cgi?taxid=10239).
 2. Append protein sequence deflines with "|eukaryotic" or "|prokaryotic" according to host information obtained from NCBI.
 3. Concatenate all sequences into one fasta file.
 4. Generate blast database out this fasta file and name this database "prok+euk" using -title option of the makeblastdb command. 

## Running

    ./identify_euk.sh <bin_nucleotide_file>
