#if... else...

#contoh if dua kondisi
angka = int(input('Masukkan angka: '))

if (angka % 2 == 0):
    print('Angka genap terdeteksi')
    print('%d adalah angka genap' % (angka))
else:
    print('Angka ganjil terdeteksi')
    print('%d adalah angka ganjil' % (angka))