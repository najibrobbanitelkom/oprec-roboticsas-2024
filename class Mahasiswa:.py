class Mahasiswa:
    def __init__(self, nama, jurusan, angkatan):
        self.nama = nama
        self.jurusan = jurusan
        self.angkatan = angkatan

    def des_mahasiswa(self):
        print("nama mahasiswa", self.nama,"jurursan", self.jurusan,"angkatan",self.angkatan)

def main():
    mhs1 = Mahasiswa("Audrey", "informatika", 2024)
    mhs2 = Mahasiswa("Lina", "informatika", 2024)
    mhs1.des_mahasiswa()
    mhs2.des_mahasiswa()

if __name__ =='__main__':
    main()