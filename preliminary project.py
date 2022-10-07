import mysql.connector

connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='20220822Metropolia',
        autocommit=True
)
user_name = str.upper(input("Enter user name: "))
query1 = f'select * from happen2 where Location = "backgroud"'
cursor = connection.cursor()
cursor.execute(query1)
result1 = cursor.fetchall()
for row in result1:
        print(row[7])
        print(row[8])
acception = str.upper(input("Enter 'MISSION' to accept the game mission: "))
if acception == "MISSION":
                print(row[9])
                print(row[10])
if acception != "MISSION":
        print("Enter the correct word!")
destination1 = str.upper(input("Enter connecting airport: "))
if destination1 == "HELSINKI":
        query2 = f'select * from happen2 where Location = "Kemi"'
        cursor2 = connection.cursor()
        cursor.execute(query2)
        result2 = cursor.fetchall()
for row in result2:
        print(row[7])
        print(row[8],row[9])

location1 = str.upper(input("Enter your current location: "))
if location1 == "HELSINKI":
        print("You are in the Helsinki now. Remaining time is 22 hours 20 minutes.")
destination2 =str.upper(input("Enter your first destination: "))
if destination2 == "AMSTERDAM":
        query3 = f'select * from happen2 where destination = "Amsterdam"'
        cursor = connection.cursor()
        cursor.execute(query3)
        result3 = cursor.fetchall()
        for row in result3:
                print(row[7])
                print(row[8])
destination3 = str.upper(input("Would you like to continue to fly to Amsterdam or choose another city: "))
if destination3 == "ATHENS":
        print("The journey duration is 5 hours 15 minutes.")
        print("Remaining time is 20 hours 45 minutes.")
location4 = str.upper(input("Enter your current location: "))
if location4 == "ATHENS":
        print("Congratulations! You have arrived in your first destination.Write down important event.")
        print("TIPS: You can get information from newspaper at airport")
resource1 = str.upper(input("What do you find: "))
if resource1 == "FOREST FIRE":
        query4 = f'select * from happen2 where destination = "Athens"'
        cursor = connection.cursor()
        cursor.execute(query4)
        result4 = cursor.fetchall()
        for row in result4:
                print(row[7])
                print(row[8])
destination4 = str.upper(input("Enter your second destination: "))
if destination4 =="PARIS":
        print("The journey duration is 3 hours 35 minutes.")
        print("Remaining time is 15 hours 45 minutes.")
location5 = str.upper(input("Enter your current location: "))
if location5 =="PARIS":
        print("Congratulations! You have arrived in your second destination.Write down important event.")
        print("Remaining time is 10 hours 10 minutes.")
resource2 = str.upper(input("What is your plan: "))
if resource2 == "EIFFEL TOWER AT NIGHT":
        query5 = f'select * from happen2 where destination = "Paris"'
        cursor = connection.cursor()
        cursor.execute(query5)
        result5 = cursor.fetchall()
        for row in result5:
                print(row[7])
                print(row[8])
destination5 = str.upper(input("Enter your third destination: "))
if destination5 == "LONDON":
        print("The journey duration is 1 hour 15 minutes.")
        print("Remaining time is 7 hours 45 minutes.")
location6 = str.upper(input("Enter your current location: "))
if location6 =="LONDON":
        print("Congratulations! You have arrived in your third destination.Write down important event.")
        print("Remaining time is 4 hours 10 minutes.")
resource3 = str.upper(input("What is your plan: "))
if resource3 =="LONDON EYE":
        print("It is the most popular paid tourist attraction in the United Kingdom ")
resource4 = str.upper(input("What is your plan: "))
if resource4 =="HEATHROW AIRPORT":
                query6 = f'select * from happen2 where destination = "London"'
                cursor = connection.cursor()
                cursor.execute(query6)
                result6 = cursor.fetchall()
                for row in result6:
                        print(row[7])
                        print(row[8])
destination6 = str.upper(input("What is your plan: "))
if destination6 =="TAXI":
        print("'{}',Time out!".format(user_name))
        print("Game over!")
        print("Life goes on!")

