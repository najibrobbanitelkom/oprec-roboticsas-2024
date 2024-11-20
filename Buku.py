class Buku:
    def __init__(self, judul, penulis, tahun, status):
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun
        self.status = status   

    def pinjam_buku(self):
        if self.status == True:
            print("Buku sudah dipinjam")
        elif self.status == False:
            self.status = True 
            print("Buku berhasil dipinjam")

    def kembalikan_buku(self):
        if self.status == False:
            print("Buku belum dipinjam.")
        elif self.status == True:
            self.status = False  
            print("Buku berhasil dikembalikan.")

    def info_buku(self):
        status_buku = "dipinjam" if self.status else "tidak dipinjam"
        print(self.judul, "oleh", self.penulis, "diterbitkan pada tahun", self.tahun, "Status:", status_buku)
 

def main():
    buku1 = Buku("Laskar Pelangi", "Andrea Hirata", 2005,False)
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
    print()

if __name__=='__main__':
    main()
    