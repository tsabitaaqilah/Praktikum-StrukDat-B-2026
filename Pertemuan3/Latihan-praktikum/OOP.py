class Permen:
    def __init__(self, rasa, harga, merk):
        self.rasa = rasa
        self.harga = harga
        self.merk = merk

    def ubah_harga(self, harga):
        self.harga = harga

    def ubah_merk(self, merk):
        self.merk = merk

p1 = Permen("manis", 1000, "Milkita")
p2 = Permen("mint", 1000, "Relaxa")
p3 = Permen("asam", 500, "Tamarin")
p3.ubah_harga(1000)
p2.ubah_merk("minz")

print(p1.rasa, p1.harga, p1.merk)
print(p2.rasa, p2.harga, p2.merk)
print(p3.rasa, p3.harga, p3.merk)
