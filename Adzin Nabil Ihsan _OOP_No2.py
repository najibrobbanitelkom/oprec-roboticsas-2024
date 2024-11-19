class Mobil:
    def __init__(self, merek, nama, tahun):
        self.merek = merek
        self.nama = nama
        self.tahun = tahun

    def info_mobil(self):
        print(f"Mobil {self.merek} {self.nama} keluaran tahun {self.tahun}")

    def ubah_tahun(self, tahun_baru):
        if tahun_baru > self.tahun:
            self.tahun = tahun_baru
            print(f"Tahun berhasil diubah menjadi {self.tahun}.")
        else:
            print("Tahun tidak valid.")

def main():
    mobil1 = Mobil("Toyota", "Avanza", 2015)
    mobil1.info_mobil()  
    mobil1.ubah_tahun(2023)  
    mobil1.info_mobil()  
    mobil1.ubah_tahun(2010)  

if __name__ == "__main__":
    main()