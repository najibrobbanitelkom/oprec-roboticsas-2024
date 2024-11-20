class Persegi:
    def __init__(self, sisi):
        self.sisi = sisi
        self.luas = 0
        self.keliling = 0

    def hitung(self):
        self.luas = self.sisi * self.sisi
        self.keliling = 4 * self.sisi
    
    def print(self):
        self.hitung()
        print("Luas: ", self.luas, "Keliling: ", self.keliling)
    
def main():
    p = Persegi(3)
    p.print()

if __name__=='__main__':
    main()