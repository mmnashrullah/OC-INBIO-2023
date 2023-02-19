#baca file

try:
    file = open("test1.txt", "rt")
except BaseException as be:
    print("Ada error saat membaca file", be)
else:
    #tulis file
    bacaFile = file.read()
    print(bacaFile)
finally:
    file.close()