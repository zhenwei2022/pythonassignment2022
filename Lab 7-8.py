#Lab 7-8
#Lab 8.1
import mysql.connector

connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='20220822Metropolia',
        autocommit=True
)
ICAO_code = input("Enter ICAO code: ")
query = f'select * from airport where gps_code ="{ICAO_code}"'
cursor = connection.cursor()
cursor.execute(query)
result = cursor.fetchall()
for row in result:
    print(f'{row[3]} is located in {row[10]}')

#Lab 8.2
import mysql.connector

connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='20220822Metropolia',
        autocommit=True
)
areacode = input("Enter area code: ")
query = f'select * from airport where iso_country ="{areacode}"order by type desc'
cursor = connection.cursor()
cursor.execute(query)
result = cursor.fetchall()
for row in result:
    print(f"Airport {row[3]} is {row[2]}, located in {row[10]}")

#Lab 8.3
import mysql.connector

connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='20220822Metropolia',
        autocommit=True
)
airport1 = input("Enter ICAO code: ")
query1 = f'select * from airport where gps_code ="{airport1}"'
cursor = connection.cursor()
cursor.execute(query1)
result = cursor.fetchall()
for row in result:
    print(row[4],row[5])
airport1 = (row[4],row[5])
airport2 = input ("Enter ICAO code: ")
query2 = f'select * from airport where gps_code ="{airport2}"'
cursor = connection.cursor()
cursor.execute(query2)
result = cursor.fetchall()
for row in result:
    airport2 = (row[4],row[5])
    print(row[4],row[5])
from geopy import distance
print(distance.distance(airport1, airport2).km)

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

