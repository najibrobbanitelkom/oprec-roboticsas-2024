class Buku:
    def __init__(self, title, writer, releaseYear, borrowed:bool = False):
        self.title = title
        self.writer = writer
        self.releaseYear = releaseYear
        self.borrowed = borrowed

    def info_buku(self):
        print(f'{self.title} oleh {self.writer}, diterbitkan pada tahun {self.releaseYear}. Status: {'dipinjam' if self.borrowed == True else 'tidak dipinjam'}')
    
    def pinjam_buku(self):
        if(self.borrowed == True): return print('buku telah dipinjam')
        self.borrowed = True
        print('buku berhasil dipinjam')

    def kembalikan_buku(self):
        if(self.borrowed == False): return print('buku belum dipinjam')
        self.borrowed = False
        print('buku berhasil dikembalikan')

def main():
    buku = Buku('laskar pelangin', 'marud', 2005, False)
    buku.info_buku()
    print()
    buku.pinjam_buku()
    print()
    buku.info_buku()
    print()
    buku.pinjam_buku()
    print()
    buku.kembalikan_buku()
    print()
    buku.info_buku()
    print()
    buku.kembalikan_buku()
    
main()