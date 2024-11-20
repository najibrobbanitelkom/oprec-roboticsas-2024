class Barang:
    def __init__(self, JenisBarang, BeratBarang):
        self.JenisBarang = JenisBarang
        self.BeratBarang = BeratBarang
    
    def Deskripsi_barang(self):
        print("Nama Barang:", self.JenisBarang, "Berat:",self.BeratBarang)

class Kurir:
    def __init__(self, NamaKurir):
        self.nama_kurir = NamaKurir

    def deskripsi_kurir(self):
        print("kurir:", self.nama_kurir)
        
class Pengiriman:
    def __init__(self, barang, kurir):
        self.barang = barang
        self.kurir = kurir

    def proses_pengiriman(self):
        print(self.kurir.nama_kurir, "telah mengambil barang1:", self.barang.JenisBarang)
        print("pengiriman diproses...")
        self.kurir.deskripsi_kurir()
        self.barang.Deskripsi_barang()

def main():
    # Membuat objek barang 1
    barang1 = Barang("Laptop", 2.5)
    # Membuat objek kurir
    kurir1 = Kurir("Joko")
    # Membuat objek pengiriman
    pengiriman = Pengiriman(barang1, kurir1)
    # Membuat proses pengiriman
    pengiriman.proses_pengiriman()

if __name__ == '__main__':
    main()
