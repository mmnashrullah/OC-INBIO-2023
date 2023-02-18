#objek sekuen fasta
import os 
from Bio import SeqIO
curr_dir = os.getcwd()
target_name = curr_dir + "\\test.fasta"

inputSeqFile = open(target_name, "r")
SeqDict = SeqIO.parse(inputSeqFile, "fasta")

for fasta in SeqDict:
    acc_id = fasta.id
    desc = fasta.description
    sequence = fasta.seq
    print("ID: ", acc_id)
    print("Deskripsi: ", desc)
    print("Sekuen: ", sequence)
