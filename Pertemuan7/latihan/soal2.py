#Tugas 1
antrean_array = ["Pasien A (Stabil)", "Pasien B (Stabil)", "Pasien C (Stabil)"]

def sisipkan_pasien_darurat_array(nama_pasien, posisi):
    antrean_array.insert(posisi - 1, nama_pasien)

sisipkan_pasien_darurat_array("Pasien D (Darurat)", 2)

print("Antrean Pasien:")
for pasien in antrean_array:
    print(pasien)

print("=========================")
#Tugas 2
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class HistoryLinkedList:
  def __init__(self):
    self.head = None

  def tambah_pencarian_linked(self, keyword):
    newNode = Node(keyword)
    newNode.next = self.head
    self.head = newNode

  def tampilkan_history(self):
    current = self.head
    while current:
      print(current.data, end=" -> ")
      current = current.next
    print("None")

  def insert_at_position(self, nama_pasien, posisi):
    newNode = Node(nama_pasien)

    if posisi == 1 or self.head is None:
      newNode.next = self.head
      self.head = newNode
      return

    current = self.head
    count = 1

    while current.next and count < posisi - 1:
      current = current.next
      count += 1

    newNode.next = current.next
    current.next = newNode

history = HistoryLinkedList()

history.tambah_pencarian_linked("Pasien A")
history.tambah_pencarian_linked("Pasien B")
history.tambah_pencarian_linked("Pasien C")

print("Antrean sebelum:")
history.tampilkan_history()
print("=========================")

history.insert_at_position("Pasien Darurat", 2)

print("Antrean sesudah:")
history.tampilkan_history()