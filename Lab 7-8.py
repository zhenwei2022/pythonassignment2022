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
