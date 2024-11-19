class Persegi:
    def __init__(self, sisi):
        self.sisi = sisi

    def keliling(self):
        return 4 * self.sisi


    def luas(self):
        return self.sisi ** 2

    def print(self):
        print(f"Luas = {self.luas() } Keliling = {self.keliling()}")

def main():
    p = Persegi(3)
    p.print()

if __name__ == "__main__":
    main()