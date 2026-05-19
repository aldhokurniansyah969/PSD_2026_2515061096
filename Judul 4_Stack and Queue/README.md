Tugas Akhir Percobaan 4

Nama : Aldho Kurniansyah

NPM : 2515061096

Judul Program : Program Playlist Film

<img width="1588" height="3978" alt="TA JUDUL 4 PSD" src="https://github.com/user-attachments/assets/921fad1d-8d67-477f-b59f-5d17d6315054" />

Mendefinisikan class QueueArray sebagai implementasi struktur data Queue menggunakan array.

Mendefinisikan method constructor init yang akan dijalankan saat objek dibuat.

Parameter max_size=100 menentukan ukuran maksimum queue, default bernilai 100.

Menyimpan ukuran maksimum queue ke variabel self.MAXN.

Membuat list/array q berisi None sebanyak ukuran maksimum queue.

Menginisialisasi indeks depan (front_idx) dengan -1 sebagai tanda queue kosong.

Menginisialisasi indeks belakang (rear_idx) dengan -1 sebagai tanda queue kosong.

Mendefinisikan method is_empty untuk mengecek apakah queue kosong.

Mengembalikan nilai True jika front_idx == -1, berarti queue kosong.

Mendefinisikan method is_full untuk mengecek apakah queue penuh.

Mengecek apakah posisi belakang berikutnya sama dengan posisi depan menggunakan circular queue.

Mendefinisikan method enqueue untuk menambahkan data ke queue.

Mengecek apakah queue penuh dengan memanggil is_full().

Jika queue penuh, tampilkan pesan "Playlist penuh".

Menghentikan proses penambahan data menggunakan return.

Mengecek apakah queue kosong dengan memanggil is_empty().

Jika queue kosong, indeks depan diatur menjadi 0.

Jika queue kosong, indeks belakang juga diatur menjadi 0.

Jika queue tidak kosong, masuk ke blok else.

Memindahkan indeks belakang satu langkah maju menggunakan konsep circular queue.

Menyimpan data x pada posisi indeks belakang queue.

Menampilkan pesan bahwa film berhasil dimasukkan.

Mendefinisikan method dequeue untuk menghapus atau memutar film dari queue.

Mengecek apakah queue kosong.

Jika queue kosong, tampilkan pesan "Playlist kosong".

Menghentikan proses dequeue menggunakan return.

Menampilkan film yang berada di posisi depan queue.

Mengecek apakah queue hanya memiliki satu elemen.

Jika hanya satu elemen, indeks depan direset menjadi -1.

Indeks belakang juga direset menjadi -1.

Jika elemen lebih dari satu, masuk ke blok else.

Memindahkan indeks depan satu langkah maju menggunakan circular queue.

Mendefinisikan method peek untuk melihat elemen paling depan tanpa menghapusnya.

Mengecek apakah queue kosong.

Jika queue kosong, tampilkan pesan "Playlist kosong".

Menghentikan proses menggunakan return.

Menampilkan film yang berada di posisi depan queue.

Mendefinisikan method display untuk menampilkan seluruh isi queue.

Mengecek apakah queue kosong.

Jika queue kosong, tampilkan pesan "Playlist kosong".

Menghentikan proses menggunakan return.

Menampilkan teks judul isi playlist.

Menginisialisasi variabel i dengan posisi indeks depan queue.

Memulai perulangan tak terbatas menggunakan while True.

Menampilkan elemen queue pada indeks i.

Mengecek apakah indeks saat ini sama dengan indeks belakang.

Jika sama, perulangan dihentikan menggunakan break.

Memindahkan indeks i satu langkah maju secara circular.

Mencetak baris baru setelah semua isi queue ditampilkan.

Mendefinisikan method clearall untuk mengosongkan queue.

Mengatur indeks depan menjadi -1 untuk menandakan queue kosong.

Mengatur indeks belakang menjadi -1.

Menampilkan pesan bahwa playlist berhasil dikosongkan.

Mendefinisikan fungsi main sebagai program utama.

Membuat objek queue dari class QueueArray.

Menginisialisasi variabel pilih dengan nilai 0.

Memulai perulangan selama pilih tidak sama dengan 5.

Menampilkan judul menu program.

Menampilkan menu pilihan nomor 1.

Menampilkan menu pilihan nomor 2.

Menampilkan menu pilihan nomor 3.

Menampilkan menu pilihan nomor 4.

Menampilkan menu pilihan nomor 5.

Menampilkan menu pilihan nomor 6.

Memulai blok try untuk menangani error input.

Meminta input pilihan menu dari pengguna lalu mengubahnya menjadi integer.

Menangkap error ValueError jika input bukan angka.

Menampilkan pesan "Input tidak valid!".

Melanjutkan perulangan menggunakan continue.

Mengecek apakah pengguna memilih menu 1.

Memulai blok try untuk input film.

Meminta input nama film dari pengguna.

Menambahkan lagu ke queue menggunakan method enqueue.

Menangkap error ValueError.

Menampilkan pesan "Input tidak valid!".

Mengecek apakah pengguna memilih menu 2.

Menjalankan method dequeue untuk memutar film berikutnya.

Mengecek apakah pengguna memilih menu 3.

Menjalankan method peek untuk melihat film berikutnya.

Mengecek apakah pengguna memilih menu 4.

Menjalankan method display untuk menampilkan isi playlist.

Mengecek apakah pengguna memilih menu 5.

Menampilkan pesan "Program selesai.".

Mengecek apakah pengguna memilih menu 6.

Menjalankan method clearall untuk mengosongkan playlist.

Jika pilihan tidak sesuai menu, masuk ke blok else.

Menampilkan pesan "Pilihan tidak valid!".

Mengecek apakah file dijalankan langsung sebagai program utama.

Menjalankan fungsi main().

Output:

<img width="389" height="724" alt="Screenshot 2026-05-19 224010" src="https://github.com/user-attachments/assets/842d52c6-f466-4cae-b71d-31e13e11da4e" />
<img width="518" height="671" alt="Screenshot 2026-05-19 224038" src="https://github.com/user-attachments/assets/78eb99b1-f822-4896-ae88-0cfba97266ca" />
<img width="532" height="444" alt="Screenshot 2026-05-19 224118" src="https://github.com/user-attachments/assets/38fc40d2-e46b-4eab-9df0-a21b11737912" />

Link Video:
