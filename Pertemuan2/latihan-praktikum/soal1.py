angka = [10, 20, 30, 40, 50]
angka.append(60)
print(angka)

angka.remove(20)
print(angka)

maksimal = max(angka)
print(maksimal)

minimal = min(angka)
print(minimal)

total = 0
for nilai in angka: #sum(angka)/len(angka)
    total += nilai
rata_rata = total/len(angka)
print(rata_rata)

print(angka)

