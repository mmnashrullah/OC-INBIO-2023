 #contoh if tiga kondisi
angka = int(input('Masukkan angka: '))

if (angka == 0):
   print('Ini bilangan nol')
elif (angka > 0):
   print('Bilangan positif terdeteksi')
   print('%d adalah bilangan positif' % (angka))
else:
   print('Bilangan negatif terdeteksi')
   print('%d adalah bilangan negatif' % (angka))

