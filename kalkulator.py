class kalkulator:

    def tambah(self, a, b):
        return a + b
        
    def kurang(self, a, b):
        return a - b

    def kali(self, a, b):
        return a * b

    def bagi(self, a, b):
        if b != 0:
            return a / b
        else: 
            return "tidak bisa dibagi nol"


def main():
    calc = kalkulator()
    print("tambah:", calc.tambah(10, 5))
    print("kurang:", calc.kurang(10, 5))
    print("kali:", calc.kali(10, 5))
    print("bagi:", calc.bagi(10, 5))

if __name__=='__main__':
    main()