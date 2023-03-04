# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 19:36:57 2023

@author: MALIK
"""

# Aktivitas Ligninase Mn-Peroxidase

# Hitung guaiacol
# ∆c = (A0 – At)/ k . b
# k (molar absorptivitas) guaiakol = 12000 M-1 cm-1
# tebal larutan (tergantung kuvet)

def deltaC_guaiacol(init_abs, n_abs, tbl_larutan):
     a = init_abs
     b = n_abs
     c = tbl_larutan
     deltaC = (a - b) / 12000 * c
     return deltaC

# Hitung aktivitas Mn-Peroxidase
# Unit aktivitas MnP = (aktivitas total enzim) – (aktivitas lakase)
# Aktivitas total enzim = ∆c1 x (10**6) x vol. LT x (10**3) / menit x vol. LE (mL) 
# Aktivitas lakase = ∆c2 x (10**6) x vol. LT x (10**3) / menit x vol. LE (mL)

def aktivitas_TotEnzimLigninase(deltaC, vol_LT, menit, vol_LE):
    a = deltaC
    b = vol_LT
    c = menit
    d = vol_LE
    aktTotLigninase = a * (10**6) * b * (10**3) / c * d
    return aktTotLigninase

def aktivitas_Lakase(deltaC, vol_LT, menit, vol_LE):
    a = deltaC
    b = vol_LT
    c = menit
    d = vol_LE
    aktLakase = a * (10**6) * b * (10**3) / c * d
    return aktLakase

def aktivitas_MnPeroxidase(aktTotEnzimLigninase, aktLakase):
    a = aktTotEnzimLigninase
    b = aktLakase
    aktMnP = a - b
    return aktMnP