class Thruster: 
    def stop(self, a):
        print(f'nilai pwm thruster1 = {a}')
        print(f'nilai pwm thruster2 = {a}')
        print(f'nilai pwm thruster3 = {a}')
        print(f'nilai pwm thruster4 = {a}')

    def maju(self, a):
        print(f'nilai pwm thruster1 = {a}')
        print(f'nilai pwm thruster2 = {a}')
        print(f'nilai pwm thruster3 = {a}')
        print(f'nilai pwm thruster4 = {a}')

    def mundur(self, a):
        print(f'nilai pwm thruster1 = {a}')
        print(f'nilai pwm thruster2 = {a}')
        print(f'nilai pwm thruster3 = {a}')
        print(f'nilai pwm thruster4 = {a}')

class BeriNilai:
    ui = Thruster()
    def stop(self):
        print('Thruster berhenti')
        self.ui.stop(1500)
        
    def maju(self):
        print('Thruster bergerak maju')
        self.ui.maju(1700)
        
    def mundur(self):
        print('Thruster bergerak mundur')
        self.ui.mundur(1300)

def main():
    beri_nilai = BeriNilai()
    beri_nilai.stop()
    print('')
    beri_nilai.maju()
    print('')
    beri_nilai.mundur()

main()