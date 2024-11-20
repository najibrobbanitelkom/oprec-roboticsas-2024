class Mobil:
    def __init__(self, nama, merek, tahunKeluar):
        self.nama = nama
        self.merek = merek
        self.tahunKeluar = tahunKeluar
    
    def info_mobil(self):
        print(f"Mobil {self.nama} {self.merek} keluaran tahun {self.tahunKeluar}")

    def ubah_tahun(self, updateTahun):
        if updateTahun > self.tahunKeluar :
            self.tahunKeluar = updateTahun
        else:
            print("Tahun tidak valid.")

def main():
    mobil1 = Mobil("Toyota", "Avanza", 2015)
    mobil1.info_mobil()
    mobil1.ubah_tahun(2023)
    mobil1.info_mobil()
    mobil1.ubah_tahun(2010)

if __name__ == '__main__':
    main()