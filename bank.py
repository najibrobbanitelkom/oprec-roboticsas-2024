class AkunBank:
    def __init__(self, pemilik, saldo=0):
        self.pemilik = pemilik
        self.saldo = saldo
    
    def des_akun(self):
        print("Pemilik akun:", self.pemilik,". Saldo yang dimiliki:", self.saldo)

    def setor(self, jumlah):
        if jumlah > 0:
            self.saldo += jumlah
            print("Berhasil Menyetor:", jumlah,"Saldo saat ini:", self.saldo)
        else: print("Jumlah setoran harus lebih besar dari 0.")

    def tarik(self, jumlah):
        if jumlah > self.saldo:
            print("Saldo tidak cukup")
        elif jumlah <= 0 :
            print("jumlah penarikan harus lebih dari 0.")
        else:
            self.saldo -= jumlah
            print("Berhasil menarik uang sebesar:", jumlah,". Saldo anda saat ini:", self.saldo)

    def cek_saldo(self):
        return self.saldo
    
def main():
    print("Masukan Akun dan Saldo awal:")
    akun1 = AkunBank(input(), int(input()))
    print('')
    akun1.des_akun() 

    print("1. Setor Tunai")
    print("2. Tarik Tunai")
    print("3. Cek Saldo")
    print("masukan jenis aktivitas yang diinginkan: ")
    pilih = int(input())
    print('')

    if pilih == 1:
        print("Masukan jumlah yang ingin di setor:")
        akun1.setor(int(input()))
        print('')
    elif pilih == 2:
        print("Masukan jumlah yang ingin di tarik:")
        akun1.tarik(int(input()))
        print('')
    elif pilih == 3:
        saldo = akun1.cek_saldo()
        print("saldo akhir anda:", saldo)
        print('')

    print("apakah masih ingin melakukan transaksi? [y/n]")
    ans = input()
    print('')

    while ans == 'y':
        print("1. Setor Tunai")
        print("2. Tarik Tunai")
        print("3. Cek Saldo")
        print("masukan jenis aktivitas yang diinginkan: ")
        pilih = int(input())
        print('')

        if pilih == 1:
            print("Masukan jumlah yang ingin di setor:")
            akun1.setor(int(input()))
            print('')
        elif pilih == 2:
            print("Masukan jumlah yang ingin di tarik:")
            akun1.tarik(int(input()))
            print('')
        elif pilih == 3:
            saldo = akun1.cek_saldo()
            print("saldo akhir anda:", saldo)
            print('')
    
        print("apakah masih ingin melakukan transaksi? [y/n]")
        ans = input()
        print('')
    
if __name__ == '__main__':
    main()