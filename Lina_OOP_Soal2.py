class Mobil:
    def __init__(self, nama, merek, tahun):
        self.nama = nama
        self.merek = merek
        self.tahun = tahun

    def info_mobil(self):
        print("Mobil", self.nama,"jenis", self.merek,"tahun", self.tahun)

    def ubah_tahun(self, tahun_ubah):
        if tahun_ubah < self.tahun:
            print("Tahun tidak valid.")
        else:
             self.tahun = tahun_ubah
             return self.tahun

def main():
    mobil = Mobil("Toyota", "Avanza", 2015)
    mobil.info_mobil()
    mobil.ubah_tahun(2023)
    mobil.info_mobil()
    mobil.ubah_tahun(2010)

if __name__ == '__main__':
    main()