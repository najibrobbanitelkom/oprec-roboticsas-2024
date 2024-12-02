class Bank:
    def __init__(self, nama, saldo_awal):
        self.nama = nama
        self.saldo = saldo_awal

    def cek_saldo(self):
        print(f"Saldo anda saat ini adalah: Rp. {self.saldo}")

    def setor_uang(self, jumlah):
        if jumlah > 0:
            self.saldo += jumlah
            print(f"Berhasil menyetor sebesar Rp. {jumlah}. Saldo kini: Rp. {self.saldo}")
        else:
            print("Jumlah setoran min. Rp.1")

    def tarik_uang(self, jumlah):
        if jumlah > self.saldo:
            print("Transaksi gagal. Saldo tidak mencukupi.")
        elif jumlah <= 0:
            print("Jumlah penarikan min. Rp.1")
        else:
            self.saldo -= jumlah
            print(f"Berhasil menarik sebesar Rp. {jumlah}. Saldo kini: Rp. {self.saldo}")
            
def main():
    print("=== Selamat Datang ===")
    nama = input("Masukkan nama Anda: ")
    saldo_awal = 1000000
    
    rekening = Bank(nama, saldo_awal)
    
    while True:
        print(f"Halo, {nama}! Apa yang bisa kami bantu:")
        print("1. Cek Saldo")
        print("2. Setor Uang")
        print("3. Tarik Uang")
        print("4. Keluar")
        
        try:
            pilihan = int(input("Masukkan pilihan Anda: "))
        except ValueError:
            print("Pilihan tidak valid. Masukkan angka 1, 2, 3, atau 4.")
            continue
        
        if pilihan == 1:
            rekening.cek_saldo()
        elif pilihan == 2:
            jumlah = int(input("Masukkan jumlah yang ingin disetor: Rp. "))
            rekening.setor_uang(jumlah)
        elif pilihan == 3:
            jumlah = int(input("Masukkan jumlah yang ingin ditarik: Rp. "))
            rekening.tarik_uang(jumlah)
        elif pilihan == 4:
            print("Terima kasih telah menggunakan layanan kami. Sampai jumpa lagi!")
            break
        else:
            print("Pilihan tidak valid. Pilih angka 1, 2, 3, atau 4.")

if __name__ == "__main__":
    main()
