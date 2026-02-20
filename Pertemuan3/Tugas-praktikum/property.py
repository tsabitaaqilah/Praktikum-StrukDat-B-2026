# Properti adalah variabel yang dimiliki oleh suatu kelas
# Variabel menyimpan data untuk setiap objek yang dibuat dari kelas
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)

# Mengakses properti objek menggunakan notasi titik
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car1 = Car("Toyota", "Corolla")

print(car1.brand)
print(car1.model)

# Properti yang didefinisikan di dalamnya __init__() adalah milik setiap objek
# Properti yang didefinisikan di luar metode adalah milik kelas itu sendiri dan dimiliki bersama oleh semua objek
class Person:
    species = "Human" # Class property

    def __init__(self, name):
        self.name = name # Instance property

p1 = Person("Emil")
p2 = Person("Tobias")

print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)

# Tambahkan properti baru ke sebuah objek
class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Tobias")

p1.age = 25
p1.city = "Oslo"

print(p1.name)
print(p1.age)
print(p1.city)