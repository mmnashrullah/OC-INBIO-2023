#contoh penangkapan semua kesalahan

try:
    a = input("Masukkan angka pertama: ")
    b = input("Masukkan angka kedua: ")
    hslbg = int(a)/int(b)
    print("Hasil baginya: ", hslbg) 
except BaseException as be:
    exception_type = type(be).__name__
    print("\nBase Exception Error: ", exception_type)
else:
    print("Pangkat dua hasil baginya: ", hslbg**2)
finally:
    print("Akhirnya, selesai.")
