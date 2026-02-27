# menyimpan nilai data dalam pasangan key:value
# terurut, dapat diubah, dan tidak mengizinkan duplikat
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

# Dirujuk menggunakan key
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict["brand"])

# Ketika terdapat nilai duplikat, maka yang terakhir yg ditampilkan
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
print(thisdict)

# Mengubah nilai item tertentu dengan merujuk pada key
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["year"] = 2018

# Loop
for x in thisdict:
    print(x)

# Kamus yang berisi kamus
myfamily = {
    "child1" : {
        "name" : "Emil",
        "year" : 2004
    },
    "child2" : {
        "name" : "Tobias",
        "year" : 2007
    },
    "child3" : {
        "name" : "Linus",
        "year" : 2011
    }
}

