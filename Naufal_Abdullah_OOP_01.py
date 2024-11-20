class Persegi:
    def __init__(self, num):
        self.keliling = num * 4
        self.luas = num * num

    def print(self):
        print(f'Luas = {self.luas} Keliling = {self.keliling}')
    
def main():
    p = Persegi(3)
    p.print()

main()