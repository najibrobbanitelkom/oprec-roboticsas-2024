class Thruster:

    def __init__ (self, thruster1, thruster2, thruster3, thruster4):
        self.thrust1 = thruster1
        self.thrust2 = thruster2
        self.thrust3 = thruster3
        self.thrust4 = thruster4
    
    def display_stop(self):
        print("Thruster berhenti")
        print("NIlai pwm thruster 1 = ", self.thrust1)
        print("NIlai pwm thruster 2 = ", self.thrust2)
        print("NIlai pwm thruster 3 = ", self.thrust3)
        print("NIlai pwm thruster 4 = ", self.thrust4)

    def display_start(self):
        print("Thruster bergerak maju")
        print("NIlai pwm thruster 1 = ", self.thrust1+200)
        print("NIlai pwm thruster 2 = ", self.thrust2+200)
        print("NIlai pwm thruster 3 = ", self.thrust3+200)
        print("NIlai pwm thruster 4 = ", self.thrust4+200)

    def display_reverse(self):
        print("Thruster bergerak mundur")
        print("NIlai pwm thruster 1 = ", self.thrust1-200)
        print("NIlai pwm thruster 2 = ", self.thrust2-200)
        print("NIlai pwm thruster 3 = ", self.thrust3-200)
        print("NIlai pwm thruster 4 = ", self.thrust4-200)

class BeriNilai:
    def __init__ (self):
        self.thruster = Thruster(1500,1500,1500,1500)

    def stop(self):
        self.thruster.display_stop()
    
    def start(self):
        self.thruster.display_start()

    def reverse(self):
        self.thruster.display_start()


def main():
    beri_nilai = BeriNilai()
    beri_nilai.stop()
    print("")
    beri_nilai.start()
    print("")
    beri_nilai.reverse()

if __name__ == "__main__":
    main()