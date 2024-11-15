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
            return "Tidak bisa dibagi dengan nol"
        

def main():
    calc = kalkulator()
    print("Tambah =", calc.tambah(10, 5))
    print("Kurang =", calc.kurang(10, 5))
    print("Kali =", calc.kali(10, 5))
    print("Bagi =", calc.bagi(10, 0))

if __name__ == '__main__':
    main()