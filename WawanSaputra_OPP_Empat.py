class Karyawan:
    def __init__(self, nama, jabatan):
        self.nama = nama
        self.jabatan = jabatan

    def info_karyawan(self):
        print(f"Nama: {self.nama}, Jabatan: {self.jabatan}")

class Perusahaan:
    def __init__(self, namaPT, karyawan):
        self.namaPT = namaPT
        self.karyawan = karyawan

    def tampilkan_info(self):
        print(f"Perusahaan: {self.namaPT}")
        print("Karyawan pertama yang bekerja:")
        self.karyawan.info_karyawan()

def main():
    karyawan1 = Karyawan("Andi", "Manager")
    perusahaan = Perusahaan("PT. Maju Jaya", karyawan1)

    perusahaan.tampilkan_info()

if __name__ == '__main__':
    main()