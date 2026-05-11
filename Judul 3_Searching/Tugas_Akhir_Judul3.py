def binary_search_partial(buku, n, target):
    l = 0
    r = n - 1
    hasil = []

    while l <= r:
        m = l + (r - l) // 2

        print(f"\nPosisi tengah: {m}")
        print(f"Judul buku : {buku[m]}")

        if target.lower() in buku[m].lower():

            hasil.append(buku[m])

            i = m - 1
            while i >= 0:
                if target.lower() in buku[i].lower():
                    hasil.append(buku[i])
                i -= 1

            i = m + 1
            while i < n:
                if target.lower() in buku[i].lower():
                    hasil.append(buku[i])
                i += 1

            break

        elif buku[m].lower() < target.lower():
            print("Mencari di kanan")
            l = m + 1

        else:
            print("Mencari di kiri")
            r = m - 1

    return hasil


def tampilkan_buku(buku):
    print("\n DAFTAR BUKU \n")

    for i in range(len(buku)):
        print(f"{i + 1}. {buku[i]}")


def main():

    buku = [
        "Laut Bercerita",
        "Bumi Manusia",
        "Anak Semua Bangsa",
        "Jejak Langkah",
        "Rumah Kaca",
        "Saman",
        "Pulang",
        "Gadis Pantai",
        "Cantik Itu Luka",
        "Laskar Pelangi",
        "Sang Pemimpi",
        "Edensor",
        "Maryamah Karpov",
        "Padang Bulan",
        "Ayat-Ayat Cinta",
        "Perahu Kertas",
    ]

    n = len(buku)

    while True:

        print("\n MENU PENCARIAN BUKU \n")
        print("1. Tampilkan daftar buku")
        print("2. Cari buku")
        print("3. Keluar")

        pilihan = input("\nMasukkan pilihan: ")

        if pilihan == "1":
            tampilkan_buku(buku)

        elif pilihan == "2":

            target = input("\nMasukkan judul buku yang ingin dicari: ")

            hasil = binary_search_partial(buku, n, target)

            if len(hasil) > 0:

                print("\n HASIL PENCARIAN \n")

                for i in range(len(hasil)):
                    print(f"{i + 1}. {hasil[i]}")

            else:
                print("\nBuku tidak ditemukan")

        elif pilihan == "3":
            print("\nProgram selesai")
            break

        else:
            print("\nPilihan tidak valid")


if __name__ == "__main__":
    main()