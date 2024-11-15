class Kalkulator:
    
    def kurang(self, a, b):
        return a - b
    
    def tambah(self, a, b):
        return a + b
    
    def kali(self, a, b):
        return a * b
    
    def bagi(self, a, b):
        if b == 0:
            return "Error! Tidak bisa membagi dengan 0"
        else:
            return a / b
    
def main():
        calc = Kalkulator()
        print("Hasil kurang: ", calc.kurang(10,5))
        print("Hasil tambah: ", calc.tambah(11,7))
        print("Hasil kali: ", calc.kali(3,2))
        print("Hasil bagi: ", calc.bagi(0,0))

if __name__ == "__main__":
    main()