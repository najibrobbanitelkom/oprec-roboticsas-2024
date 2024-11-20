class bank:
    def __init__(self, pengguna, balance):
        self.pengguna = pengguna
        self.balance = balance
    
    def setor(self, saldo):
        if saldo > 10000:
            self.balance += saldo
            print(f"Setoran berhasil! Saldo saat ini: {self.balance}")
        else:
            print("Jumlah setoran harus lebih dari 10.000")

    def tarik(self, saldo):
        if saldo > self.balance:
            print("Saldo tidak cukup untuk melakukan penarikan")
        elif saldo <= 10000:
            print("Jumlah penarikan harus lebih dari 10.000")
        else:
            self.balance -= saldo
            print(f"Penarikan saldo berhasil! Saldo saat ini: {self.balance}")

    def check_saldo(self):
        print(f"Saldo saat ini: {self.balance}")

def main():
    print("Selamat datang di Bank AJA!")
    name = input("Masukkan nama Anda: ")
    akun = bank(pengguna=name, balance=0)

    while True:
        print("Menu:")
        print("1. Cek saldo")
        print("2. Setor uang")
        print("3. Tarik uang")
        print("4. Keluar")

        choice = input("Pilih menu (1/2/3/4): ")

        if choice == '1':
            akun.check_saldo()
        elif choice == '2':
            amount = float(input("Masukkan jumlah setoran: "))
            akun.setor(amount)
        elif choice == '3':
            amount = float(input("Masukkan jumlah penarikan: "))
            akun.tarik(amount)
        elif choice == '4':
            print("Terima kasih telah menggunakan layanan Bank AJA!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()