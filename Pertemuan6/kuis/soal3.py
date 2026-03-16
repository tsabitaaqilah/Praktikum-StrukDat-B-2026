katalog = [
    {'nama': 'Belajar Python', 'harga': 75000, 'stok': 5},
    {'nama': 'Struktur Data', 'harga': 95000, 'stok': 3},
    {'nama': 'Algoritma Dasar', 'harga': 60000, 'st0k': 8},
]

riwayat_transaksi = set()

def proses_transaksi(katalog, nama_buku, jumlah_beli):
    print(f"\nMemproses pembelian: {nama_buku} (Jumlah: {jumlah_beli})")
    
    buku_ditemukan = False
    
    for buku in katalog:
        if buku['nama'].lower() == nama_buku.lower():
            buku_ditemukan = True

            if buku['stok'] >= jumlah_beli:
                total_harga = buku['harga'] * jumlah_beli
                buku['stok'] -= jumlah_beli
                print(f"Berhasil membeli: {buku['nama']}")
                print(f"Total harga: Rp{total_harga:,}")

                riwayat_transaksi.add(buku['nama'])
            else:
    
                print(f"Peringatan: Stok '{buku['nama']}' tidak cukup (Tersisa: {buku['stok']}).")
    

    if not buku_ditemukan:
        print(f"Error: Buku '{nama_buku}' tidak ditemukan di katalog.")

proses_transaksi(katalog, "Belajar Python", 2)
proses_transaksi(katalog, "struktur data", 4)
proses_transaksi(katalog, "Algoritma Dasar", 1)
proses_transaksi(katalog, "Python Lanjutan", 1) 

print("\n" + "="*30)
print("Riwayat Transaksi (Unique):")
for item in riwayat_transaksi:
    print(f"- {item}")
