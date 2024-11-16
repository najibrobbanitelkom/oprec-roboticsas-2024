class Bank:
    def __init__(self):
        self.saldo = 0

    def menu(self):
        print("---------------------")
        print("        Menu         ")
        print("---------------------")
        print("1. Tarik Tunai")
        print("2. Setor Tunai")
        print("3. Cek Saldo")
        print("4. Keluar")
        print("---------------------")
        
    def tarik(self):
        print("Selamat datang di menu Tarik Tunai")
        tarik = int(input("Masukkan jumlah uang yang ingin di tarik: "))
        if tarik > self.saldo:
            print("Maaf, saldo tidak cukup")
        if tarik < self.saldo:
            self.saldo -= tarik
            print("Saldo Anda sekarang adalah: ", self.saldo)

    def setor(self):
        print("Selamat datang di menu Setor Tunai")
        setor = int(input("Masukkan jumlah uang yang ingin di setor: "))
        self.saldo += setor
        print("Saldo Anda sekarang adalah: ", self.saldo)

    def cek(self):
        print("Saldo Anda sekarang adalah: ", self.saldo)

    def utama(self):
        while True:
            self.menu()
            pilihan = input("Pilih menu: ")
            if pilihan == "1":
                self.tarik()
            elif pilihan == "2":
                self.setor()
            elif pilihan == "3":
                self.cek()
            elif pilihan == "4":
                print("Terima kasih telah menggunakan jasa kami")
                break
            else:
                print("Pilihan tidak tersedia, silakan pilih menu lainnya")

if __name__ == "__main__":
    bank = Bank()
    bank.utama()