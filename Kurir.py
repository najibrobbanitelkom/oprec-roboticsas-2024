class Barang:
    def __init__(self, nama, berat):
        self.nama = nama
        self.berat = berat

    def info_barang(self):
       print("Nama Barang:", self.nama,"," , "Berat:", self.berat, "kg")

class Kurir:
    def __init__(self, kurir):
        self.kurir = kurir 
        self.barang = None    

    def ambil_barang(self, barang):
        self.barang = barang
        print(self.kurir, "telah mengambil barang1:",self.barang.nama) 
        print("Pengiriman diproses...")

class Pengiriman:
    def __init__(self, barang, kurir):
        self.barang = barang
        self.kurir = kurir

    def proses_pengiriman(self):
        self.kurir.ambil_barang(self.barang)
        print("Kurir:", self.kurir.kurir)
        self.barang.info_barang()


def main():
   barang1 = Barang("Laptop", 2.5)
   kurir1 = Kurir("Joko")
   pengiriman = Pengiriman(barang1, kurir1)
   pengiriman.proses_pengiriman()

if __name__=='__main__':
    main() 