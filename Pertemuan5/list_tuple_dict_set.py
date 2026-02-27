#1
nilai_tugas = [70, 85, 90, 65, 80]
nilai_tugas[4] = 75
print(nilai_tugas)

nilai_tugas.append (95)
nilai_tugas.sort(reverse=True)
print(nilai_tugas)


nilai_tugas = sum(nilai_tugas)
print(nilai_tugas)

if nilai_tugas == 100:
    print("Ada nilai sempurna")
else:
    print("Tidak ada")

#2
kumpulan_nilai = [("Andi", 85), ("Budi", 60), ("Cici", 90), ("Deni", 72)]

for i in kumpulan_nilai:
    if i [1] >=75:
        print(f"Selamat {i[0]}, Anda Lulus")
    else:
        print(f"maaf {i[0]}, Anda harus remidi")

#3
sesi_pagi = {"Andi", "Budi", "Cici"} 
sesi_siang = {"Budi", "Deni", "Eka"}

kehadiran = sesi_pagi & sesi_siang
print(kehadiran)

kehadiran = sesi_pagi | sesi_siang
print(kehadiran)

set_hari_ini = sesi_pagi.union(sesi_siang)
print(set_hari_ini)

#4
transaksi = [
 {"produk": "Buku", "harga": 10000, "jumlah": 3},
 {"produk": "Pena", "harga": 5000, "jumlah": 10},
 {"produk": "Penghapus", "harga": 2000, "jumlah": 2}
]

transaksi[0]["jumlah"] = 8
print(transaksi)

produk_baru1 = {"produk" : "kuas", "harga" : 80000, "jumlah" : 7}
produk_baru2 = {"produk" : "penggaris", "harga" : 90000, "jumlah" : 1}
transaksi.append(produk_baru1) 
transaksi.append(produk_baru2)

for item in transaksi:
        total = item["harga"]*item["jumlah"]
        print(f"produk: {item['produk']} | total: {'total'}")