# List adalah struktur data mirip array 
mylist = ["apple", "banana", "cherry"] # Pakai kurung siku
print(mylist)

# Ciri-cirinya: Terurut (Ordered), artinya urutan tidak bisa diubah
# item yang ditambahkan, diletakkan di akhir daftar
mylist = ["apple", "banana", "cherry"]
mylist.append("orange")
print(mylist)

# Ciri-cirinya: Bisa diubah (Changeable), artinya bisa nambah, bisa hapus
mylist = ["apple", "banana", "cherry"]
mylist.insert(1, "grape")
print(mylist)

mylist = ["apple", "banana", "cherry"]
mylist.remove("apple")
print(mylist)

# Ciri-cirinya: Boleh duplikat (Allow Duplicates)
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# len() menentukan banyak item yang dimiliki list
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(len(thislist))

mylist = ["apple", "banana", "cherry"]
print(len(mylist))

# List dapat berisi berbagai tipe data
list1 = ["abc", 34, True, 40, "male"]
print(list1)

# Diakses dengan indexing 
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist[1]) #
print(thislist[-1]) # nampilkan item paling belakang

# List[start : stop : step]
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist[2:]) # Start di index 2 sampai selesai
print(thislist[2:5]) # Start di index 2, stop di index 4
print(thislist[:4]) # Start di index 0, stop di index 3
print(thislist[-4:-1]) # Start di index 4 dari belakang, stop di index 2 dari belakang

# Mengubah nilai item dalam list
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant" # banana diganti blackcurrant
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"] # banana cherry diganti blackcurrant watermelon
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"] # banana diganti blackcurrant watermelon
print(thislist)

# Extend() menambahkan elemen dari list lain ke list saat ini
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical) # memasukan elemen di tropical ke thislist
print(thislist)

# Hapus Item yang Ditentukan remove()
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
# Jika terdapat lebih dari satu item dengan nilai yang mau dihapus 
# metode ini akan menghapus item yang pertama muncul
thislist = ["apple", "banana", "cherry", "banana"]
thislist.remove("banana")
print(thislist)

# Hapus Indeks yang Ditentukan pop()
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
# Jika index tidak ditentukan, item terakhir yang dihapus
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# del() juga menghapus indeks yang ditentukan
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
# juga dapat menghapus list sepenuhnya
thislist = ["apple", "banana", "cherry"]
del thislist

# clear() membersihkan list
thislist = ["apple", "banana", "cherry"]
thislist.clear() # listnya masih ada, tapi tidak berisi 
print(thislist)

# Perulangan (loop)
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

# List Comprehension (sintaks yang lebih singkat)
# manampilkan buah yang ada huruf a nya
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

# Mengurutkan list
# .sort() mengurutkan isi list secara alfabet
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort() # b, k, m, o, p
print(thislist)

# .sort() mengurutkan isi list secara numerik
thislist = [100, 50, 65, 82, 23]
thislist.sort() # 23, 50, 65, 82, 100
print(thislist)

# reverse = True (membuat sort terbalik)
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True) # p, o, m, k, b
print(thislist)

# key = function (Urutkan isi list berdasarkan nilai yang dikembalikan oleh fungsi)
def myfunc(n):
    return abs(n - 50)

thislist = [100, 50, 65, 82, 23] # dilihat selisih yang paling kecil
thislist.sort(key = myfunc) # 50, 65, 23, 82, 100
print(thislist)
