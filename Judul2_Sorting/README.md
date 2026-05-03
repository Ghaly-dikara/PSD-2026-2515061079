# Sistem Pengurutan Nilai Mahasiswa menggunakan Selection Sort
Sistem ini merupakan sistem yang berjalan di python dengan menggunakan Selection Sort untuk mengelola data nilai mahasiswa yang telah diinputkan. yang pertama dalam program ini berisikan fungsi untuk menukar nilai dari variabel temp yang dibuat untuk menyimpan nilai dari array ber indeks i dan array dengan indeks i akan menyimpan nilai dari array berindeks j, dan array berindeks j yang akan menyimpan nilai dari variabel temp. fungsi dibuat untuk menukar nilai yang digunakan dalam fungsi selection sort. Selanjutnya ada fungsi selection sort yang berisi perulangan untuk indeks i yang dimulai dari 

# Source Code:
<img width="365" height="592" alt="image" src="https://github.com/user-attachments/assets/e8dede21-db83-4fd0-98b5-71dd107c21a8" />
<img width="778" height="530" alt="image" src="https://github.com/user-attachments/assets/d1808c41-70be-4115-acc1-1f373ff633f9" />
<img width="531" height="156" alt="image" src="https://github.com/user-attachments/assets/e14f92f2-f501-4fad-b563-2c49e41d067b" />

# Penjelasan:

Baris 1: Membuat fungsi bernama tukar menggunakan atribut arr, i, j.

Baris 2: Menyimpan nilai arr[i] ke dalam variabel sementara temp.

Baris 3: Mengisi arr[i] dengan nilai dari arr[j].

Baris 4: Mengisi arr[j] dengan nilai dari temp untuk menyelesaikan pertukaran.

Baris 5: Baris kosong.

Baris 6: Membuat fungsi bernama selection_sort menggunakan atribut arr dan n.

Baris 7: Melakukan perulangan i dari 0 hingga sebelum elemen terakhir (n - 1).

Baris 8: Menetapkan posisi nilai minimum sementara (pos) pada indeks i.

Baris 9: Melakukan perulangan j untuk memeriksa sisa elemen dari i + 1 hingga n.

Baris 10: Memeriksa apakah nilai arr[j] lebih kecil dari nilai arr[pos].

Baris 11: Jika lebih kecil, ubah pos menjadi j sebagai penanda posisi minimum baru.

Baris 12: Memeriksa apakah nilai pos sudah berubah (tidak sama dengan asumsi awal i).

Baris 13: Jika berubah, panggil fungsi tukar untuk menukar elemen pada indeks i dan pos.

Baris 14: Baris kosong.

Baris 15: Membuat fungsi bernama klasifikasi_nilai menggunakan atribut nilai.

Baris 16: Memeriksa apakah nilai lebih besar atau sama dengan 76.

Baris 17: Jika ya, kembalikan huruf 'A'.

Baris 18: Memeriksa apakah nilai lebih besar atau sama dengan 66.

Baris 19: Jika ya, kembalikan huruf 'B'.

Baris 20: Memeriksa apakah nilai lebih besar atau sama dengan 56.

Baris 21: Jika ya, kembalikan huruf 'C'.

Baris 22: Memeriksa apakah nilai lebih besar atau sama dengan 50.

Baris 23: Jika ya, kembalikan huruf 'D'.

Baris 24: Kondisi apabila nilai tidak memenuhi semua persyaratan di atas (kurang dari 50).

Baris 25: Kembalikan huruf 'E'.

Baris 26: Baris kosong.

Baris 27: Membuat fungsi utama bernama main.

Baris 28: Membuka blok try untuk menangani kemungkinan error saat pengguna menginput data.

Baris 29: Meminta pengguna memasukkan jumlah nilai, mengubahnya ke format integer (int), dan menyimpannya di variabel n.

Baris 30: Menangkap error ValueError jika pengguna mengetik huruf alih-alih angka.

Baris 31: Mencetak pesan "Input tidak valid!".

Baris 32: Keluar dari fungsi main (program berhenti bekerja).

Baris 33: Membuat variabel arr berisi list (array) kosong.

Baris 34: Mencetak tulisan "Masukkan nilai-nilai mahasiswa:" ke layar.

Baris 35: Melakukan perulangan i sebanyak n kali sesuai jumlah mahasiswa.

Baris 36: Memulai perulangan tanpa henti (while True) untuk memaksa input benar.

Baris 37: Membuka blok try untuk menangani error penginputan nilai satu per satu.

Baris 38: Meminta pengguna memasukkan nilai, mengubahnya ke integer, lalu disimpan di nilai.

Baris 39: Memasukkan nilai tersebut ke dalam list arr.

Baris 40: Keluar dari perulangan while karena input angka sudah benar.

Baris 41: Menangkap error ValueError jika input bukan angka.

Baris 42: Mencetak peringatan "Input tidak valid, silakan masukkan angka!".

Baris 43: Menghitung dan mencetak rata-rata dengan membagi total isi array (sum) dengan jumlah elemennya (len).

Baris 44: Mencetak isi array arr sebelum diurutkan.

Baris 45: Memanggil fungsi selection_sort untuk mengurutkan arr.

Baris 46: Mencetak teks "Nilai setelah diurutkan (Selection Sort):" tanpa pindah ke baris baru.

Baris 47: Melakukan perulangan i sebanyak n kali.

Baris 48: Mencetak elemen arr[i] yang sudah berurutan secara mendatar.

Baris 49: Mencetak baris kosong atau enter baru.

Baris 50: Mencetak teks "Klasifikasi nilai (setelah diurutkan):".

Baris 51: Melakukan perulangan i sebanyak n kali.

Baris 52: Memanggil fungsi klasifikasi_nilai terhadap arr[i] lalu menyimpannya di variabel nilai.

Baris 53: Mencetak nilai angka beserta hasil huruf mutu (nilai) mahasiswa tersebut.

Baris 54: Baris kosong.

Baris 55: Memeriksa apakah file script ini dijalankan secara langsung sebagai program utama.

Baris 56: Memanggil fungsi main() untuk mulai menjalankan seluruh alur program.

# Output:
<img width="462" height="180" alt="image" src="https://github.com/user-attachments/assets/3a57fb1d-0270-4c29-bb7a-b183ccf06805" />
<img width="317" height="106" alt="image" src="https://github.com/user-attachments/assets/751b1c48-068d-469d-bdc6-cccb887e654b" />
