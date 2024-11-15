class Calculator:
    def tambah(self, a, b): return a + b
    def kurang(self, a, b): return a - b
    def kali(self, a, b): return a * b
    def bagi(self, a, b): 
        if(b == 0): return "invalid"
        return a / b

def main():
    calc = Calculator()
    print("tambah: ", calc.tambah(5, 4))
    print("kurang: ", calc.kurang(5, 4))
    print("kali: ", calc.kali(5, 4))
    print("bagi: ", calc.bagi(5, 0))

main()