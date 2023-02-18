#contoh if tiga atau lebih kondisi
Sal_tanah = float(input('Input nilai salinitas tanah: '))

if ((Sal_tanah >= 0) and (Sal_tanah <= 2)):
    print('Tanah non-salin')
elif ((Sal_tanah >= 2) and (Sal_tanah <= 4)):
    print('Tanah salin sedikit')
elif ((Sal_tanah >= 4) and (Sal_tanah <= 8)):
    print('Tanah salin moderat')
elif ((Sal_tanah >= 8) and (Sal_tanah <= 16)):
    print('Tanah salin kuat')
elif (Sal_tanah >= 16):
    print('Tanah salin sangat kuat')
else :
    print('Tidak boleh ada angka negatif')