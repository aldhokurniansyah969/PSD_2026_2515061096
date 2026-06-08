Tugas Akhir Percobaan 6 : Hash Map

Judul Proyek : Sistem Parkir Digital

Sistem Parkir Digital ini merupakan implementasi struktur data Hash Map dengan metode Separate Chaining untuk mengelola data kendaraan yang berada di area parkir. Sistem menyimpan nomor parkir sebagai key dan informasi kendaraan sebagai value. Melalui sistem ini, pengguna dapat menambahkan data kendaraan yang masuk ke area parkir, mencari data kendaraan berdasarkan nomor parkir, menghapus data kendaraan yang telah keluar, serta menampilkan seluruh kendaraan yang masih terdaftar di area parkir. Penggunaan Hash Map membuat proses pengelolaan data menjadi lebih cepat dan efisien karena data dapat diakses melalui indeks yang dihasilkan oleh fungsi hash.

Metode Separate Chaining digunakan untuk mengatasi collision atau tabrakan data yang terjadi ketika beberapa key menghasilkan indeks hash yang sama. Pada metode ini, setiap slot dalam Hash Table dapat menyimpan lebih dari satu data menggunakan struktur linked list. Ketika collision terjadi, data baru akan ditambahkan ke linked list pada slot yang sama tanpa menghapus data yang sudah ada. Dengan demikian, seluruh data kendaraan tetap tersimpan dengan baik dan dapat dicari maupun dihapus dengan mudah. Implementasi metode ini membuat sistem lebih andal dalam menangani banyak data kendaraan secara terorganisir dan efisien.

Source Code :

<img width="1448" height="3560" alt="bad" src="https://github.com/user-attachments/assets/639467d3-6818-4598-b28b-7efe10f32a57" />

1.	Mendefinisikan class Node. 
2.	Mendefinisikan constructor pada class Node. 
3.	Menyimpan nilai key ke dalam atribut objek. 
4.	Menyimpan nilai value ke dalam atribut objek. 
5.	Menginisialisasi pointer next dengan nilai None. 
6.	(kosong) 
7.	Mendefinisikan class HashMapSeparateChaining. 
8.	Mendefinisikan constructor pada class HashMap. 
9.	Menyimpan ukuran Hash Table. 
10.	Membuat array Hash Table sesuai ukuran yang ditentukan. 
11.	(kosong) 
12.	Mendefinisikan fungsi hash. 
13.	Mengembalikan hasil perhitungan indeks hash. 
14.	(kosong) 
15.	Mendefinisikan fungsi insert. 
16.	Menghitung indeks penyimpanan berdasarkan key. 
17.	Mengambil data pertama pada indeks tersebut. 
18.	Melakukan perulangan selama node masih ada. 
19.	Memeriksa apakah key sudah tersimpan. 
20.	Memperbarui value jika key ditemukan. 
21.	Menghentikan proses insert. 
22.	Berpindah ke node berikutnya. 
23.	Membuat node baru. 
24.	Menghubungkan node baru dengan node lama pada slot yang sama. 
25.	Menjadikan node baru sebagai node pertama. 
26.	(kosong) 
27.	Mendefinisikan fungsi search. 
28.	Menghitung indeks pencarian. 
29.	Mengambil node pertama pada slot tersebut. 
30.	Melakukan penelusuran linked list. 
31.	Memeriksa apakah key ditemukan. 
32.	Mengembalikan node yang ditemukan. 
33.	Berpindah ke node berikutnya. 
34.	Mengembalikan None jika data tidak ditemukan. 
35.	(kosong) 
36.	Mendefinisikan fungsi remove_key. 
37.	Menghitung indeks penghapusan. 
38.	Mengambil node pertama pada slot tersebut. 
39.	Membuat variabel untuk menyimpan node sebelumnya. 
40.	Menelusuri linked list. 
41.	Memeriksa apakah key yang dicari ditemukan. 
42.	Memeriksa apakah node yang akan dihapus berada di awal linked list. 
43.	Menghapus node pertama dengan menggeser pointer. 
44.	Menjalankan kondisi jika node yang dihapus bukan node pertama. 
45.	Menghubungkan node sebelumnya dengan node setelah node yang dihapus. 
46.	Mengembalikan nilai True sebagai tanda berhasil. 
47.	Memperbarui posisi node sebelumnya. 
48.	Berpindah ke node berikutnya. 
49.	(kosong) 
50.	Mengembalikan nilai False jika data tidak ditemukan. 
51.	(kosong) 
52.	Mendefinisikan fungsi display. 
53.	Menampilkan judul data kendaraan. 
54.	Melakukan perulangan untuk seluruh slot Hash Table. 
55.	Menampilkan nomor slot. 
56.	Mengambil node pertama pada slot tersebut. 
57.	Menelusuri linked list pada slot tersebut. 
58.	Menampilkan key dan value setiap node. 
59.	Berpindah ke node berikutnya. 
60.	(kosong) 
61.	Menampilkan NULL sebagai penanda akhir linked list. 
62.	(kosong) 
63.	Mendefinisikan fungsi utama program. 
64.	Membuat objek HashMapSeparateChaining. 
65.	(kosong) 
66.	Menampilkan judul program Sistem Parkir Digital. 
67.	Menambahkan data kendaraan Honda Beat. 
68.	Menambahkan data kendaraan Yamaha NMAX. 
69.	Menambahkan data kendaraan Toyota Avanza. 
70.	Menambahkan data kendaraan Honda Brio. 
71.	Menampilkan pesan kendaraan berhasil masuk. 
72.	Menampilkan seluruh data kendaraan yang tersimpan. 
73.	(kosong) 
74.	Mencari kendaraan dengan key 1011. 
75.	Memeriksa apakah kendaraan ditemukan. 
76.	Menampilkan data kendaraan yang ditemukan. 
77.	Menjalankan blok else jika kendaraan tidak ditemukan. 
78.	Menampilkan pesan kendaraan tidak ditemukan. 
79.	(kosong) 
80.	Menghapus kendaraan dengan key 1011. 
81.	Menampilkan informasi bahwa kendaraan keluar dari area parkir. 
82.	Menampilkan judul data parkir setelah penghapusan. 
83.	Menampilkan kembali seluruh data kendaraan. 
84.	(kosong) 
85.	Memeriksa apakah file dijalankan secara langsung. 
86.	Menjalankan fungsi main().

Ouput :

<img width="876" height="564" alt="Screenshot 2026-06-08 224520" src="https://github.com/user-attachments/assets/7fb644fb-02b4-4b41-ac52-f2892b3d93bd" />

Link : https://youtu.be/gKzBYLztx4Y
