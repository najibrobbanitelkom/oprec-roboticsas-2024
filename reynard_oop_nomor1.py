class Persegi:
    def __init__(self, sisi):
        self.sisi = sisi
    
    def print(self):
        print("Luas =", self.sisi*self.sisi)
        print("Keliling =", self.sisi*4)

def main():
    p = Persegi(3)
    p.print()

if __name__ == '__main__':
    main()