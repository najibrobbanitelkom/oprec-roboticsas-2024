class Mahasiswa:
    def __init__(data, nama, jurusan, angkatan):
        data.nama = nama
        data.jurusan = jurusan
        data.angkatan = angkatan

    def deskripsi_mahasiswa(data):
        print("nama", data.nama, "jurusan", data.jurusan, "dari angkatan", data.angkatan)

def main():
    mahasiswa1 = Mahasiswa("Alyaa", "Informatika", "48")
    mahasiswa2 = Mahasiswa("Hanni", "DKV", "48")
    mahasiswa1.deskripsi_mahasiswa()
    mahasiswa2.deskripsi_mahasiswa()

if __name__=='__main__':
    main()
