# Lab 9
# 1.
class Car:
    def __init__(self, registration_number, maximum_speed, current_speed, travelled_distance):
        self.registration_number=registration_number
        self.maximum_speed="'{}'km/h".format(maximum_speed)
        self.current_speed= current_speed
        self.travelled_distance= travelled_distance
car = Car("ABC-123", 142, 0, 0)
print(vars(car))

# 2.
class Car:
    def __init__(self, registration_number, maximum_speed, current_speed, travelled_distance=0):
        self.registration_number=registration_number
        self.maximum_speed="'{}'km/h".format(maximum_speed)
        self.current_speed= current_speed
        self.travelled_distance = travelled_distance
    def accelerate(self, accelerate_speed):
        self.current_speed = self.current_speed + accelerate_speed
        if self.current_speed >= 142:
           self.current_speed = 142
        elif self.current_speed <= 0:
            self.current_speed = 0
        else: self.current_speed == self.current_speed
car1 = Car("ABC-123", 142, 0)
car1.accelerate(30)
print(vars(car1))
car1 = Car("ABC-123", 142, 30)
car1.accelerate(70)
print(vars(car1))
car1 = Car("ABC-123", 142, 100)
car1.accelerate(50)
print(vars(car1))
car1= Car("ABC-123", 142, 142)
car1.accelerate(-200)
print(vars(car1))

# 3.
class Car:
    def __init__(self, registration_number, maximum_speed, current_speed, travelled_distance):
        self.registration_number=registration_number
        self.maximum_speed="'{}'km/h".format(maximum_speed)
        self.current_speed= current_speed
        self.travelled_distance = travelled_distance
    def drive(self,travelled_distance):
        self.travelled_distance = self.travelled_distance + 1.5 * self.current_speed
car1 = Car("ABC-123", 142, 60, 0)
car1.drive(1.5)
print(vars(car1))

# 4.
import random
class Car:

    def __init__(self, registration_number, maximum_speed, current_speed, travelled_distance):
        self.registration_number=registration_number
        self.maximum_speed="'{}'km/h".format(maximum_speed)
        self.current_speed= current_speed
        self.travelled_distance = travelled_distance
    def accelerate(self, accelerate_speed):
        self.current_speed = self.current_speed + accelerate_speed
        if self.current_speed >= 200:
           self.current_speed = 200
        elif self.current_speed <= 100:
            self.current_speed = 100
        else: self.current_speed == self.current_speed
    def drive(self,travelled_distance):
        distance_list = []
        self.travelled_distance = self.travelled_distance + 1 * self.current_speed
car1 = Car("ABC-123", 200, random.randint(100, 200), 0)
car1.accelerate(random.randint(-10, 15))
car1.drive(1)
distance_list = []
distance_list.append(car1.travelled_distance)
circle =1
while car1.travelled_distance <= 10000:
    car1.accelerate(random.randint(-10, 15))
    car1.drive(1)
    distance_list.append(car1.travelled_distance)
    circle = circle +1
else:
    print(circle)
    print((distance_list))

#Lab 10
#1
class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor= bottom_floor
        self.top_floor = top_floor
    def go_to_floor(self, destination_floor):
        self.destination_floor = destination_floor
    def floor_up(self, up_floors_number):
        self.up_floors_number = present_floor + up_floors_number
    def floor_down(self, down_floors_number):
        self.down_floors_number = present_floor + down_floors_number

elevator = Elevator(0,10)
elevator.go_to_floor(5)
move_floors = elevator.destination_floor - elevator.bottom_floor
present_floor = elevator.bottom_floor
while present_floor < elevator.destination_floor:
    print("You are in the {} floor.".format(present_floor)+"Next floor is {} floor".format(present_floor +1))
    elevator.floor_up(1)
    present_floor = present_floor + 1
if present_floor == elevator.destination_floor:
    print("You are in the {} floor.".format(present_floor) + "The elevator will go back to the bottom floor.")
while present_floor > elevator.bottom_floor:
        print("You are in the {} floor.".format(present_floor)+"Next floor is {} floor".format(present_floor -1))
        elevator.floor_down(-1)
        present_floor = present_floor - 1
if present_floor == elevator.bottom_floor:
    print("You are in the {} floor.".format(present_floor) + "It is bottom floor.")

