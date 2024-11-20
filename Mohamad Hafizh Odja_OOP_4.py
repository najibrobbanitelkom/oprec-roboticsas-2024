class Karyawan:
    def __init__(self, nama, jabatan):
        self.nama = nama
        self.jabatan = jabatan

    def deskripsi_karyawan(self):
         print(f"Nama: {self.nama}, Jabatan: {self.jabatan}")

class Perusahaan:
    def __init__(self, nama_pt, urut_karyawan):
        self.nama_pt = nama_pt
        self.urut_karyawan = urut_karyawan

    def tampilan_info(self):
        print("Perusahaan:", self.nama_pt)
        print("Karyawan pertama yang bekerja:")
        self.urut_karyawan.deskripsi_karyawan()

def main():
    karyawan1 = Karyawan("Andi", "Manager")
    perusahaan = Perusahaan("PT. Maju Jaya", karyawan1)

    perusahaan.tampilan_info()

if __name__ == '__main__':
    main()

