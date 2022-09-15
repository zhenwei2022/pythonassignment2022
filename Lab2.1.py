 # Lab 2.6
import random
print(random.randint(0,9))
print(random.randint(0,9))
print(random.randint(0,9))
import random
value = random.randint(1111,6666)
print(value)

#Lab 2.5
#num1="enter talents"
#num2="enter prouds"
#nub3="enter lots"
num1=input("enter talents: ")
num2=input("enter pounds: ")
num3=input("enter lots: ")
result = float(((float(num1)*20 + float(num2)) * 32 + float(num3)) * 13.3)
print((str(int(result)) + "kilograms"))
gram = int(result)%1000
print(str(round(gram,2))+"grams")

#Lab 2.4
num1 = input("Enter num1: ")
num2 = input("Enter num2: ")
num3 = input("Enter num3: ")
print(float(num1) + float(num2) + float(num3))
print(float(num1) * float(num2) * float(num3))
print((float(num1) + float(num2) + float(num3))/3)

# Lab 2.3
import math
# num1 = "the length of the rectangle"
# num2 = "the width of the rectangle"
# perimeter = 2 * (num1 + num2)
# area = num1 * num2
num1 = input("Enter num1: ")
num2 = input("Enter num2: ")
print(2*(float(num1)+float(num2)))
print(float(num1) * float(num2))

# Lab 2.2
import math
r = float(input("enter the value of r: "))
print((math.pi) * r * r)

# Lab 2.1
name = input("Enter your name : ")
print("Hello," + name+ "!")

# Lab 1.1
name = input("Enter your name : ")
print("Hello," + name + "!")
