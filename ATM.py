class User:
    def __init__(self, name="", norek="", pasrek="", salrek=0):
        self.name = name
        self.norek = norek
        self.pasrek = pasrek
        self.salrek = salrek

    def register(self):
        print("$$$$$#####=====--- REGISTER ---=====#####$$$$$")
        self.name = input("Masukkan nama Anda           : ")
        self.norek = input("Masukkan nomor rekening      : ")
        self.pasrek = input("Buat password rekening       : ")
        self.salrek = float(input("Masukkan saldo awal          : "))
        print("Pendaftaran berhasil!\n")
    
    def login(self):
        print("$$$$$#####=====---- LOG-IN ----=====#####$$$$$")
        norek_input = input("Masukkan nomor rekening      : ")
        pasrek_input = input("Masukkan password rekening   : ")
        if norek_input == self.norek and pasrek_input == self.pasrek:
            print("Login berhasil!\n")
            return True
        else:
            print("Login gagal! Nomor rekening atau password salah.\n")
            return False

class ATM:
    def __init__(self, user):
        self.user = user

    def tampil(self):
        print("$$$$$#####=====----- MENU -----=====#####$$$$$")
        print("[1] Tarik Uang")
        print("[2] Setor Tunai")
        print("[3] Cek Saldo")
        print("[4] Keluar")
        print()

    def tarik_uang(self):
        print("$$$$$#####====--- TARIK UANG ---====#####$$$$$")
        jumlah = float(input("Masukkan jumlah yang ingin ditarik: "))
        if jumlah <= self.user.salrek:
            self.user.salrek -= jumlah
            print(f"Berhasil menarik uang sebesar Rp{jumlah}. Saldo Anda sekarang Rp{self.user.salrek}\n")
        else:
            print("Saldo tidak mencukupi!\n")

    def setor_tunai(self):
        print("$$$$$#####===--- SETOR TUNAI ---====#####$$$$$")
        jumlah = float(input("Masukkan jumlah yang ingin disetor: "))
        self.user.salrek += jumlah
        print(f"Berhasil menyetor uang sebesar Rp{jumlah}. Saldo Anda sekarang Rp{self.user.salrek}\n")

    def cek_saldo(self):
        print("$$$$$#####====--- CEK SALDO ---=====#####$$$$$")
        print(f"Saldo Anda: Rp{self.user.salrek}\n")

def main():
    user = User()
    user.register()

    while not user.login():
        pass

    atm = ATM(user)
    while True:
        atm.tampil()
        pilihan = input("Pilih menu: ")
        if pilihan == '1':
            atm.tarik_uang()
        elif pilihan == '2':
            atm.setor_tunai()
        elif pilihan == '3':
            atm.cek_saldo()
        elif pilihan == '4':
            print("[[ Terima kasih telah menggunakan layanan kami! ]]")
            break
        else:
            print("Pilihan tidak valid! Silakan coba lagi.\n")

if __name__ == '__main__':
    main()