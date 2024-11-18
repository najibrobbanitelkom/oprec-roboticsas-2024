class Buku:
    def __init__(self, judul, pengarang, tahun_terbit, status):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit
        self.status = status
    
    def info_buku(self):
        if self.status == False:
            status = "tidak dipinjam"
        else:
            status = "dipinjam"
        
        print(f"{self.judul} oleh {self.pengarang}, diterbitkan pada tahun {self.tahun_terbit}. Status: {status}")
    
    def pinjam_buku(self):
        if self.status == True:
            print("Buku sudah dipinjam")
        else:
            print("Buku berhasil dipinjam")
            self.status = True
    
    def kembalikan_buku(self):
        if self.status == True:
            print("Buku berhasil dikembalikan")
            self.status = False
        else:
            print("Buku belum dipinjam")

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
    print()

if __name__ == '__main__':
    main()