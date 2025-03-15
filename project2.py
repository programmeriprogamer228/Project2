class Car:
    def __init__(self,speed_car):
        self.speed=speed_car
    def info(self):
        print("Швидкість авто:", self.speed)
sp=int(input('Максимальна шв авто: '))
auto=Car(sp)
auto.info()
auto2=Car(180)
auto2.info()