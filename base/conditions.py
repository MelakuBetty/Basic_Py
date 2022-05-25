

#1#################################################################
num = int(input("Type a number: "))
num1 = int(input("Type another number"))
if num > num1:
    print("Max number is: ", num)
else:
    print("Max number is: ", num1)


#2#################################################################
num = int(input("Type a number: "))
num1 = int(input("Type a number: "))
num2 = int(input("Type a number: "))
if num == num1 == num2:
    print("The numbers are identical")
elif num > num1 and num > num2:
    print("Max number is: ", num)
elif num1 > num2:
    print("Max number is: ", num1)
else:
    print("Max number is: ", num2)


#3#################################################################
hour = int(input("Hours you have been parking: "))
elcCar = input("Is your car electric? Y / N ")
carYear = int(input("Type your car year: "))
price = 0
if hour <= 3:
    price = hour * 20
if hour >= 3 and hour <= 5:
    price = hour * 15
if hour >= 5 and hour <= 24:
    price = hour * 10
if hour > 24:
    price = hour * 5
if carYear == 2022 and elcCar == "Y":
    print("You have a 20% discount, please pay: ", price - (price * 0.2))
elif carYear == 2022 and elcCar == "N":
    print("You have a 15% discount, please pay: ", price - (price * 1.5))
else:
    print("You have a 10% discount, please pay: ", price - (price * 0.1))


#4#################################################################
L = [1, 8, 12, 48, -3, 14, 22, 15]
i = 0
while i < len(L):
    if L[i] < 0:
        if i > 0:
            L[i - 1] *= -1
        if i < len(L) - 1:
           L[i + 1] *= -1
        i += 1
    i += 1
print(L)
