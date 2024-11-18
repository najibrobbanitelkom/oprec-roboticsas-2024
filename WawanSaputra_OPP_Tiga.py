class Buku:
    def __init__(self, judul, pengarang, tahun_terbit, status):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit
        self.status = status
    
    def info_buku(self):
        status_str = "dipinjam" if self.status else "tidak dipinjam"
        print(f"{self.judul} oleh {self.pengarang}, diterbitkan pada tahun {self.tahun_terbit}. Status: {status_str}")
    
    def pinjam_buku(self):
        if(self.status == False):
            self.status = True
            print("Buku berhasil dipinjam.")
        else:
            print("Buku sudah dipinjam.")

    def kembalikan_buku(self):
        if(self.status == True):
            self.status = False
            print("Buku berhasil dikembalikan.")
        else:
            print("Buku belum dipinjam.")

def main():
    # False -> tidak dipinjam
    # True -> dipinjam
    buku = Buku("Laskar Pelangi", "Andrea Hirata", 2005, False)
    buku.info_buku() #1
    print()
    buku.pinjam_buku() #2
    print()
    buku.info_buku() #3
    print()
    buku.kembalikan_buku() #4
    print()
    buku.info_buku() #5
    print()
    buku.kembalikan_buku() #7

if __name__ == '__main__':
    main()