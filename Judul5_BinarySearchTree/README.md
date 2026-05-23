# Sistem Pesananan Restoran Serba Ada

## Source Code:
<img width="660" height="689" alt="image" src="https://github.com/user-attachments/assets/fec2fe7e-7790-4bb0-985a-0a18f6627856" />
<img width="725" height="709" alt="image" src="https://github.com/user-attachments/assets/b6533da5-e1f2-4b4e-bcd3-311e534e70c4" />
<img width="612" height="777" alt="image" src="https://github.com/user-attachments/assets/0525cfac-918b-41f5-93d7-a33927eb3af2" />
<img width="567" height="529" alt="image" src="https://github.com/user-attachments/assets/7563f798-cf1b-4ba8-b2cb-1ab1f5e1b9a9" />
<img width="922" height="896" alt="image" src="https://github.com/user-attachments/assets/c228d85d-61de-41fe-bb4e-05b61893d5c3" />
<img width="1315" height="524" alt="image" src="https://github.com/user-attachments/assets/50a5e968-8faa-4d44-8d3d-8cf8b5169260" />


## Penjelasan:

Baris 1: Mendefinisikan class Node untuk membuat simpul (node) pada struktur data Tree.

Baris 2: Membuat fungsi inisialisasi awal saat objek Node baru dibuat.

Baris 3: Menyimpan variabel key yang nantinya digunakan untuk menyimpan nomor antrean.

Baris 4: Menyimpan variabel key2 yang digunakan untuk menyimpan nama menu pesanan.

Baris 5: Mengatur petunjuk cabang kiri (left) menjadi kosong (None).

Baris 6: Mengatur petunjuk cabang kanan (right) menjadi kosong (None).

Baris 7: (Baris kosong untuk memisahkan antar class/fungsi)

Baris 8: (Baris kosong)

Baris 9: Mendefinisikan class BSTLanjut untuk mengelola sistem Binary Search Tree (BST).

Baris 10: Fungsi inisialisasi awal saat objek BSTLanjut dibuat.

Baris 11: Mengatur posisi puncak (akar/root) dari tree menjadi kosong.

Baris 12: (Baris kosong)

Baris 13: Fungsi rekursif untuk menyisipkan node baru ke tempat yang sesuai.

Baris 14: Mengecek apakah posisi root/node saat ini sedang kosong.

Baris 15: Jika kosong, letakkan node baru beserta antrean dan nama pesanannya di posisi tersebut.

Baris 16: Mengecek apakah nomor antrean baru lebih kecil dari nomor node saat ini.

Baris 17: Jika ya, geser ke kiri dan ulangi pencarian posisi kosong di cabang kiri.

Baris 18: Mengecek apakah nomor antrean baru lebih besar dari nomor node saat ini.

Baris 19: Jika ya, geser ke kanan dan ulangi pencarian posisi kosong di cabang kanan.

Baris 20: Mengembalikan node yang telah dimasukkan posisi barunya.

Baris 21: (Baris kosong)

Baris 22: Fungsi pembantu agar penyisipan lebih mudah dipanggil dari luar (cukup input dua variabel).

Baris 23: Memperbarui self.root dengan memanggil fungsi insert_node mulai dari puncak.

Baris 24: (Baris kosong)

Baris 25: Fungsi untuk mencari node yang memiliki angka paling kecil.

Baris 26: Memulai pencarian dari node yang dilempar sebagai argumen (variabel current).

Baris 27: Melakukan perulangan selama masih ada cabang kiri.

Baris 28: Terus bergeser ke cabang kiri (karena sebelah kiri selalu lebih kecil pada BST).

Baris 29: Mengembalikan node dengan nilai terkecil yang ditemukan.

Baris 30: (Baris kosong)

Baris 31: Fungsi rekursif untuk menghapus node berdasarkan nomor antreannya.

Baris 32: Jika node yang dicek ternyata kosong (data tidak ditemukan).

Baris 33: Langsung kembalikan nilai None (tidak ada yang dihapus).

Baris 34: Jika angka yang mau dihapus lebih kecil dari node saat ini.

Baris 35: Bergeser mencari node tersebut ke cabang kiri.

Baris 36: Jika angka yang mau dihapus lebih besar dari node saat ini.

Baris 37: Bergeser mencari node tersebut ke cabang kanan.

Baris 38: Jika angka yang dicari sama (node ditemukan!).

Baris 39: Cek apakah node tersebut tidak punya cabang kiri dan kanan (disebut daun).

Baris 40: Langsung hapus dengan mengembalikan nilai None.

Baris 41: Cek apakah node tersebut hanya punya cabang kanan.

Baris 42: Gantikan posisi node yang dihapus dengan anak kanannya.

Baris 43: Cek apakah node tersebut hanya punya cabang kiri.

Baris 44: Gantikan posisi node yang dihapus dengan anak kirinya.

Baris 45: Jika node tersebut memiliki kedua anak (kiri dan kanan).

Baris 46: Cari node penerus pengganti dari nilai terkecil di cabang kanan (successor).

Baris 47: Ganti nomor antrean node saat ini dengan milik successor.

Baris 48: Ganti nama pesanan node saat ini dengan milik successor.

Baris 49: Hapus posisi successor yang asli dari cabang kanan.

Baris 50: Mengembalikan struktur root/node yang sudah diperbarui.

Baris 51: (Baris kosong)

Baris 52: Fungsi pembantu agar perintah hapus mudah dipanggil dari luar program.

Baris 53: Memanggil kembali delete_node mulai dari root agar keseluruhan tree diperbarui.

Baris 54: (Baris kosong)

Baris 55: Fungsi untuk menghitung tinggi dari tree.

Baris 56: Jika tree/node kosong.

Baris 57: Kembalikan nilai -1.

Baris 58: Hitung tinggi cabang kiri dengan memanggil fungsi diri sendiri (rekursif).

Baris 59: Hitung tinggi cabang kanan dengan cara yang sama.

Baris 60: Mengambil nilai tertinggi dari cabang kiri atau kanan dan ditambahkan 1.

Baris 61: (Baris kosong)

Baris 62: Fungsi mencetak seluruh pesanan secara menyamping (dari tingkat teratas ke bawah).

Baris 63: Jika tree masih belum ada isinya (kosong).

Baris 64: Tampilkan teks "(Tidak ada pesanan)".

Baris 65: Keluar dari fungsi (berhenti).

Baris 66: Membuat list kosong queue (antrean) untuk membantu proses pencetakan.

Baris 67: Memasukkan posisi awal (root) ke dalam list antrean.

Baris 68: Mengulang proses selama masih ada isi di list antrean.

Baris 69: Mengeluarkan data pertama dari antrean dan menyimpannya di variabel current.

Baris 70: Mencetak nomor antrean dan nama pesanan ke layar.

Baris 71: Jika node saat ini memiliki anak di sebelah kiri.

Baris 72: Tambahkan anak kiri tersebut ke list antrean untuk diproses nanti.

Baris 73: Jika node saat ini memiliki anak di sebelah kanan.

Baris 74: Tambahkan anak kanan tersebut ke list antrean.

Baris 75: Mencetak baris kosong (enter) agar hasil cetak terlihat rapi.

Baris 76: (Baris kosong)

Baris 77: Fungsi untuk mencari pesanan dengan nomor terdekat di atasnya (successor).

Baris 78: Mulai pencarian dari akar (root).

Baris 79: Menetapkan nilai pencarian successor awalnya kosong.

Baris 80: Looping berjalan terus selama node yang dicek tidak kosong.

Baris 81: Jika angka yang dicari lebih kecil dari node saat ini.

Baris 82: Catat node saat ini sebagai kandidat pengganti/lanjutan sementara (successor).

Baris 83: Terus bergeser ke cabang kiri.

Baris 84: Jika angka yang dicari lebih besar dari node saat ini.

Baris 85: Langsung lompat dan cek kecabang kanan tanpa mencatat kandidat.

Baris 86: Jika angkanya persis sama (ditemukan posisinya).

Baris 87: Berhenti melakukan pencarian perulangan.

Baris 88: Setelah perulangan, jika ternyata node-nya tidak ditemukan (kosong).

Baris 89: Kembalikan informasi bahwa pencarian lanjutan gagal (False).

Baris 90: Jika node ditemukan dan memiliki anak di sebelah kanan.

Baris 91: Timpa kandidat sebelumnya. Nilai penerusnya pasti ada di nilai terkecil di cabang kanan tersebut.

Baris 92: Jika di akhir tidak ada satupun nilai yang lebih besar (tidak punya successor).

Baris 93: Kembalikan informasi kegagalan (False).

Baris 94: Kembalikan nomor antrean, nama pesanan, dan status pencarian sukses (True).

Baris 95: (Baris kosong)

Baris 96: Fungsi untuk mencari pesanan dengan nomor terdekat di bawahnya (predecessor).

Baris 97: Memulai posisi pengecekan dari puncak tree (root).

Baris 98: Menetapkan nilai predecessor awalnya kosong.

Baris 99: Looping selama pencarian belum berujung pada kekosongan (None).

Baris 100: Jika angka yang dicari lebih besar dari node saat ini.

Baris 101: Simpan node saat ini sebagai kandidat angka lebih kecil sementara (predecessor).

Baris 102: Geser pencarian selanjutnya ke cabang kanan.

Baris 103: Jika angka yang dicari lebih kecil dari node saat ini.

Baris 104: Geser pencarian langsung ke cabang kiri tanpa mencatat kandidat.

Baris 105: Jika angkanya persis sama (node ditemukan).

Baris 106: Berhentikan pencarian looping.

Baris 107: Mengecek ulang, jika ujung-ujungnya node tidak ketemu di dalam sistem.

Baris 108: Kembalikan pesan kegagalan (False).

Baris 109: Jika node yang dicari ketemu dan memiliki anak cabang kiri.

Baris 110: Mulai mencari ke bawah dari anak cabangnya yang kiri (temp).

Baris 111: Melakukan looping mencari terus ke arah kanan mentok.

Baris 112: Menggeser pengecekan ke kanan.

Baris 113: Tetapkan node paling kanan tersebut sebagai nilai predecessor yang paling tepat.

Baris 114: Jika di akhir pencarian nilai predecessor sama sekali tidak ditemukan.

Baris 115: Mengembalikan informasi gagal mencari angka yang lebih kecil.

Baris 116: Mengembalikan nomor antrean, nama pesanan, dan status sukses (True).

Baris 117: (Baris kosong)

Baris 118: (Baris kosong)

Baris 119: Mendefinisikan fungsi utama aplikasi berjalan (main()).

Baris 120: Membuat cetakan objek dari class BSTLanjut ke dalam variabel bernama bst.

Baris 121: Mengatur variabel sementara pilih = 0 untuk menampung masukan menu pengguna.

Baris 122: Membuat perulangan yang akan terus muncul selama pengguna belum menginput angka 6.

Baris 123: Menampilkan judul "Sistem Pesanan Restoran Serba Ada".

Baris 124: Menampilkan menu 1 ke layar teks.

Baris 125: Menampilkan menu 2 ke layar teks.

Baris 126: Menampilkan menu 3 ke layar teks.

Baris 127: Menampilkan menu 4 ke layar teks.

Baris 128: Menampilkan menu 5 ke layar teks.

Baris 129: Menampilkan menu 6 ke layar teks (Keluar).

Baris 130: Blok try digunakan untuk mencegah error (program berhenti tiba-tiba) saat menerima input pengguna.

Baris 131: Meminta pengguna memasukkan angka untuk variabel pilih.

Baris 132: Menangkap error tipe ValueError (jika misalnya pengguna tidak sengaja mengetik huruf).

Baris 133: Tampilkan pemberitahuan bahwa input salah.

Baris 134: Gunakan perintah continue untuk mengulang menu ke atas lagi.

Baris 135: Mengecek apakah pengguna memilih menu nomor 1.

Baris 136: Blok pengaman try lagi saat menginput detail nomor antrean pesanan.

Baris 137: Meminta input nomor antrean ke variabel x dalam bentuk angka (integer).

Baris 138: Meminta input nama menu masakan ke variabel y.

Baris 139: Memasukkan x dan y ke dalam fungsi insert pada objek bst.

Baris 140: Cetak pesan sukses jika pesanan baru sudah masuk.

Baris 141: Menangkap apabila input pada Baris 137 adalah huruf, bukan angka.

Baris 142: Tampilkan pesan teguran ke pengguna bahwa nomor antrean wajib angka.

Baris 143: Cek apakah pengguna memilih opsi menu 2.

Baris 144: Pengaman blok try ketika ingin menyelesaikan antrean.

Baris 145: Meminta nomor antrean yang ingin dihapus lalu mengubahnya ke tipe data integer di dalam variabel x.

Baris 146: Memanggil perintah menghapus node (pesanan) dari objek bst berdasarkan input x.

Baris 147: Tampilkan pesan bahwa antrean tersebut telah berhasil diselesaikan/dihapus.

Baris 148: Menangkap error di menu nomor 2 apabila user memasukkan karakter non-angka.

Baris 149: Berikan peringatan bahwa yang diinput tidak sah.

Baris 150: Cek apakah pengguna memilih menu 3.

Baris 151: Tampilkan kalimat awalan "Daftar Pesanan yang Sedang Diproses: ".

Baris 152: Tampilkan struktur tree dengan menggunakan fungsi level_order.

Baris 153: Cek apakah pengguna memilih menu 4 (Cek pesanan lanjutan).

Baris 154: Blok try mengamankan input nomor pencarian.

Baris 155: Meminta pengguna menginput antrean patokan pencarian untuk selanjutnya.

Baris 156: Memanggil fungsi find_successor lalu memecah hasilnya ke variabel: ans (nomor), wer (nama), found (status).

Baris 157: Mengecek jika status nilai dari found bernilai True (berhasil ditemukan).

Baris 158: Tampilkan nama pesanan dan antrean selanjutya yang ditemukan di layar pengguna.

Baris 159: Apabila gagal / found bernilai False.

Baris 160: Tampilkan konfirmasi pesan bahwa antrean tersebut memang tidak ada pesanan setelahnya.

Baris 161: Menangkap gagal input string di blok menu 4.

Baris 162: Tampilkan teks input tidak valid.

Baris 163: Cek apakah pengguna memilih menu 5.

Baris 164: Memulai pengamanan try input khusus menu ke-5.

Baris 165: Meminta angka antrean pesanan yang ingin dilacak nomor sebelumnya.

Baris 166: Memanggil fungsi find_predecessor dan mengisikan hasil 3 nilai balasannya ke ans, wer, found.

Baris 167: Jika pencarian statusnya True (berhasil ditemukannya angka sebelumnya).

Baris 168: Cetak konfirmasi nomor dan pesanan yang dicari ke layar.

Baris 169: Jika status pencarian berstatus gagal (False).

Baris 170: Cetak pesan error yang menyimpulkan antrean yang dicari paling pertama atau memang kosong.

Baris 171: Tangkap error masukan di menu ke-5 (misal user mengetik huruf 'A').

Baris 172: Cetak pesan bahwa masukan salah.

Baris 173: Mengecek opsi terakhir, jika pengguna menekan angka 6.

Baris 174: Cetak tulisan "Program selesai." dan perulangan while di baris 122 otomatis putus dengan sendirinya.

Baris 175: Baris pancingan ini (else) bekerja jika pengguna menginput angka tapi selain 1,2,3,4,5, dan 6.

Baris 176: Cetak peringatan "Pilihan tidak valid!" ke monitor.

Baris 177: (Baris kosong)

Baris 178: (Baris kosong)

Baris 179: Perintah untuk mengecek apakah script Python ini dieksekusi secara langsung.

Baris 180: Jika ya, jalankan fungsi main() untuk memanggil program keseluruhan.

## Output:
<img width="461" height="870" alt="image" src="https://github.com/user-attachments/assets/1ab38de5-fc17-4a2e-8820-6adf7fc137bc" />
<img width="551" height="804" alt="image" src="https://github.com/user-attachments/assets/ad5330e3-4dd8-496b-b072-d82509f15ad9" />
<img width="581" height="186" alt="image" src="https://github.com/user-attachments/assets/282f5f9e-8849-4b19-9535-38fa0ffb4345" />


### Youtube:
