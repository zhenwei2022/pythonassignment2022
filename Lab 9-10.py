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
        print(f"registration_number ABC-{new_car.registration_number},maximum_speed: {new_car.maximum_speed}, current_speed:{new_car.current_speed}, travelled_distance:{new_car.travelled_distance}")

#Lab 10
#1
class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor= bottom_floor
        self.top_floor = top_floor
    def go_to_floor(self, destination_floor):
        self.destination_floor = destination_floor
    def floor_up(self):
        self.current_floor = self.current_floor + 1
        print("Moving up. Next floor is {} floor.".format(self.current_floor))
    def floor_down(self):
        self.current_floor = self.current_floor - 1
        print("Moving down. Next floor is {} floor.".format(self.current_floor))
h = Elevator(0,10)
h.go_to_floor(5)
h.current_floor = h.bottom_floor
while h.current_floor < h.destination_floor:
    h.floor_up()
print("You are in the destination floor.")
h.destination_floor = h.bottom_floor
while h.current_floor > h.destination_floor:
    h.floor_down()
print("You are in the bottom floor.")
# 2 & 3
class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor= bottom_floor
        self.top_floor = top_floor
    def go_to_floor(self, destination_floor):
        self.destination_floor = destination_floor
    def floor_up(self):
        self.current_floor = self.current_floor + 1
        print("Moving up. Next floor is {} floor.".format(self.current_floor))
    def floor_down(self):
        self.current_floor = self.current_floor - 1
        print("Moving down. Next floor is {} floor.".format(self.current_floor))
class Building:
    def __init__(self, bottom_floor, top_floor, elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators= elevators
        self.elevator_list = []
        i = 1
        for i in range(1, elevators + 1):
            elevator = Elevator(bottom_floor, top_floor)
            self.elevator_list.append(elevator)
            i = i + 1
    def run_elevator(self, elevators, destination_floor):
        i = 1
        for i in range(1,elevators + 1):
            elevator.go_to_floor(destination_floor)
            print("elevator{}".format(i))
            print(vars(elevator))
            i = i + 1
    def fire_alarm(self):
        i = 1
        for i in range(1, building.elevators + 1):
            elevator.go_to_floor(elevator.bottom_floor)
            print("elevator{}".format(i))
            print(vars(elevator))
            i = i + 1
elevator = Elevator(0,10)
building = Building(0,10,3)
building.run_elevator(3,9)
building.fire_alarm()
#4
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

class Race:
    def __init__(self, name, race_distance, car_amount):
        self.name = name
        self.race = race_distance
        self.car_amount = car_amount
    def hour_passes(self):
        for car in car_list:
            car.accelerate(random.randint(-10,16))
            car.drive(1)
            print(vars(car))
    def print_status(self):
        for car in self.car_list:
            print(vars(self.car_list[i]))
    def race_finished(self):
        for i in range(len(self.car_list)):
            if car.travlled_distance >= self.race_distance:
                return Ture
race= Race("Grand_Demolition_Derby", 8000 , 10)
car_list = []
registration_number = 1
for i in range(1,11):
    maximum_speed = random.randint(100,200)
    current_speed = random.randint(100,200)
    if maximum_speed < current_speed:
        current_speed = maximum_speed
    else:
        current_speed = current_speed
    new_car = Car(registration_number, maximum_speed, current_speed, 0)
    car_list.append(new_car)
    registration_number = registration_number + 1

finish = False
while finish == False:
    for new_car in car_list:
        new_car.accelerate(random.randint(-10, 16))
        new_car.drive(1)
        if race_finished == True:
            print(vars(new_car))

