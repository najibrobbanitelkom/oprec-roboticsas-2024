class Mobil:
    def __init__(self, nama, jenis, tahun):
        self.nama = nama
        self.jenis = jenis
        self.tahun = tahun

    def ubah_tahun(self, tahun_baru):
        self.tahun = tahun_baru
        return self.tahun

    def info_mobil(self):
        print("Mobil", self.nama,"jenis", self.jenis,"tahun", self.tahun)


def main():
    mobil1 = Mobil("Toyota", "Avanza", 2015)
    mobil1.info_mobil()
    mobil1.ubah_tahun(2023)
    mobil1.info_mobil()
    mobil1.ubah_tahun(2010)

if __name__ == "__main__":
    main()