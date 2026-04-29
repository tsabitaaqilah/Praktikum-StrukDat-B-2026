class Node:
    def __init__(self, nama):
        self.nama = nama
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_tail(self, nama):
        new_node = Node(nama)

        if self.head == None:
            self.head = new_node
            new_node.next = self.head
        else:
            node_sekarang = self.head

            while node_sekarang.next != self.head:
                node_sekarang = node_sekarang.next

            node_sekarang.next = new_node
            new_node.next = self.head

    def print_antrian(self):
        if self.head == None:
            return

        node_sekarang = self.head

        while True:
            print(node_sekarang.nama, end=" -> ")
            node_sekarang = node_sekarang.next

            if node_sekarang == self.head:
                break

        print("(kembali ke awal)")

    def delete_head(self):
        if self.head == None:
            return

        if self.head.next == self.head:
            self.head = None
        else:
            node_sekarang = self.head

            while node_sekarang.next != self.head:
                node_sekarang = node_sekarang.next

            node_sekarang.next = self.head.next
            self.head = self.head.next

antrian = CircularLinkedList()

antrian.insert_tail("Andi")
antrian.insert_tail("Budi")
antrian.insert_tail("Citra")
antrian.insert_tail("Dina")

print("Antrian awal:")
antrian.print_antrian()

antrian.insert_tail("Edo")

print("\nSetelah tambah Edo:")
antrian.print_antrian()

antrian.delete_head()

print("\nSetelah Andi dilayani:")
antrian.print_antrian()