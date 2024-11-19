class Barang:
    def __init__(self, nama, berat):
        self.nama = nama
        self.berat = berat

    def info_barang(self):
        return f"Nama Barang: {self.nama}, Berat: {self.berat} kg"

class Kurir:
    def __init__(self, nama):
        self.nama = nama
        self.barang = None

    def ambil_barang(self, barang):
        self.barang = barang
        print(f"Kurir telah mengambil barang: {barang.nama}")

    def info_kurir(self):
        return f"Kurir: {self.nama}"

class Pengiriman:
    def __init__(self, barang, kurir):
        self.barang = barang
        self.kurir = kurir

    def proses_pengiriman(self):
        print("Pengiriman diproses.")
        print(self.kurir.info_kurir())
        print(self.barang.info_barang())

def main():
    
    barang1 = Barang("Laptop", 2.5)
    
    kurir1 = Kurir("Joko")
    
    kurir1.ambil_barang(barang1)
    
    pengiriman = Pengiriman(barang1, kurir1)
    
    pengiriman.proses_pengiriman()

if __name__ == "__main__":
    main()
