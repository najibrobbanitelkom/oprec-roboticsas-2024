class Persegi:
    def __init__(self, sisi):
        self.sisi = sisi
    
    def luas(self): 
       return self.sisi*self.sisi

    def keliling(self): 
        return 4*self.sisi

    def print(self):
        print(f"Luas = {self.luas()}   Keliling = {self.keliling()}")

def main():
   p = Persegi(3)
   p.print()

if __name__ == '__main__':
    main()