# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 20:04:49 2023

@author: MALIK
"""

# Aktivitas Fosfatase pyrofosfatase

# 1 g tanah, susut berapa shg berat konstan
# Misal dikeringkan hasilnya 0.7 g, sehingga kadar airnya
# adalah 30% (0.3) -> Faktor kadar air

# lalu tanah tsb diencerkan 
# misal dari 0.7 g tanah kering menjadi 7 ml
# berarti faktor pengencerannya 10

def aktivitas_Pyrofosfatase(konsentrasi_Fosfat_padasampel, faktor_kadarair,
                            faktor_pengenceran):
    a = konsentrasi_Fosfat_padasampel
    b = faktor_kadarair
    c = faktor_pengenceran
    aktPyrofosfatase = a * b * c
    return aktPyrofosfatase

def aktivitas_Fosfodiesterase(konsentrasi_pNitrofenol_padasampel, faktor_kadarair,
                              faktor_pengenceran):
    a = konsentrasi_pNitrofenol_padasampel
    b = faktor_kadarair
    c = faktor_pengenceran
    aktFosfodiesterase = a * b * c
    return aktFosfodiesterase