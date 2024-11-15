class Kalkulator:
    def tambah(self, a, b):
        return a + b
    
    def kurang(self, a, b):
        return a - b
        
    def kali(self, a, b):
        return a * b
        
    def bagi(self, a, b):
        if b == 0:
            return "Tidak dapat dibagi 0 >:("
        else:
            return a / b
            
def main():
    calc = Kalkulator()
    print("Tambah   : ",calc.tambah(10,5))
    print("kurang   : ",calc.kurang(10,5))
    print("kali     : ",calc.kali(10,5))
    print("bagi     : ",calc.bagi(10,2))
    
if __name__ == '__main__':
    main()