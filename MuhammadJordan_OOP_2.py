class Mobil:
    def __init__(self, nama, merek, tahun):
        self.nama = nama
        self.merek = merek
        self.tahun = tahun

    def info_mobil(self):
        print("Mobil", self.nama, self.merek, "Keluaran", self.tahun)
    
    def ganti_tahun(self,x):
        if x < self.tahun:
            print("Error: Tahun tidak valid")
        else:
            self.tahun = x
        
    
def main():
    mobil1 = Mobil("Toyota", "Avanza", 2015)
    mobil1.info_mobil()
    mobil1.ganti_tahun(2023)
    mobil1.info_mobil()
    mobil1.ganti_tahun(2010)

if __name__ == '__main__':
    main()


        
        