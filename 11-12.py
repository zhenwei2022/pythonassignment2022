#Lab 11-12
#11.1
class Publication:
    def __init__(self, name):
        self.name = name

class Book(Publication):
    def __init__(self, name, author, page_count):
        self.author = author
        self.page_count = page_count
        super().__init__(name)

    def print_information(self):
        print(f"The book name is {self.name}. The author is {self.author}. The book has {self.page_count} pages.")

class Magazine(Publication):
    def __init__(self, name, chief_editor):
        self.chief_editor = chief_editor
        super().__init__(name)

    def print_information(self):
        print(f"The chief editor of magazine is {self.chief_editor}.")

publication= []
publication.append(Book("Compartment NO.6", "Rosa Likson", 192))
publication.append(Magazine("Donald Duck", "Aki Hyyppä"))
for i in publication:
    i.print_information()
#11.2


#12.1
import requests

request = "https://api.chucknorris.io/jokes/random"
response = requests.get(request).json()
print("The joke as following.")
print(response["value"])

#12.2
import requests

city_information = input("Enter municipality name: ")
country_information = input("Enter country name: ")
request = "api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=f8d1968db6a83d9aceb39e0711a32dbb"
response = requests.get(request).json()
print(response)

