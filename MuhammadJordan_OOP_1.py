class Persegi:
    def __init__(self,x):
        self.x = x

    def luas(self):
        return self.x * self.x
    
    def keliling(self):
        return 4 * self.x

    def print(self):
        print("Luas =", self.luas(), "Keliling =", self.keliling())
    
def main():
    p = Persegi(3)
    p.print()

if __name__ == '__main__':
    main()
    