# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 20:48:43 2023

@author: MALIK
"""

# Aktivitas Urease (Schinner)

# Aktivitas urease = {(S – C).10.A.100} / (B.%dm.a.b)
# dengan asumsi fp1 10 dan fp2 100
# bm_NH4 =  18.039 g/mol

def aktivitas_Urease(konsentrasi_NH4_bebas_sampel,
                     konsentrasi_NH4_bebas_kontrol,
                     vol_LE, 
                     beratkering_sampel,
                     faktor_beratkering_sampel,
                     waktu_inkubasi):
    a = konsentrasi_NH4_bebas_sampel
    b = konsentrasi_NH4_bebas_kontrol
    c = vol_LE
    d = beratkering_sampel
    e = faktor_beratkering_sampel
    f = waktu_inkubasi
    aktUrease = ((a - b) * 10 * c * 100) / (d * e * 18.039 * f)
    return aktUrease

#misal fp1 dan fp2 tidak 10 dan 100
def aktivitas_Urease2(konsentrasi_NH4_bebas_sampel,
                      konsentrasi_NH4_bebas_kontrol,
                      fp1, fp2,
                      vol_LE, 
                      beratkering_sampel,
                      faktor_beratkering_sampel,
                      waktu_inkubasi):
    a = konsentrasi_NH4_bebas_sampel
    b = konsentrasi_NH4_bebas_kontrol
    c = vol_LE
    d = beratkering_sampel
    e = faktor_beratkering_sampel
    f = waktu_inkubasi
    v1 = fp1
    v2 = fp2
    aktUrease = ((a - b) * v1 * c * v2) / (d * e * 18.039 * f)
    return aktUrease