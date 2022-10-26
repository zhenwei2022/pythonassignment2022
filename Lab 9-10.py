# Lab 9
# 1.
class Car:
    def __init__(self, registration_number, maximum_speed, current_speed=0, travelled_distance=0):
        self.registration_number=registration_number
        self.maximum_speed="'{}'km/h".format(maximum_speed)
        self.current_speed=0
        self.travelled_distance=0
car = Car("ABC-123", 142)
print(vars(car))

# 2.
class Car:
    def __init__(self, registration_number, maximum_speed, current_speed=0, travelled_distance=0):
        self.registration_number=registration_number
        self.maximum_speed="'{}'km/h".format(maximum_speed)
        self.current_speed=0
        self.travelled_distance = 0
    def accelerate(self, accelerate_speed):
        self.current_speed = self.current_speed + accelerate_speed
        if self.current_speed >= 142:
           self.current_speed = 142
        elif self.current_speed <= 0:
            self.current_speed = 0
        else: self.current_speed == self.current_speed
car1 = Car("ABC-123", 142)
car1.accelerate(30)
print(vars(car1))
class Car:
    def __init__(self, registration_number, maximum_speed, current_speed=0, travelled_distance=0):
        self.registration_number=registration_number
        self.maximum_speed="'{}'km/h".format(maximum_speed)
        self.current_speed=30
        self.travelled_distance = 0
    def accelerate(self, accelerate_speed):
        self.current_speed = self.current_speed + accelerate_speed
        if self.current_speed >= 142:
           self.current_speed = 142
        elif self.current_speed <= 0:
            self.current_speed = 0
        else: self.current_speed == self.current_speed
car2 = Car("ABC-123", 142)
car2.accelerate(70)
print(vars(car2))
class Car:
    def __init__(self, registration_number, maximum_speed, current_speed=100, travelled_distance=0):
        self.registration_number=registration_number
        self.maximum_speed="'{}'km/h".format(maximum_speed)
        self.current_speed=100
        self.travelled_distance = 0
    def accelerate(self, accelerate_speed):
        self.current_speed = self.current_speed + accelerate_speed
        if self.current_speed >= 142:
           self.current_speed = 142
        elif self.current_speed <= 0:
            self.current_speed = 0
        else: self.current_speed == self.current_speed
car3 = Car("ABC-123", 142)
car3.accelerate(50)
print(vars(car3))
class Car:
    def __init__(self, registration_number, maximum_speed, current_speed=100, travelled_distance=0):
        self.registration_number=registration_number
        self.maximum_speed="'{}'km/h".format(maximum_speed)
        self.current_speed=100
        self.travelled_distance = 0
    def accelerate(self, accelerate_speed):
        self.current_speed = self.current_speed + accelerate_speed
        if self.current_speed >= 142:
           self.current_speed = 142
        elif self.current_speed <= 0:
            self.current_speed = 0
        else: self.current_speed == self.current_speed
car4 = Car("ABC-123", 142)
car4.accelerate(-200)
print(vars(car4))

# 3.
class Car:
    def __init__(self, registration_number, maximum_speed, current_speed=60, travelled_distance=2000):
        self.registration_number=registration_number
        self.maximum_speed="'{}'km/h".format(maximum_speed)
        self.current_speed= 60
        self.travelled_distance = 2000
    def drive(self,travelled_distance):
        self.travelled_distance = self.travelled_distance + 1.5 * self.current_speed
car1 = Car("ABC-123", 142)
car1.drive(1.5)
print(vars(car1))

