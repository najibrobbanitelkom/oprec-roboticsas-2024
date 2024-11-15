class Data:
    def __init__(self, nama, jurusan, angkatan):
        self.nama = nama
        self.jurusan = jurusan
        self.angkatan = angkatan
    
    def deskripsi_data(self):
        print(self.nama,self.jurusan,self.angkatan)

def main():
    datadiri1 = Data("Reynard Elroy Rande", "RPL", "2024")
    datadiri1.deskripsi_data()

if __name__ == '__main__':
    main()