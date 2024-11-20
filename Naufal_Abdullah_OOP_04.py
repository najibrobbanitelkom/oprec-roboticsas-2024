class Karyawan:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def info_karyawan(self):
        print(f'{self.name} {self.position}')

class Perusahaan:
    def __init__(self, name, start):
        self.name = name
        self.karyawan = start.name
        self.jabat = start.position

    def tampilkan_info(self):
        print(f'Perusahaan: {self.name} \nKaryawan pertama yang bekerja: \nNama: {self.karyawan}, Jabatan: {self.jabat}')

def main():
    kartap1 = Karyawan('andi', 'manager')
    perusahaan1 = Perusahaan('Asus', kartap1)

    perusahaan1.tampilkan_info()

main()