Tugas Akhir Percobaan 4

Nama : Aldho Kurniansyah

NPM : 2515061096

Judul Program : Program Leaderboard Game Modern Warfare

<img width="1462" height="6410" alt="code" src="https://github.com/user-attachments/assets/97b290c2-af06-4f25-8e2a-281803cb4bb2" />

Mendefinisikan class TeamNode untuk membuat node BST.

Mendefinisikan constructor init pada class TeamNode.

Parameter tim dan poin digunakan saat membuat node baru.

Menyimpan tim ke atribut self.tim.

Menyimpan poin tim ke atribut self.poin.

Child kiri diisi None.

Child kanan diisi None.

Mendefinisikan class LeaderboardModernWarfare.

Mendefinisikan constructor class leaderboard.

Root BST awalnya kosong (None).

Mendefinisikan fungsi insert_node.

Jika root kosong maka membuat node baru.

Membuat object TeamNode.

Jika poin lebih kecil dari root.

Masuk ke subtree kiri secara rekursif.

Jika poin lebih besar dari root.

Masuk ke subtree kanan secara rekursif.

Mengembalikan root setelah insert selesai.

Fungsi insert utama.

Root BST diisi hasil insert.

Fungsi mencari node terkecil.

Variabel current menunjuk root awal.

Perulangan selama node kiri masih ada.

Bergerak terus ke kiri.

Mengembalikan node terkecil.

Fungsi menghapus node.

Jika root kosong maka return None.

Jika poin lebih kecil dari root.

Hapus node di subtree kiri.

Jika poin lebih besar dari root.

Hapus node di subtree kanan.

Jika poin ditemukan.

Jika node tidak punya child.

Node dihapus dengan return None.

Jika hanya child kanan yang ada.

Menggantikan node dengan child kanan.

Jika hanya child kiri yang ada.

Menggantikan node dengan child kiri.

Jika node punya dua child.

Mencari successor dari subtree kanan.

Mengganti poin root dengan poin successor.

Mengganti nama tim root dengan nama successor.

Menghapus successor lama.

Mengembalikan root setelah delete selesai.

Fungsi delete utama.

Root diisi hasil delete.

Fungsi menghitung tinggi pohon.

Jika root kosong.

Mengembalikan -1.

Menghitung tinggi subtree kiri.

Menghitung tinggi subtree kanan.

Mengembalikan tinggi terbesar ditambah 1.

Fungsi traversal level-order.

Jika root kosong.

Menampilkan tulisan (kosong).

Keluar dari fungsi.

Membuat queue kosong.

Root dimasukkan ke queue.

Perulangan selama queue tidak kosong.

Mengambil node paling depan queue.

Menampilkan nama tim dan poin.

Jika child kiri ada.

Child kiri dimasukkan queue.

Jika child kanan ada.

Child kanan dimasukkan queue.

Fungsi inorder descending.

Jika root tidak kosong.

Traversal subtree kanan terlebih dahulu.

Menampilkan nama tim dan poin.

Traversal subtree kiri.

Mendefinisikan fungsi main.

Membuat object leaderboard.

Variabel menu awal bernilai 0.

Perulangan program selama pilih bukan 5.

Menampilkan judul program.

Menampilkan menu tambah tim.

Menampilkan menu hapus tim.

Menampilkan menu leaderboard.

Menampilkan menu tinggi pohon.

Menampilkan menu successor.

Menampilkan menu predecessor.

Menampilkan menu keluar.

Mencoba membaca input menu.

Input diubah menjadi integer.

Jika input bukan angka.

Menampilkan pesan error.

Mengulang menu.

Jika memilih menu 1.

Mencoba input data tim.

Input nama tim.

Input poin tim.

Memasukkan tim ke BST.

Menampilkan pesan berhasil.

Jika input salah.

Menampilkan pesan error.

Jika memilih menu 2.

Mencoba input poin yang dihapus.

Menghapus tim dari BST.

Menampilkan pesan berhasil.

Jika input salah.

Menampilkan pesan error.

Jika memilih menu 3.

Menampilkan judul leaderboard.

Menampilkan data secara descending.

Jika memilih menu 4.

Menampilkan tinggi BST.

Jika memilih menu 5.

Menampilkan pesan program selesai.

Jika menu tidak valid.

Mengecek apakah file dijalankan langsung.

Menjalankan fungsi main().

Output:

<img width="521" height="865" alt="Screenshot 2026-05-25 205941" src="https://github.com/user-attachments/assets/fcbf952e-d782-4e2d-9254-2a4443a2ef66" />

Link Video: https://youtu.be/oyFf3TsFJrU?si=xYjtWKrVopRoS9J3
