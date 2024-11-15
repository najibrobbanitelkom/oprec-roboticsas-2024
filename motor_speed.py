class Motor:
    def __init__(self, speed1, speed2, speed3, speed4):
        self.speed_motor1 = speed1
        self.speed_motor2 = speed2
        self.speed_motor3 = speed3
        self.speed_motor4 = speed4

    def display_speeds(self):
        print("Speed of motor 1 =", self.speed_motor1)
        print("Speed of motor 2 =", self.speed_motor2)
        print("Speed of motor 3 =", self.speed_motor3)
        print("Speed of motor 4 =", self.speed_motor4)

    def average_speed(self):
        average = (self.speed_motor1 + self.speed_motor2 + self.speed_motor3 + self.speed_motor4) / 4
        print("Average Speed of motors =", average)

class SetSpeed:
    def __init__(self, speed1, speed2, speed3, speed4):
        self.motor = Motor(speed1, speed2, speed3, speed4)

    def show_speeds(self):
        self.motor.display_speeds()

    def show_average_speed(self):
        self.motor.average_speed()

def main():
    set_speed = SetSpeed(1200, 1300, 1400, 1500)
    set_speed.show_speeds()
    set_speed.show_average_speed()

if __name__ == '__main__':
    main()
