#BLAST

import os
from Bio.Blast.NCBIWWW import qblast
curr_dir = os.getcwd()
FASTA_name = curr_dir + "\\test.fasta"
BLAST_file = curr_dir + "\\BLAST test.xml"

try:
    if (os.path.dirname(BLAST_file)) != str(""):
        print(BLAST_file + " tidak ada!")
        print(BLAST_file + " harus dibuat!")
        os.makedirs(os.path.dirname(BLAST_file))
        print(BLAST_file + " sudah dibuat!")
except FileExistsError:
    print(BLAST_file + " sudah ada...")
    pass

fasta_seq = open(FASTA_name).read()

if not os.path.isfile(BLAST_file):  
    print("Menulis hasil BLAST ke: " + BLAST_file)
    
    PROGRAM = "blastn"
    DATABASE = "nr"
    SEQUENCE = fasta_seq
    BLAST_handle = qblast(PROGRAM, DATABASE, SEQUENCE,
                          hitlist_size = 5,
                          megablast = False)

    try:
        with open(BLAST_file,"w+") as BLAST_result:
            BLAST_result.write(BLAST_handle.read())
            BLAST_result.close()
    except BaseException as be:
        exception_type = type(be).__name__
        print("Ada Error: ", exception_type)
    finally:
        BLAST_handle.close()
        print("BLAST selesai.")
        print("Cek hasil BLAST di: " + BLAST_file)
else:
    print("Tidak bisa mendownload BLAST")
    print("Karena file " + BLAST_file + " ada! ")
