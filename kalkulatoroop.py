class Kalkulator:
    def tambah(self, a, b):
        return a + b
    
    def kurang(self, a, b):
        return a - b
    
    def kali(self, a, b):
        return a * b
    
    def bagi(self, a, b):
       if b == 0:
           return "TIDAK BISA MEMBAGI DENGAN NOL"
       else:
           return a / b

def main():
    calc = Kalkulator()
    print("Tambah:", calc.tambah(10,5))
    print("Kurang:", calc.kurang(10,5))
    print("Kali:", calc.kali(10,5))
    print("Bagi:", calc.bagi(10,0))
  
if __name__ == '__main__':
    main()