def tambah_buku(nama, harga, stok):
    if harga <= 0:
        print("Error")
        return None
    
    if stok < 0:
        print("Error")
        return None

    return {
        "nama": nama,
        "harga": harga,
        "stok": stok
    }

daftar_buku = []

print("Masukkan data 3 buku:")
for i in range(3):
    print(f"\nBuku ke-{i+1}:")
    nama = input("Nama Buku: ")
    harga = float(input("Harga Buku: "))
    stok = int(input("Stok Buku: "))
    
    buku = tambah_buku(nama, harga, stok)
    
    for buku in nama, harga, stok:
        i+=1
        print(buku)
        




