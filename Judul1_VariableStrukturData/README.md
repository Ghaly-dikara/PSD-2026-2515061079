Sistem Pelayanan Pasien Rumah Sakit

Sistem ini merupakan sistem yang berjalan di python menggunakan algoritma LinkedList, dari algoritma tersebut saya gunakan class Node dan LinkedList itu sendiri.
Didalam Class Linked List menggunakan fungsi-fungsi untuk menambahkan pasien dari depan dan belakang, melayani pasien terdepan, dan menampilkan barisan pasien.
Setelah itu ada fungsi menu, menu pertama untuk mendaftarkan pasien dengan menginputkan nama. Yang kedua untuk melayani pasien terdepan.
yang ketiga untuk menampilkan antrean.
Dan yang terakhir adalah untuk menghentikan program.

Dan yang terakhir ada fungsi utama, yang berisikan sebagai berikut. Yang pertama akan memanggil Class Linkedlist menjadi ll, kedua menggunakan while True
selanjutnya akan memanggil fungsi menu dan akan meminta user untuk menginput angka yang akan memilih salah satu dari menu yang ditampilkan.
Menu yang pertama ada menambahkan pasien.
menu ini akan otomatis jalan karena perkondisian True yang dijalankan akan meminta user meninput nama pasien saat sistem dijalankan, 
dan menciptakan antrean baru (LinkedList). Setelah itu sistem akan meminta input apakah ingin ditaruh didepan atau belakang antrean.
Dan selanjutnya akan menanyakan kembali apakah mau menambahkan pasien lagi atau tidak. Jika Ya,
akan kembali menanyakan nama pasien, menambahkan nama pasien ke antrean, dan yang terakhir menanyakan kembali. 
Setelah itu menu selanjutnya adalah menu untuk melayani pasien, menu ini akan menampilkan pasien yang sudah didaftarkan dan akan melayani pasien terdepan.
Dan yang terakhir ada menu untuk menampilkan antrean pasien.

Source code:
<img width="454" height="502" alt="image" src="https://github.com/user-attachments/assets/a1f4a74c-eb2d-4718-9dc3-ec5bc532afa3" />
<img width="729" height="394" alt="image" src="https://github.com/user-attachments/assets/15792d1b-7acb-4de7-be1b-7e21d8856580" />
<img width="793" height="389" alt="image" src="https://github.com/user-attachments/assets/5587152a-5a49-404f-9d7b-3c2ca7ab31e0" />
<img width="740" height="551" alt="image" src="https://github.com/user-attachments/assets/f93a96ce-adfc-4080-acd6-2d984dc73e31" />
<img width="866" height="368" alt="image" src="https://github.com/user-attachments/assets/47addacb-d198-435e-8992-14096d6083d2" />
<img width="546" height="379" alt="image" src="https://github.com/user-attachments/assets/aca2b281-d360-4c83-8161-907ab42e19cd" />
Penjelasan :
\nBaris 1: Membuat Class Node, ibarat cetakan untuk membuat objek satu orang pasien.
\nBaris 2: Fungsi inisialisasi awal setiap kali ada pasien baru yang dibuat.
Baris 3: Menyimpan nama pasien ke dalam node tersebut.
Baris 4: Mengatur penunjuk (pointer) ke antrean pasien berikutnya menjadi kosong (None) karena dia belum punya orang di belakangnya.
Baris 5: (Baris kosong)
Baris 6: Membuat Class LinkedList, ini cetakan untuk sistem antrean utamanya.
Baris 7: Fungsi inisialisasi saat antrean pertama kali dibuka.
Baris 8: Menandai posisi paling depan (start) antrean masih kosong.
Baris 9: Menandai posisi paling belakang (rear) antrean juga masih kosong.
Baris 10: (Baris kosong)
Baris 11: Membuat fungsi untuk membungkus nama pasien baru ke dalam cetakan Node.
Baris 12: Memasukkan nama pasien (n) menjadi objek new_node.
Baris 13: Mengembalikan hasil objek pasien yang sudah siap masuk antrean.
Baris 14: (Baris kosong)
Baris 15: Fungsi untuk memasukkan pasien ke posisi paling depan (Jalur VIP).
Baris 16: Mengecek apakah antrean masih kosong.
Baris 17: Jika kosong, pasien VIP ini langsung jadi orang terdepan.
Baris 18: Dan otomatis dia juga jadi orang paling belakang (karena sendirian).
Baris 19: Tapi jika antrean sudah ada isinya:
Baris 20: Pasien VIP ini akan menunjuk ke orang yang tadinya ada di paling depan.
Baris 21: Posisi terdepan (start) resmi diganti jadi pasien VIP ini.
Baris 22: (Baris kosong)
Baris 23: Fungsi untuk memasukkan pasien ke posisi paling belakang (Jalur Reguler).
Baris 24: Mengecek apakah antrean masih kosong.
Baris 25: Jika kosong, dia jadi yang paling depan.
Baris 26: Sekaligus jadi yang paling belakang.
Baris 27: Tapi jika antrean sudah ada isinya:
Baris 28: Pasien yang tadinya paling belakang disuruh menunjuk ke pasien reguler baru ini.
Baris 29: Posisi paling belakang (rear) resmi digeser ke pasien reguler baru ini.
Baris 30: (Baris kosong)
Baris 31: Fungsi untuk mengeluarkan pasien dari antrean (pasien dipanggil/dilayani).
Baris 32: Mengecek apakah antreannya kosong.
Baris 33: Jika kosong, munculkan teks "Pasien kosong!".
Baris 34: Jika ada pasien di antrean:
Baris 35: Menyimpan nama pasien terdepan ke variabel deleted_data sebelum dihapus.
Baris 36: Menggeser posisi terdepan (start) ke pasien urutan kedua.
Baris 37: Memunculkan pesan bahwa pasien bernama tersebut sudah selesai dilayani.
Baris 38: Mengecek lagi, apakah setelah pasien itu maju, antrean jadi kosong melompong?
Baris 39: Jika iya, posisi belakang (rear) juga harus diubah jadi kosong (None).
Baris 40: (Baris kosong)
Baris 41: Fungsi untuk melihat/menampilkan daftar antrean saat ini.
Baris 42: Mengecek jika posisi depan kosong.
Baris 43: Jika kosong, cetak pesan "Antrean kosong".
Baris 44: Menghentikan fungsi tampilan ini (return) karena tak ada yang perlu dilihat.
Baris 45: Menyiapkan variabel current yang dimulai dari pasien terdepan.
Baris 46: Mencetak garis pembatas hiasan untuk layar antrean.
Baris 47: Melakukan perulangan selama masih ada pasien yang terdeteksi.
Baris 48: Mencetak nama pasien disambung tanda panah -> ke samping.
Baris 49: Menggeser variabel current untuk mengecek pasien di urutan selanjutnya.
Baris 50: Jika sudah habis, cetak teks "None" di ujung antrean.
Baris 51: (Baris kosong)
Baris 52: Fungsi untuk menampilkan menu program di layar.
Baris 53: Mencetak teks pertanyaan menu.
Baris 54: Opsi 1 untuk pendaftaran pasien.
Baris 55: Opsi 2 untuk melayani/memanggil pasien.
Baris 56: Opsi 3 untuk mengecek daftar antrean.
Baris 57: Opsi 4 untuk keluar dari program.
Baris 58: (Baris kosong)
Baris 59: Fungsi utama (main) tempat semua sistem berjalan.
Baris 60: Membuat saklar running = True agar program terus menyala.
Baris 61: Membuat sistem antrean baru menggunakan cetakan LinkedList, dinamai ll.
Baris 62: Melakukan perulangan utama selama running masih menyala (True).
Baris 63: Menampilkan teks menu ke layar.
Baris 64: Meminta pengguna mengetik angka pilihan menu (1-4).
Baris 65: Mengecek jika pengguna memilih angka 1.
Baris 66: Membuat saklar choice menjadi "y" untuk masuk ke mode pendaftaran.
Baris 67: Perulangan khusus pendaftaran selama input bernilai "y".
Baris 68: Meminta ketikan nama pasien baru.
Baris 69: Menampilkan ulang nama pasien yang barusan diketik.
Baris 70: Menampilkan info "Membuat antrean baru".
Baris 71: Memproses nama tersebut jadi objek Node siap antre.
Baris 72: Mengecek apakah pembuatan node pasien berhasil.
Baris 73: Jika sukses, tampilkan pesan berhasil.
Baris 74: Jika gagal:
Baris 75: Tampilkan pesan gagal.
Baris 76: Keluar paksa dari perulangan pendaftaran (break).
Baris 77: Menampilkan teks pilihan antrean VIP.
Baris 78: Menampilkan teks pilihan antrean Reguler.
Baris 79: Blok try untuk mencegah program error jika user iseng mengetik huruf, bukan angka.
Baris 80: Meminta pengguna memasukkan angka 1 (VIP) atau 2 (Reguler).
Baris 81: Menangkap error ValueError jika yang diketik memang bukan angka.
Baris 82: Jika error terjadi, jalur otomatis dipaksa jadi 1 (VIP).
Baris 83: Mengecek jika jalur 1 (VIP) yang terpilih.
Baris 84: Memasukkan pasien ke antrean terdepan (insert_at_beg).
Baris 85: Mencetak info bahwa dia masuk VIP.
Baris 86: Menampilkan ilustrasi antreannya (ll.display).
Baris 87: Mengecek alternatif jika jalur 2 (Reguler) yang terpilih.
Baris 88: Memasukkan pasien ke antrean belakang (insert_at_end).
Baris 89: Mencetak info bahwa dia masuk Reguler.
Baris 90: Menampilkan ilustrasi antreannya.
Baris 91: Jika angka yang dimasukkan bukan 1 atau 2:
Baris 92: Cetak pesan tidak valid, pasien otomatis dilempar ke jalur Reguler.
Baris 93: Memasukkan pasien ke antrean belakang.
Baris 94: Menampilkan ilustrasi antreannya.
Baris 95: Menanyakan "Mau membuat pendaftaran baru? (y/n)".
Baris 96: Mengecek jika input bukan huruf "y".
Baris 97: Cetak pesan bahwa input selain "y" akan dikembalikan ke menu utama.
Baris 98: continue untuk mengulang looping (jika bukan "y", looping baris 67 akan berhenti dan kembali ke menu).
Baris 99: (Baris kosong)
Baris 100: Mengecek jika di menu awal tadi pengguna memilih angka 2.
Baris 101: Mencetak teks "Daftar Antrean Saat Ini:".
Baris 102: Memperlihatkan dulu siapa saja yang ada di antrean.
Baris 103: Memanggil/melayani dan menghapus pasien yang paling depan (delete_node).
Baris 104: (Baris kosong)
Baris 105: Mengecek jika di menu awal pengguna memilih angka 3.
Baris 106: Memanggil fungsi untuk mencetak daftar antrean ke layar.
Baris 107: (Baris kosong)
Baris 108: Mengecek jika di menu awal pengguna memilih angka 4.
Baris 109: Mematikan saklar perulangan (running = False) agar program berhenti.
Baris 110: Mencetak ucapan terima kasih.
Baris 111: (Baris kosong)
Baris 112: Jika pengguna mengetik angka sembarangan (bukan 1-4) di menu utama:
Baris 113: Mencetak peringatan "Pilihan tidak valid!".
Baris 114: (Baris kosong)
Baris 115: Menjalankan fungsi main() agar seluruh logika dari atas hingga bawah mulai beroperasi.
Output :
<img width="504" height="790" alt="image" src="https://github.com/user-attachments/assets/9af03e19-1c4d-4b16-9ae8-291295218ec6" />
<img width="511" height="207" alt="image" src="https://github.com/user-attachments/assets/54171867-440d-4445-b255-202f85ba18bc" />
Youtube:
https://www.youtube.com/watch?v=WzYYh1PoCaY
