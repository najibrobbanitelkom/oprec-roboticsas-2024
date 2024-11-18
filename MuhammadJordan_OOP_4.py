class Karyawan:
    def __init__(self, nama, jabatan):
        self.nama = nama
        self.jabatan = jabatan
    def info_karyawan(self):
        print("Nama:", self.nama, "Jabatan:", self.jabatan)

class Perusahaan:
    def __init__(self, Nama_Perusahaan, Karyawan_Pertama):
        self.Perusahaan = Nama_Perusahaan
        self.Karyawanpertama = Karyawan_Pertama

    def Tampilkan_info(self):
        print("Perusahaan:", self.Perusahaan)
        print("Karyawan pertama yang berkerja:")
        self.Karyawanpertama.info_karyawan()
def main():
    karyawan1 = Karyawan("Andi", "Manager")
    perusahaan = Perusahaan("PT. Maju Jaya", karyawan1)

    perusahaan.Tampilkan_info()

if __name__ == '__main__':
    main()


