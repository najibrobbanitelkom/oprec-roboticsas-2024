class Kalkulator:

    def tambah(self,x,y):
        return x + y

    def kurang(self, x, y):
        return x - y
    
    def kali(self, x, y):
        return x * y
    
    def bagi(self, x, y):
        if y == 0:
            return "Tidak bisa membagi dengan nol!"
        else:
            return x / y

def main():
    calc = Kalkulator()
    print("Tambah:", calc.tambah(10,5))
    print("Kurang:", calc.kurang(10,5))
    print("Kali:", calc.kali(10,5))
    print("Bagi:", calc.bagi(10,5))
    print("Bagi:", calc.bagi(10,0))

if __name__ == '__main__':
    main()    
    
