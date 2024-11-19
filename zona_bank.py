class Bank:
    def __init__(self):
        self.saldo = 0

    def menu(self):
        print("=====================")
        print("  Selamat Datang!    ")
        print("=====================")
        print("1. Tarik Tunai")
        print("2. Setor Tunai")
        print("3. Cek Saldo")
        print("4. Keluar")
        print("=====================")

    def tarik(self):
        print("\n=== Menu Tarik Tunai ===")
        try:
            tarik = int(input("Masukkan jumlah uang yang ingin Anda tarik: "))
            if tarik > self.saldo:
                print("Maaf, saldo Anda tidak mencukupi untuk transaksi ini.")
            elif tarik <= 0:
                print("Nominal yang dimasukkan harus lebih besar dari nol.")
            else:
                self.saldo -= tarik
                print(f"Berhasil menarik uang sebesar Rp{tarik}.")
                print(f"Sisa saldo Anda saat ini: Rp{self.saldo}")
        except ValueError:
            print("Input tidak valid. Masukkan angka yang benar.")

    def setor(self):
        print("\n=== Menu Setor Tunai ===")
        try:
            setor = int(input("Masukkan jumlah uang yang ingin Anda setor: "))
            if setor <= 0:
                print("Nominal yang dimasukkan harus lebih besar dari nol.")
            else:
                self.saldo += setor
                print(f"Berhasil menyetor uang sebesar Rp{setor}.")
                print(f"Saldo Anda sekarang: Rp{self.saldo}")
        except ValueError:
            print("Input tidak valid. Masukkan angka yang benar.")

    def cek(self):
        print("\n=== Menu Cek Saldo ===")
        print(f"Saldo Anda saat ini adalah: Rp{self.saldo}")

    def utama(self):
        while True:
            self.menu()
            pilihan = input("Silakan pilih menu (1-4): ")
            if pilihan == "1":
                self.tarik()
            elif pilihan == "2":
                self.setor()
            elif pilihan == "3":
                self.cek()
            elif pilihan == "4":
                print("\nTerima kasih telah menggunakan layanan kami.")
                print("Semoga harimu menyenangkan!")
                break
            else:
                print("\nPilihan tidak valid. Silakan pilih menu yang tersedia.\n")


if __name__ == "__main__":
    bank = Bank()
    bank.utama()
