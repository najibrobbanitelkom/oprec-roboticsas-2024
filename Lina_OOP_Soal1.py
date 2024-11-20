class persegi:
    def __init__(self, s):
        self.s = s

    def luas(self):
        return self.s*self.s

    def keliling(self):
        return 4*self.s
        
    def hasil(self):
        print(f"Luas = {self.luas()}")
        print(f"Keliling = {self.keliling()}")

def main():
    p = persegi(3)
    p.hasil()

if __name__ == '__main__':
    main()