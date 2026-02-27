# Tuple adalah kumpulan yang terurut dan tidak dapat diubah
# Tidak dapat menambah, atau menghapus item setelah tuple dibuat
thistuple = ("apple", "banana", "cherry") # Pakai kurung biasa
print(thistuple)

# Tuple dapat memiliki item dengan nilai yang sama
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# Tuple dapat berisi berbagai tipe data
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)

# Akses tuple dengan indexing
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# Untuk rentang, index negatif, semua sama dengan list

# Mengubah tuple menjadi list, dan mengubah list tersebut kembali menjadi tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

