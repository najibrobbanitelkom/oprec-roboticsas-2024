class Barang:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def info_barang(self):
        print(f'{self.name} {self.weight}')

class Kurir: 
    def __init__(self, name):
        self.name = name

    def ambil_barang(self, item):
        print(item.name)

class Peingiriman:
    def __init__(self, item, kurir):
        self.kurir = kurir
        self.item = item

    def proses_pengiriman(self):
        print(f'{self.kurir.name} telah mengambil barang: {self.item.name}')
        print(f'pengiriman diproses...')
        print(f'Kurir: {self.kurir.name} \nNama barang: {self.item.name}, Berat: {self.item.weight}')

def main():
    barang1 = Barang('Laptop', 2.5)
    kurir1 = Kurir('Joko')
    pengiriman = Peingiriman(barang1, kurir1)

    pengiriman.proses_pengiriman()

main()