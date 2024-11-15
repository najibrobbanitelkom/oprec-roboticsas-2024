class Mahasiswa:
    def __init__(self, nama, kelas, angkatan):
        self.nama = nama
        self.kelas = kelas
        self.angkatan = angkatan

    def perkenalan(self): print(f'nama saya {self.nama} dari kelas {self.kelas} angkatan {self.angkatan}')

class Dosen:
    def __init__(self, dosen, nama, kelas, angkatan):
        self.name = dosen
        self.mahasiswa = Mahasiswa(nama, kelas, angkatan)

    def memperkenalkan(self):
        print(f'karna bu {self.name} telah mempersilahkan saya untuk mengenalkan diri')
        self.mahasiswa.perkenalan()

def main():
    person1 = Dosen('Mia' ,'azuki', 'D3IF', 2024)
    person1.memperkenalkan()

main()