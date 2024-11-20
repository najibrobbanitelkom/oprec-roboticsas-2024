class Mobil:
    def __init__(self, merek, model, tahun):
        self.merek = merek
        self.model = model
        self.tahun = tahun

    def info_mobil(self):
        print("Mobil", self.merek, self.model, "keluaran tahun",self.tahun)
    
    def ubah_tahun(self, tahun_baru):
        if tahun_baru > self.tahun:
            self.tahun = tahun_baru
        else:
            print("Error: Tahun tidak valid.")
        

def main():
    mobil1 = Mobil("Toyota", "Avanza", 2015)
    mobil1.info_mobil()
    mobil1.ubah_tahun(2023)
    mobil1.info_mobil()
    mobil1.ubah_tahun(2010)

if __name__=='__main__':
    main()