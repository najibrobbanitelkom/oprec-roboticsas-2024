class Mobil:
    def __init__(self, name, merek, tahun):
        self.name = name
        self.merek = merek
        self.tahun = tahun

    def info_mobil(self):
        print (f"Mobil {self.name} {self.merek} keluaran tahun {self.tahun}.")
    
    def ubah_tahun(self, tahun):
        if(tahun < 2015):
            print("Error: Tahun tidak valid")
        else:
            self.tahun = tahun


def main():
    mobil1 = Mobil("Toyota", "Avanze", 2015)
    mobil1.info_mobil()
    mobil1.ubah_tahun(2023)
    mobil1.info_mobil()
    mobil1.ubah_tahun(2010)

if __name__ == '__main__':
    main()