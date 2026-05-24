# Sistem Pesananan Restoran Serba Ada
Sistem ini merupakan simuali antrean pesanan menggunakan struktur data binary serch tree. Sistem menggunakan bahasa pemrograman python, yang berisikan class Node yang berisikan dua key, class BSTLanjut untuk struktur datanya. Dalam class BSTLanjut terdapat fungsi insert_node, insert, find_min_node, delete_node, delete, 

## Source Code:
<img width="660" height="689" alt="image" src="https://github.com/user-attachments/assets/fec2fe7e-7790-4bb0-985a-0a18f6627856" />
<img width="725" height="709" alt="image" src="https://github.com/user-attachments/assets/b6533da5-e1f2-4b4e-bcd3-311e534e70c4" />
<img width="612" height="777" alt="image" src="https://github.com/user-attachments/assets/0525cfac-918b-41f5-93d7-a33927eb3af2" />
<img width="567" height="529" alt="image" src="https://github.com/user-attachments/assets/7563f798-cf1b-4ba8-b2cb-1ab1f5e1b9a9" />
<img width="922" height="896" alt="image" src="https://github.com/user-attachments/assets/c228d85d-61de-41fe-bb4e-05b61893d5c3" />
<img width="1315" height="524" alt="image" src="https://github.com/user-attachments/assets/50a5e968-8faa-4d44-8d3d-8cf8b5169260" />


## Penjelasan:

Baris 1: Mendefinisikan class Node sebagai kerangka/elemen pembentuk pohon (tree).

Baris 2: Fungsi awal (konstruktor) yang otomatis jalan saat sebuah Node baru dibuat.

Baris 3: Menyimpan nomor antrean sebagai kunci pencarian utama (key).

Baris 4: Menyimpan nama menu pesanan sebagai data tambahan (key2).

Baris 5: Menyiapkan jalur/penunjuk ke anak sebelah kiri, awalnya dikosongkan.

Baris 6: Menyiapkan jalur/penunjuk ke anak sebelah kanan, awalnya dikosongkan.

Baris 7: (Baris kosong)

Baris 8: (Baris kosong)

Baris 9: Mendefinisikan class BSTLanjut (Binary Search Tree) khusus untuk mengatur logika antrean.

Baris 10: Fungsi awal saat sistem BST dibuat pertama kali.

Baris 11: Menetapkan akar (root) atau pusat dari pohon dengan kondisi awal kosong.

Baris 12: (Baris kosong)

Baris 13: Fungsi khusus yang bekerja berulang (rekursif) untuk memasukkan node baru ke posisi yang pas.

Baris 14: Jika posisi/cabang saat ini masih kosong...

Baris 15: ...buat dan letakkan node baru berisi antrean dan pesanan tersebut di sini.

Baris 16: Jika nomor antrean baru lebih kecil dari nomor di cabang saat ini...

Baris 17: ...geser pencarian untuk memasukkan pesanan ke cabang sebelah kiri.

Baris 18: Sebaliknya, jika nomor antrean baru lebih besar dari nomor saat ini...

Baris 19: ...geser pencarian untuk memasukkan pesanan ke cabang sebelah kanan.

Baris 20: Kembalikan struktur pohon yang sudah diperbarui dengan node baru.

Baris 21: (Baris kosong)

Baris 22: Fungsi utama penyisipan pesanan agar mudah dipanggil dari luar.

Baris 23: Memulai proses penyisipan pesanan mulai dari titik awal (akar/root) pohon.

Baris 24: (Baris kosong)

Baris 25: Fungsi untuk mencari pesanan dengan nomor antrean paling kecil di suatu cabang.

Baris 26: Jadikan posisi awal (root) sebagai titik mulai pencarian.

Baris 27: Selama masih ada node saat ini dan node di cabang sebelah kirinya...

Baris 28: ...terus bergeser ke cabang paling kiri karena angka terkecil ada di sana.

Baris 29: Kembalikan node yang berisi nomor paling kecil tersebut.

Baris 30: (Baris kosong)

Baris 31: Fungsi untuk mencari dan menghapus pesanan tertentu di dalam sistem pohon.

Baris 32: Jika pohonnya kosong (atau antrean tidak ditemukan)...

Baris 33: ...hentikan pencarian dan kembalikan penanda kosong (None).

Baris 34: Jika nomor yang ingin dihapus lebih kecil dari posisi saat ini...

Baris 35: ...cari dan hapus pesanan tersebut di bagian kiri pohon.

Baris 36: Jika nomor yang ingin dihapus lebih besar dari posisi saat ini...

Baris 37: ...cari dan hapus pesanan tersebut di bagian kanan pohon.

Baris 38: Jika akhirnya pesanan yang dicari cocok dengan posisi saat ini...

Baris 39: Cek jika pesanan ini ada di ujung (tidak punya cabang kiri dan kanan)...

Baris 40: ...langsung hapus (ubah menjadi kosong/None).

Baris 41: Jika pesanan ini hanya tidak punya cabang kiri (punya cabang kanan)...

Baris 42: ...timpa posisi saat ini dengan cabang kanannya.

Baris 43: Jika pesanan ini hanya tidak punya cabang kanan (punya cabang kiri)...

Baris 44: ...timpa posisi saat ini dengan cabang kirinya.

Baris 45: Jika pesanan ini punya anak di kedua cabang (kiri dan kanan)...

Baris 46: ...cari nilai terkecil di cabang kanan sebagai penggantinya (successor).

Baris 47: Ganti nomor antrean saat ini dengan nomor penggantinya.

Baris 48: Ganti nama menu pesanan saat ini dengan nama menu penggantinya.

Baris 49: Hapus node pengganti yang asli dari posisi asalnya di cabang sebelah kanan.

Baris 50: Kembalikan struktur cabang yang baru setelah penghapusan selesai.

Baris 51: (Baris kosong)

Baris 52: Fungsi utama penghapusan pesanan agar mudah dipanggil dari luar.

Baris 53: Memulai proses pencarian dan penghapusan mulai dari titik akar (root).

Baris 54: (Baris kosong)

Baris 55: Fungsi untuk menampilkan daftar seluruh pesanan tingkat demi tingkat dari atas ke bawah.

Baris 56: Cek, jika akar pohon kosong sama sekali...

Baris 57: ...tampilkan teks bahwa "Tidak ada pesanan".

Baris 58: Hentikan fungsi karena tidak ada yang perlu ditampilkan.

Baris 59: Siapkan antrean buatan (queue) berupa daftar kosong untuk membantu proses cetak.

Baris 60: Masukkan pesanan utama (root) ke dalam antrean buatan.

Baris 61: Selama antrean buatan masih ada isinya...

Baris 62: ...ambil dan keluarkan pesanan urutan paling depan.

Baris 63: Cetak nomor antrean dan nama menunya ke layar.

Baris 64: Jika pesanan tersebut punya cabang kiri...

Baris 65: ...tambahkan cabang kirinya ke antrean buatan untuk dicetak nanti.

Baris 66: Jika pesanan tersebut punya cabang kanan...

Baris 67: ...tambahkan cabang kanannya ke antrean buatan untuk dicetak nanti.

Baris 68: Cetak satu baris kosong (enter) sebagai pembatas (agar lebih rapi).

Baris 69: (Baris kosong)

Baris 70: Fungsi mencari pesanan yang urutannya berada tepat setelah suatu nomor (successor).

Baris 71: Mulai pencarian dari akar pohon.

Baris 72: Siapkan variabel successor dengan nilai kosong sementara.

Baris 73: Lakukan pencarian selama posisi node saat ini masih ada (belum ujung)...

Baris 74: Jika nomor referensi lebih kecil dari posisi node saat ini...

Baris 75: ...catat node ini karena kemungkinan ini adalah pesanan tepat setelahnya.

Baris 76: ...dan lanjutkan pencarian ke sebelah kiri agar mencari selisih paling dekat.

Baris 77: Jika nomor referensi lebih besar dari posisi saat ini...

Baris 78: ...langsung cari saja ke sebelah kanan (tidak perlu mencatat).

Baris 79: Jika angkanya sama persis dengan yang dicari...

Baris 80: ...hentikan perulangan.

Baris 81: Jika setelah mencari ke ujung pohon target tetap tidak ditemukan...

Baris 82: ...kembalikan indikasi gagal (kosong dan False).

Baris 83: Jika node yang dicari tadi ketemu dan dia punya cabang kanan...

Baris 84: ...maka pesanan yang tepat setelahnya pasti adalah nilai paling kecil di cabang kanan itu.

Baris 85: Jika sama sekali tidak ditemukan ada node successor...

Baris 86: ...kembalikan indikasi gagal (kosong dan False).

Baris 87: Kembalikan nomor antrean, nama menu selanjutnya, dan indikator sukses (True).

Baris 88: (Baris kosong)

Baris 89: Fungsi mencari pesanan yang urutannya berada tepat sebelum suatu nomor (predecessor).

Baris 90: Mulai pencarian dari akar pohon.

Baris 91: Siapkan variabel predecessor dengan nilai kosong.

Baris 92: Lakukan perulangan selama masih ada pesanan yang dicek...

Baris 93: Jika nomor yang direferensikan lebih besar dari pesanan saat ini...

Baris 94: ...catat pesanan ini sebagai calon kuat sebelumnya,

Baris 95: ...dan lanjutkan mencari ke cabang kanan.

Baris 96: Jika nomor lebih kecil dari pesanan saat ini...

Baris 97: ...cukup lompati dan lanjut cek cabang kiri.

Baris 98: Jika angkanya pas sama dengan yang dicari...

Baris 99: ...hentikan perulangan.

Baris 100: Jika nomor tadi dicari hingga ujung tidak ketemu...

Baris 101: ...kembalikan indikasi bahwa data tidak ada (False).

Baris 102: Jika node ketemu dan ia memiliki cabang anak sebelah kiri...

Baris 103: ...pindah ke anak cabang sebelah kiri,

Baris 104: ...lalu telusuri terus sampai menyentuh anak bagian paling kanan,

Baris 105: ...geser terus sampai mentok kanan.

Baris 106: Node paling kanan ini adalah pesanan pendahulu sebenarnya.

Baris 107: Jika setelah diproses pun predecessor masih kosong...

Baris 108: ...kembalikan tanda tidak ada pesanan sebelumnya (False).

Baris 109: Kembalikan nomor antrean, nama menu sebelumnya, beserta tanda sukses (True).

Baris 110: (Baris kosong)

Baris 111: (Baris kosong)

Baris 112: Mendefinisikan program utama main tempat aplikasi dijalankan berinteraksi dengan manusia.

Baris 113: Membuat sistem pesan (objek) baru dari class BSTLanjut bernama bst.

Baris 114: Memberi nilai awal 0 untuk variabel pemilih menu.

Baris 115: Membuat perulangan tiada henti, aplikasi tetap jalan asalkan pengguna tidak memilih opsi angka 6.

Baris 116: Mencetak header/judul aplikasi ke layar.

Baris 117: Menampilkan pilihan pertama (Tambah Pesanan).

Baris 118: Menampilkan pilihan kedua (Pesanan Selesai).

Baris 119: Menampilkan pilihan ketiga (Lihat Semua Antrean).

Baris 120: Menampilkan pilihan keempat (Cek Berikutnya).

Baris 121: Menampilkan pilihan kelima (Cek Sebelumnya).

Baris 122: Menampilkan pilihan keenam (Keluar).

Baris 123: Membuka penanganan error try-except (agar jika salah ketik, aplikasi tidak langsung mati).

Baris 124: Meminta pengguna memasukkan angka pilihan dan menyimpannya di variabel pilih.

Baris 125: Menangkap error kalau pengguna memasukkan teks huruf alih-alih angka.

Baris 126: Memberikan notifikasi "Input tidak valid!".

Baris 127: Melewati siklus ini dan langsung kembali menampilkan daftar menu (lanjut ke atas loop).

Baris 128: Jika angka yang dipilih adalah 1...

Baris 129: Buka penanganan error khusus untuk fitur tambah pesanan.

Baris 130: Meminta nomor antrean (harus angka murni).

Baris 131: Meminta nama menu pesanan (boleh teks).

Baris 132: Simpan ke dalam sistem struktur pohon dengan memanggil fungsi insert.

Baris 133: Tampilkan konfirmasi bahwa pesanan sudah masuk.

Baris 134: Tangkap error jika pengguna mengetik huruf di isian nomor antrean.

Baris 135: Peringatkan bahwa antrean harus berupa angka (bulat).

Baris 136: Jika yang dipilih angka 2...

Baris 137: Buka blok pelindung error untuk fitur penyelesaian pesanan.

Baris 138: Minta nomor antrean berapa yang baru saja selesai disajikan (wajib angka).

Baris 139: Hapus nomor antrean tersebut dari sistem melalui pemanggilan fungsi delete.

Baris 140: Tampilkan info bahwa antrean nomor sekian telah diserahkan dan dihapus.

Baris 141: Tangkap pesan error kalau dimasukkan abjad, bukan angka.

Baris 142: Beri tahu bahwa inputan keliru.

Baris 143: Jika opsi yang dipilih angka 3...

Baris 144: Beri tulisan awalan (header) untuk daftar pesan yang sedang antre.

Baris 145: Panggil fungsi level_order untuk mencetak struktur antrean dari atas ke bawah.

Baris 146: Jika opsi yang dipilih angka 4...

Baris 147: Buka keamanan blok penanganan error.

Baris 148: Minta titik fokus pencarian: siapa yang berada setelah nomor berapa?

Baris 149: Cari ke dalam pohon sistem melalui fungsi find_successor.

Baris 150: Jika pesanan setelahnya berhasil diidentifikasi...

Baris 151: ...Cetak nomor dan menu yang harus disiapkan.

Baris 152: Jika urutan setelahnya kosong...

Baris 153: ...Sampaikan bahwa tidak ada pesanan lagi atau nomor tersebut adalah pesanan terakhir.

Baris 154: Tangkap error tipe data semisal huruf dimasukkan di isian angka.

Baris 155: Beri pemberitahuan bahwa yang ditekan bukan angka.

Baris 156: Jika yang dipilih angka 5...

Baris 157: Blok pengaman (try-except) untuk proses pencarian ini.

Baris 158: Tanya pengguna mencari data pesanan sebelum antrean nomor berapa.

Baris 159: Lacak dalam antrean lewat fungsi find_predecessor.

Baris 160: Cek apakah ketemu atau tidak (parameter found bernilai True/False).

Baris 161: Bila ketemu, tunjukkan rincian pesanan tersebut.

Baris 162: Apabila tidak ditemukan...

Baris 163: ...Beri kabar bahwa itu adalah daftar pertama, tidak ada yang mendahului, atau nomornya salah.

Baris 164: Antisipasi crash jika mengetik abjad.

Baris 165: Tolak input selain angka.

Baris 166: Kalau pengguna mengetik angka 6 dari menu awal...

Baris 167: ...tampilkan perpisahan, "Program selesai."

Baris 168: Dan kalau mereka memasukkan angka asal (misal 9 atau 100)...

Baris 169: ...sampaikan keterangan bahwa pilihannya di luar nalar.

Baris 170: (Baris kosong)

Baris 171: (Baris kosong)

Baris 172: Memeriksa apakah file Python ini dijalankan langsung sebagai program utama atau cuma file numpang import dari file lain.

Baris 173: Jika benar, segera jalankan main() (memunculkan menu pertama kalinya).

## Output:
<img width="461" height="870" alt="image" src="https://github.com/user-attachments/assets/1ab38de5-fc17-4a2e-8820-6adf7fc137bc" />
<img width="551" height="804" alt="image" src="https://github.com/user-attachments/assets/ad5330e3-4dd8-496b-b072-d82509f15ad9" />
<img width="581" height="186" alt="image" src="https://github.com/user-attachments/assets/282f5f9e-8849-4b19-9535-38fa0ffb4345" />


### Youtube:
