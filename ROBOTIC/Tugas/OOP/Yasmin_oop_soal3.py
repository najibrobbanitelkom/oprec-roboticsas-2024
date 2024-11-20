class Buku:
    def __init__(self, judul, penulis, tahun_terbit, status_pinjam):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit
        self.judul = judul
        self.status_pinjam = False

    def info_buku(self):
        if self.status_pinjam == False :
            status = "tidak dipinjam"
        else:
            status = "dipinjam"
        print(f"{self.judul} oleh {self.penulis}, diterbitkan pada tahun {self.tahun_terbit}, Status: {status}")

    def pinjam_buku(self):
        if self.status_pinjam == False :
            self.status_pinjam = True
            print("Buku berhasil dipinjam")
        else:
            print("Buku sudah dipinjam")

    def kembalikan_buku(self):
        if self.status_pinjam == False :
            print("Buku belum dipinjam")
            self.status_pinjam = True
        else:
            print("Buku berhasil dikembalikan")
            self.status_pinjam = False

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

if __name__ == '__main__':
    main()