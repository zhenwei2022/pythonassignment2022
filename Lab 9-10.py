# Lab 9
# 1 & 2
class Car:
    def __init__(self, registration_number, maximum_speed, current_speed, travelled_distance):
        self.registration_number=registration_number
        self.maximum_speed= maximum_speed
        self.current_speed= current_speed
        self.travelled_distance= travelled_distance

    def accelerate(self, accelerate_speed):
        self.current_speed = self.current_speed + accelerate_speed
        if self.current_speed > self.maximum_speed:
                self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
                self.current_speed = 0
        else: self.current_speed == self.current_speed

car = Car("ABC-123", 142, 0, 0)
print(vars(car))
car.accelerate(30)
car.accelerate(70)
car.accelerate(50)
print(vars(car))
car.accelerate(-200)
print(vars(car))

# 3.
class Car:
    def __init__(self, registration_number, maximum_speed, current_speed, travelled_distance):
        self.registration_number= registration_number
        self.maximum_speed= maximum_speed
        self.current_speed= current_speed
        self.travelled_distance = travelled_distance
    def drive(self,drive_hour):
        self.travelled_distance = self.travelled_distance + drive_hour * self.current_speed
car = Car("ABC-123", 142, 60, 2000)
car.drive(1.5)
print(vars(car))

# 4.
import random
class Car:
    def __init__(self, registration_number, maximum_speed, current_speed, travelled_distance):
        self.registration_number=registration_number
        self.maximum_speed= maximum_speed
        self.current_speed= current_speed
        self.travelled_distance = travelled_distance
    def accelerate(self, accelerate_speed):
        self.current_speed = self.current_speed + accelerate_speed
        if self.current_speed > maximum_speed:
           self.current_speed = maximum_speed
    def drive(self, drive_hour):
       self.travelled_distance = self.travelled_distance + drive_hour * self.current_speed
car_list = []
registration_number = 1
for i in range(1,11):
    maximum_speed = random.randint(100, 200)
    current_speed = random.randint(100, 200)
    new_car = Car(registration_number, maximum_speed, current_speed, 0)
    car_list.append(new_car)
    registration_number = registration_number + 1
travelled_distance = 0
finish = False
while finish == False:
    for new_car in car_list:
        new_car.accelerate(random.randint(-10, 16))
        new_car.drive(1)
        if new_car.travelled_distance > 10000:
            finish = True
        print(vars(new_car))

#Lab 10
#1
class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor= bottom_floor
        self.top_floor = top_floor
    def go_to_floor(self, destination_floor):
        self.destination_floor = destination_floor
    def floor_up(self):
        self.up_floors_number = present_floor + 1
        print("You are in the {} floor.".format(present_floor) + "Next floor is {} floor".format(present_floor + 1))
    def floor_down(self):
        self.down_floors_number = present_floor -1
        print("You are in the {} floor.".format(present_floor) + "Next floor is {} floor".format(present_floor - 1))
h = Elevator(0,10)
h.go_to_floor(5)
present_floor = h.bottom_floor
while present_floor < h.destination_floor:
    h.floor_up()
    present_floor = present_floor + 1
if present_floor == h.destination_floor:
    print("You are in the {} floor.".format(present_floor) + "The elevator will go back to the bottom floor.")
while present_floor > h.bottom_floor:
    h.floor_down()
    present_floor = present_floor - 1
if present_floor == h.bottom_floor:
    print("You are in the {} floor.".format(present_floor) + "It is bottom floor.")
#2
class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor= bottom_floor
        self.top_floor = top_floor
    def go_to_floor(self, destination_floor):
        self.destination_floor = destination_floor
    def floor_up(self):
        self.up_floors_number = present_floor + 1
    def floor_down(self):
        self.down_floors_number = present_floor -1
class Building:
    def __init__(self, bottom_floor, top_floor, elevator_number):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevator_number = elevator_number
        self.elevator_list = []
        i = 1
        while i <= elevator_number:
            self.elevator_list.append("elevator{}".format(i))
            i = i + 1
    def run_elevator(self, elevator_number, destination_floor):
        self.elevator_number = elevator_number
        self.destination_floor = destination_floor
building = Building(0,10,3)
building.run_elevator(3,8)
print(vars(building))
#3
class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor= bottom_floor
        self.top_floor = top_floor
    def go_to_floor(self, destination_floor):
        self.destination_floor = destination_floor
    def floor_up(self):
        self.up_floors_number = present_floor + 1
    def floor_down(self):
        self.down_floors_number = present_floor -1
class Building:
    def __init__(self, bottom_floor, top_floor, elevator_number):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevator_number = elevator_number
        self.elevator_list = []
        i = 1
        while i <= elevator_number:
            self.elevator_list.append("elevator{}".format(i))
            i = i + 1
    def run_elevator(self, elevator_number, destination_floor):
        self.elevator_number = elevator_number
        self.destination_floor = destination_floor
    def fire_alarm(self):
        self.destination_floor = self.bottom_floor
building = Building(0,10,3)
building.run_elevator(3,8)
building.fire_alarm()
print(vars(building))
# 4.
import random
class Car:
    def __init__(self, registration_number, maximum_speed, current_speed, travelled_distance):
        self.registration_number= registration_number
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
    def drive(self, drive_hour):
        if self.current_speed >= 200:
           travelled_distance = 200
        elif self.current_speed <= 100:
            travelled_distance = 100
        else: self.travelled_distance= self.travelled_distance
        self.travelled_distance = self.travelled_distance + drive_hour * self.current_speed

class Race:
    def __init__(self, name, travelled_distance, car_list):
        self.name = name
        self.travelled_distance = travelled_distance
        self.car_list = car_list
    def hour_passes(self):
        self.hour_passes = car.drive(1)
    def print_status(self):
        distance_list = []
        distance_list.append(race.travelled_distance)
        print(Race.car_list)
    def race_finished(self,race_distance):
        self.race_distance = race_distance
        self.race_finished = race.travelled_distance >= race_distance
race= Race("Grand_Demolition_Derby",0,0)
race_distance = 8000
i = 1
while i <= 10:
    car = Car("ABC-{}".format(i),200, random.randint(100, 200), 0)
    i = i + 1
    car_list= []
    car_list.append(car)
    car.accelerate(random.randint(-10, 15))
    race.hour_passed()
    if race_finished == False:
        race.hour_passed()
    if race_finished == True:
        race.print_status()


