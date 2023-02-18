#contoh mencetak string berpola dengan pola cetak

a = "Ahmad"
b = "Malang"
u = 45
j = 12.5

#cetak string berpola
print("Nama saya", a, "." , "Asal saya dari", b, ".")

#cetak string berpola
print("Nama saya", a + "." , "Asal saya dari", b + ".")

#cetak string berpola
print("Nama saya %s. Asal saya dari %s." % (a, b))

#cetak string berpola
print("Nama saya %s. Umur saya %d tahun. Asal saya dari %s. Rumah saya %f km dari sini." % (a, u, b, j))

#cetak string berpola
print("Nama saya {0}. Asal saya dari {1}.".format(a, b)) 

#cetak string berpola
print("Nama saya {}. Umur saya {} tahun. Asal saya dari {}. Rumah saya {:.3f} km dari sini.".format(a, u, b, j))
