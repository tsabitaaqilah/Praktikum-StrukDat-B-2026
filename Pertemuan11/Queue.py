class Node:
    def __init__(self, nama, keluhan):
        self.nama = nama
        self.keluhan = keluhan
        self.next = None

class queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0

    def is_empty(self):
        return self.front is None
    
    def enqueue(self, nama, keluhan):
        new_node = Node(nama, keluhan)
        if self.front is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        self.count += 1
        print(f"[DAFTAR] {nama.upper()} terdaftar dengan keluhan: {keluhan} (No. Antrian: {self.count})")

    def dequeue(self):
        if self.is_empty():
            print("Kosong!")
            return None
        
        removed = self.front
        self.front = self.front.next

        if self.front is None:  
            self.rear = None

        self.count -= 1
        print(f"[PANGGIL] Dokter memanggil: {removed.nama.upper()} (keluhan: {removed.keluhan})")
        return removed
    
    def peek(self):
        if self.is_empty():
            print("[PEEK] Antrian kosong!")
        else:
            print(f"[PEEK] Pasien berikutnya: {self.front.nama.upper()} — {self.front.keluhan}")

    def size(self):
        return self.count
    
    def clear(self):
        self.front = None
        self.rear = None
        self.count = 0
        print("[CLEAR] Sesi poliklinik selesai. Antrian dikosongkan!")

    def tampilkan(self):
        if self.is_empty():
            print("[ANTRIAN SAAT INI] Kosong")
            return
        
        print("[ANTRIAN SAAT INI]")
        current = self.front
        nomor = 1
        while current:
            print(f"  {nomor}. {current.nama.upper():<10} → {current.keluhan}")
            current = current.next
            nomor += 1

def main():
    p = queue()  

    print("====================================")
    print("  SISTEM ANTRIAN POLI UMUM")
    print("  RS Sehat Bersama")
    print("====================================")

    print("[CEK] Apakah antrian kosong? →", "YA, antrian masih kosong." if p.is_empty() else "TIDAK")

    p.enqueue("aini", "mabuk cinta")
    p.enqueue("jejes", "putus cinta")
    p.enqueue("gledis", "gilak")

    print(f"[INFO] Jumlah pasien menunggu: {p.size()} orang")

    p.peek()
    p.dequeue()
    p.enqueue("bita", "sedih")
    p.tampilkan() 

    p.dequeue()
    print(f"[INFO] Jumlah pasien masih menunggu: {p.size()} orang")

    p.clear()
    print("[CEK] Apakah antrian kosong? →", "YA, antrian sudah kosong." if p.is_empty() else "TIDAK")

    print("====================================")
    print("  Simulasi Selesai!")
    print("====================================")

if __name__ == "__main__":
    main()