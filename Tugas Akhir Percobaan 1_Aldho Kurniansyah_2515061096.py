def menu():
    print("\nSISTEM DATA PENJUALAN BUAH")
    print("1. Tampilkan Total Pembelian")
    print("2. Input Jumlah Pembelian")
    print("0. Keluar")

def main():
    jenis_buah = ["Apel", "Mangga", "Jeruk", "Alpukat", "Durian", "Kiwi", "Pir"]
    jumlah_buah = len(jenis_buah)
    jumlah_pembeli = int(input("Masukkan jumlah pembeli: "))
    pembelian_buah = [[0 for _ in range(jumlah_buah)] for _ in range(jumlah_pembeli)]
    
    running = True
    while running:
        menu()
        try:
            choice = int(input("Pilih menu : "))
        except ValueError:
            print("Masukkan angka yang ada di menu")
            continue

        if choice == 1:
            print("\nTabel Penjualan")
            width = 10
            header = f"{'Pembeli':<{width}}" + "".join([f"{m[:6]:<{width}}" for m in jenis_buah])
            print(header)
            print("-" * (width * (len(jenis_buah) + 1)))
            for i in range(jumlah_pembeli):
                baris_nilai = "".join([f"{str(n):<{width}}" for n in pembelian_buah[i]])
                print(f"{'Pembeli ' + str(i+1):<{width}}{baris_nilai}")

        elif choice == 2:
            print("\nInput Jumlah")
            for i in range(jumlah_pembeli):
                print(f"> Mengisi data untuk Pembeli {i+1}:")
                for j in range(jumlah_buah):
                    while True:
                        try:
                            val = int(input(f"  Masukkan data untuk buah {jenis_buah[j]}: "))
                            if 0 <= val <= 100000:
                                pembelian_buah[i][j] = val
                                break
                            else:
                                print("Nilai harus antara 0 - 100000")
                        except ValueError:
                            print("Input error mohon untuk hanya memasukkan angka.")

        elif choice == 0:
            running = False
            print("Program selesai. Terima kasih!")
        else:
            print("Pilihan tidak tersedia.")

if __name__ == "__main__":
    main()