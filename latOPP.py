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
    
class beriNilai:
    def __init__(self):
        self.nilai = truster()
        
    def stop(self):
        print("Truster Stop")
        self.nilai.thr1 = 1500
        self.nilai.thr2 = 1500
        self.nilai.thr3 = 1500
        self.nilai.thr4 = 1500
        
        self.nilai.display()
        
    def gerakMaju(self):
        print("Truster Maju")
        self.nilai.thr1 = 1700
        self.nilai.thr2 = 1700
        self.nilai.thr3 = 1700
        self.nilai.thr4 = 1700
        
        self.nilai.display()
        
    def gerakMundur(self):
        print("Truster Mundur")
        self.nilai.thr1 = 1300
        self.nilai.thr2 = 1300
        self.nilai.thr3 = 1300
        self.nilai.thr4 = 1300
        
        self.nilai.display()
        
def main():
    beri_Nilai = beriNilai()
    beri_Nilai.stop()
    print("")
    beri_Nilai.gerakMaju()
    print("")
    beri_Nilai.gerakMundur()
    
if __name__ == '__main__':
    main()