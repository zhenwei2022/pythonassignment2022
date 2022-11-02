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
    def drive(self, change_speed):
        self.current_speed = self.current_speed + change_speed
        if self.current_speed < 100:
            self.current_speed = 100
        elif self.current_speed > 200:
            self.current_speed = 200
        self.travelled_distance = self.travelled_distance + self.current_speed
        return self.current_speed, self.travelled_distance
    def get_travelled_distance(self):
        return self.travelled_distance

class Race:
    def __init__(self, name, kilometers, car_list):
        self.name = name
        self.distance = kilometers
        self.car_list = car_list
    def hour_passes(self):
        for car in self.car_list:
            change_speed  = random.randint(-10,15)
            car.drive(change_speed)
    def print_status(self):
        for car in self.car_list:
            print(f"registration_number:{car.registration_number}, current_speed:{car.current_speed} kilometers/hour, travelled_distance:{car.travelled_distance} kilometers")

    def race_finished(self):
        race_over = False
        for car in self.car_list:
            travelled_distance = car.get_travelled_distance()
            if travelled_distance >= self.distance:
                race_over = True
        return race_over
car_list = []
registration_number = 1
for i in range(1,11):
    maximum_speed = random.randint(100, 200)
    current_speed = random.randint(100, 200)
    new_car = Car("ABC-{}".format(i), maximum_speed, current_speed, 0)
    car_list.append(new_car)
    registration_number = registration_number + 1
race = Race("Grand Demolition Derby", 8000, car_list)
race_over = False
hour = 1
progress = False
hour = 1
while progress == False:
    race.hour_passes()
    progress = race.race_finished()
    race.print_status()
    hour = hour + 1
    print(f"Time takes {hour} hours.")

print("Race over!!! The final result as following.")
race.print_status()


