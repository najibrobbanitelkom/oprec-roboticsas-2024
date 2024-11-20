class buku:
    def __init__(self, judul, author, tahun, pinjam):
        self.judul = judul
        self.author = author
        self.tahun = tahun
        self.pinjam = pinjam
    
    def info_buku(self):
        if self.pinjam:
            print(self.judul, "oleh", self.author, "pada tahun", self.tahun, "Status: dipinjam")
        else:
            print(self.judul, "oleh", self.author, "pada tahun", self.tahun, "Status: tidak dipinjam")
    
    def pinjam_buku(self):
        if not self.pinjam:
            self.pinjam = True
            print("Buku berhasil dipinjam!")
        else:
            print("Buku sudah dipinjam.")

    def kembalikan_buku(self):
        if self.pinjam:
            self.pinjam = False
            print("Buku berhasil dikembalikan!")
        else:
            print("Buku belum dipinjam.")

def main():
    buku1 = buku("Laskar Pelangi", "Andrea Hirata", 2005, False)
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

if __name__ == '__main__':
    main()