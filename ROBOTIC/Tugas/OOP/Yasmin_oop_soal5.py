class Barang:
    def __init__(self, barang, berat):
        self.nama_barang = barang
        self.berat_barang = berat

    def info_barang(self):
        return(f"Nama Barang: {self.nama_barang},  Berat: {self.berat_barang} kg")

class Kurir:
    def __init__(self, nama_kurir):
        self.nama_kurir = nama_kurir

    def ambil_barang(self, barang):
        return f"{self.nama_kurir} telah mengambil barang1: {barang.nama_barang}"

class Pengiriman:
    def __init__(self, barang, nama_kurir):
        self.barang = barang
        self.nama_kurir = nama_kurir

    def proses_pengiriman(self):
        print(self.nama_kurir.ambil_barang(self.barang)) 
        print("Pengiriman diproses...")
        print(f"Kurir: {self.nama_kurir.nama_kurir}")
        print(self.barang.info_barang())

def main():
    barang1 = Barang("Laptop", 2.5)
    kurir1 = Kurir("Joko")
    pengiriman = Pengiriman(barang1, kurir1)
    pengiriman.proses_pengiriman()

if __name__ == '__main__':
    main()