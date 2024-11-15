class Thruster:
    def __init__(self):
        self.thruster1 = 1500
        self.thruster2 = 1500
        self.thruster3 = 1500
        self.thruster4 = 1500

    def set_val(self, value):
        self.thruster1 = value
        self.thruster2 = value
        self.thruster3 = value
        self.thruster4 = value
    
    def dis_thruster(self):
        print("nilai per thruster1 =", self.thruster1)
        print("nilai per thruster2 =", self.thruster2)
        print("nilai per thruster3 =", self.thruster3)
        print("nilai per thruster4 =", self.thruster4)

class BeriNilai:
    def __init__(self):
        self.thruster = Thruster()

    def stop(self):
        print("Thruster Berhenti")
        self.thruster.dis_thruster()

    def gerakMaju(self):
        self.thruster.set_val(1700)
        print("Thruster maju")
        self.thruster.dis_thruster()

    def gerakMundur(self):
        self.thruster.set_val(1300)
        print("Thruster mundur")
        self.thruster.dis_thruster()
        

def main():
    beri_nilai = BeriNilai()
    beri_nilai.stop()
    print("")
    beri_nilai.gerakMaju()
    print("")
    beri_nilai.gerakMundur()

if __name__=='__main__':
    main()