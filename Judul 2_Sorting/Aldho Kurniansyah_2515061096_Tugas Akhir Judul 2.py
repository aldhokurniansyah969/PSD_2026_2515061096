def tukar(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def bubble_sort(arr, n):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j].lower() > arr[j + 1].lower():
                tukar(arr, j, j + 1)


def main():
    try:
        n = int(input("Masukkan jumlah film: "))
    except ValueError:
        print("Input tidak valid!")
        return

    arr = []

    print("Masukkan judul film:")
    for i in range(n):
        judul = input(f"Judul film ke-{i + 1}: ")
        arr.append(judul)

    print(f"\nDaftar judul film sebelum diurutkan: {arr}")

    bubble_sort(arr, n)

    print("\nDaftar judul film yang telah diurutkan:")
    for i in range(n):
        print(arr[i])


if __name__ == "__main__":
    main()