class Node:
    def __init__(self, id_buku, judul):
        self.id = id_buku
        self.judul = judul
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, id_buku, judul):
        new_node = Node(id_buku, judul)

        if self.root is None:
            self.root = new_node
        else:
            self._insert_recursive(self.root, new_node)

        print(f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}")

    def _insert_recursive(self, current, new_node):
        if new_node.id < current.id:
            if current.left is None:
                current.left = new_node
            else:
                self._insert_recursive(current.left, new_node)
        else:
            if current.right is None:
                current.right = new_node
            else:
                self._insert_recursive(current.right, new_node)

    def search(self, id_buku):
        return self._search_recursive(self.root, id_buku)

    def _search_recursive(self, node, id_buku):
        if node is None:
            return None
        if node.id == id_buku:
            return node
        elif id_buku < node.id:
            return self._search_recursive(node.left, id_buku)
        else:
            return self._search_recursive(node.right, id_buku)

    def traversal_inorder(self, node, no=[1]):
        if node:
            self.traversal_inorder(node.left, no)
            print(f"{no[0]}. {node.id} - {node.judul}")
            no[0] += 1
            self.traversal_inorder(node.right, no)

    def get_min(self):
        current = self.root
        while current.left:
            current = current.left
        return current

    def get_max(self):
        current = self.root
        while current.right:
            current = current.right
        return current

    def height(self, node):
        if node is None:
            return -1
        left_h = self.height(node.left)
        right_h = self.height(node.right)
        return max(left_h, right_h) + 1

tree = BST()

print("SISTEM KATALOG PERPUSTAKAAN \"ILMU TERANG\"")
print("=========================================")

tree.insert(50, "Dasar Pemrograman")
tree.insert(30, "Struktur Data")
tree.insert(70, "Kecerdasan Buatan")
tree.insert(20, "Matematika Diskrit")
tree.insert(40, "Basis Data")
tree.insert(60, "Jaringan Komputer")
tree.insert(80, "Sistem Operasi")

print("\n[INFO] Koleksi Buku (In-Order Traversal):")
tree.traversal_inorder(tree.root)

print("\n[SEARCH] Mencari ID 60...", end=" ")
hasil = tree.search(60)
if hasil:
    print(f"Ditemukan! Judul: {hasil.judul}")
else:
    print("Data tidak ditemukan.")

print("[SEARCH] Mencari ID 100...", end=" ")
hasil = tree.search(100)
if hasil:
    print(f"Ditemukan! Judul: {hasil.judul}")
else:
    print("Data tidak ditemukan.")

print("\n[STATISTIK] ID Terkecil:", tree.get_min().id)
print("[STATISTIK] ID Terbesar:", tree.get_max().id)

print("[INFO] Tinggi (Height) Tree:", tree.height(tree.root))

print("=========================================")
print("Simulasi Selesai!")