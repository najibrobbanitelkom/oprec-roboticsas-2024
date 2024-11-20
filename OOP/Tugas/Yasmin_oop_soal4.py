class Karyawan:
    def __init__(self, nama, jabatan):
        self.nama = nama
        self.jabatan = jabatan

    def info_karyawan(self):
        return(f"Nama: {self.nama}, Jabatan: {self.jabatan}")

class Perusahaan:
    def __init__(self, nama_perusahaan, karyawan_pertama):
        self.nama_perusahaan = nama_perusahaan
        self.karyawan_pertama = karyawan_pertama

    def tampilkan_info(self):
        print(f"Perusahaan: {self.nama_perusahaan}")
        print(f"Karyawan pertama yang bekerja: \n{self.karyawan_pertama.info_karyawan()}")

def main():
    karyawan1 = Karyawan("Andi", "Manager")
    perusahaan = Perusahaan("PT. Maju Jaya", karyawan1)

    perusahaan.tampilkan_info()

if __name__ == '__main__':
    main()