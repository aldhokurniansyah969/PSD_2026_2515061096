class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMapSeparateChaining:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [None] * self.SIZE

    def hash_function(self, key):
        return (key % self.SIZE + self.SIZE) % self.SIZE

    def insert(self, key, value):
        index = self.hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                current.value = value
                return
            current = current.next
        new_node = Node(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node

    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                return current
            current = current.next
        return None

    def remove_key(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        prev = None
        while current is not None:
            if current.key == key:
                if prev is None:
                    self.table[index] = current.next
                else:
                    prev.next = current.next
                return True
            prev = current
            current = current.next

        return False

    def display(self):
        print("\nData Kendaraan di Area Parkir:")
        for i in range(self.SIZE):
            print(f"Slot {i}: ", end="")
            current = self.table[i]
            while current is not None:
                print(f"({current.key}, {current.value}) -> ", end="")
                current = current.next

            print("NULL")

def main():
    hashmap = HashMapSeparateChaining()

    print("SISTEM PARKIR DIGITAL")
    hashmap.insert(1001, "Honda Beat - BE 1234 AA")
    hashmap.insert(1011, "Yamaha NMAX - BE 5678 BB")
    hashmap.insert(1021, "Toyota Avanza - BE 1111 CC")
    hashmap.insert(1002, "Honda Brio - BE 2222 DD")
    print("\nKendaraan berhasil masuk area parkir.")
    hashmap.display()

    hasil = hashmap.search(1011)
    if hasil is not None:
        print(f"\nKendaraan ditemukan: {hasil.value}")
    else:
        print("\nKendaraan tidak ditemukan.")

    hashmap.remove_key(1011)
    print("\nKendaraan dengan nomor parkir 1011 keluar dari area parkir.")
    print("\nData parkir setelah kendaraan keluar:")
    hashmap.display()

if __name__ == "__main__":
    main()