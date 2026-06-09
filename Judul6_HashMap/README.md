# Sistem Pengelolaan Data Mahasiswa

## Source Code:
<img width="581" height="660" alt="image" src="https://github.com/user-attachments/assets/a2f85e4e-3acc-4650-bc39-22418c15b69c" />
<img width="908" height="780" alt="image" src="https://github.com/user-attachments/assets/ed7465ad-e905-4f3e-bdbf-4c457a573898" />
<img width="1240" height="776" alt="image" src="https://github.com/user-attachments/assets/f57ef42f-a635-40cd-aeda-ea9506ef42be" />
<img width="1012" height="481" alt="image" src="https://github.com/user-attachments/assets/bc6fc3d0-3238-4bde-b2cb-b954ceb1454d" />

## Penjelasan:
Baris 1: Mendefinisikan class Node sebagai cetakan untuk satu elemen data di dalam linked list.

Baris 2: Fungsi __init__ untuk menginisialisasi atribut (sifat) saat objek Node baru dibuat.

Baris 3: Menyimpan variabel key (nantinya berupa NPM mahasiswa) ke dalam node.

Baris 4: Menyimpan variabel value (nama mahasiswa) ke dalam node.

Baris 5: Menyimpan variabel value2 (IPK mahasiswa) ke dalam node.

Baris 6: Membuat penunjuk next ke elemen selanjutnya, diisi None (kosong) sebagai nilai awal.

Baris 7: Baris kosong.

Baris 8: Baris kosong.

Baris 9: Mendefinisikan class HashMapSeparateChaining untuk struktur data tabel hash.

Baris 10: Fungsi __init__ untuk inisialisasi tabel hash dengan ukuran default (bawaan) 10.

Baris 11: Menyimpan ukuran tabel ke atribut self.SIZE.

Baris 12: Membuat list (tabel) yang berisi elemen kosong (None) sebanyak ukuran SIZE.

Baris 13: Baris kosong.

Baris 14: Mendefinisikan fungsi hash_function untuk menghitung lokasi/indeks array dari suatu key.

Baris 15: Mengembalikan hasil hitungan matematis modulo (sisa bagi) key dengan SIZE untuk menentukan indeks.

Baris 16: Baris kosong.

Baris 17: Mendefinisikan fungsi insert untuk menambahkan atau memperbarui data di dalam tabel.

Baris 18: Memanggil hash_function untuk mencari indeks tempat data akan disimpan.

Baris 19: Mengambil elemen pertama (head) dari indeks tersebut dan menyimpannya ke variabel current.

Baris 20: Melakukan perulangan selama current belum kosong (mencari ke dalam linked list).

Baris 21: Mengecek jika key node saat ini sama dengan key baru yang ingin dimasukkan (data sudah ada).

Baris 22: Jika ya, perbarui value (nama mahasiswa).

Baris 23: Perbarui juga value2 (IPK mahasiswa).

Baris 24: Berhenti dan keluar dari fungsi (return) karena data cuma diperbarui, tidak ditambah baru.

Baris 25: Pindah ke node selanjutnya dalam linked list.

Baris 26: Jika data belum ada, buat objek Node baru dengan key, value, dan value2 tersebut.

Baris 27: Sambungkan penunjuk next dari node baru ke elemen pertama yang sudah ada di indeks tersebut.

Baris 28: Jadikan node baru sebagai elemen pertama (head) di indeks tabel tersebut.

Baris 29: Baris kosong.

Baris 30: Mendefinisikan fungsi search untuk mencari data berdasarkan key.

Baris 31: Mencari indeks lokasi penyimpanan key tersebut menggunakan fungsi hash.

Baris 32: Mengambil elemen pertama (head) pada indeks tersebut ke variabel current.

Baris 33: Memulai perulangan selama current belum mencapai ujung kosong (None).

Baris 34: Mengecek apakah key node saat ini cocok dengan yang dicari.

Baris 35: Jika cocok, langsung kembalikan objek current (node yang ditemukan).

Baris 36: Pindah ke node selanjutnya untuk lanjut mencari.

Baris 37: Jika perulangan selesai dan tidak ada yang cocok, kembalikan None (tidak ditemukan).

Baris 38: Baris kosong.

Baris 39: Mendefinisikan fungsi remove_key untuk menghapus data dari tabel hash.

Baris 40: Menghitung indeks dari key yang ingin dihapus.

Baris 41: Menyimpan elemen head di indeks tersebut ke current.

Baris 42: Menyiapkan variabel prev bernilai None untuk mengingat posisi node sebelumnya.

Baris 43: Melakukan perulangan selama masih ada elemen current.

Baris 44: Mengecek apakah key pada current cocok dengan yang akan dihapus.

Baris 45: Mengecek apakah ini adalah elemen pertama/head (karena prev masih None).

Baris 46: Jika ya, ganti elemen pertama di tabel dengan elemen kedua (node berikutnya).

Baris 47: Jika bukan elemen pertama (kondisi else).

Baris 48: Sambungkan next dari node sebelumnya langsung ke node sesudah current (mem-bypass node yang dihapus).

Baris 49: Kembalikan nilai True karena penghapusan berhasil.

Baris 50: Menyimpan current ke prev sebelum maju.

Baris 51: Geser current ke node selanjutnya.

Baris 52: Kembalikan nilai False jika sampai akhir list data gagal ditemukan.

Baris 53: Baris kosong.

Baris 54: Mendefinisikan fungsi display untuk menampilkan semua data dalam hash map.

Baris 55: Mencetak judul tampilan tabel data.

Baris 56: Melakukan perulangan untuk setiap nomor indeks dalam batas SIZE (0 sampai 9).

Baris 57: Mencetak nomor indeks tabel tanpa ganti baris (end="").

Baris 58: Mengambil elemen head dari indeks saat ini.

Baris 59: Melakukan perulangan ke seluruh elemen linked list pada indeks tersebut.

Baris 60: Mencetak detail isi node berupa NPM, Nama, dan IPK dengan tanda panah penghubung.

Baris 61: Geser current ke node di sebelahnya.

Baris 62: Mencetak kata "NULL" di akhir linked list untuk indeks tersebut, lalu pindah baris.

Baris 63: Baris kosong.

Baris 64: Baris kosong.

Baris 65: Mendefinisikan fungsi main sebagai program utama interaktif.

Baris 66: Membuat objek (instance) bernama hashmap dari class HashMapSeparateChaining.

Baris 67: Menyiapkan variabel pilih dengan nilai awal 0 untuk kendali perulangan menu.

Baris 68: Memulai perulangan menu utama, terus berjalan selama pengguna belum menginput angka 5.

Baris 69: Menampilkan opsi menu ke-1 (Tambah).

Baris 70: Menampilkan opsi menu ke-2 (Cari).

Baris 71: Menampilkan opsi menu ke-3 (Hapus).

Baris 72: Menampilkan opsi menu ke-4 (Tampilkan).

Baris 73: Menampilkan opsi menu ke-5 (Keluar).

Baris 74: Memulai blok try untuk menangani apabila pengguna salah memasukkan tipe data pada menu.

Baris 75: Menerima input pilihan (sebagai angka int) dari pengguna.

Baris 76: Blok except untuk menangkap error ValueError (misalnya pengguna menginput huruf).

Baris 77: Menampilkan teks "Input tidak valid!".

Baris 78: Memerintahkan continue untuk mengulang loop dari atas tanpa membaca baris di bawahnya.

Baris 79: Menjalankan blok ini jika pengguna memilih menu 1.

Baris 80: Blok try untuk mencegah error saat mengisi data mahasiswa.

Baris 81: Meminta input nama bertipe string / teks.

Baris 82: Meminta input NPM bertipe integer / angka bulat.

Baris 83: Meminta input IPK bertipe float / angka desimal.

Baris 84: Memasukkan data tersebut ke objek hashmap lewat fungsi insert().

Baris 85: Menampilkan teks bahwa data sukses ditambahkan.

Baris 86: Menangkap error tipe data saat input mahasiswa menggunakan except ValueError.

Baris 87: Menampilkan teks "Input tidak valid!".

Baris 88: Menjalankan blok ini jika pengguna memilih menu 2.

Baris 89: Blok try mencegah error input saat proses pencarian.

Baris 90: Meminta NPM bertipe integer sebagai kata kunci pencarian.

Baris 91: Memanggil fungsi search() lalu menyimpan output node-nya ke variabel hasil.

Baris 92: Mengecek apakah nilai hasil tidak kosong (node berhasil ditemukan).

Baris 93: Menampilkan teks beserta nilai nama, NPM, dan IPK jika datanya ada.

Baris 94: Kondisi else yang berjalan apabila pencarian gagal (hasil bernilai None).

Baris 95: Menampilkan teks bahwa data NPM yang dicari tidak ketemu.

Baris 96: Menangkap error saat input NPM pencarian bukan berbentuk angka.

Baris 97: Menampilkan peringatan "NPM tidak valid!".

Baris 98: Menjalankan blok ini jika pengguna memilih menu 3.

Baris 99: Blok try mencegah error input sewaktu menghapus.

Baris 100: Meminta angka NPM dari mahasiswa yang mau dihapus.

Baris 101: Mencari NPM itu dahulu menggunakan search() dan menyimpannya di variabel hasil.

Baris 102: Mengecek apabila hasil tidak kosong (berarti datanya dikonfirmasi ada).

Baris 103: Memanggil fungsi remove_key() untuk membuang node tersebut dari tabel.

Baris 104: Menampilkan teks keberhasilan penghapusan data.

Baris 105: Kondisi else apabila data mahasiswa awalnya memang sudah tidak ada.

Baris 106: Menampilkan teks pemberitahuan bahwa data tidak ditemukan.

Baris 107: Menangkap error jika input hapus bukan berbentuk angka.

Baris 108: Menampilkan peringatan "NPM tidak valid!".

Baris 109: Menjalankan blok ini jika pengguna memilih menu 4.

Baris 110: Memanggil fungsi display() untuk mem-print keseluruhan isi hash table.

Baris 111: Menjalankan blok ini jika pengguna memilih opsi menu 5 (Keluar).

Baris 112: Menampilkan pesan "Program selesai."

Baris 113: Kondisi pengecualian else ketika pengguna memasukkan angka selain 1, 2, 3, 4, atau 5.

Baris 114: Menampilkan pemberitahuan "Pilihan tidak valid!".

Baris 115: Baris kosong.

Baris 116: Baris kosong.

Baris 117: Pengecekan otomatis bawaan Python untuk memastikan script hanya dieksekusi saat dijalankan langsung (bukan saat di-import dari file lain).

Baris 118: Menjalankan/memanggil fungsi main() untuk mengawali seluruh program.

## Output:

### Youtube: 
