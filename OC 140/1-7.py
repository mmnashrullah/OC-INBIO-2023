import re

text = r"""
p53 adalah protein faktor transkripsi yang mendapat julukan
sebagai "the guardian of the genome" atau "penjaga genom", karena
peran protein tersebut dalam menjaga sel dari mutasi genetik 
akibat kerusakan DNA. p53 berperan pada berbagai fungsi seluler,
regulasi, apoptosis, replikasi DNA, proliferasi, dan lain – lain.
Dalam kondisi normal, jumlah konsentrasi p53 dalam sitoplasma
sangat sedikit. Upregulasi protein ini dapat terjadi apabila
sel terpapar berbagai faktor stress, diantaranya kerusakan DNA
(baik oleh paparan UV, infra merah, ataupun senyawa kimia), stres
oksidatif, syok osmotik, kekurangan ribonukleotida, dan ekspresi
onkogen yang terderegulasi. Sebagai "penjaga genom", p53 berperan 
dalam meregulasi siklus sel, apoptosis, dan kestabilan genom. 
p53 berperan dalam mengaktivasi mekanisme DNA repair, menahan 
pertumbuhan sel di fase G1/S dari siklus sel untuk memberikan 
waktu perbaikan DNA, memicu mekanisme apostosis jika 
perbaikan DNA tidak memungkinkan, dan memicu respon senesens sel.         
"""

print(re.findall("p53", text))
