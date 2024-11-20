class Account():
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit berhasil. Saldo Anda sekarang: Rp{self.balance}")
        else:
            print("Jumlah deposit harus lebih dari 0.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Saldo tidak mencukupi untuk melakukan penarikan.")
        elif amount > 0:
            self.balance -= amount
            print(f"Penarikan berhasil. Saldo Anda sekarang: Rp{self.balance}")
        else:
            print("Jumlah penarikan harus lebih dari 0.")

    def check_balance(self):
        print(f"Saldo Anda saat ini: Rp{self.balance}")


class Bank():
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, name, initial_deposit=0):
        if account_number in self.accounts:
            print("Nomor rekening sudah terdaftar.")
        else:
            self.accounts[account_number] = Account(account_number, name, initial_deposit)
            print(f"Rekening dengan nomor {account_number} berhasil dibuat.")

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)


# Simulasi
bank = Bank()

# Membuat akun baru
bank.create_account("12345", "Budi", 100000)
bank.create_account("67890", "Ani", 200000)

# Akses akun dan operasikan
account = bank.get_account("12345")
if account != None:
    print("Pemilik akun:", account.name)
    account.deposit(50000)
    account.withdraw(20000)
    account.check_balance()
else:
    print("Akun tidak ditemukan.")
