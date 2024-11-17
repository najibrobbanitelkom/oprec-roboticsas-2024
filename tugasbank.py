class Menu:
    saldo = 0

    def pilih_menu(self):
        iterasi = True
        while iterasi:
            print("\n=====MENU=====")
            print("1. Masukkan Uang")
            print("2. Tarik Uang")
            print("3. Cek Saldo")
            print("0. Exit")
            pilihan = int(input("Pilih Menu: "))

            if pilihan == 1:
                self.setor_uang()
            elif pilihan == 2:
                self.tarik_uang()
            elif pilihan == 3:
                self.cek_saldo()
            elif pilihan == 0:
                print("\nProgram Selesai")
                iterasi = False
            else:
                print("Pilihan tidak ada")
    
    def setor_uang(self):
        uang = int(input("Masukkan nominal yang ingin disetor: "))
        self.saldo += uang

    def tarik_uang(self):
        uang = int(input("Masukkan nominal yang ingin ditarik: "))
        if(uang < self.saldo):
            self.saldo -= uang
            print("Penarikan Berhasil")
        else:
            print("Saldo tidak cukup")
    
    def cek_saldo(self):
        print("Saldo Anda sekarang:", self.saldo)

class Bank:
    user = "reynard"
    sandi = 123

    def __init__(self):
        username = input("Masukkan username: ")
        password = int(input("Masukkan password: "))

        self.menu = Menu()

        if(username == self.user and password == self.sandi):
            print("Selamat datang, " + username)
        else:
            print("Maaf username atau password salah")
            exit() 

    
    def show_menu(self):
        self.menu.pilih_menu()



def main():
    beri_nilai = Bank()
    beri_nilai.show_menu()

if __name__ == '__main__':
    main()