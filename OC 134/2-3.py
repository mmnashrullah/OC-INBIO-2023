#contoh penanganan semua kesalahan multi eksepsi

try:
    a = input("Masukkan angka pertama: ")
    b = input("Masukkan angka kedua: ")
    hslbg = int(a)/int(b)
    print("Hasil baginya: ", hslbg) 
except (ZeroDivisionError):
    print("Tidak boleh dibagi nol")
except (ValueError):
    print("Ada nilai yang salah")
except (KeyboardInterrupt):
    print("Program dihentikan paksa dengan Ctrl+C")
else:
    print("Lanjut proses...")
    print("Pangkat dua hasil baginya: ", hslbg**2)
finally:
    print("Akhirnya, selesai.")
