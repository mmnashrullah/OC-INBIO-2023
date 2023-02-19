#Alignment DNA dengan MAFFT

import os
from Bio.Align.Applications import MafftCommandline

curr_dir = os.getcwd()
FASTA_file = curr_dir + "\\najas3.fasta"

MAFFT_result = curr_dir + "\\Aln najas3.fasta"

if not os.path.isfile(MAFFT_result):
    MAFFT_exe = "D:\\BIOTOOLS\\MAFFT-win\\mafft.bat"
   
    m_line = MafftCommandline(MAFFT_exe, 
                              input = FASTA_file, 
                              auto = True
                              )
    print("Run Command:", m_line)
    stdout, stderr = m_line()
    with open(MAFFT_result, "w") as handle:
        handle.write(stdout)
    print(MAFFT_result, "berhasil dibuat!")
    print("Alignment MAFFT berhasil!")
else:
    print("Tidak bisa melakukan alignment!")
    print("Karena file" , MAFFT_result , "ada!")
