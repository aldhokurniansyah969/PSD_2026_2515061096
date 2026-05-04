Tugas Akhir Percobaan 2

Nama : Aldho Kurniansyah

NPM : 2515061096

Judul Program : Program Pengurutan Judul Film Berdasarkan Abjad

Program ini digunakan untuk mengurutkan judul film berdasarkan abjad A–Z menggunakan algoritma Bubble Sort. Pengguna diminta memasukkan jumlah judul film, kemudian memasukkan setiap judul satu per satu. Data yang dimasukkan akan diproses dengan metode Bubble Sort, yaitu membandingkan dua judul yang berdekatan dan menukarnya. Proses ini dilakukan berulang hingga semua judul tersusun sesuai dengan alfabet. Setelah proses selesai, program akan menampilkan daftar judul film sebelum dan sesudah diurutkan.

<img width="1202" height="1736" alt="code" src="https://github.com/user-attachments/assets/56c4e176-57b4-4511-8813-988cdd3136f8" />

1.	Mendefinisikan fungsi bernama tukar yang digunakan untuk menukar posisi dua elemen dalam array berdasarkan index.
2.	Menyimpan sementara nilai elemen pada index i ke dalam variabel temp agar tidak hilang saat proses penukaran.
3.	Mengisi posisi index i dengan nilai dari index j.
4.	Mengisi posisi index j dengan nilai yang sebelumnya disimpan di temp, sehingga kedua elemen berhasil ditukar.
5.	
6.	
7.	Mendefinisikan fungsi bubble_sort yang bertugas mengurutkan isi array menggunakan metode Bubble Sort.
8.	Melakukan perulangan luar sebanyak n - 1 kali, karena dalam Bubble Sort maksimal diperlukan n-1 tahap untuk memastikan semua data terurut.
9.	Melakukan perulangan dalam untuk membandingkan elemen yang bersebelahan dari awal hingga bagian yang belum terurut.
10.	Membandingkan dua elemen bertipe string dengan mengubah keduanya ke huruf kecil (lower()), agar pengurutan tidak terpengaruh huruf besar/kecil.
11.	Memanggil fungsi tukar untuk menukar posisi kedua elemen agar urutan menjadi benar.
12.	
13.	
14.	Mendefinisikan fungsi main sebagai fungsi utama yang mengatur alur program dari awal sampai akhir.
15.	Memulai blok try untuk mengantisipasi kesalahan saat user memasukkan jumlah film.
16.	Meminta user memasukkan jumlah film yang akan diinput, lalu mengubahnya menjadi tipe data integer.
17.	Menangkap error ValueError jika user memasukkan input selain angka.
18.	Menampilkan pesan bahwa input tidak valid agar user tahu kesalahannya.
19.	Menghentikan program menggunakan return jika terjadi kesalahan input.
20.	
21.	Membuat list kosong bernama arr yang akan digunakan untuk menyimpan judul-judul film.
22.	
23.	Menampilkan pesan instruksi kepada user untuk mulai memasukkan judul film.
24.	Melakukan perulangan sebanyak jumlah film (n) agar semua judul bisa diinput.
25.	Meminta user memasukkan judul film satu per satu sesuai urutan.
26.	Menambahkan setiap judul yang diinput ke dalam list arr menggunakan method append().
27.	
28.	Menampilkan isi list arr sebelum dilakukan proses pengurutan, agar bisa dibandingkan dengan hasil setelah sorting.
29.	
30.	Memanggil fungsi bubble_sort dengan parameter array dan jumlah data untuk mengurutkan judul film.
31.	
32.	Menampilkan judul bahwa data berikut adalah hasil setelah diurutkan.
33.	Melakukan perulangan untuk menampilkan semua isi array yang sudah diurutkan.
34.	Menampilkan setiap judul film satu per satu sesuai urutan alfabet.
35.	
36.	
37.	Baris standar Python yang memastikan bahwa kode di dalam main() hanya dijalankan jika file ini dijalankan langsung, bukan di-import.
38.	Memanggil fungsi main() untuk menjalankan seluruh program dari awal.

Output:
<img width="1150" height="290" alt="Screenshot 2026-05-04 214309" src="https://github.com/user-attachments/assets/e38cb1bc-bb61-494a-84be-d0312eafd0b8" />

