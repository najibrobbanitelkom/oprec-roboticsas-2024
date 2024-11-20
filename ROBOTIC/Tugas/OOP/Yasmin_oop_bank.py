# Bank pecahan 50k
class Bank():
    def __init__ (self):
        self.action = Action()
        pin = int(input("Masukkan PIN anda : "))
        print("Pilih aksi : \n1. Cek Saldo\n2. Setor Tunai\n3. Tarik Tunai\n4. Transfer")
        menu = int(input("Pilihan anda : "))
        if menu == 1 :
            self.action.cekSaldo()
        elif menu == 2 :
            self.action.tarikTunai()
        elif menu == 3 :
            self.action.setorTunai()
        elif menu == 4 :
            self.action.transfer()
        else :
            print("Unvalid")
        

class Action():
    def set_saldo(self):
        self.value = 200000
    def cekSaldo(self):
        print("cek saldo")
        # self.saldo = set_saldo(self.value)
        print(f"Saldo Anda saat ini adalah: {self.saldo}")
    def tarikTunai(self):
        print("tarik tunai")
    def setorTunai(self):
        print("setor tunai")
    def transfer(self):
        print("transfer")

def main():
   Bank()

if __name__ == '__main__':
    main()