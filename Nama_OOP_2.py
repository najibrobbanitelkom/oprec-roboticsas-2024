class Mobil():
    def __init__(self, nama:str, merek:str, tahun:int):
        assert isinstance(nama, str), 'Value of nama should be string.'
        assert isinstance(merek, str), 'Value of merek should be string.'
        assert isinstance(tahun, int), 'Value of tahun should be integer.'

        self.nama = nama
        self.merek = merek
        self.tahun = tahun
        self.awalTahun = tahun #untuk menyimpan nilai tahun pertama kali keluaran mobil

    def info_mobil(self):
        print(f'Mobil {self.nama} {self.merek} keluaran tahun {self.tahun}.')

    def ubah_tahun(self, newTahun):
        if newTahun < self.awalTahun: #hanya akan berubah jika tahun yang diubah di bawah tahun PERTAMA KALI keluaran mobil
            print("Error: Tahun tidak valid.")
        else:
            self.tahun = newTahun

def main():
    mobil1 = Mobil("Toyota","Avanza",2015)
    mobil1.info_mobil()
    mobil1.ubah_tahun(2023)
    mobil1.info_mobil()
    mobil1.ubah_tahun(2010)

if __name__ == '__main__':
    main()
