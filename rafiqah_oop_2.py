class mobil:
    def __init__(self, nama, merk, tahun):
        self.nama = nama
        self.merk = merk
        self.tahun = tahun
    
    def ubah_tahun(self, tahun):
        self.newtahun = tahun
        if self.newtahun < self.tahun:
            print("Error: Tahun tidak valid.")
        else:
            self.tahun = self.newtahun
    
    def info(self):
        print(f"mobil {self.nama} {self.merk} keluaran tahun {self.tahun}.")

def main():
    mobil1 = mobil("Suzuki", "Ertiga", 2015)
    mobil1.info()
    mobil1.ubah_tahun(2023)
    mobil1.info()
    mobil1.ubah_tahun(2010)

if __name__ == '__main__':
    main()