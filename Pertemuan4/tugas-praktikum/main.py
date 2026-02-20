from tabulate import tabulate
from kurs import data_kurs
from konverter import konversi_ke_idr, konversi_dari_idr

def tampilkan_tabel():
    print("=== KONVERTER MATA UANG ===")
    tabel = [[k, f"{v:,}"] for k, v in data_kurs.items()]
    print(tabulate(tabel, headers=["Kode", "Kurs"], tablefmt="grid"))

def main():
    tampilkan_tabel()
    
    asal = input("Dari (IDR/USD/EUR/SGD/JPY): ").upper()
    tujuan = input("Ke (IDR/USD/EUR/SGD/JPY): ").upper()
    jumlah = float(input("Jumlah: "))

    nilai_idr = konversi_ke_idr(jumlah, asal)
    hasil = konversi_dari_idr(nilai_idr, tujuan)

    print(f"{asal} {jumlah:,.2f} = {tujuan} {hasil:,.2f}")

if __name__ == "__main__":
    main()