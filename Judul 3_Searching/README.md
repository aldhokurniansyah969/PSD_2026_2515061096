Tugas Akhir Percobaan 3

Nama : Aldho Kurniansyah

NPM : 2515061096

Judul Program : Program Pencarian Buku

<img width="1416" height="4396" alt="code123" src="https://github.com/user-attachments/assets/8e41be7e-e96c-417c-b46a-480475a7ba8a" />

1.	Mendefinisikan fungsi pencarian biner yang mencari kecocokan parsial dari string target dalam daftar buku yang sudah terurut.
2.	
3.	Menginisialisasi penunjuk kiri (left pointer) ke awal daftar.
4.	
5.	Menginisialisasi penunjuk kanan (right pointer) ke indeks terakhir daftar.
6.	
7.	Membuat daftar kosong untuk menyimpan hasil pencarian.
8.	
9.	Memulai loop (perulangan) yang berlanjut selama penunjuk kiri kurang dari atau sama dengan penunjuk kanan.
10.	
11.	Menghitung indeks tengah menggunakan pembagian integer untuk menghindari overflow.
12.	
13.	Mencetak posisi tengah yang sedang diperiksa saat ini.
14.	
15.	Mencetak judul buku pada posisi tengah tersebut.
16.	
17.	Memeriksa apakah string target (yang diubah ke huruf kecil) terkandung dalam judul buku di posisi tengah (yang juga diubah ke huruf kecil).
18.	
19.	Menambahkan buku yang cocok ke dalam daftar hasil.
20.	
21.	Menginisialisasi penunjuk untuk mencari kecocokan di sebelah kiri dari posisi tengah.
22.	
23.	Memulai loop untuk mencari ke arah kiri dari posisi tengah hingga mencapai awal daftar.
24.	
25.	Memeriksa apakah target terkandung dalam judul buku saat ini di sebelah kiri.
26.	
27.	Menambahkan buku yang cocok ke dalam daftar hasil.
28.	
29.	Menggeser penunjuk satu posisi ke arah kiri.
30.	
31.	Menginisialisasi penunjuk untuk mencari kecocokan di sebelah kanan dari posisi tengah.
32.	
33.	Memulai loop untuk mencari ke arah kanan dari posisi tengah hingga mencapai akhir daftar.
34.	
35.	Memeriksa apakah target terkandung dalam judul buku saat ini di sebelah kanan.
36.	
37.	Menambahkan buku yang cocok ke dalam daftar hasil.
38.	
39.	Menggeser penunjuk satu posisi ke arah kanan.
40.	
41.	Keluar dari loop pencarian biner setelah menemukan semua buku yang cocok.
42.	
43.	Memeriksa apakah judul buku di posisi tengah muncul sebelum target secara alfabetis.
44.	
45.	Mencetak pesan yang menunjukkan bahwa pencarian akan dilanjutkan ke sisi kanan.
46.	
47.	Menggeser penunjuk kiri ke posisi tengah ditambah satu untuk mencari di belahan kanan.
48.	
49.	Menangani kasus di mana judul buku di posisi tengah muncul setelah target secara alfabetis.
50.	
51.	Mencetak pesan yang menunjukkan bahwa pencarian akan dilanjutkan ke sisi kiri.
52.	
53.	Menggeser penunjuk kanan ke posisi tengah dikurangi satu untuk mencari di belahan kiri.
54.	
55.	Mengembalikan (return) daftar buku yang cocok dengan target pencarian.
56.	
57.	Mendefinisikan fungsi untuk menampilkan semua buku di dalam daftar.
58.	
59.	Mencetak header (judul) untuk daftar buku.
60.	
61.	Melakukan loop pada setiap buku dalam daftar menggunakan indeksnya.
62.	
63.	Mencetak setiap buku dengan indeks bernomor yang dimulai dari angka 1.
64.	
65.	Mendefinisikan fungsi utama (main function) yang menjalankan program.
66.	
67.	Membuat daftar berisi 16 judul buku Indonesia.
68.	
69.	Menyimpan jumlah total buku yang ada di dalam daftar.
70.	
71.	Memulai loop tak terbatas (infinite loop) agar menu tetap berjalan sampai pengguna keluar.
72.	
73.	Mencetak header menu.
74.	
75.	Mencetak opsi menu pertama untuk menampilkan daftar buku.
76.	
77.	Mencetak opsi menu kedua untuk mencari buku.
78.	
79.	Mencetak opsi menu keluar.
80.	
81.	Meminta pengguna untuk memasukkan pilihan menu dalam bentuk string.
82.	
83.	Memeriksa apakah pengguna memilih opsi 1 untuk menampilkan daftar buku.
84.	
85.	Memanggil fungsi untuk menampilkan semua buku.
86.	
87.	Memeriksa apakah pengguna memilih opsi 2 untuk mencari buku.
88.	
89.	Meminta pengguna memasukkan judul buku yang ingin dicari.
90.	
91.	Memanggil fungsi pencarian biner untuk menemukan buku yang cocok dengan judul target.
92.	
93.	Memeriksa apakah ada buku yang ditemukan dalam pencarian tersebut.
94.	
95.	Mencetak header hasil pencarian.
96.	
97.	Melakukan loop pada setiap buku yang ditemukan menggunakan indeksnya.
98.	
99.	Mencetak setiap buku yang ditemukan dengan indeks bernomor mulai dari 1.
100.	
101.	Menangani kasus di mana tidak ada buku yang ditemukan yang cocok dengan pencarian.
102.	
103.	Mencetak pesan yang menyatakan bahwa buku tidak ditemukan.
104.	
105.	Memeriksa apakah pengguna memilih opsi 3 untuk keluar dari program.
106.	
107.	Mencetak pesan bahwa program akan berakhir.
108.	
109.	Keluar dari loop menu dan menghentikan program.
110.	
111.	Menangani pilihan menu yang tidak valid (selain 1, 2, atau 3).
112.	
113.	Mencetak pesan bahwa pilihan tersebut tidak valid.
114.	
115.	Memeriksa apakah skrip sedang dijalankan secara langsung (bukan diimpor sebagai modul).
116.	
117.	Memanggil fungsi utama untuk memulai program.

Output:
<img width="232" height="590" alt="Screenshot 2026-05-11 221201" src="https://github.com/user-attachments/assets/8a01d3e0-478b-4ce7-8aaf-be04d42b84e7" />
<img width="492" height="713" alt="Screenshot 2026-05-11 221237" src="https://github.com/user-attachments/assets/c5a45b66-e130-42e0-bcc9-b8a480e18b3c" />
<img width="257" height="204" alt="Screenshot 2026-05-11 221259" src="https://github.com/user-attachments/assets/b436eecc-4ed3-4379-ad0f-d17143a9183c" />

Link:
