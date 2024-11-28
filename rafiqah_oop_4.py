class karyawan:
    def __init__(self, nama, jabatan):
        self.nama = nama
        self.jabatan = jabatan
    
    def info_karyawan(self, namaperusahaan):
        print("company:", namaperusahaan)
        print("karyawan pertama yang bekerja:")
        print(f"Nama : {self.nama}, Jabatan: {self.jabatan}")

class company:
    def __init__(self, nama_perusahaan, karyawan):
        self.nama_perusahaan = nama_perusahaan
        self.karyawan_pertama = karyawan
    
    def tampilkan_info(self):
        self.karyawan_pertama.info_karyawan(self.nama_perusahaan)

def main():
    karyawan1 = karyawan("Andi", "Manager")
    perusahaan = company("PT. Maju Jaya", karyawan1)

    perusahaan.tampilkan_info()

if __name__ == '__main__':
    main()