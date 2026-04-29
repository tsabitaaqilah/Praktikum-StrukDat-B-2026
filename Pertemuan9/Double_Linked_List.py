class Node:
    def __init__(self, judul, pengarang):
        self.judul = judul
        self.pengarang = pengarang
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def insert_tail(self, judul, pengarang):
        new_node = Node(judul, pengarang)

        if self.head == None:
            self.head = new_node
        else:
            node_sekarang = self.head
            while node_sekarang.next != None:
                node_sekarang = node_sekarang.next

            node_sekarang.next = new_node
            new_node.prev = node_sekarang

    def print_forward(self):
        node_sekarang = self.head
        while node_sekarang != None:
            print(node_sekarang.judul, "-", node_sekarang.pengarang)
            node_sekarang = node_sekarang.next

    def print_backward(self):
        node_sekarang = self.head

        while node_sekarang.next != None:
            node_sekarang = node_sekarang.next

        while node_sekarang != None:
            print(node_sekarang.judul, "-", node_sekarang.pengarang)
            node_sekarang = node_sekarang.prev

    def delete_by_judul(self, judul):
        node_sekarang = self.head

        while node_sekarang != None:
            if node_sekarang.judul == judul:

                if node_sekarang.prev == None:
                    self.head = node_sekarang.next
                    if self.head != None:
                        self.head.prev = None
                else:
                    node_sekarang.prev.next = node_sekarang.next
                    if node_sekarang.next != None:
                        node_sekarang.next.prev = node_sekarang.prev

                break

            node_sekarang = node_sekarang.next

daftar_buku = DoubleLinkedList()

daftar_buku.insert_tail("Laskar Pelangi", "Andrea Hirata")
daftar_buku.insert_tail("Bumi Manusia", "Pramoedya Ananta Toer")
daftar_buku.insert_tail("Sang Pemimpi", "Andrea Hirata")

print("Data dari depan:")
daftar_buku.print_forward()

print("\nData dari belakang:")
daftar_buku.print_backward()

daftar_buku.delete_by_judul("Bumi Manusia")

print("\nSetelah dihapus:")
daftar_buku.print_forward()