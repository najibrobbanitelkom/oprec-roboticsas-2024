class persegi:
    def __init__(self, sisi):
       self.sisi = sisi

    def keliling(self):
       self.keliling = self.sisi * 4

    def luas(self):
        self.luas = self.sisi ** 2
    
    def print(self):
        self.keliling()
        self.luas()
        print(f"luas =", self.luas)
        print(f"keliling =", self.keliling)
       
def main ():
    p = persegi(3)
    p.print()

if __name__ == '__main__':
    main()