class Kalkulator:
    def tambah(self,bilangan1,bilangan2):
        return bilangan1+bilangan2
    def kurang(self,bilangan1,bilangan2):
        return bilangan1-bilangan2
    def kali(self,bilangan1,bilangan2):
        return bilangan1*bilangan2
    def bagi(self,bilangan1,bilangan2):
        if bilangan2!=0:
            return bilangan1/bilangan2
        else:
            return"Error"
def main():
    calc = Kalkulator()
    print("Tambah : ", calc.tambah(10,5))
    print("Kurang: ", calc.kurang(10,5))
    print("Kali: ", calc.kali(10,5))
    print("Bagi: ", calc.bagi(10,0))

if __name__ == '__main__':
    main()