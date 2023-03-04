# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 19:27:06 2023

@author: MALIK
"""

# Aktivitas Kitinase
# A unit = {[N-AGA]. 1.000 . 2 . T} / (BM N - AGA)
# BM N-AGA = 221.21 g/mol

def aktivitas_kitinase(Konsentrasi_N_AGA, waktu_inkubasi):
    a = Konsentrasi_N_AGA
    b = waktu_inkubasi
    aktivitas_enzim = (a * 1000 * 2 * b) / 221.21
    return aktivitas_enzim