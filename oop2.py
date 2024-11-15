class Motor:
    def __init__(self, speed1, speed2, speed3, speed4):
        self.speedM1 = speed1
        self.speedM2 = speed2
        self.speedM3 = speed3
        self.speedM4 = speed4
    
    def display_speeds(self):
        print("Speed of Motor 1 = ", self.speedM1)
        print("Speed of Motor 2 = ", self.speedM2)
        print("Speed of Motor 3 = ", self.speedM3)
        print("Speed of Motor 4 = ", self.speedM4)
        
    def ave_speed(self):
        average = (self.speedM1 + self.speedM2 + self.speedM3 + self.speedM4) / 4
        print("Average Speed of Motors = ", average)
        
class SetSpeed:
    def __init__(self, speed1, speed2, speed3, speed4):
        self.motor = Motor(speed1, speed2, speed3, speed4)
        
    def show_speeds(self):
        self.motor.display_speeds()
        
    def show_ave_speed(self):
        self.motor.ave_speed()
        
def main():
    set_speed = SetSpeed(1200, 1300, 1400, 1500)
    set_speed.show_speeds()
    set_speed.show_ave_speed()
    
if __name__ == '__main__':
    main()