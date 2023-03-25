import os
from xml.etree import ElementTree

def parseBLASTIteration(iteration, banyak_record):
    hitList = list()
    for hit in iteration.findall(".//Hit")[:banyak_record]:
        hitDict = dict()
        for k in ["Hit_id","Hit_def",
                  "Hit_accession", "Hit_len"]:
            hitDict[k] = hit.findtext(k)
        
        hitDict["hsps"] = list()
        for hsp in hit.findall(".//Hit_hsps"):
            hspDict = dict()
            hspDict["bit_score"] = hsp.findtext(".//Hsp_bit-score")
            hspDict["score"] = hsp.findtext(".//Hsp_score")
            hspDict["evalue"] = hsp.findtext(".//Hsp_evalue")
            hspDict["identity"] = hsp.findtext(".//Hsp_identity")
            hspDict["positivity"] = hsp.findtext(".//Hsp_positive")
            hspDict["gaps"] = hsp.findtext(".//Hsp_gaps")
            hspDict["length"] = hsp.findtext(".//Hsp_align-len")
            hspDict["query"] = hsp.findtext(".//Hsp_qseq")
            hspDict["midline"] = hsp.findtext(".//Hsp_midline")
            hspDict["hitseq"] = hsp.findtext(".//Hsp_hseq")            
            hspDict["qfrom"] = hsp.findtext(".//Hsp_query-from")
            hspDict["qto"] = hsp.findtext(".//Hsp_query-to")
            hspDict["hfrom"] = hsp.findtext(".//Hsp_hit-from")
            hspDict["hto"] = hsp.findtext(".//Hsp_hit-to")
            ident = int(hspDict["identity"])
            posit = int(hspDict["positivity"])
            length = int(hspDict["length"])
            
            try:
                hspDict["pc_id"] = ident * 100.0 / length
            except ZeroDivisionError:
                hspDict["pc_id"] = "error"
            
            try:
                hspDict["pc_pos"] = posit * 100.0 / length
            except ZeroDivisionError:
                hspDict["pc_pos"] = "error"
                        
            hitDict["hsps"].append(hspDict)
        hitList.append(hitDict)
    return hitList

def parseSingleIteration(tree, banyak_record):
    iteration = tree.find(".//Iteration")
    hitList = parseBLASTIteration(iteration, 
                                  banyak_record)
    return hitList

def printHspAlignment(hspD):
    panjang_baris = 50
    query = hspD["query"]
    midline = hspD["midline"]
    hitseq = hspD["hitseq"]
    for i in range(0,len(query),panjang_baris):
        print("  Query", query[i:i + panjang_baris])
        print("       ", midline[i:i + panjang_baris])
        print("Subject", hitseq[i:i + panjang_baris])

def showHitList(hitList, withaccession = True):
    for j, hitDict in enumerate(hitL):
        print("hit #", j + 1)
        if (withaccession):
            print("ID:",
                  hitDict["Hit_id"])
            print("Nama:",
                  hitDict["Hit_def"])
            print("Kode Aksesi:",
                  hitDict["Hit_accession"])
            print("Panjang sekuen:",
                  hitDict["Hit_len"], "bp")
            hspList = hitDict["hsps"]
            for hspDict in hspList[:1]:    
                print("Query (start - end):",
                      hspDict["qfrom"] + 
                      " - " + 
                      hspDict["qto"])
                print("Subject (start - end):",
                      hspDict["hfrom"] + 
                      " - " + 
                      hspDict["hto"])
                print("Bitscore:",
                      hspDict["bit_score"])
                print("Score:",
                      hspDict["score"])
                print("E value:",
                      hspDict["evalue"])
                print("Gaps:",
                      hspDict["gaps"] + 
                      "/" + 
                      hspDict["length"])
                print("Identities:", 
                      hspDict["identity"] + 
                      "/" + 
                      hspDict["length"])
                print("% Identity:", 
                      "%3.2f" % hspDict["pc_id"], 
                      "%")
                print("% Positivity:", 
                      "%3.2f" % hspDict["pc_pos"], 
                      "%")
                print("HSP Alignment (Query/Hit):")
                printHspAlignment(hspDict)
        print("")
        
curr_dir = os.getcwd()
BLAST_file = curr_dir + "\\BLAST test.xml"
tree = ElementTree.parse(BLAST_file)
hitL = parseSingleIteration(tree, 5)
showHitList(hitL[:5])
