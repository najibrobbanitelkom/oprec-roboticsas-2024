class karyawan:
    def __init__(self, nama, jabatan):
        self.nama = nama
        self.jabatan = jabatan

    def info_karyawan(self):
        print("Nama:", self.nama, ", Jabatan:", self.jabatan)

class Perusahaan:
    def __init__(self, nama_perusahaan, karyawan_1):
        self.perusahaan = nama_perusahaan
        self.karyawan = karyawan_1

    def tampilkan_info(self):
        print("Perusahaan:", self.perusahaan)
        print("Karyawan pertama yang bekerja:")
        self.karyawan.info_karyawan()

def main():
    karyawan1 = karyawan("Andi", "Manager")
    perusahaan = Perusahaan("PT. Maju Jaya", karyawan1)
    perusahaan.tampilkan_info()

if __name__ == '__main__':
    main()