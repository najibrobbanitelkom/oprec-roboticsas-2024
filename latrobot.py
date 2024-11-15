class Thruster:
    def __init__(self, thruster1, thruster2, thruster3, thruster4):
        self.thruster_1 = thruster1
        self.thruster_2 = thruster2
        self.thruster_3 = thruster3
        self.thruster_4 = thruster4
    
    def stop(self):
        print("Thruster Berhenti")
        print("nilai pwm thruster 1 =", self.thruster_1)
        print("nilai pwm thruster 2 =", self.thruster_2)
        print("nilai pwm thruster 3 =", self.thruster_3)
        print("nilai pwm thruster 4 =", self.thruster_4)

    def move_forward(self):
        print("Thruster Begerak Maju")
        print("nilai pwm thruster 1 =", self.thruster_1+200)
        print("nilai pwm thruster 2 =", self.thruster_2+200)
        print("nilai pwm thruster 3 =", self.thruster_3+200)
        print("nilai pwm thruster 4 =", self.thruster_4+200)

    def move_backward(self):
        print("Thruster Begerak Maju")
        print("nilai pwm thruster 1 =", self.thruster_1-200)
        print("nilai pwm thruster 2 =", self.thruster_2-200)
        print("nilai pwm thruster 3 =", self.thruster_3-200)
        print("nilai pwm thruster 4 =", self.thruster_4-200)



class BeriNilai:
    def __init__(self):
        self.Thruster = Thruster(1500, 1500, 1500, 1500)

    def stop(self):
        self.Thruster.stop()

    def gerakMaju(self):
        self.Thruster.move_forward()

    def gerakMundur(self):
        self.Thruster.move_backward()


def main():
    beri_nilai = BeriNilai()
    beri_nilai.stop()
    print("")
    beri_nilai.gerakMaju()
    print("")
    beri_nilai.gerakMundur()

if __name__ == '__main__':
    main()