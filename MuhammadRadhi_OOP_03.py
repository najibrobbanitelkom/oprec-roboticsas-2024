class Buku:
    def __init__(self, judul, penulis, tahun_terbit, status_pinjam=False):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit
        self.status_pinjam = status_pinjam

    def info_buku(self):
        print(f"Judul: {self.judul}")
        print(f"Penulis: {self.penulis}")
        print(f"Tahun Terbit: {self.tahun_terbit}")
        print(f"Status: {'Dipinjam' if self.status_pinjam else 'Tidak Dipinjam'}")

    def pinjam_buku(self):
        if self.status_pinjam:
            print("Buku sudah dipinjam")
        else:
            self.status_pinjam = True
            print("Buku berhasil dipinjam")

    def kembalikan_buku(self):
        if not self.status_pinjam:
            print("Buku belum dipinjam")
        else:
            self.status_pinjam = False
            print("Buku berhasil dikembalikan")

def main():
    buku1 = Buku("Laskar Pelangi", "Andrea Hirata", 2005)
    buku1.info_buku()
    print()
    
    buku1.pinjam_buku()
    print()
    buku1.info_buku()
    print()
    
    buku1.kembalikan_buku()
    print()
    buku1.info_buku()

if __name__ == "__main__":
    main()
