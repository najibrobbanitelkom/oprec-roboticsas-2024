class profil:
    def __init__(self, nama, nim, jurusan, angkatan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan 
        self.angkatan = angkatan
        
    def deskripsi(self):
        print(self.nama,self.nim,self.jurusan,self.angkatan)
        
def main():
    profil1 = profil("Wawan Saputra", 103022400098, "RPL", 2024)
    profil1.deskripsi()
    
if __name__ == '__main__':
    main()