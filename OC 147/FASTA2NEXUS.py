#konversi data FASTA ke NEXUS
import os
import dendropy

curr_dir = os.getcwd()
FASTA_file = curr_dir + "\\file.fasta"
NEXUS_file = curr_dir + "\\file.nexus"

if not os.path.isfile(NEXUS_file):
    SeqData = dendropy.DnaCharacterMatrix.get(path = FASTA_file, schema = "fasta")
    SeqData.write(path = NEXUS_file, schema = "nexus")
    print("File", FASTA_file, "telah dikonversi ke", NEXUS_file )
else:
    print("Tidak bisa membuat file NEXUS!")
    print("Karena file" , NEXUS_file, "ada!")