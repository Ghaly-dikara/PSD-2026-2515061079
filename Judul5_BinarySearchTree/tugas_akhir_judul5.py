class Node:
    def __init__(self, key, key2):
        self.key = key
        self.key2 = key2 
        self.left = None
        self.right = None


class BSTLanjut:
    def __init__(self):
        self.root = None

    def insert_node(self, root, key, key2):
        if root is None:
            return Node(key, key2)
        if key < root.key:
            root.left = self.insert_node(root.left, key, key2)
        elif key > root.key:
            root.right = self.insert_node(root.right, key, key2)
        return root

    def insert(self, key, key2):
        self.root = self.insert_node(self.root, key, key2)

    def find_min_node(self, root):
        current = root
        while current is not None and current.left is not None:
            current = current.left
        return current

    def delete_node(self, root, key):
        if root is None:
            return None
        if key < root.key:
            root.left = self.delete_node(root.left, key)
        elif key > root.key:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                successor = self.find_min_node(root.right)
                root.key = successor.key
                root.key2 = successor.key2
                root.right = self.delete_node(root.right, successor.key)
        return root

    def delete(self, key):
        self.root = self.delete_node(self.root, key)

    def height(self, root):
        if root is None:
            return -1
        height_left = self.height(root.left)
        height_right = self.height(root.right)
        return 1 + max(height_left, height_right)

    def level_order(self, root):
        if root is None:
            print("(Tidak ada pesanan)")
            return
        queue = []
        queue.append(root)
        while len(queue) > 0:
            current = queue.pop(0)
            print(f"Antrean {current.key}: {current.key2}")
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
        print()

    def find_successor(self, root, key):
        current = root
        successor = None
        while current is not None:
            if key < current.key:
                successor = current
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                break
        if current is None:
            return None, False
        if current.right is not None:
            successor = self.find_min_node(current.right)
        if successor is None:
            return None, False
        return successor.key, successor.key2, True

    def find_predecessor(self, root, key):
        current = root
        predecessor = None
        while current is not None:
            if key > current.key:
                predecessor = current
                current = current.right
            elif key < current.key:
                current = current.left
            else:
                break
        if current is None:
            return None, False
        if current.left is not None:
            temp = current.left
            while temp.right is not None:
                temp = temp.right
            predecessor = temp
        if predecessor is None:
            return None, False
        return predecessor.key, predecessor.key2, True


def main():
    bst = BSTLanjut()
    pilih = 0
    while pilih != 6:
        print("\n=== Sistem Pesanan Restoran Serba Ada ===")
        print("1. Tambah Pesanan Baru")
        print("2. Pesanan Selesai Dihidangkan")
        print("3. Lihat Semua Antrean")
        print("4. Cek Pesanan Selanjutnya")
        print("5. Cek Pesanan Sebelumnya")
        print("6. Keluar")
        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid!")
            continue
        if pilih == 1:
            try:
                x = int(input("Masukkan nomor antrean: "))
                y = input("Masukkan Nama Menu: ")
                bst.insert(x, y)
                print(f"Pesanan {y} dengan nomor antrean {x} berhasil dicatat")
            except ValueError:
                print("Nomor antrean harus berupa angka (angka bulat)!")
        elif pilih == 2:
            try:
                x = int(input("Nomor Antrean yang sudah selesai: "))
                bst.delete(x)
                print(f"Pesanan antrean nomor {x} telah diserahkan dan dihapus dari sistem.")
            except ValueError:
                print("Input tidak valid!")
        elif pilih == 3:
            print("Daftar Pesanan yang Sedang Diproses: ")
            bst.level_order(bst.root)
        elif pilih == 4:
            try:
                x = int(input("Cari pesanan yang harus dikerjakan setelah antrean nomor: "))
                ans, wer, found = bst.find_successor(bst.root, x)
                if found:
                    print(f"Yang harus dikerjakan setelahnya adalah antrean nomor {ans}: {wer}")
                else:
                    print("Tidak ada pesanan setelahnya (pesananan mungkin tidak ada atau ini adalah pesanan terakhir yang tercatat).")
            except ValueError:
                print("Input tidak valid!")
        elif pilih == 5:
            try:
                x = int(input("Cari pesanan yang harus dikerjakan sebelum antrean nomor: "))
                ans, wer, found = bst.find_predecessor(bst.root, x)
                if found:
                    print(f"Yang harus dikerjakan sebelumnya adalah antrean nomor {ans}: {wer}")
                else:
                    print("Tidak ada pesanan sebelumnya (pesanan mungkin tidak ada atau ini adalah pesanan yang paling awal).")
            except ValueError:
                print("Input tidak valid!")
        elif pilih == 6:
            print("Program selesai.")
        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()