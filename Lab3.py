# Lab 3.1
length = float(input("Enter the length of the zander(in centimeters): "))
if length >= 42:
    print("It meets the size limit.")
else:
    print("It does not fulfiil the size limit.The limit of the size is 42 centimeters. Please release the fish back into the lake. ")

# Lab 3.2
cabin = input("enter cabin class(LUX/A/B/C): ")
if str.upper(cabin) == "LUX":
    print("upper-deck cabin with a balcony.")
elif str.upper(cabin) == "A":
    print("above the car deck, equipped with a window.")
elif str.upper(cabin) == "B":
    print("windowless cabin above the car deck.")
elif str.upper(cabin) == "C":
    print("windowless cabin below the car deck.")
else:
    print("error message! please input valid cabin class.")

# Lab 3.3
gender = input(" enter your gender(female/male) : ")
hemoglobin = input(" enter your hemoglobin(g/l) : ")
if str.upper(gender) == "FEMALE" and int(hemoglobin) >= 156:
    print("your hemoglobin value is high.")
elif str.upper(gender) == "FEMALE" and int(hemoglobin) >= 117:
    print("your hemoglobin value is normal.")
elif str.upper(gender) == "FEMALE" and int(hemoglobin) <= 116:
    print("your hemoglobin value is low.")
elif str.upper(gender) == "MALE" and int(hemoglobin) >= 168:
    print("your hemoglobin value is high.")
elif str.upper(gender) == "MALE" and int(hemoglobin) >= 134:
    print("your hemoglobin value is normal.")
else:
    print("your hemoglobin value is low.")

# Lab 3.4
year = input(" enter the year: ")
if int(year) % 4 != 0:
    print(" It is not leap year.")
elif int(year) % 4 == 0 and int(year) % 100 != 0:
    print(" It is leap year.")
elif int(year) % 4 == 0 and int(year) % 100 == 0 and int(year) % 400 == 0:
    print(" It is leap year.")
else:
    print(" It is not leap year.")