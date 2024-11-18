class Buku:
    def __init__(self,judul, penulis, tahun, pinjam):
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun
        self.pinjam = pinjam

    def info_buku(self):
        if self.pinjam == True:
            print(self.judul, "oleh", self.penulis, "diterbitkan pada tahun", self.tahun, "Status: dipinjam" )
        else:
            print(self.judul, "oleh", self.penulis, "diterbitkan pada tahun", self.tahun, "Status: tidak dipinjam")

    def Pinjam_buku(self):
        if self.pinjam == True:
            print("Buku sudah dipinjam")
        else:
            print("Buku berhasil dipinjam")
            self.pinjam = True

    def Kembalikan_buku(self):
        if self.pinjam == True:
            print("Buku berhasil dikembalikan")
            self.pinjam = False
        else:
            print("Buku belum dipinjam")

def main():
    buku1 = Buku("Laskar Pelangi", "Andrea Hirata", 2005, False)
    buku1.info_buku()
    print()
    buku1.Pinjam_buku()
    print()
    buku1.info_buku()
    print()
    buku1.Pinjam_buku()
    print()
    buku1.Kembalikan_buku()
    print()
    buku1.info_buku()
    print()
    buku1.Kembalikan_buku()


if __name__ == '__main__':
    main()