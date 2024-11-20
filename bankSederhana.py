class bankSederhana: 
    def __init__(self, nama, no_rekening, saldo_awal=0):
        self.nama = nama
        self.no_rekening = no_rekening
        self.saldo_awal = saldo_awal

    def setor_saldo(self, total_saldo):
        self.saldo_awal += total_saldo
        print("Rp.", total_saldo, "berhasil disetor. Saldo saat ini: Rp.", self.saldo_awal)

    def tarik_saldo(self, total_saldo):
        if total_saldo > self.saldo_awal:
            print("Saldo tidak cukup. Saldo saat ini: Rp.", self.saldo_awal)
        else:
            self.saldo_awal -= total_saldo
            print("Rp.", total_saldo, "berhasil ditarik. Saldo saat ini: Rp.", self.saldo_awal)

    def pengecekan_saldo(self):
        print("Saldo saat ini: Rp.", self.saldo_awal)


def main():
    nama = input("Masukkan Nama Anda: ")
    no_rekening = input("Masukkan Nomor Rekening Anda: ")
    saldo_awal = 0

   
    bank = bankSederhana(nama, no_rekening, saldo_awal)

    while True:
        print("\nPilih tindakan:")
        print("1. Setoran")
        print("2. Penarikan")
        print("3. Cek Saldo")
        print("4. Keluar")
        
        pilihan = input("Masukkan pilihan Anda (1/2/3/4): ")
        
        if pilihan == "1":
            jumlah = int(input("Masukkan jumlah setoran: Rp."))
            bank.setor_saldo(jumlah)
        elif pilihan == "2":
            jumlah = int(input("Masukkan jumlah penarikan: Rp."))
            bank.tarik_saldo(jumlah)
        elif pilihan == "3":
            bank.pengecekan_saldo()
        elif pilihan == "4":
            print("Terima kasih telah menggunakan layanan bank kami. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")


if __name__ == '__main__':
    main()
