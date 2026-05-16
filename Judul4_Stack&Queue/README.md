# Sistem Simulasi History Browser
Sistem ini merupakan simulasi history browser yang memakai bahasa pemrograman python. Dalam sistem ini menggunakan struktur data Stack dalam mekanisme penyimpanan elemennya. Terdapat class StackArray, fungsi is_empty(self), fungsi is_full(self), fungsi push(self, x), fungsi pop(self), fungsi peek(self) dan fungsi display(self).

Class StackArray digunakan untuk membuat stack yang dimana setiap ada StackArray tidak diperlukan pemanggilan, fungsi is_empty() untuk cek apakah Stack kosong atau tidak, fungsi is_full() mengecek stack penuh atau tidak, fungsi push yang berguna untuk menambahkan history browsing ke dalam stack. Fungsi pop() berguna untuk menghapus elemen terakhir pada array, dalam kasus ini digunakan untuk keluar dari halaman website yang terakhir diakses, fungsi peek() untuk menampilkan situs yang sedang diakses (digunakan untuk mengakses elemen terakhir stack tanpa menghapusnya, dan fungsi display() yang berfungsi untuk menampilkan full history browser dari yang terbaru ke yang terlama. Terakhir adalah fungsi utama, yang berisikan menu-menu untuk mengunjungi web, kembali, lihat halaman sekarang yang sedang diakses, dan keluar dari browser.

## Source Code:
<img width="682" height="833" alt="image" src="https://github.com/user-attachments/assets/4a2ea753-e2bf-4e88-80af-a5b897dac043" />
<img width="695" height="608" alt="image" src="https://github.com/user-attachments/assets/f66272c7-d46c-464d-975d-45aaa902e2e2" />


## Penjelasan:
Baris 1: Mendefinisikan class StackArray yang berfungsi sebagai kerangka struktur data tumpukan (stack).

Baris 2: Fungsi inisialisasi awal (constructor) dengan kapasitas maksimal default 100 elemen.

Baris 3: Menyimpan nilai kapasitas ke dalam variabel self.MAX.

Baris 4: Membuat list atau array bernama self.st berisi elemen kosong (None) sebanyak nilai MAX.

Baris 5: Mengatur self.top_idx menjadi -1, sebagai tanda bahwa tumpukan saat ini masih kosong.

Baris 6: (Baris kosong)

Baris 7: Mendefinisikan fungsi is_empty untuk memeriksa apakah tumpukan kosong.

Baris 8: Mengembalikan nilai True jika top_idx bernilai -1 (kosong).

Baris 9: (Baris kosong)

Baris 10: Mendefinisikan fungsi is_full untuk memeriksa apakah kapasitas tumpukan sudah penuh.

Baris 11: Mengembalikan nilai True jika top_idx sudah mencapai batas akhir list (self.MAX - 1).

Baris 12: (Baris kosong)

Baris 13: Mendefinisikan fungsi push untuk menambahkan nama web/halaman baru ke riwayat.

Baris 14: Memeriksa apakah tumpukan/riwayat sudah penuh.

Baris 15: Jika penuh, kapasitas self.MAX dilipatgandakan (dikali 2).

Baris 16: Memperluas ukuran list self.st dengan elemen kosong tambahan sesuai kapasitas baru.

Baris 17: Menghentikan proses fungsi (Note: dalam logika kodemu, jika kapasitas diperbesar, nilai baru justru gagal tersimpan karena ada return di sini).

Baris 18: Menambah nilai top_idx sebanyak 1 untuk posisi tempat elemen baru.

Baris 19: Memasukkan nama web (x) ke dalam list pada posisi top_idx tersebut.

Baris 20: Menampilkan pesan di layar bahwa situs berhasil dikunjungi.

Baris 21: (Baris kosong)

Baris 22: Mendefinisikan fungsi pop untuk menghapus halaman terakhir (seolah menekan tombol back).

Baris 23: Memeriksa apakah riwayat kosong.

Baris 24: Jika kosong, tampilkan pesan peringatan bahwa tidak ada riwayat.

Baris 25: Menghentikan fungsi pop agar tidak terjadi error.

Baris 26: Menampilkan pesan informasi halaman mana yang sedang ditinggalkan.

Baris 27: Mengurangi nilai top_idx sebanyak 1, menggeser penanda tumpukan mundur ke halaman sebelumnya.

Baris 28: (Baris kosong)

Baris 29: Mendefinisikan fungsi peek untuk melihat halaman apa yang saat ini sedang dibuka.

Baris 30: Memeriksa apakah riwayat kosong.

Baris 31: Jika kosong, tampilkan pesan bahwa belum ada halaman dikunjungi.

Baris 32: Menghentikan fungsi peek.

Baris 33: Jika tidak kosong, tampilkan nama web yang ada di tumpukan paling atas (top_idx).

Baris 34: (Baris kosong)

Baris 35: Mendefinisikan fungsi display untuk mencetak seluruh daftar riwayat web.

Baris 36: Memeriksa apakah riwayat kosong.

Baris 37: Jika kosong, tampilkan teks "Riwayat browser kosong".

Baris 38: Menghentikan fungsi display.

Baris 39: Mencetak teks pengantar riwayat (tanpa pindah ke baris baru karena end="").

Baris 40: Melakukan perulangan (mundur) dari indeks paling atas hingga indeks 0.

Baris 41: Mencetak setiap halaman web yang pernah dikunjungi dengan jarak spasi.

Baris 42: Mencetak baris baru (enter) agar tampilan rapi setelah perulangan selesai.

Baris 43: (Baris kosong)

Baris 44: (Baris kosong)

Baris 45: Mendefinisikan fungsi main() sebagai alur utama jalannya program.

Baris 46: Membuat objek stack baru berdasarkan class StackArray.

Baris 47: Membuat variabel pilih dengan nilai awal 0 untuk menampung pilihan menu user.

Baris 48: Memulai perulangan menu (terus berulang selama user tidak memilih angka 5).

Baris 49: Menampilkan judul menu.

Baris 50: Menampilkan teks opsi 1 (Kunjungi web baru).

Baris 51: Menampilkan teks opsi 2 (Kembali).

Baris 52: Menampilkan teks opsi 3 (Lihat halaman sekarang).

Baris 53: Menampilkan teks opsi 4 (Tampilkan history).

Baris 54: Menampilkan teks opsi 5 (Keluar).

Baris 55: Memulai blok try untuk menangkap error jika user memasukkan huruf, bukan angka.

Baris 56: Meminta input user dan langsung mengubahnya menjadi tipe bilangan bulat (integer).

Baris 57: Menangkap error ValueError jika konversi ke angka gagal.

Baris 58: Menampilkan peringatan bahwa input tidak valid jika yang diketik bukan angka.

Baris 59: Melanjutkan paksa perulangan (kembali ke awal menu) mengabaikan baris di bawahnya.

Baris 60: Mengecek apakah pilihan user adalah 1.

Baris 61: Jika ya, meminta input nama website dari user.

Baris 62: Memanggil fungsi push untuk memasukkan website tersebut ke riwayat.

Baris 63: Mengecek apakah pilihan user adalah 2.

Baris 64: Jika ya, memanggil fungsi pop (mundur ke web sebelumnya).

Baris 65: Mengecek apakah pilihan user adalah 3.

Baris 66: Jika ya, memanggil fungsi peek (melihat halaman web yang sedang aktif saat ini).

Baris 67: Mengecek apakah pilihan user adalah 4.

Baris 68: Jika ya, memanggil fungsi display (mencetak daftar seluruh web yang dikunjungi).

Baris 69: Mengecek apakah pilihan user adalah 5.

Baris 70: Jika ya, menampilkan pesan bahwa program selesai ditutup (lalu otomatis perulangan while berhenti).

Baris 71: Kondisi lain jika angka yang dimasukkan bukan 1 sampai 5.

Baris 72: Menampilkan pesan peringatan bahwa pilihan menu tidak tersedia.

Baris 73: (Baris kosong)

Baris 74: (Baris kosong)

Baris 75: Mengecek apakah file Python ini dijalankan secara langsung (bukan sebagai module yang di-import).

Baris 76: Jika ya, maka fungsi main() akan dipanggil untuk mulai mengeksekusi program.

## Output:
<img width="590" height="847" alt="image" src="https://github.com/user-attachments/assets/ed1c0f09-28e9-4325-8a75-71bc220d4887" />
<img width="830" height="771" alt="image" src="https://github.com/user-attachments/assets/0ab7d281-3412-4d4c-8be8-86a2aa6fc0a5" />


### Youtube:
