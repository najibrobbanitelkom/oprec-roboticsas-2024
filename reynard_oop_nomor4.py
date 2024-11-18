class Karyawan:
    def __init__(self, nama, jabatan):
        self.nama = nama
        self.jabatan = jabatan
    
    def info_karyawan(self, namaperusahaan):
        print("Perusahaan:", namaperusahaan)
        print("Karyawan pertama yang bekerja:")
        print(f"Nama : {self.nama}, Jabatan: {self.jabatan}")

class Perusahaan:
    def __init__(self, nama_perusahaan, Karyawan):
        self.nama_perusahaan = nama_perusahaan
        self.karyawan_pertama = Karyawan
    
    def tampilkan_info(self):
        self.karyawan_pertama.info_karyawan(self.nama_perusahaan)

def main():
    karyawan1 = Karyawan("Andi", "Manager")
    perusahaan = Perusahaan("PT. Maju Jaya", karyawan1)

    perusahaan.tampilkan_info()

if __name__ == '__main__':
    main()