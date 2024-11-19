class Persegi():
    def __init__(self, s:int):
        assert isinstance(s, int), 'value of s should be integer.'

        self.luas = s*s
        self.keliling = 4*s

    def print(self):
        print(f'Luas = {self.luas} Keliling = {self.keliling}')

def main():
    p = Persegi(3)
    p.print()

if __name__ == '__main__':
    main()
