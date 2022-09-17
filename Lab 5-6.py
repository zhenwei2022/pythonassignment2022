#Lab 5-6
#Lab 6.1
def dice():
    import random
    list = []
    num = random.randint(1, 6)
    while num< 6:
        list.append(num)
        num = random.randint(1, 6)
    else:
        print(list)
        return
dice()

#Lab 6.2
def dice(max):
    import random
    list = []
    num = random.randint(1, 21)
    while num< max:
        list.append(num)
        num = random.randint(1, 21)
    else:
        print(list)
        return
max = int(input("please enter the maximum number: "))
dice(max)

#Lab 6.3
def conversion():
    gallon = input("please enter the quantity of gasoline (gallon): ")
    while gallon != " ":
        liter = 3.78541178 * int(gallon)
        print(liter)
        gallon = input("please enter the quantity of gasoline (gallon): ")
    else:
        print("execution stopped")
        return
conversion()

#Lab 6.4
def my_function(caltulation):
    list2 = []
    for i in range(0, num):
        ele = int(input())
        list1.append(ele)
        liter = int(3.78541178 * ele)
        list2.append(liter)
        print(list1)
        print(list2)
        print(sum(list2))
    return
list1 = []
num = int(input("Enter number of elements:"))
my_function(list1)

#Lab 6.5
def my_function(fetch):
    list2 = list(filter(lambda num: num % 2 == 0,list1))
    print(list1)
    print(list2)
    return
list1 = []
num = int(input("Enter number of elements:"))
for i in range(0, num):
        ele = int(input())
        list1.append(ele)
my_function(list1)

#Lab 6.6
def calculation():
    import math
    area1 = math.pi * (diameter1 / 200) *(diameter1 / 200)
    area2 = math.pi * (diameter2 / 200) * (diameter2 / 200)
    pizza1 = price1 / area1
    pizza2  = price2 / area2
    print(pizza1)
    print(pizza2)
    if pizza1 < pizza2:
        print("pizza1 is better value")
    else:
        print("pizza2 is better value")
        return
pizza1 = int(input("please enter the diamter1:  and price  "))

calculation()


#Lab 5.1
import random
import math
num = input("How many dice to roll: ")
list = []
roll = 0
for roll in range(0, num):
    if roll <= num + 1:
        dice = int(random.randint(1,6))
        list.append(dice)
        roll = roll + 1
        total = sum(list)
        print(list)
        print(total)

# Lab 5.2
mylist=[]
num= input("Enter number: ")
while str(num) != " ":
    mylist.append(int(num))
    num = input("Enter number: ")
while str(num) == " ":
    print(mylist)
    list.reverse(mylist)
    print(mylist[0:5])
    break

# Lab 5.3
import math
num = int(input("enter a integer: "))
k = int (math.sqrt(num))
if num <= 1:
    print("This is not a prime number")
if num >1:
    for i in range(2, k+2):
        if num % i == 0:
            print("This is not a prime number")
            break
        if i== k +1:
            print("This is a prime number")

#Lab 5.4
list=[]
city = input(" Enter city name: ")
for round in range(0,5):
    list.append(city)
    round = round + 1
    city = input(" Enter city name: ")
for items in list:
        print(items)