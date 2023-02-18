#objek sekuen

file_FASTA = "test.fasta"

from Bio import Entrez
Entrez.email = "localuser@localhost.localdomain" 
efetch_handle = Entrez.efetch(db="nuccore", 
                              id="OM037657", 
                              rettype="fasta", 
                              retmode="text")
fasta_record = efetch_handle.read()
#print(fasta_record)
output_file_handle = open(file_FASTA, "w")
output_file_handle.write(efetch_handle.read())
output_file_handle.close()
efetch_handle.close()