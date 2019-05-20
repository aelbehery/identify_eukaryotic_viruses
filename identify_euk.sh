#!/bin/bash
# set up a standard unix shell
#$ -S /bin/bash
#
# set working directory to current one
#$ -cwd
#
# define the name of the job
#$ -N blast
#
#State that the job should have the same environment variables as the shell
#executing qsub
#$ -V
#
# reserve the requested slots
#$ -R y
#
# path for standard output log
#$ -o logs/
#
# merge standard output and standard error logs
#$ -j y
#
#$ -pe hmp 3

fna=$1
faa=${1%.*}.faa
blast=${faa%.*}.vs.prok+euk.blastp.txt
filtered=${blast%.*}_filtered.txt

prodigal -i $fna -a $faa || prodigal -i $fna -a $faa -p meta

blastp -query $faa -db prok+euk -out $blast -outfmt "6 std stitle" -num_threads 3

awk '!seen[$1]++' $blast > $filtered

./identify.py $fna $faa $filtered

