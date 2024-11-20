class Barang():
    """berat dalam kg"""

    def __init__(self,barang:str,berat:float):
        if berat == int:
            berat = float(berat)
        assert isinstance(berat,float), 'Value of berat should be integer or float.'

        self.barang = barang
        self.berat = berat

    def info_barang(self):
        print(f'Nama Barang: {self.barang}, Berat: {self.berat} kg')

class Kurir():

    def __init__(self,nama:str):
        assert isinstance(nama,str), 'Value of nama should be string.'

        self.nama = nama

    def ambil_barang(self,b:Barang = None):
        assert isinstance(b,Barang), 'b should be Barang(class)'

        self.b = b
        print(f'{self.nama} telah mengambil barang1: {self.b.barang}')

class Pengiriman():

    def __init__(self,b:Barang,k:Kurir):
        assert isinstance(b,Barang), 'b should be Barang(class)'
        assert isinstance(k,Kurir), 'k should be Kurir(class)'

        self.b = b
        self.k = k

    def proses_pengiriman(self):
        self.k.ambil_barang(self.b)
        print('Pengiriman diproses...')
        print(f'Kurir: {self.k.nama}')
        self.b.info_barang()

def main():
    barang1 = Barang("Laptop", 2.5)
    kurir1 = Kurir("Joko")
    pengiriman = Pengiriman(barang1, kurir1)
    pengiriman.proses_pengiriman()

if __name__ == '__main__':
    main()