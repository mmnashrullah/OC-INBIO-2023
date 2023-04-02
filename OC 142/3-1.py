import os
from Bio import SeqIO
import primer3

curr_dir = os.getcwd()
FASTA_file = curr_dir + "\\ndhD Elaeis guineensis.fasta"

inputSeqFile = open(FASTA_file, "r")
SeqDict = SeqIO.parse(inputSeqFile, "fasta")

for fasta in SeqDict:
    acc_id = fasta.id
    desc = fasta.description
    sequence = str(fasta.seq)

primer_list = primer3.bindings.designPrimers(
            {
                "SEQUENCE_ID": "ndhD Elaeis guineensis gene",
                "SEQUENCE_TEMPLATE": sequence,
            },
            {
                "PRIMER_TASK": "generic",
                "PRIMER_PICK_LEFT_PRIMER": 1,
                "PRIMER_PICK_RIGHT_PRIMER": 1,
                "PRIMER_NUM_RETURN": 1,
                "PRIMER_OPT_SIZE": 22,
                "PRIMER_MIN_SIZE": 18,
                "PRIMER_MAX_SIZE": 24,
                "PRIMER_OPT_TM": 58.0,
                "PRIMER_MIN_TM": 55.0,
                "PRIMER_MAX_TM": 61.0,
                "PRIMER_MIN_GC": 45.0,
                "PRIMER_MAX_GC": 65.0,
                "PRIMER_MAX_POLY_X": 4,
                "PRIMER_GC_CLAMP": 3,
                "PRIMER_MAX_END_GC": 3,
                "PRIMER_PRODUCT_SIZE_RANGE": [100, 200],
                "PRIMER_TM_FORMULA" : 1,
                "PRIMER_SALT_CORRECTIONS" : 1
            }
            )
#print(primer_list.items())
for key in primer_list:
    print(key, ":", primer_list[key])