kelas_A = {"Struktur Data", "Basis Data", "AI",
"Pemrograman Web"}
kelas_B = {"Struktur Data", "Machine Learning", "AI",
"Cloud Computing"}

#irisan = kelas_A.intersaction(kelas_B)
print(kelas_A & kelas_B)

#difference = kelas_A.difference(kelas_B)
#print (difference)

kelas_A.update(kelas_B)
print(kelas_A)

