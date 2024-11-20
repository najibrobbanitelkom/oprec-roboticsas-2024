class BeriNilai:
    def __init__(self):
        self.thruster= Thruster()

    def stop(self):
        print("Thruster Berhenti",)
        self.thruster.printNilai()
        
    def gerakMaju(self):
        print("Thruster Gerak Maju")
        self.thruster.printNilai()
        
    def gerakMundur(self):
        print("Thruster Gerak Mundur")
        self.thruster.printNilai()

class Thruster:
    def __init__ (self):
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
        print("NIlai pwm thruster 1 ", self.pwm_thruster1)
        print("NIlai pwm thruster 2 ", self.pwm_thruster2)
        print("NIlai pwm thruster 3 ", self.pwm_thruster3)
        print("NIlai pwm thruster 4 ", self.pwm_thruster4)

# thruster.value(gerakmaju)
def main():
    beri_nilai = BeriNilai()
    beri_nilai.stop()
    print(" ")
    beri_nilai.gerakMaju()
    print(" ")
    beri_nilai.gerakMundur()
    print(" ")

if __name__ == '__main__':
    main()



    # PR
    # BIkin bank, pakai class
    # deadline rabu pas offline