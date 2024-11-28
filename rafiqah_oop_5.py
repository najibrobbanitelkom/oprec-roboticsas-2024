class barang:
    def __init__(self, nama_barang, berat_barang):
        self.nama_barang = nama_barang
        self.berat_barang = berat_barang
    
    def info_barang(self):
        return f"Nama barang: {self.nama_barang}, Berat: {self.berat_barang}"

class kurir:
    def __init__(self, nama):
        self.nama = nama
    
    def ambil_barang(self, barang):
        return f"{self.nama} telah mengambil barang1: {barang.nama_barang}"

class pengiriman:
    def __init__(self, barang, kurir):
        self.barang = barang
        self.kurir = kurir
    
    def proses_pengiriman(self):
        print(self.kurir.ambil_barang(self.barang))
        print("pengiriman diproses....")
        print(f"kurir: {self.kurir.nama}")
        print(self.barang.info_barang())
    
def main():
    barang1 = barang("Album", 2.5)
    kurir1 = kurir("Fizzy")
    pengiriman = pengiriman(barang1, kurir1)
    pengiriman.proses_pengiriman()

if __name__ == '__main__':
    main()