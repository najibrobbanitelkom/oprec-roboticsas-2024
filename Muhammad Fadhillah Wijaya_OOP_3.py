class Buku():
    def __init__(self, judul:str, penulis:str, tahun:int, status:bool = False):
        assert isinstance(judul,str), 'Value of judul should be string.'
        assert isinstance(penulis,str), 'Value of penulis should be string.'
        assert isinstance(tahun,int), 'Value of tahun should be integer.'
        assert isinstance(status,bool), 'Value of judul should be boolean.'

        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun
        self.status = status

    def info_buku(self):
        if self.status == True:
            stat = "dipinjam"
        else:
            stat = "tidak dipinjam"

        print(f'{self.judul} oleh {self.penulis}, diterbitkan pada tahun {self.tahun}. Status: {stat}')

    def pinjam_buku(self):
        if self.status == True:
            print('Buku sudah dipinjam.')
        else:
            self.status = True
            print('Buku berhasil dipinjam.')

    def kembalikan_buku(self):
        if self.status == False:
            print('Buku belum dipinjam.')
        else:
            self.status = False
            print('Buku berhasil dikembalikan.')

def main():
    buku1 = Buku("Laskar Pelangi", "Andrea Hirata", 2005, False)
    buku1.info_buku()
    print()
    buku1.pinjam_buku()
    print()
    buku1.info_buku()
    print()
    buku1.pinjam_buku()
    print()
    buku1.kembalikan_buku()
    print()
    buku1.info_buku()
    print()
    buku1.kembalikan_buku()

if __name__=='__main__':
    main()