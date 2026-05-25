class TeamNode:
    def __init__(self, tim, poin):
        self.tim = tim
        self.poin = poin
        self.left = None
        self.right = None

class LeaderboardModernWarfare:
    def __init__(self):
        self.root = None

    def insert_node(self, root, tim, poin):
        if root is None:
            return TeamNode(tim, poin)

        if poin < root.poin:
            root.left = self.insert_node(root.left, tim, poin)

        elif poin > root.poin:
            root.right = self.insert_node(root.right, tim, poin)

        return root

    def insert(self, tim, poin):
        self.root = self.insert_node(self.root, tim, poin)

    def find_min_node(self, root):
        current = root

        while current is not None and current.left is not None:
            current = current.left

        return current

    def delete_node(self, root, poin):
        if root is None:
            return None

        if poin < root.poin:
            root.left = self.delete_node(root.left, poin)

        elif poin > root.poin:
            root.right = self.delete_node(root.right, poin)

        else:
            if root.left is None and root.right is None:
                return None

            elif root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            else:
                successor = self.find_min_node(root.right)

                root.poin = successor.poin
                root.tim = successor.tim

                root.right = self.delete_node(root.right, successor.poin)

        return root

    def delete(self, poin):
        self.root = self.delete_node(self.root, poin)

    def height(self, root):
        if root is None:
            return -1

        height_left = self.height(root.left)
        height_right = self.height(root.right)

        return 1 + max(height_left, height_right)

    def level_order(self, root):
        if root is None:
            print("(kosong)")
            return

        queue = []
        queue.append(root)

        while len(queue) > 0:
            current = queue.pop(0)

            print(f"{current.tim} | {current.poin} poin")

            if current.left is not None:
                queue.append(current.left)

            if current.right is not None:
                queue.append(current.right)

    def inorder_descending(self, root):
        if root is not None:
            self.inorder_descending(root.right)

            print(f"{root.tim} | {root.poin} poin")

            self.inorder_descending(root.left)

def main():
    leaderboard = LeaderboardModernWarfare()

    pilih = 0

    while pilih != 5:
        print("\n=== MW Leaderboard ===")
        print("1. Tambah Tim")
        print("2. Hapus Tim")
        print("3. Tampilkan Leaderboard")
        print("4. Tinggi Pohon")
        print("5. Keluar")

        try:
            pilih = int(input("Pilih: "))

        except ValueError:
            print("Input tidak valid!")
            continue

        if pilih == 1:
            try:
                nama_tim = input("Nama tim: ")
                poin = int(input("Poin tim: "))

                leaderboard.insert(nama_tim, poin)

                print("Tim berhasil ditambahkan")

            except ValueError:
                print("Input tidak valid!")

        elif pilih == 2:
            try:
                poin = int(input("Poin tim yang dihapus: "))

                leaderboard.delete(poin)

                print("Tim berhasil dihapus")

            except ValueError:
                print("Input tidak valid!")

        elif pilih == 3:
            print("\n=== Leaderboard ===")
            leaderboard.inorder_descending(leaderboard.root)

        elif pilih == 4:
            print(f"Tinggi pohon: {leaderboard.height(leaderboard.root)}")

        elif pilih == 5:
            print("Program selesai.")

        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()