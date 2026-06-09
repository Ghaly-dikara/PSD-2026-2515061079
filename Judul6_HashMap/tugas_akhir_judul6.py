class Node:
    def __init__(self, key, value, value2):
        self.key = key
        self.value = value
        self.value2 = value2
        self.next = None


class HashMapSeparateChaining:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [None] * self.SIZE

    def hash_function(self, key):
        return (key % self.SIZE + self.SIZE) % self.SIZE

    def insert(self, key, value, value2):
        index = self.hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                current.value = value
                current.value2 = value2
                return
            current = current.next
        new_node = Node(key, value, value2)
        new_node.next = self.table[index]
        self.table[index] = new_node

    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                return current
            current = current.next
        return None

    def remove_key(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        prev = None
        while current is not None:
            if current.key == key:
                if prev is None:
                    self.table[index] = current.next
                else:
                    prev.next = current.next
                return True
            prev = current
            current = current.next
        return False

    def display(self):
        print("\nIsi Data Mahasiswa (Hash Table Separate Chaining):")
        for i in range(self.SIZE):
            print(f"{i}: ", end="")
            current = self.table[i]
            while current is not None:
                print(f"({current.key}, {current.value}, ipk: {current.value2}) -> ", end="")
                current = current.next
            print("NULL")


def main():
    hashmap = HashMapSeparateChaining()
    pilih = 0
    while pilih != 5:
        print("\n1. Tambah data mahasiswa")
        print("2. Cari data mahasiswa")
        print("3. Hapus data mahasiswa")
        print("4. Tampilkan data mahasiswa")
        print("5. Keluar")
        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid!")
            continue
        if pilih == 1:
            try:
                nama = str(input("Masukkan nama siswa: "))
                npm = int(input("Masukkan NPM siswa: "))
                ipk = float(input("Masukkan ipk semester ini: "))
                hashmap.insert(npm, nama, ipk)
                print("\nData mahasiswa berhasil ditambah")
            except ValueError:
                print("Input tidak valid!")
        elif pilih == 2:
            try:
                npm = int(input("Masukkan NPM mahasiswa yang ingin dicari: "))
                hasil = hashmap.search(npm)
                if hasil is not None:
                    print(f"\nMahasiswa bernama {hasil.value} dengan NPM {hasil.key} dan ipk: {hasil.value2} berhasil ditemukan")
                else:
                    print(f"\nData mahasiswa dengan NPM {npm} tidak ditemukan")
            except ValueError:
                print("NPM tidak valid!")
        elif pilih == 3:
            try:
                npm = int(input("Masukkan NPM dari mahasiswa yang datanya ingin dihapus: "))
                hasil = hashmap.search(npm)
                if hasil is not None :
                    hashmap.remove_key(npm)
                    print(f"\nMahasiswa dengan NPM {hasil.key} bernama {hasil.value} berhasil dihapus")
                else:
                    print(f"\nData mahasiswa dengan NPM {npm} tidak ada")
            except ValueError:
                print("NPM tidak valid!")
        elif pilih == 4:
            hashmap.display()
        elif pilih == 5:
            print("Program selesai.")
        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()