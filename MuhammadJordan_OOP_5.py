class Barang:
    def __init__(self, namabarang, berat):
        self.barang = namabarang
        self.berat = berat

    def info_barang(self):
        print("Nama Barang:", self.barang, "Berat:", self.berat)

class Kurir:
    def __init__(self, namakurir):
        self.kurir = namakurir

    def ambil_barang(self, barang):  
        print(self.kurir, "telah mengambil barang:", barang.barang)

class Pengiriman:
    def __init__(self, kurir, barang):
        self.kurir = kurir
        self.barang = barang

    def proses_pengiriman(self):
        self.kurir.ambil_barang(self.barang)
        print("Pengiriman diproses..")
        print("Kurir:", self.kurir.kurir)
        self.barang.info_barang()

def main():
    barang1 = Barang("Laptop", 2.5)
    kurir1 = Kurir("Joko")
    pengiriman = Pengiriman(kurir1, barang1)

    pengiriman.proses_pengiriman()

if __name__ == '__main__':
    main()
