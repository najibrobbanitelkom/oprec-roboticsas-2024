class truster:
    def __init__(self):
        self.thr1 = 1500
        self.thr2 = 1500
        self.thr3 = 1500
        self.thr4 = 1500
        
    def display(self):
        print("Nilai pwm Truster1 = ", self.thr1)
        print("Nilai pwm Truster2 = ", self.thr2)
        print("Nilai pwm Truster3 = ", self.thr3)
        print("Nilai pwm Truster4 = ", self.thr4)

class pwd():
    def __init__(self):
        self.power = truster()
        
    def atur(self, value):
        self.power.thr1 = value
        self.power.thr2 = value
        self.power.thr3 = value
        self.power.thr4 = value
    def display(self):
        self.power.display()
        
class beriNilai:
    def __init__(self):
        self.pwd = pwd()
        
    def stop(self):
        print("Truster Stop")
        self.pwd.display()
        
    def gerakMaju(self):
        print("Truster Maju")
        self.pwd.atur(1700)
        self.pwd.display()
        
    def gerakMundur(self):
        print("Truster Mundur")
        self.pwd.atur(1300)
        self.pwd.display()
        
def main():
    beri_Nilai = beriNilai()
    beri_Nilai.stop()
    print("")
    beri_Nilai.gerakMaju()
    print("")
    beri_Nilai.gerakMundur()
    
if __name__ == '__main__':
    main()