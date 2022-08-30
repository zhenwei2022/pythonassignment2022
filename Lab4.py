# Lab4.1
num = 1
while 3 * num <= 1000:
    print(3 * (num))
    num = num + 1

# Lab4.2
inch = float(input("enter inch: "))
while inch >= 0:
    print(str(2.54 * inch) + "cm")
    break
while inch < 0:
    break

# Lab 4.3
mylist=[]
num= input("Enter number: ")
mylist.append(num)
while str(num) != " ":
    num= input("Enter number: ")
    mylist.append(num)
while str(num) == " ":
    mylist.remove(" ")
    mylist = list(map(int,mylist))
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


