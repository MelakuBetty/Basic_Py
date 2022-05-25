"""HomeWork"""


#1#################################################################
import math
num = int(input("Enter a number: "))
print(math.pow(num, 2))


#2#################################################################
Age = int(input("Type your age: "))
age_20 = Age + 20
print("In 20 years you will be ", age_20, " years old.")


#3#################################################################
price = int(input("Enter price: "))
print(price*1.17)


#4#################################################################
num = input("enter 2 numbers: ")
new_num = int(num[0])
new_num2 = int(num[1])
print(" Sum: ", new_num + new_num2, "\n", "Difference: ",
      new_num2 - new_num, "\n", "multiply: ", new_num2 * new_num, "\n",
      "Division: ", new_num2 / new_num)


#5%################################################################
import datetime
x = datetime.datetime.now()
b = datetime.datetime.now()
print("Welcome: ", x.strftime("%A"), b.strftime("%x"))


#6#################################################################
num = input("enter 4 numbers: ")
new_num1 = int(num[0])
new_num2 = int(num[1])
new_num3 = int(num[2])
new_num4 = int(num[3])
Avg = ((new_num1 + new_num2 + new_num3 + new_num4) / 4)
print("The average is: ", Avg)


#7################################################################
masmerim = int(input("Type a amount of masmerim: "))
Box = int(masmerim / 40)
print("The amount of boxes you need is: ", Box)


#8#################################################################
kilometer = int(input("Type your kilometers: "))
Speed = int(input("Type your speed: "))
timeH = kilometer/Speed
timeM = (kilometer/Speed)*60
print(timeH,timeM)


#9#################################################################

num = input("enter your phone number without the first digit: ")
print("the number is:", '0' + num)
