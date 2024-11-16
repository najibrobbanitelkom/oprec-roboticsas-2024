class Kalkulator:
    def tambah (self,a,b):
        return a + b
    def kurag (self,a,b):
        return a - b
    def kali (self,a,b):
        return a * b
    def bagi (self,a,b):
        if b !=0:
            return a / b
        else:
            return "tidak dapat membagi dengan nol"
        
def main():
    calc = Kalkulator()
    print("Tambah :", calc.tambah(10, 5))
    print("Kurang :", calc.kurag(10, 5))
    print("Kali :", calc.kali(10, 5))
    print("Bagi :", calc.bagi(10, 5))

if __name__ == '__main__':
    main()