#Lab 11-12
#11.1
class Publication:
    def __init__(self, name):
        self.name = name

class Book(Publication):
    def __init__(self, name, author, page_count ):
        self.author = author
        self.page_count = page_count
        super().__init__(name)

    def print_information(self):
        print(f"The author of {self.name} is {self.author}. It has {self.page_count} pages.")

class Magazine(Publication):
    def __init__(self,name, chief_editor):
        self.chief_editor = chief_editor
        super().__init__(name)

    def print_information(self):
        print(f"The chief editor of {self.name} is {self.chief_editor}.")

book = Book("Compartment No.6", "Rosa Likson", 192)
magazine = Magazine("Donald Duck","Aki Hyppä")
book.print_information()
magazine.print_information()

#11.2
class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed


class ElectricCar(Car):
    def __init__(self, registration_number, maximum_speed, capacity_battery):
        self.capacity_battery = capacity_battery
        super().__init__(registration_number, maximum_speed)
        Ecar_distance = hour * self.maximum_speed
        print(f"The distance of electric car is {Ecar_distance} kilometers")


class GasolineCar(Car):
    def __init__(self, registration_number, maximum_speed, volume_tank):
        self.volume_tank = volume_tank
        super().__init__(registration_number, maximum_speed)
        Gcar_distance = hour * self.maximum_speed
        print(f"The distance of gasoline car is {Gcar_distance} kilometers.")


hour = 3
car_list = []
car_list.append(ElectricCar("ABC-15", 180, 52.5))
car_list.append(GasolineCar("ACD-123", 165, 32.3))

#12.1
import requests
request = "https://api.chucknorris.io/jokes/random"
response = requests.get(request).json()
print(response["value"])
print(f"The joke as following: {response['value']}.")

#12.2
import json
import requests

Enter_municipality = input("Enter the name of municipality: ")
request = ("http://api.openweathermap.org/data/2.5/weather?q=" +Enter_municipality + "&APPID=f8d1968db6a83d9aceb39e0711a32dbb")
response = requests.get(request)
if response.status_code==200:
    json_response = response.json()
    weather = json_response["weather"][0]
    description = weather["main"]
    temp_K = json_response["main"]["temp"]
    wind = json_response["wind"]
    wind_speed = json_response["wind"]["speed"]
    temp_C = temp_K - 273.15
    temp_C_print = round(temp_C,2)
    print(f"{Enter_municipality} is {description}. The temperature is {temp_C_print}ºC. Wind speed is {wind_speed}m/s.")

