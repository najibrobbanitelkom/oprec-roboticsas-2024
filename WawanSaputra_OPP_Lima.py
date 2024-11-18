class Barang:
    def __init__(self, namaBarang, beratBarang):
        self.namaBarang = namaBarang
        self.beratBarang = beratBarang

    def info_barang(self):
        print(f"Nama Barang: {self.namaBarang}, Berat: {self.beratBarang} kg")

class Kurir:
    def __init__(self, namaKurir):
        self.namaKurir = namaKurir
        self.barang = None

    def ambil_barang(self, barang):
        self.barang = barang
        print(f"{self.namaKurir} telah mengambil barang1: {self.barang.namaBarang}")

class Pengiriman:
    def __init__(self, barangK, kurirK):
        self.barangK = barangK
        self.kurirK = kurirK

    def proses_pengiriman(self):
        self.kurirK.ambil_barang(self.barangK)
        print("Pengiriman diproses...")
        print(f"Kurir: {self.kurirK.namaKurir}")
        self.barangK.info_barang()


def main():
    # Membuat objek barang1
    barang1 = Barang("Laptop", 2.5)
    # Membuat objek kurir
    kurir1 = Kurir("Joko")
    # Membuat objek pengiriman
    pengiriman = Pengiriman(barang1, kurir1)
    # Memproses pengiriman
    pengiriman.proses_pengiriman()

if __name__ == '__main__':
    main()