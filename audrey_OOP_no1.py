class Persegi:
    def __init__(self, sisi):
        self.sisi = sisi

    def hitung(self):
        luas = self.sisi * self.sisi
        keliling = 4 * self.sisi
        return luas, keliling
    
    def print(self):
        luas, keliling = self.hitung()
        print("Luas =", luas," keliling =", keliling)

def main():
    p = Persegi(3)
    p.print()

if __name__ == '__main__':
    main()