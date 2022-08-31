# Lab4.1
num = 1
while num <= 1000:
    if int(num) % 3 == 0:
        print(num)
    num = num + 1

# Lab4.2
inch = float(input("enter inch: "))
while inch >= 0:
    print(str(2.54 * inch) + "cm")
    inch = float(input("enter inch: "))
while inch < 0:
        print("The program ends")
        break

# Lab 4.3
mylist=[]
num= input("Enter number: ")
while str(num) != " ":
    mylist.append(num)
    num = input("Enter number: ")
while str(num) == " ":
    print(min(mylist))
    print(max(mylist))
    break

#Lab 4.4
import random
num1 = random.randint(1,10)
num2 =int(input("enter number: "))
while num1 > num2:
    print("Too low")
    num2 = int(input("enter number: "))
while num1 < num2:
    print("Too High")
    num2 = int(input("enter number: "))
while num1 == num2:
        print("correct")
        break

#Lab 4.5
num = 1
username1 = "python"
password1 = "rules"
username2 = input("enter your username: ")
password2 = input("enter password: ")
while num <= 4:
    if username1 == username2 and password1 == password2:
        print("Welcome")
        break
    if username1 != username2 or password1 != password2:
        username2 = input("enter your username: ")
        password2 = input("enter password: ")
        num = num + 1
while num >= 5:
    if username1 == username2 and password1 == password2:
        num = num + 1
        print("Welcome")
    if username1 != username2 or password1 != password2:
        num = num + 1
        print("Access denied")
    break

Lab4.6
import random
import math
num = 0
darts = 1000000
for i in range(1,1000000):
    x = random.random()
    y = random.random()
    r = math.sqrt(x ** 2 + y ** 2)
    if r <= 1:
        num = num + 1
    else:
        pass
    pi=4*(num/darts)
print(pi)



