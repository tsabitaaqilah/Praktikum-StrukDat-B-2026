# Sets tidak terurut , tidak dapat diubah , tidak terindeks, dan tidak mengizinkan nilai duplikat
# Item yang sudah ditetapkan tidak dapat diubah, tapi bisa dihapus dan ditambahkan item baru
thisset = {"apple", "banana", "cherry"} # kurung kurawal
print(thisset)

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

# Nilai True dan 1 dianggap sebagai nilai yang sama
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

# Nilai False dan 0 dianggap sebagai nilai yang sama
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)

# dapat berisi berbagai tipe data

# Akses item dengan cara for loop/in
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

# add() untuk menambah satu item ke set
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# update() Untuk menambahkan item dari set lain ke set saat ini
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# remove() Jika item yang akan dihapus tidak ada, error
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

# discard() Jika item yang akan dihapus tidak ada, tidak error
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

# pop() menghapus item secara acak
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)