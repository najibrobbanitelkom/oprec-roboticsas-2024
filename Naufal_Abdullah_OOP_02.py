class Mobil:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def info_mobil(self):
        print(f'Mobil {self.brand} {self.model} keluaran tahun {self.year}')
    
    def ubah_tahun(self, changeYear):
        if(changeYear <= self.year): return print('Error: Tahun tidak valid')
        self.year = changeYear

def main():
    mobil1 = Mobil('Toyta', 'Avanza', 2015)
    mobil1.info_mobil()
    mobil1.ubah_tahun(2023)
    mobil1.info_mobil()
    mobil1.ubah_tahun(2011)

main()