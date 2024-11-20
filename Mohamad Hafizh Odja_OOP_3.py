class Buku:

    def __init__(self, judul, pengarang, tahun, pinjam):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit  = tahun
        self.pinjam = pinjam

    def info_buku(self):
        print(self.judul, "oleh", self.pengarang, "tahun terbit", self.tahun_terbit, "status : ", self.pinjam)
    
    def pinjam_buku(self):
        if self.pinjam == True:
            print("Buku berhasil dipinjam.")
        else:
            print("Buku tidak dipinjam.")

    def kembalikan_buku(self):
        if self.pinjam == True:
            self.pinjam = False
            print("Buku sudah di pinjam.")
        else:
            print("Buku berhasil dikembalikan")
    
def main():
    # false -> tidak dipinjam
    # true -> dipinjam
    buku1 = Buku("Laskar Pelangi", "Andrea Hinata", 2005,False)
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