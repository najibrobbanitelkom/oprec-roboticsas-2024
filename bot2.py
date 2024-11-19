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

    def display_thrusters(self):
        print("nilai pwm thruster1 =", self.pwm_thruster1)
        print("nilai pwm thruster2 =", self.pwm_thruster2)
        print("nilai pwm thruster3 =", self.pwm_thruster3)
        print("nilai pwm thruster4 =", self.pwm_thruster4)
    
class BeriNilai:
    def __init__(self):
        self.thruster = Thruster()

    def stop(self):
        self.thruster.set_pwm(1500)
        print("Thruster Berhenti")
        self.thruster.display_thrusters()
    
    def gerakMaju(self):
        self.thruster.set_pwm(1700)
        print("Thruster bergerak maju")
        self.thruster.display_thrusters()

    def gerakMundur(self):
        self.thruster.set_pwm(1300)
        print("Thruster bergerak mundur")
        self.thruster.display_thrusters()

def main():
    beri_nilai = BeriNilai()
    beri_nilai.stop()
    print("")
    beri_nilai.gerakMaju()
    print("")
    beri_nilai.gerakMundur()

if __name__ == "__main__":
    main()