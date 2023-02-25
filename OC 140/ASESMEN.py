# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 14:15:07 2023

@author: MALIK
"""

#merekam data

import traceback as tb
import statistics as stat

print("==============================")
print("===PROGRAM HITUNG KADAR IAA===")
print("Masukkan data dalam bentuk µg/g")
print("==============================")
limitData = int(input("Masukkan jumlah sampel: "))
try:
    #inisiasi semua objek
    recData = open("recordIAA.txt","w")
    recList = []
    #iterasi untuk input data sejumlah sampel
    for i in range(limitData):
        sampleData = int(input(
            "Data ke-" + str(i+1) + ": "))
        #tulis data ke file
        recData.write(str(sampleData)+"\n")
        #record ke list
        recList.insert(i, sampleData)
    #cetak pesan bila data terekam
    print("==============================")
    print("Data terekam di recordIAA.txt!")
    print("==============================")
    #tutup file
    recData.close()
except BaseException as be:
    be = tb.format_exc()
    print("Error: ", be)
else:
    #bila tidak ada error
    #hitung kadar IAA
    rerata = stat.mean(recList)
    galat = stat.stdev(recList)
    #cetak hasil
    hasil = ("{a:.2f} ± {b:.2f} µg/g".format(a = rerata, b = galat))
    #bila menggunakan %formatting, bulatkan angka dengan round()
    #a = round(rerata, 2)
    #b = round(galat, 2)
    #hasil = ("%s ± %s µg/g" % (a, b))
    print("Kadar IAA pada sampel adalah:", hasil)
finally:
    #cleanup
    #bersihkan list
    recList = []
    #tutup file
    recData.close()