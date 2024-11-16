class Bio: 
    jenis = "biodata"
    def __init__(self, nama, jurusan, angkatan):
        self.nama = nama
        self.jurusan = jurusan
        self.angkatan = angkatan

    def deskripsi_bio(self):
        print(self.nama,self.jurusan,self.angkatan,self.jenis)

def main():
    Bio1 = Bio("Mohamad hafizh","s1 teknik elektro",2023)
    Bio1.deskripsi_bio()

if __name__=='__main__': 
    main()