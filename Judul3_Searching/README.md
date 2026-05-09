# Sistem Pengelolaan Barang pada Toko

Sistem ini adalah sistem yang berjalan menggunakan bahasa pemrograman python dan algoritma pencarian sequential (sequential search) yang berfungsi untuk menambah barang dari penyimpanan, menghapus barang dari penyimpanan, dan mengecek stok barang dengan kode barang.
Didalam sistem ini terdapat berbagai fungsi, yang pertama adalah fungsi menu yang menampilkan menu untuk menambah, menghapus, mengecek, dan keluar dari sistem. Yang kedua ada fungsi sequential search yang mencari kode barang dalam array menggunakan indeks. Fungsi ini mengecek dari kode barang pertama hingga kode barang terakhir yang ada pada array.

Dan yang ketiga ada fungsi utama yang terdapat data stok barang, dan menu serta fungsi yang akan dijalankan sesuai dengan apa yang diingginkan (diinput oleh user). Jika user menginput 1, maka fungsi tambah barang akan dilakukan dengan menambah kode barang ke belakang array. Jika user menginput 2, maka fungsi hapus barang akan dijalankan dengan menghapus stok barang yang pertama kali masuk ke dalam array. Jika user menginput 3, maka sistem akan menanyakan kode barang berapa yang ingin dicari setelah itu akan mencari kode barang di array menggunakan fungsi sequential search.

# Source Code:
<img width="505" height="521" alt="image" src="https://github.com/user-attachments/assets/2525f6fc-7cbf-4857-8483-5bbb7c694156" />
<img width="1142" height="772" alt="image" src="https://github.com/user-attachments/assets/5c619dc2-a9a2-4c1f-9239-c88048a40ed5" />
<img width="988" height="630" alt="image" src="https://github.com/user-attachments/assets/196f780e-0f52-4a51-acf9-6bc6c3150044" />

# Penjelasan:

Baris 1: Komentar yang menjelaskan bahwa program ini adalah sistem pengelolaan barang.

Baris 2: Baris kosong (spasi antar kode).

Baris 3: Mendefinisikan fungsi menu() untuk menampilkan daftar pilihan ke layar.

Baris 4: Menampilkan teks menu "1. Tambahkan barang".

Baris 5: Menampilkan teks menu "2. Hapus Barang".

Baris 6: Menampilkan teks menu "3. Cek barang".

Baris 7: Menampilkan teks menu "4. Keluar".

Baris 8: Baris kosong.

Baris 9: Baris kosong.

Baris 10: Mendefinisikan fungsi sequential_search untuk mencari barang dan menghitung jumlahnya.

Baris 11: Membuat variabel i (indeks) dengan nilai awal 0.

Baris 12: Membuat variabel counter (penghitung jumlah barang yang ditemukan) dengan nilai awal 0.

Baris 13: Memulai perulangan selama nilai i lebih kecil dari total data (n).

Baris 14: Mengecek apakah data pada urutan ke-i sama dengan barang yang dicari (target).

Baris 15: Jika sama, nilai counter ditambah 1.

Baris 16: Menambahkan nilai i dengan 1 untuk lanjut mengecek data berikutnya.

Baris 17: Mengembalikan nilai akhir counter (total barang yang ditemukan).

Baris 18: Baris kosong.

Baris 19: Baris kosong.

Baris 20: Mendefinisikan fungsi utama program yang bernama main().

Baris 21: Membuat daftar berisi angka-angka yang merepresentasikan kode stok barang.

Baris 22: Menghitung total jumlah barang di daftar dan menyimpannya di variabel n.

Baris 23: Menampilkan seluruh daftar kode stok barang ke layar.

Baris 24: Membuat variabel running menjadi True untuk mengatur agar program terus berjalan.

Baris 25: Memulai perulangan utama selama running bernilai True.

Baris 26: Memanggil fungsi menu() untuk menampilkan pilihan kepada pengguna.

Baris 27: Memulai blok try untuk berjaga-jaga jika ada error (kesalahan ketik) saat pengguna memasukkan input.

Baris 28: Meminta pengguna memasukkan angka pilihan menu, lalu menyimpannya di variabel choice.

Baris 29: Menangkap error ValueError jika pengguna mengetik huruf, bukan angka.

Baris 30: Menampilkan peringatan bahwa yang dimasukkan harus angka.

Baris 31: Mengulang kembali program ke awal perulangan (Baris 25).

Baris 32: Mengecek jika pengguna memilih menu angka 1 (Tambah barang).

Baris 33: Menampilkan daftar kode stok barang saat ini.

Baris 34: Memulai blok try untuk input penambahan barang.

Baris 35: Meminta pengguna memasukkan kode barang baru untuk disimpan.

Baris 36: Menangkap error jika input yang dimasukkan bukan angka.

Baris 37: Menampilkan peringatan untuk memasukkan angka.

Baris 38: Menambahkan kode barang baru tersebut ke dalam daftar data.

Baris 39: Menampilkan pesan berhasil dan daftar stok barang yang baru diperbarui.

Baris 40: Mengecek jika pengguna memilih menu angka 2 (Hapus barang).

Baris 41: Menampilkan daftar kode stok barang saat ini.

Baris 42: Memulai blok try untuk input penghapusan barang.

Baris 43: Meminta pengguna memasukkan kode barang yang ingin dihapus.

Baris 44: Menangkap error jika input yang dimasukkan bukan angka.

Baris 45: Menampilkan peringatan untuk memasukkan angka.

Baris 46: Menghapus kode barang yang dimasukkan pengguna dari daftar data.

Baris 47: Menampilkan pesan sukses menghapus dan daftar stok barang yang tersisa.

Baris 48: Mengecek jika pengguna memilih menu angka 3 (Cek jumlah barang).

Baris 49: Memperbarui hitungan total jumlah data saat ini ke dalam variabel n.

Baris 50: Menampilkan daftar kode stok barang saat ini.

Baris 51: Memulai perulangan tanpa henti untuk memastikan pengguna memasukkan kode pencarian yang benar.

Baris 52: Memulai blok try untuk input pencarian barang.

Baris 53: Meminta pengguna memasukkan kode barang yang sedang dicari.

Baris 54: Menghentikan perulangan (keluar dari Baris 51) jika input angka sudah benar.

Baris 55: Menangkap error jika input yang dimasukkan bukan angka.

Baris 56: Menampilkan peringatan bahwa kode tidak valid.

Baris 57: Memanggil fungsi pencarian untuk menghitung berapa kali kode tersebut muncul di dalam daftar.

Baris 58: Mengecek apakah jumlah barang (counter) lebih dari 0 (artinya barang ditemukan).

Baris 59: Menampilkan info bahwa barang ditemukan berserta total jumlahnya.

Baris 60: Pilihan alternatif jika barang tidak ditemukan (counter bernilai 0).

Baris 61: Menampilkan pesan bahwa barang tidak ada di dalam stok.

Baris 62: Mengecek jika pengguna memilih menu angka 4 (Keluar dari program).

Baris 63: Mengubah running menjadi False sehingga perulangan utama berhenti.

Baris 64: Menampilkan pesan bahwa program telah selesai.

Baris 65: Menangkap kondisi jika pengguna memilih angka selain 1, 2, 3, atau 4.

Baris 66: Menampilkan pesan bahwa pilihan tersebut tidak valid.

Baris 67: Baris kosong.

Baris 68: Baris kosong.

Baris 69: Mengecek apakah file Python ini dijalankan secara langsung (bukan diimpor oleh file lain).

Baris 70: Menjalankan fungsi main() untuk memulai seluruh proses program di atas.

# Output:
<img width="976" height="722" alt="image" src="https://github.com/user-attachments/assets/30fd7ef9-60c2-44fa-b7cf-deeb5ac9ed0c" />
