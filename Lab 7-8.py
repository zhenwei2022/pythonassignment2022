#Lab 7-8
#Lab 7.1
season_of_year = ("Winter","Winter","Spring","Spring","Spring","Summer","Summer","Summer","Autumn","Autumn","Autumn","Winter")
month_number = int(input("enter a num of month(1-12):  "))
season = season_of_year[month_number -1]
print(f"{month_number} month is {season}.")

#Lab 7.2
my_set = set()
enter_name = input("enter name: ")
while enter_name != " ":
    if enter_name in my_set:
        print("Existing name")
        enter_name = input("enter name: ")
    elif enter_name not in my_set:
        print("New name")
        my_set.add(enter_name)
        enter_name = input("enter name: ")
while enter_name ==" ":
    print(my_set)
    break

#Lab 7.3
x = {}
information = str.upper(input("Would you like to enter a new airport,fetch information or quit:"))
while information == str.upper("enter a new airport"):
    enter_ICAO = str.upper(input(" Enter the ICAO code : "))
    enter_name = str.upper(input(" Enter the name of airport : "))
    x[enter_ICAO] = enter_name
    print(x)
    information = str.upper(input("Would you like to enter a new airport,fetch information or quit:"))
while information == str.upper("fetch information"):
    fetch_ICAO = str.upper(input(" Enter the ICAO code : "))
    print(x[fetch_ICAO])
    information = str.upper(input("Would you like to enter a new airport,fetch information or quit:"))
while information == str.upper("quit"):
        print("Program execution ends")
        break