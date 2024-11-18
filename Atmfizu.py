class ATM:
    
    def __init__(self, saldo=0):
        self.saldo = saldo
        self.pin = "1234"
        self.parameter_log_in = False

    def login(self):
        kesempatan = 3
        while kesempatan > 0:
            input_pin = input(f"Masukkan PIN anda ({kesempatan} percobaaan tersisa): ")
            if input_pin == self.pin:
                self.parameter_log_in = True
                print("=== Selamat Anda Berhasil Login! ===")
                return
            else:
                kesempatan -= 1
                print(f"PIN yang anda masukkan SALAH! kesempatan yang anda miliki adalah {kesempatan} percobaan")
        print("Percobaan yang anda lakukan terlalu banyak, kartu anda di tahan untuk sementara.")
        print("Demi keamanan, silahkan mengunjungi bank terdekat.")
        exit()
    
    def logout(self):
        self.parameter_log_in = False
        print("Terimakasih, Sudah menggunakan ATM kami.")
        print("Anda telah keluar.")

    def cek_saldo(self):
        if not self.parameter_log_in:
            print("Dimohon untuk melakukan login terlebih dahulu.")
            return
        print(f"Saldo yang Anda miliki saat ini: Rp {self.saldo}")

    def tarik_tunai(self):
        if not self.parameter_log_in:
            print("Dimohon untuk melakukan login terlebih dahulu.")
            return
        try:
            Jtarik = int(input("Masukkan nominal uang yang ingin anda tarik: Rp "))
            if Jtarik > self.saldo:
                print("Mohon maaf saldo Anda tidak cukup.")
                print(f"Saldo yang Anda miliki saat ini: Rp {self.saldo}")
            else:
                self.saldo -= Jtarik
                print("Penarikan Anda berhasil!")
                print(f"Saldo yang Anda miliki saat ini: Rp {self.saldo}")
        except ValueError:
            print("Masukkan jumlah yang valid!")

    def setor_tunai(self):
        if not self.parameter_log_in:
            print("Dimohon untuk melakukan login terlebih dahulu.")
            return
        try:
            Jsetor = int(input("Masukkan nominal yang ingin Anda setor: Rp "))
            self.saldo += Jsetor
            print("Setoran Anda berhasil!")
            print(f"Saldo yang Anda miliki saat ini: Rp {self.saldo}")
        except ValueError:
            print("Masukkan jumlah yang valid!")

    def transfer(self):
        if not self.parameter_log_in:
            print("Dimohon untuk melakukan login terlebih dahulu.")
            return
        try:
            Jtransfer = int(input("Masukkan nominal yang ingin Anda transfer: Rp "))
            if Jtransfer > self.saldo:
                print("Mohon maaf saldo Anda tidak cukup.")
                print(f"Saldo yang Anda miliki saat ini: Rp {self.saldo}")
            else:
                rekening_tujuan = input("Masukkan nomor rekening yang Anda tuju: ")
                self.saldo -= Jtransfer
                print(f"Transfer telah berhasil! Rp {Jtransfer} telah ditransfer ke rekening {rekening_tujuan}.")
                print(f"Saldo yang Anda miliki saat ini: Rp {self.saldo}")
        except ValueError:
            print("Masukkan jumlah yang valid!")

    def bayar_tagihan(self):
        if not self.parameter_log_in:
            print("Dimohon untuk melakukan login terlebih dahulu.")
            return
        print("=== Pilih Jenis Tagihan ===")
        print("1. Listrik")
        print("2. Air")
        print("3. Telepon")
        print("4. Internet")
        pilih_tagihan = input("Masukkan jenis tagihan yang ingin dibayar: ")
        try:
            Jtagihan = int(input("Masukkan nominal tagihan yang akan dibayar: Rp "))
            if Jtagihan > self.saldo:
                print("Mohon maaf saldo Anda tidak cukup.")
                print(f"Saldo yang Anda miliki saat ini: Rp {self.saldo}")
            else:
                self.saldo -= Jtagihan  
                print("Pembayaran tagihan berhasil!")
                print(f"Saldo yang Anda miliki saat ini: Rp {self.saldo}")
        except ValueError:
            print("Masukkan jumlah yang valid!")

    def ganti_pin(self):
        if not self.parameter_log_in:
            print("Dimohon untuk melakukan login terlebih dahulu.")
            return
        pin_baru = input("Masukkan PIN baru: ")
        self.pin = pin_baru
        print("PIN Anda berhasil diganti!")

    def main(self):
        while True:
            print("")
            print("=== Selamat Datang di Fyzuuu ATM ===")
            print("------------------------------------")
            print("1. Cek Saldo")
            print("2. Tarik Tunai")
            print("3. Setor Tunai")
            print("4. Transfer Antar Rekening")
            print("5. Bayar Tagihan")
            print("6. Ganti PIN")
            print("7. Logout")
            print("------------------------------------")
            menu = input("Silahkan memilih menu yang tertera (1-7): ")
            if menu == '1':
                self.cek_saldo()
            elif menu == '2':
                self.tarik_tunai()
            elif menu == '3':
                self.setor_tunai()
            elif menu == '4':
                self.transfer()
            elif menu == '5':
                self.bayar_tagihan()
            elif menu == '6':
                self.ganti_pin()
            elif menu == '7':
                self.logout()
                break
            else:
                print("Pilihan yang Anda masukkan tidak valid!")

# Menjalankan ATM
atm = ATM(saldo=1000000)
atm.login()
atm.main()

#penggunaan program harus mendapat izin dari pemilik _mohamad hafizh odja_