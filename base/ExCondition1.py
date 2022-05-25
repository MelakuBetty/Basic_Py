# 1################################################
Age = int(input("Type your age: "))
if Age > 7:
    print("Go to the left side")
else:
    print("Go to the right side")


# 2################################################
Age = int(input("Type your age: "))
if Age > 7:
    print("Go to the left side")
else:
    print("Go to the right side")


# 3################################################
Plate = int(input("How many plates would you like? : "))
if Plate == 1:
    print("The price is 15₪")
elif Plate == 2:
    print("The price is 25₪")
elif Plate == 3:
    print("The price is 30₪")
else:
    print("We do not sell over 3 Plates")


# 4################################################
num1 = 1
num2 = 2
num3 = 3
print(num1, num2, num3)
User = int(input("Witch of the numbers is the biggest? "))
if User == num3:
    print("Bravo")
else:
    print("Wrong")


# 5################################################
num = int(input("Type a number: "))
if num < 10 and num > 10:
    if num % 2 == 0 or num % 3 == 0:
        print("All conditions is happening")
else:
    print("Error")


# 6################################################
Age = int(input("Type your age: "))
if Age < 0 or Age > 120:
    print("Age is not risible")
else:
    print("Age risible")


# 7################################################
Angle = int(input("Type an Angle: "))
if Angle > 0 and Angle < 90:
    print("sharp angle")
if Angle == 90:
    print("right angle")
elif Angle > 90 or Angle < 180:
    print("Obtuse angle")


# 8################################################
Name = input("Type your name: ")
Age = int(input("Type your age: "))
Experience = int(input("Years of experience: "))
if Experience >= 3 and 25 <= Age <= 40:
    print("You are hired")
else:
    print("sorry,", Name, ",but you are not hired")


# 9################################################
a = int(input("Type a number: "))
b = int(input("Type a number: "))
c = int(input("Type a number: "))
if b < a < c:
    print("First number is between 'b' and 'c'")
else:
    print("First number is not between 'b' and 'c'")
