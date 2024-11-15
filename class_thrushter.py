class thrushter:
    def __init__(self):
        self.thrushter1 = 1500
        self.thrushter2 = 1500
        self.thrushter3 = 1500
        self.thrushter4 = 1500

    def set_pwm(self, value):
        self.thrushter1 = value
        self.thrushter2 = value
        self.thrushter3 = value
        self.thrushter4 = value

    def nilai(self):
        print("Nilai pwm thrushter1 =", self.thrushter1)
        print("Nilai pwm thrushter2 =", self.thrushter2)
        print("Nilai pwm thrushter3 =", self.thrushter3)
        print("Nilai pwm thrushter4 =", self.thrushter4)

class BeriNilai:
    def __init__(self):
        self.trushter = thrushter()

    def stop(self):
        print("Trushter Berhenti")
        self.trushter.nilai() #1500

    def GerakMaju(self):
        self.trushter.set_pwm(1700)
        print("Trushter Bergeak Maju")
        self.trushter.nilai() #1700

    def GerakMundur(self):
        self.trushter.set_pwm(1300)
        print("Trushter Bergerak Mundur")
        self.trushter.nilai() #1300

def main():
    beri_nilai = BeriNilai()
    beri_nilai.stop()
    print("")
    beri_nilai.GerakMaju()
    print("")
    beri_nilai.GerakMundur()
    print("")

if __name__ == '__main__':
    main()