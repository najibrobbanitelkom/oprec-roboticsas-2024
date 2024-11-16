class Thruster:
    def __init__(self):
        self.pwm_thruster1 = 1500
        self.pwm_thruster2 = 1500
        self.pwm_thruster3 = 1500
        self.pwm_thruster4 = 1500
    
    def set_pwm(self, value):
        self.pwm_thruster1 = value
        self.pwm_thruster2 = value
        self.pwm_thruster3 = value
        self.pwm_thruster4 = value
    
    def printNilai(self):
        print("nilai pwm truster1 =", self.pwm_thruster1)
        print("nilai pwm truster2 =", self.pwm_thruster2)
        print("nilai pwm truster3 =", self.pwm_thruster3)
        print("nilai pwm truster4 =", self.pwm_thruster4)

class BeriNilai:
    def __init__(self):
        self.thruster = Thruster()
    def stop(self):
        print("Thruster berhenti")
        self.thruster.printNilai()
    def gerakMaju(self):
        self.thruster.set_pwm(1700)
        print("Thruster bergerak maju")
        self.thruster.printNilai()
    def gerakMundur(self):
        self.thruster.set_pwm(1300)
        print("Thruster bergerak mundur")
        self.thruster.printNilai()
def main():
    beri_nilai = BeriNilai()
    beri_nilai.stop()
    print("")
    beri_nilai.gerakMaju()
    print("")
    beri_nilai.gerakMundur()

if __name__ == '__main__':
    main()