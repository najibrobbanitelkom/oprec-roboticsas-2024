class Thruster:
    def __init__(self):
        self.thruster_1 = 1500
        self.thruster_2 = 1500
        self.thruster_3 = 1500
        self.thruster_4 = 1500

    def value(self,value):
        self.thruster_1 = value
        self.thruster_2 = value
        self.thruster_3 = value
        self.thruster_4 = value
    def print(self):
        print("Nilai pwm thruster 1=", self.thruster_1)
        print("Nilai pwm thruster 2=", self.thruster_2)
        print("Nilai pwm thruster 3=", self.thruster_3)
        print("Nilai pwm thruster 4=", self.thruster_4)
class BeriNilai:
    def __init__(self):
        self.thruster =Thruster()

    def stop(self):
        self.thruster.print

    def gerakMaju(self):
        self.thruster.value(1700)
        self.thruster.print
    
    def gerakMundur(self):
        self.thruster.value(1300)
        self.thruster.print

def main():
    beri_nilai =BeriNilai()
    beri_nilai.stop()
    print("")
    beri_nilai.gerakMaju()
    print("")
    beri_nilai.gerakMundur()

if __name__ == '__main__':
    main()


   

