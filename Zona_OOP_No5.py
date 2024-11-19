class Barang:
    def __init__(self, nama, berat):
        self.nama = nama
        self.berat = berat

    def info_barang(self):
        return f"Nama Barang: {self.nama}, Berat: {self.berat} kg"

class Kurir:
    def __init__(self, nama):
        self.nama = nama

    def ambil_barang(self, barang):
        return f"{self.nama} telah mengambil barang1: {barang.nama}"

class Pengiriman:
    def __init__(self, barang, kurir):
        self.barang = barang
        self.kurir = kurir

    def proses_pengiriman(self):
        print(self.kurir.ambil_barang(self.barang))
        print("Pengiriman diproses...")
        print(f"Kurir: {self.kurir.nama}")
        print(self.barang.info_barang())

def main():
    barang1 = Barang("Laptop", 2.5)

    kurir1 = Kurir("Joko")

    pengiriman = Pengiriman(barang1, kurir1)

    pengiriman.proses_pengiriman()

if __name__ == "__main__":
    main()
