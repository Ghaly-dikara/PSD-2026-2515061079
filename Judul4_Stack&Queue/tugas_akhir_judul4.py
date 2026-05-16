class StackArray:
    def __init__(self, max_size=100):
        self.MAX = max_size
        self.st = [None] * self.MAX
        self.top_idx = -1

    def is_empty(self):
        return self.top_idx == -1

    def is_full(self):
        return self.top_idx == self.MAX - 1

    def push(self, x):
        if self.is_full():
            self.MAX *= 2
            self.st.extend([None] * self.MAX)
            return
        self.top_idx += 1
        self.st[self.top_idx] = x
        print(f"Berhasil mengunjungi situs {x} ")

    def pop(self):
        if self.is_empty():
            print("Tidak ada riwayat browser, anda berada di halaman kosong")
            return
        print(f"Tombol back ditekan, meinggalkan halaman {self.st[self.top_idx]}")
        self.top_idx -= 1

    def peek(self):
        if self.is_empty():
            print("Riwayat browser kosong, belum ada halaman yang dikunjungi")
            return
        print(f"Sedang berada ada di halaman: {self.st[self.top_idx]}")

    def display(self):
        if self.is_empty():
            print("Riwayat browser kosong")
            return
        print("Riwayat browser (dari yang terbaru ke yang lama): ", end="")
        for i in range(self.top_idx, -1, -1):
            print(self.st[i], end=" ")
        print()


def main():
    stack = StackArray()
    pilih = 0
    while pilih != 5:
        print("\n=== Riwayat browser ===")
        print("1. Kunjungi web baru (push)")
        print("2. Kembali (pop)")
        print("3. Lihat halaman sekarang")
        print("4. Tampilkan history browser")
        print("5. Keluar browser")
        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid!, harap pilih menu dengan angka yang tertera.")
            continue
        if pilih == 1:
            val = (input("Masukkan nama website yang ingin dikunjungi: "))
            stack.push(val)
        elif pilih == 2:
            stack.pop()
        elif pilih == 3:
            stack.peek()
        elif pilih == 4:
            stack.display()
        elif pilih == 5:
            print("Browser ditutup, program selesai.")
        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()