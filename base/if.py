# 1################################################
a = int(input("Enter a number: "))
if a == 1:
    print("True")
elif a % 2 != 0:
    print("number is not even")
else:
    print("False")


# 2################################################
a = 5
b = 0
c = 11
if a > 0 and c > 0:
    print("OK")
if a > 0 or b > 0:
    print("Good")
if a > -1 and b > -1 and c > -1:
    print("Smart")


# 3################################################
a = int(input("Enter a number between 0 and 100: "))
if 0 < a < 100 and a == 1:
    print("1")
elif a == 2:
    print("2")
else:
    print("False")


# 4################################################
a = 3
b = "smart"
c = -4
d = "Group"
if a > 0:
    print("OK")
else:
    print("Not")
if c > 0:
    print("Good")
else:
    print("Nope")
if d == b:
    print("Same")
else:
    print("DIFFERENT")


# 5################################################
a = int(input("Enter a number between 1 and 5: "))
if a == 1:
    print("ONE")
elif a == 2:
    print("TWO")
elif a == 3:
    print("Three")
elif a == 4:
    print("Four")
elif a == 5:
    print("FIVE")
else:
    print("Wrong number")


# 6################################################
Tel_Aviv = input("Are you living in Tel-Aviv? Y/N ")
if Tel_Aviv == "N":
    print("Discount only for people living in Tel-Aviv")
elif Tel_Aviv == "Y":
    Age = int(input("what is your Age? "))
    if Age > 65:
        print("You may receive discount")
    elif Age <= 65:
        print("Too young for discount")


# 7################################################
Israeli = input("Are you an Israeli citizen? y/n ")
if Israeli == "y":
    print("Israeli citizen")
    Age = int(input("What is your age? "))
    if Age >= 18:
        print("You may receive discount")
    else:
        print("You are too young")
else:
    print("You are not an Israeli citizen")


# 8################################################
Hours = int(input("Type how much hours you park? "))
if Hours < 3:
    Money = Hours * 20
    print("You need to pay:", Money, "₪")
elif 3 < Hours < 5:
    Money1 = Hours * 15
    print("You need to pay:", Money1, "₪")
elif 5 < Hours < 24:
    Money2 = Hours * 10
    print("You need to pay:", Money2, "₪")
elif Hours > 24:
    Money2 = Hours * 5
    print("You need to pay:", Money2, "₪")
