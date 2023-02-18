#Mass Downloader
import os
from Bio import Entrez
from xml.etree import ElementTree

Entrez.email = "localuser@localhost.localdomain" 

def ambilMatchedSeqRecords(iteration, banyak_record):
    MatchedSeqRecordIDs = list()
    for hit in iteration.findall(".//Hit_accession")[:banyak_record]:
        MatchedSeqRecordIDs.append(hit.text)
    return MatchedSeqRecordIDs

def parseSingleIteration(tree, banyak_record):
    iteration = tree.find(".//Iteration")
    hitList = ambilMatchedSeqRecords(iteration, 
                                     banyak_record)
    return hitList

curr_dir = os.getcwd()
BLAST_file = curr_dir + "\\BLAST test.xml"
tree = ElementTree.parse(BLAST_file)
hitL = parseSingleIteration(tree, 5)
target_name = curr_dir + "\\BLAST test dumps.fasta"

if not os.path.dirname(target_name):
    os.makedirs(os.path.dirname(target_name))
    
if not os.path.isfile(target_name):
    print("Download file FASTA ke " + target_name)
    post_query = Entrez.epost("nuccore", 
                              id=",".join(hitL))
    search_results = Entrez.read(post_query)
    qkey = search_results["QueryKey"]
    web_env = search_results["WebEnv"]
    seqs_dumps = Entrez.efetch(db = "nuccore", 
                               query_key = qkey,
                               WebEnv = web_env,
                               rettype ="fasta", 
                               retmode="text")
    try:
        output_file_handle = open(target_name, "w")
        output_file_handle.write(seqs_dumps.read())
        print("Download FASTA selesai")
    except BaseException as be:
        exception_type = type(be).__name__
        print("Ada Error: ", exception_type)
    finally:
        output_file_handle.close()
        seqs_dumps.close()
else:
    print("Tidak bisa mendownload FASTA!")
    print("Karena file " + target_name + " ada! ")

a = open(target_name).read()
print("Isi file: " + target_name)
print(a)
