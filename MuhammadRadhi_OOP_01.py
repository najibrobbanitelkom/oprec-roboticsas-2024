class Persegi:
    def __init__(self, sisi):
        self.sisi = sisi

    def print(self):
        luas = self.sisi ** 2
        keliling = 4 * self.sisi
        print(f"Luas = {luas}, Keliling = {keliling}")

def main():
    p = Persegi(3)
    p.print()

if __name__ == '__main__':
    main()
