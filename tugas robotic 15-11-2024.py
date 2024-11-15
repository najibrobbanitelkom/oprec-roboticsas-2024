class mahasiswa:

    jenis = "data diri"

    def __init__(self, nama, jurusan, angkatan):
        self.nama = nama
        self.jurusan = jurusan
        self.angkatan = angkatan

    def deskripsi(self):
        print("Nama:", self.nama, ",Jurusan:", self.jurusan, ",Angkatan:", self.angkatan)

def main():
    mahasiswa1 = mahasiswa("Radhi", "Software Engineer","2024")
    mahasiswa1.deskripsi()

if __name__ == "__main__":
    main()
