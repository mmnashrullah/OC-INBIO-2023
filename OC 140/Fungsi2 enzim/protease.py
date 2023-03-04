# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 20:32:14 2023

@author: MALIK
"""

#Aktivitas protease (kaseinase)
#Aktivitas protease (μg tirosin g-1 (bk) 2 jam-1) = (C X 15) / bk
# 15 = vol. total larutan

def aktivitas_Kaseinase(konsentrasi_Tyrosin_bebas, vol_LT, beratkering_sampel):
    a = konsentrasi_Tyrosin_bebas
    b = vol_LT
    c = beratkering_sampel
    aktKaseinase = (a * b) / c
    return aktKaseinase
