class Mahasiswa:

    def __init__(self, nama, jurusan, angkatan):
        self.nama = nama
        self.jurusan = jurusan
        self.angkatan = angkatan

    def deskripsi_mahasiswa(self):
        print(self.nama,"dari Jurusan", self.jurusan, "dari angkatan", self.angkatan)


def main():
    Mahasiswa1 = Mahasiswa("Zona","S1 Informatika", 48)
    Mahasiswa2 = Mahasiswa("Mustofa","Ilmu Terapan", 47)   
    Mahasiswa1.deskripsi_mahasiswa()
    Mahasiswa2.deskripsi_mahasiswa()

if __name__ == '__main__':
    main()