class Mobil:
    def __init__(self, nama, merek, tahun):
        self.nama = nama
        self.merek = merek
        self.tahun = tahun
    
    def ubah_tahun(self, tahun):
        self.newtahun = tahun
        if self.newtahun < self.tahun:
            print("Error: Tahun tidak valid.")
        else:
            self.tahun = self.newtahun
    
    def info_mobil(self):
        print(f"Mobil {self.nama} {self.merek} keluaran tahun {self.tahun}.")

def main():
    mobil1 = Mobil("Toyota", "Avanza", 2015)
    mobil1.info_mobil()
    mobil1.ubah_tahun(2023)
    mobil1.info_mobil()
    mobil1.ubah_tahun(2010)

if __name__ == '__main__':
    main()