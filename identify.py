#!/usr/bin/env python
import sys
from Bio import SeqIO

fna = sys.argv[1]
faa = sys.argv[2]
blast = sys.argv[3]
d = {}
bin = 0

for record in SeqIO.parse(fna, "fasta"):
    d[record.id] = [len(record.seq), 0, 0, 0, False]
    bin += len(record.seq)

for record in SeqIO.parse(faa, "fasta"):
    d[record.id.rsplit("_", 1)[0]][1] +=1

with open(blast, "rU") as blast_fh:
    for line in blast_fh:
        line = line.rstrip()
        fields = line.split("\t")
        if fields[-1].split("|")[-1] == "eukaryotic":
            d[fields[0].rsplit("_", 1)[0]][2] +=1
        elif fields[-1].split("|")[-1] == "prokaryotic":
            d[fields[0].rsplit("_", 1)[0]][3] +=1
for k, v in d.iteritems():
    if float(v[2])/v[1] > 0.5:
        d[k][4] = True
    elif v[2] >=1 and v[3] == 0:
        d[k][4] = True
    elif v[2] >= (0.1 * v[1]) and v[2] >=3 :
        if v[3] < (0.25 * v[1]):
            d[k][4] = True
length = 0
for k, v in d.iteritems():
    if v[4]:
        length += v[0]
print d

if length > 10000 or length > (0.25 * bin):
    print "%s\teukaryotic" % fna
else:
    print "%s\tnot eukaryotic" % fna
