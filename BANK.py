class BankAccount:
    def __init__(self, pemilik, nomor_akun, balance=0):
        self.pemilik = pemilik
        self.nomor_akun = nomor_akun
        self.balance = balance

    def show_account_info(self):
        print(f"Pemilik Akun  : {self.pemilik}")
        print(f"No. Rekening  : {self.nomor_akun}")
        print(f"Saldo Saat Ini: Rp{self.balance:,}")

    def deposit(self, amount):
        if amount <= 0:
            print("Jumlah setoran harus lebih dari 0.")
        elif amount > 10000000:
            print("Setoran melebihi batas maksimum Rp10.000.000.")
        else:
            self.balance += amount
            print(f"Berhasil menyetor Rp{amount:,}. Saldo sekarang: Rp{self.balance:,}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Jumlah penarikan harus lebih dari 0.")
        elif amount > self.balance:
            print("Saldo tidak cukup untuk menarik uang.")
        else:
            self.balance -= amount
            print(f"Berhasil menarik Rp{amount:,}. Saldo sekarang: Rp{self.balance:,}")

    def check_balance(self):
        print(f"Saldo Anda saat ini adalah Rp{self.balance:,}")


account = BankAccount("Andi", "123456789", 5_000_000)

account.show_account_info()
print("\n--- Transaksi ---")
account.deposit(2000000) #deposit uang
account.withdraw(6000000) #menarik uang
account.check_balance() #cek isi akun
account.deposit(12000000) #cek saat deposit kelebihan dari batas
account.withdraw(500_000)
