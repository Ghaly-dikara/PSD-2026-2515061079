# Sistem pengelolaan barang pada Toko

def menu():
    print("1. Tambahkan barang")
    print("2. Hapus Barang")
    print("3. Cek barang")
    print("4. Keluar")


def sequential_search(data, n, target):
    i = 0
    counter = 0
    while i < n:
        if data[i] == target:
            counter += 1
        i += 1
    return counter


def main():
    data = [101, 102, 101, 103, 101, 102, 104, 105, 101, 102, 103, 101, 102, 105, 106]
    n = len(data)
    print(f"Daftar kode stok barang: {data}")
    running = True
    while running:
        menu()
        try:
            choice = int(input("Pilihan: "))
        except ValueError:
            print("Masukkan angka yang valid!")
            continue
        if choice == 1:
            print(f"Daftar kode stok barang: {data}")
            try:
                tambah = int(input("Masukkan kode barang yang ingin disimpan: "))
            except ValueError:
                print("Tolong masukkan angka kode barang!")
            data.append(tambah)
            print(f"Barang berhasil ditambahkan\nDaftar kode stok sekarang: {data}")
        elif choice == 2:
            print(f"Daftar kode stok barang: {data}")
            try:
                hapus = int(input("Masukkan kode barang yang ingin dihapus: "))
            except ValueError:
                print("Tolong masukkan angka kode barang!")
            data.remove(hapus)
            print(f"Barang berhasil dihapus dari penyimpanan\nDaftar kode stok sekarang: {data}")
        elif choice == 3:
            n = len(data)
            print(f"Daftar kode stok: {data}")
            while True:
                try:
                    target = int(input("Masukkan kode barang yang dicari: "))
                    break
                except ValueError:
                    print("Kode tidak valid, masukkan angka!")
            counter = sequential_search(data, n, target)
            if counter > 0:
                print(f"Kode barang {target} ada sebanyak {counter} item di stok.")
            else:
                print(f"Kode barang {target} tidak ada di stok.")
        elif choice == 4:
            running = False
            print("Program selesai.")
        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()