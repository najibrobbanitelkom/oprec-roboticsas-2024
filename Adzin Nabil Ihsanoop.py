class Mahasiswa:

    def __init__(self, nama, jurusan , angkatan):
        self.nama = nama
        self.jurusan = jurusan
        self.angkatan = angkatan
    
    def tampilkan_mahasiswa(self):
        print(self.nama, self.angkatan, self.jurusan)


def main():
    mahasiswa1= Mahasiswa("Adzin Nabil Ihsan", "Teknik ELektro", 2024)
    mahasiswa1.tampilkan_mahasiswa()

    


if __name__=='__main__':
    main()