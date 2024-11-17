class Transaksi:
    def __init__(self, username, pin):
        self.username = username
        self.pin = pin
        self.saldo = 0

    def setor(self, total_saldotambah):
        if total_saldotambah > 0:
            self.saldo += total_saldotambah
            print(f"Setor Rp {total_saldotambah} berhasil")
        else:
            print("Anda menambahkan saldo 0")
    
    def penarikan(self, total_penarikan):
        if total_penarikan <= self.saldo:
            self.saldo -= total_penarikan
            print(f"Penarikan berhasil. Sisa saldo Rp {self.saldo}")
        else:
            print(f"Saldo tidak cukup, saldo anda sekarang adalah Rp {self.saldo}")

    def ubah_pin(self, pin_lama, pin_baru):
        if pin_lama == self.pin:
            self.pin = pin_baru
            print("PIN berhasil diubah")
        else:
            print("PIN lama salah")

    def cek_saldo(self):
        print(f"Saldo anda sekarang adalah Rp {self.saldo}")

class User:
    def __init__(self, username, pin):
        self.username = username
        self.akun = Transaksi(username, pin)

class Bank:
    def __init__(self):
        self.users = []

    def tambah_user(self, username, pin):
        user_baru = User(username, pin)
        self.users.append(user_baru)
        print(f" akun {username} berhasil dibuat ")

    def temukan(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None

def main():
    bank_utama = Bank()
    print("======= Selamat datang ========")
    
    while True:
        print("1. pengguna baru")
        print("2. login")
        print("3. keluar")
        pilihan = input("Masukkan pilihan : ")
        
        if pilihan == '1':
            username = input("Masukkan username : ")
            pin = input("Masukkan pin: ")
            bank_utama.tambah_user(username, pin)
        elif pilihan == '2':
            username = input("Masukkan username : ")
            pin = input("Masukkan pin: ")
            pengguna = bank_utama.temukan(username)

            if pengguna and pengguna.akun.pin == pin:
                print("Selamat datang")
                while True:
                    print("menu Utama")
                    print("1. setor saldo")
                    print("2. senarikan saldo")
                    print("3. ganti PIN")
                    print("4. cek saldo")
                    print("5. logout")

                    pilihan_utama = input("Masukkan pilihan : ")

                    if pilihan_utama == '1':
                        jumlah = float(input("Masukkan jumlah setoran : "))
                        pengguna.akun.setor(jumlah)
                    elif pilihan_utama == '2':
                        jumlah = float(input("Masukkan jumlah penarikan : "))
                        pengguna.akun.penarikan(jumlah)
                    elif pilihan_utama == '3':
                        pin_lama = input("Masukkan PIN lama : ")
                        pin_baru = input("Masukkan PIN baru : ")
                        pengguna.akun.ubah_pin(pin_lama, pin_baru)
                    elif pilihan_utama == '4':
                        pengguna.akun.cek_saldo()
                    elif pilihan_utama == '5':
                        print("Anda telah logout")
                        break
                    else:
                        print("Pilihan tidak tersedia")
            else:
                print("Username atau PIN salah")
        elif pilihan == '3':
            print("Terima kasih")
            break
        else:
            print("Pilihan tidak tersedia")

if __name__ == "__main__":
    main()