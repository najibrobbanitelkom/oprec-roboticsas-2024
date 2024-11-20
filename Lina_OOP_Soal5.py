class barang:
    def __init__(self, benda, berat):
        self.benda = benda
        self.berat = berat

    def info_barang(self):
        print("Nama barang:", self.benda, ", Berat:", self.berat, "kg")

class kurir:
    def __init__(self, nama):
        self.nama = nama

    def barang_ambil(self, benda):
        self.benda = benda
        print(self.nama, "telah mengambil barang1:", benda.benda)

class Pengiriman:
    def __init__(self, barang, kurir):
        self.barang = barang
        self.kurir = kurir
    
    def proses_pengiriman(self):
        self.kurir.barang_ambil(self.barang)
        print("Pengiriman diproses...")
        print("Kurir:", self.kurir.nama)
        self.barang.info_barang()

def main():
    barang1 = barang("Laptop", 2.5)
    kurir1 = kurir("Joko")
    pengiriman = Pengiriman(barang1, kurir1)
    pengiriman.proses_pengiriman()

if __name__ == '__main__':
    main()