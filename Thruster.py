
class Thruster:
    def __init__(self):
        self.pmw_thruster1 = 1500
        self.pmw_thruster2 = 1500
        self.pmw_thruster3 = 1500
        self.pmw_thruster4 = 1500

    def set_pwm(self, value):
        self.pmw_thruster1 = value
        self.pmw_thruster2 = value
        self.pmw_thruster3 = value
        self.pmw_thruster4 = value
    
    def printNilai(self):
        print("nilai pwm thruster1 =", self.pmw_thruster1)
        print("nilai pwm thruster2 =", self.pmw_thruster2)
        print("nilai pwm thruster3 =", self.pmw_thruster3)
        print("nilai pwm thruster4 =", self.pmw_thruster4)
       
class BeriNilai:
    def __init__(self):
        self.thruster = Thruster()

    def stop(self):
        print("Thruster Berhenti")
        self.thruster.printNilai()
    
    def gerakMaju(self):
        self.thruster.set_pwm(1700)
        print("Truster bergerak maju")
        self.thruster.printNilai()

    def gerakMundur(self):
        self.thruster.set_pwm(1300)
        print("Thruster Bergerak mundur")
        self.thruster.printNilai()

def main():
    beri_nilai = BeriNilai()
    beri_nilai.stop()
    print("")
    beri_nilai.gerakMaju()
    print("")
    beri_nilai.gerakMundur()

if __name__=='__main__':
    main()
