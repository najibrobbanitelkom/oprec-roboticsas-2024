class Buku:
    def __init__(self, judul, author, tahun, peminjaman):
        self.judul = judul
        self.author = author
        self.tahun = tahun
        self.peminjaman = peminjaman

    def pinjam_buku(self):
        if not self.peminjaman:
            self.peminjaman = True
            print("buku berhasil dipinjam")
        else:
            print("buku sudah dipinjam")      

    def kembalikan_buku(self):
        if self.peminjaman:
            self.peminjaman = False
            print("buku berhasil dikembalikan")
        else:
            print("buku belum dipinjam")

    def info_buku(self):
        if not self.peminjaman:
            print(self.judul, "oleh", self.author,", diterbitkan pada tahun", self.tahun,". Status: tidak dipinjam")
        else:
            print(self.judul, "oleh", self.author,", diterbitkan pada tahun", self.tahun,". Status: dipinjam")

def main():
    # false -> tdk dipinjam
    # true -> dipinjam

    buku1 = Buku("Laskar Pelangi", "Andrea Hirata", 2005, False)
    buku1.info_buku()#1
    print()
    buku1.pinjam_buku()#2
    print()
    buku1.info_buku()#3
    print()
    buku1.pinjam_buku()#4
    print()
    buku1.kembalikan_buku()#5
    print()
    buku1.info_buku()#6
    print()
    buku1.kembalikan_buku()#7

if __name__ == "__main__":
    main()