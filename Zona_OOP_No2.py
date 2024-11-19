class Mobil:
    def __init__(self, nama, merek, tahun_keluar):
        self.nama = nama
        self.merek = merek
        self.tahun_keluar = tahun_keluar

    def info_mobil(self):
        print(f"Mobil {self.merek} {self.nama} keluaran tahun {self.tahun_keluar}.")

    def ubah_tahun(self, tahun_baru):
        if tahun_baru < self.tahun_keluar:
            print("Error: Tahun tidak valid.")
        else:
            self.tahun_keluar = tahun_baru
            # print(f"PERUBAHAN TAHUN {tahun_baru}.")

def main():
    mobil1 = Mobil("Toyota", "Avanza", 2015)
    mobil1.info_mobil()
    mobil1.ubah_tahun(2023)
    mobil1.info_mobil()
    mobil1.ubah_tahun(2010)

if __name__ == "__main__":
    main()
