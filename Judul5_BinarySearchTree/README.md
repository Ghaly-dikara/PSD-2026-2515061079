# Sistem Pesananan Restoran Serba Ada
Sistem ini merupakan simuali antrean pesanan menggunakan struktur data binary serch tree. Sistem menggunakan bahasa pemrograman python, yang berisikan class Node yang berisikan dua key, class BSTLanjut untuk struktur datanya. Dalam class BSTLanjut terdapat fungsi insert_node, insert, find_min_node, delete_node, delete, level_order, find_successor, find_predecessor, dan main.

fungsi insert_node dan insert digunakan untuk memasukkan nomor pesanan ke dalam BST dengan membandingkan nilai key (nomor pesanan) untuk posisinya. Selanjutnya ada fungsi find_min_node berguna untuk mencari node dengan key (nomor pesanan) terkecil, yang nanti akan digunakan di fungsi find_successor. Fungsi delete_node dan delete digunakan untuk menghapus node dengan membandingkan key (nomor antrean)- nya. setelah itu level_order berfungsi untuk menampilkan pesanan dari nomor pesanan yang terkecil hingga yang terbesar. selanjutnya ada fungsi find_successor digunakan untuk menampilkan nomor pesanan setelah nomor pesanan yang dimasukkan, dan find_predecessor untuk menampilkan nomor pesanan sebelum nomor pesanan yang dimasukkan. Dan yang terakhir ada fungsi menu yang berisi menu tambah pesanan baru, pesanan selesai dihidangkan, lihat semua antrean, cek pesanan sebelumnya, cek pesanan setelahnya, dan keluar yang akan mengakhiri jalannya sistem.

## Source Code:
<img width="660" height="689" alt="image" src="https://github.com/user-attachments/assets/fec2fe7e-7790-4bb0-985a-0a18f6627856" />
<img width="719" height="872" alt="image" src="https://github.com/user-attachments/assets/db5319c2-3714-43a4-852c-606f1599e09f" />
<img width="586" height="458" alt="image" src="https://github.com/user-attachments/assets/e954112b-6caa-403a-b848-ffc82852a3fc" />
<img width="566" height="527" alt="image" src="https://github.com/user-attachments/assets/2f959526-eee9-43c7-8c08-7b2acb26277b" />
<img width="919" height="896" alt="image" src="https://github.com/user-attachments/assets/5dbaf2b2-207f-40ae-adc4-99a78197dc20" />
<img width="1300" height="528" alt="image" src="https://github.com/user-attachments/assets/39747c81-a4c6-42c0-b7ca-5e110f5c4ce9" />

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

Baris 55: Fungsi mencetak seluruh pesanan secara menyamping (dari tingkat teratas ke bawah).

Baris 56: Jika tree masih belum ada isinya (kosong).

Baris 57: Tampilkan teks "(Tidak ada pesanan)".

Baris 58: Keluar dari fungsi (berhenti).

Baris 59: Membuat list kosong queue (antrean) untuk membantu proses pencetakan.

Baris 60: Memasukkan posisi awal (root) ke dalam list antrean.

Baris 61: Mengulang proses selama masih ada isi di list antrean.

Baris 62: Mengeluarkan data pertama dari antrean dan menyimpannya di variabel current.

Baris 63: Mencetak nomor antrean dan nama pesanan ke layar.

Baris 64: Jika node saat ini memiliki anak di sebelah kiri.

Baris 65: Tambahkan anak kiri tersebut ke list antrean untuk diproses nanti.

Baris 66: Jika node saat ini memiliki anak di sebelah kanan.

Baris 67: Tambahkan anak kanan tersebut ke list antrean.

Baris 68: Mencetak baris kosong (enter) agar hasil cetak terlihat rapi.

Baris 69: (Baris kosong)

Baris 70: Fungsi untuk mencari pesanan dengan nomor terdekat di atasnya (successor).

Baris 71: Mulai pencarian dari akar (root).

Baris 72: Menetapkan nilai pencarian successor awalnya kosong.

Baris 73: Looping berjalan terus selama node yang dicek tidak kosong.

Baris 74: Jika angka yang dicari lebih kecil dari node saat ini.

Baris 75: Catat node saat ini sebagai kandidat pengganti/lanjutan sementara (successor).

Baris 76: Terus bergeser ke cabang kiri.

Baris 77: Jika angka yang dicari lebih besar dari node saat ini.

Baris 78: Langsung lompat dan cek kecabang kanan tanpa mencatat kandidat.

Baris 79: Jika angkanya persis sama (ditemukan posisinya).

Baris 80: Berhenti melakukan pencarian perulangan.

Baris 81: Setelah perulangan, jika ternyata node-nya tidak ditemukan (kosong).

Baris 82: Kembalikan informasi bahwa pencarian lanjutan gagal (False).

Baris 83: Jika node ditemukan dan memiliki anak di sebelah kanan.

Baris 84: Timpa kandidat sebelumnya. Nilai penerusnya pasti ada di nilai terkecil di cabang kanan tersebut.

Baris 85: Jika di akhir tidak ada satupun nilai yang lebih besar (tidak punya successor).

Baris 86: Kembalikan informasi kegagalan (False).

Baris 87: Kembalikan nomor antrean, nama pesanan, dan status pencarian sukses (True).

Baris 88: (Baris kosong)

Baris 89: Fungsi untuk mencari pesanan dengan nomor terdekat di bawahnya (predecessor).

Baris 90: Memulai posisi pengecekan dari puncak tree (root).

Baris 91: Menetapkan nilai predecessor awalnya kosong.

Baris 92: Looping selama pencarian belum berujung pada kekosongan (None).

Baris 93: Jika angka yang dicari lebih besar dari node saat ini.

Baris 94: Simpan node saat ini sebagai kandidat angka lebih kecil sementara (predecessor).

Baris 95: Geser pencarian selanjutnya ke cabang kanan.

Baris 96: Jika angka yang dicari lebih kecil dari node saat ini.

Baris 97: Geser pencarian langsung ke cabang kiri tanpa mencatat kandidat.

Baris 98: Jika angkanya persis sama (node ditemukan).

Baris 99: Berhentikan pencarian looping.

Baris 100: Mengecek ulang, jika ujung-ujungnya node tidak ketemu di dalam sistem.

Baris 101: Kembalikan pesan kegagalan (False).

Baris 102: Jika node yang dicari ketemu dan memiliki anak cabang kiri.

Baris 103: Mulai mencari ke bawah dari anak cabangnya yang kiri (temp).

Baris 104: Melakukan looping mencari terus ke arah kanan mentok.

Baris 105: Menggeser pengecekan ke kanan.

Baris 106: Tetapkan node paling kanan tersebut sebagai nilai predecessor yang paling tepat.

Baris 107: Jika di akhir pencarian nilai predecessor sama sekali tidak ditemukan.

Baris 108: Mengembalikan informasi gagal mencari angka yang lebih kecil.

Baris 109: Mengembalikan nomor antrean, nama pesanan, dan status sukses (True).

Baris 110: (Baris kosong)

Baris 111: (Baris kosong)

Baris 112: Mendefinisikan fungsi utama aplikasi berjalan (main()).

Baris 113: Membuat cetakan objek dari class BSTLanjut ke dalam variabel bernama bst.

Baris 114: Mengatur variabel sementara pilih = 0 untuk menampung masukan menu pengguna.

Baris 115: Membuat perulangan yang akan terus muncul selama pengguna belum menginput angka 6.

Baris 116: Menampilkan judul "Sistem Pesanan Restoran Serba Ada".

Baris 117: Menampilkan menu 1 ke layar teks.

Baris 118: Menampilkan menu 2 ke layar teks.

Baris 119: Menampilkan menu 3 ke layar teks.

Baris 120: Menampilkan menu 4 ke layar teks.

Baris 121: Menampilkan menu 5 ke layar teks.

Baris 122: Menampilkan menu 6 ke layar teks (Keluar).

Baris 123: Blok try digunakan untuk mencegah error (program berhenti tiba-tiba) saat menerima input pengguna.

Baris 124: Meminta pengguna memasukkan angka untuk variabel pilih.

Baris 125: Menangkap error tipe ValueError (jika misalnya pengguna tidak sengaja mengetik huruf).

Baris 126: Tampilkan pemberitahuan bahwa input salah.

Baris 127: Gunakan perintah continue untuk mengulang menu ke atas lagi.

Baris 128: Mengecek apakah pengguna memilih menu nomor 1.

Baris 129: Blok pengaman try lagi saat menginput detail nomor antrean pesanan.

Baris 130: Meminta input nomor antrean ke variabel x dalam bentuk angka (integer).

Baris 131: Meminta input nama menu masakan ke variabel y.

Baris 132: Memasukkan x dan y ke dalam fungsi insert pada objek bst.

Baris 133: Cetak pesan sukses jika pesanan baru sudah masuk.

Baris 134: Menangkap apabila input pada Baris 130 adalah huruf, bukan angka.

Baris 135: Tampilkan pesan teguran ke pengguna bahwa nomor antrean wajib angka.

Baris 136: Cek apakah pengguna memilih opsi menu 2.

Baris 137: Pengaman blok try ketika ingin menyelesaikan antrean.

Baris 138: Meminta nomor antrean yang ingin dihapus lalu mengubahnya ke tipe data integer di dalam variabel x.

Baris 139: Memanggil perintah menghapus node (pesanan) dari objek bst berdasarkan input x.

Baris 140: Tampilkan pesan bahwa antrean tersebut telah berhasil diselesaikan/dihapus.

Baris 141: Menangkap error di menu nomor 2 apabila user memasukkan karakter non-angka.

Baris 142: Berikan peringatan bahwa yang diinput tidak sah.

Baris 143: Cek apakah pengguna memilih menu 3.

Baris 144: Tampilkan kalimat awalan "Daftar Pesanan yang Sedang Diproses: ".

Baris 145: Tampilkan struktur tree dengan menggunakan fungsi level_order.

Baris 146: Cek apakah pengguna memilih menu 4 (Cek pesanan lanjutan).

Baris 147: Blok try mengamankan input nomor pencarian.

Baris 148: Meminta pengguna menginput antrean patokan pencarian untuk selanjutnya.

Baris 149: Memanggil fungsi find_successor lalu memecah hasilnya ke variabel: ans (nomor), wer (nama), found (status).

Baris 150: Mengecek jika status nilai dari found bernilai True (berhasil ditemukan).

Baris 151: Tampilkan nama pesanan dan antrean selanjutya yang ditemukan di layar pengguna.

Baris 152: Apabila gagal / found bernilai False.

Baris 153: Tampilkan konfirmasi pesan bahwa antrean tersebut memang tidak ada pesanan setelahnya.

Baris 154: Menangkap gagal input string di blok menu 4.

Baris 155: Tampilkan teks input tidak valid.

Baris 156: Cek apakah pengguna memilih menu 5.

Baris 157: Memulai pengamanan try input khusus menu ke-5.

Baris 158: Meminta angka antrean pesanan yang ingin dilacak nomor sebelumnya.

Baris 159: Memanggil fungsi find_predecessor dan mengisikan hasil 3 nilai balasannya ke ans, wer, found.

Baris 160: Jika pencarian statusnya True (berhasil ditemukannya angka sebelumnya).

Baris 161: Cetak konfirmasi nomor dan pesanan yang dicari ke layar.

Baris 162: Jika status pencarian berstatus gagal (False).

Baris 163: Cetak pesan error yang menyimpulkan antrean yang dicari paling pertama atau memang kosong.

Baris 164: Tangkap error masukan di menu ke-5 (misal user mengetik huruf 'A').

Baris 165: Cetak pesan bahwa masukan salah.

Baris 166: Mengecek opsi terakhir, jika pengguna menekan angka 6.

Baris 167: Cetak tulisan "Program selesai." dan perulangan while di baris 115 otomatis putus dengan sendirinya.

Baris 168: Baris pancingan ini (else) bekerja jika pengguna menginput angka tapi selain 1,2,3,4,5, dan 6.

Baris 169: Cetak peringatan "Pilihan tidak valid!" ke monitor.

Baris 170: (Baris kosong)

Baris 171: (Baris kosong)

Baris 172: Perintah untuk mengecek apakah script Python ini dieksekusi secara langsung.

Baris 173: Jika ya, jalankan fungsi main() untuk memanggil program keseluruhan.

## Output:
<img width="461" height="870" alt="image" src="https://github.com/user-attachments/assets/1ab38de5-fc17-4a2e-8820-6adf7fc137bc" />
<img width="551" height="804" alt="image" src="https://github.com/user-attachments/assets/ad5330e3-4dd8-496b-b072-d82509f15ad9" />
<img width="581" height="186" alt="image" src="https://github.com/user-attachments/assets/282f5f9e-8849-4b19-9535-38fa0ffb4345" />


### Youtube: https://youtu.be/BAZbJ1eb2Tg?si=wa343wn_5nkOIqJI
