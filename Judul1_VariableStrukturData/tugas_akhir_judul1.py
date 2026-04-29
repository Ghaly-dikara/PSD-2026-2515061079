class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.start = None
        self.rear = None

    def create_new_node(self, n):
        new_node = Node(n)
        return new_node

    def insert_at_beg(self, new_node):
        if self.start is None:
            self.start = new_node
            self.rear = new_node
        else:
            new_node.next = self.start
            self.start = new_node

    def insert_at_end(self, new_node):
        if self.start is None:
            self.start = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def delete_node(self):
        if self.start is None:
            print("Pasien kosong!")
        else:
            deleted_data = self.start.data
            self.start = self.start.next
            print(f"Pasien dengan nama {deleted_data} telah dilayani.")
            if self.start is None:
                self.rear = None

    def display(self):
        if self.start is None:
            print("Antrean kosong")
            return
        current = self.start
        print("===========================Antrean===========================")
        while current is not None:
            print(current.data, end n=" -> ")
            current = current.next
        print("None")

def menu():
    print("Mau melakukan apa?")
    print("1. Daftar sakit")
    print("2. Layani pasien")
    print("3. Cek antrean")
    print("4. Keluar")

def main():
    running = True
    ll = LinkedList()
    while running:
        menu()
        choice = int(input("Pilihan: "))
        if choice == 1:
            choice = "y"
            while choice.lower() == "y":
                p = (input("Masukkan nama pasien : "))
                print(f"Nama Pasien : {p}")
                print("Membuat antrean baru")
                new_node = ll.create_new_node(p)
                if new_node is not None:
                    print("Berhasil membuat antrian baru")
                else:
                    print("Antrian tidak dapat dibuat")
                    break
                print("1. VIP")
                print("2. Reguler")
                try:
                    insert_choice = int(input("Ambil jalur yang mana? "))
                except ValueError:
                    insert_choice = 1
                if insert_choice == 1:
                    ll.insert_at_beg(new_node)
                    print("Pasien dimasukkan di antrean VIP")
                    ll.display()
                elif insert_choice == 2:
                    ll.insert_at_end(new_node)
                    print("Pasien dimasukkan di antrean Reguler")
                    ll.display()
                else:
                    print("Pilihan tidak valid, Pasien dimasukkan di antrean Reguler")
                    ll.insert_at_end(new_node)
                    ll.display()
                print("Antrean: ", end="")
                choice = input("Mau membuat pendaftaran baru? (y/n) ")
                if choice != "y":
                    print("input tidak valid akan dikembalikan ke menu")
                continue

        elif choice == 2:
            print("Daftar Antrean Saat Ini:")
            ll.display()
            ll.delete_node()

        elif choice == 3:
            ll.display()
    
        elif choice == 4:
            running = False
            print("Terimakasih telah memilih kami.")
    
        else:
            print("Pilihan tidak valid!")

main()