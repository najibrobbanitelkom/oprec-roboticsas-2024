class mahasiswa:
    def __init__(self, nama, jurusan, angkatan):
        self.nama = nama
        self.jurusan = jurusan
        self.angkatan = angkatan

    def keterangan_mahasiswa(self):
        print("Nama:", self.nama, "Jurusan:", self.jurusan, "Angkatan:", self.angkatan)

def main():
    mahasiswa1 = mahasiswa("Lina", "Informatika", 2024)
    mahasiswa2 = mahasiswa("Audrey", "Informatika", 2030)
    mahasiswa3 = mahasiswa("Hanni", "Informatika", 2024)
    mahasiswa1.keterangan_mahasiswa()
    mahasiswa2.keterangan_mahasiswa()
    mahasiswa3.keterangan_mahasiswa()

if __name__== '__main__':
    main()
