class Karyawan():
    def __init__(self, nama:str, jabatan:str):
        assert isinstance(nama,str), 'Value of nama should be string.'
        assert isinstance(jabatan,str), 'Value of jabatan should be string.'

        self.Nama = nama
        self.Jabatan = jabatan
    
    def info_karyawan(self):
        print(f'Nama: {self.Nama}, Jabatan: {self.Jabatan}')

class Perusahaan():
    def __init__(self, namaP, k:Karyawan):
        assert isinstance(k, Karyawan), 'k should be Karyawan(class)'

        self.Nama_perusahaan = str(namaP)
        self.Karyawan_pertama = k
    
    def tampilkan_info(self):
        print(f'Perusahaan: {self.Nama_perusahaan}')
        print('Karyawan pertama yang bekerja:')
        self.Karyawan_pertama.info_karyawan()

def main():
    karyawan1 = Karyawan("Andi", "Manager")
    perusahaan = Perusahaan("PT. Maju Jaya", karyawan1)

    perusahaan.tampilkan_info()

if __name__ == '__main__' :
    main()
