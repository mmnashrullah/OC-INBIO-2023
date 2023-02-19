#tulis file

try:
    file = open("test1.txt", "wt")
except BaseException as be:
    print("Ada error saat menulis file", be)
else:
    #tulis file
    file.write("Nama pohon; Nama latin\n") 
    file.write("Aren; Arenga pinnata\n")
    file.write("Bintaro; Cerbera manghas\n")
    file.write("Durian; Duri zibethinus\n")
    #cetak pesan berhasil
    print("File", file , "berhasil ditulis!")
finally:
    file.close()