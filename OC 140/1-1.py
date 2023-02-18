#contoh operasi pada string

A = "Halo"
B = "Semuanya"

#operasi concatenation
C1 = A + B

#operasi multiple concatenation
C21 = A * 3 #angka tidak boleh negatif
C22 = B * 2

#operasi membership
C31 = "H" in A
C32 = "H" in B

#operasi non-membership
C41 = "H" not in A
C42 = "H" not in B

print("A adalah : " + A)
print("B adalah : " + B)
print("Hasil concat A dan B adalah : " + C1)
print("Hasil multiple concat A 3x adalah : " + C21)
print("Hasil multiple concat B 2x adalah : " + C22)
print("Huruf H adalah anggota A : " + str(C31))
print("Huruf H adalah anggota B : " + str(C32))
print("Huruf H bukanlah anggota A : " + str(C41))
print("Huruf H bukanlah anggota B : " + str(C42))