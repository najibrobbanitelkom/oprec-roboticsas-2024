class Mahasiswa:
    def __init__(self, nama, jurusan, angkatan):
        self.nama = nama
        self.jurusan = jurusan
        self.angkatan = angkatan

    def perkenalan_mahasiswa(self):
        print("Nama : ", self.nama, "\nJurusan: ", self.jurusan, "\nAngkatan: ",self.angkatan)
        print("======================================")

def main():
    mahasiswa1 = Mahasiswa("Aaa", "ilkom", 23)
    mahasiswa2 = Mahasiswa("bbb", "infor", 29)
    mahasiswa1.perkenalan_mahasiswa()
    mahasiswa2.perkenalan_mahasiswa()

if __name__ == '__main__':
    main()