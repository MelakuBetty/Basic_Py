
# 1################################################
Age = int(input("Type your age: "))
if Age >= 18:
    pass
else:
    print("You are less then 18 years old")


# 2################################################
Guess = 92
num = int(input("Type a number: "))
while num != Guess:
    print("wrong number!, guess again")
    num = int(input("Type a number: "))
print("win!!!!!")


# 3################################################
total = 0
count = 0
price = input("please enter a price, 'Stop' to exit")
while price != 'Stop':
    count += 1
    total = total + int(price)
    price = input("please enter a price, 'Stop' to exit")
print(total)
print(total/count)


# 4################################################
num = int(input("Type a number: "))
while num > 0:
    if num % 3 == 0:
        print(num)
    num = num - 1
print("Number is not divisible by 3 with no remainder ")


# 5################################################
count = 0
Betty = "i love python"
while count < 4:
    count += 1
    print(Betty)


# 6################################################
num = 50
Guess = int(input("Type a number: "))
if 0 < num < Guess:
    print("Found!")


# 7################################################
num = 20
while num > 0:
    if num % 2 != 0:
        print(num)
    num = num - 1


# 8################################################
num = 19
while num > 0:
    print(num)
    num = num - 2


# 9################################################
start = int(input("Type a number: "))
end = int(input("Type a number: "))
for x in range(start, end):
    print(x)


# 10################################################
sum = 0
for x in range(1000):
    sum += x
print(sum)


# 11################################################
sum = 1
for x in range(1000,2500,4):
    sum *= x
print(sum)


# 12################################################
i = 1
while i <= 10:
    print(i)
    i += 1


# 13################################################
num = 1
k = 10
prod = 2
while num < prod + 1:
    prod **= num
    num += 1
print(prod)


# 14################################################
num = 1
k = 10
while num < k + 1:
    print(num ** 2)
    num += 1


# 15################################################
Grade = int(input("Enter your grade: "))
while Grade < 100:
    print("Must do another test")
    Grade = int(input("Enter your grade: "))
print("You are the queen!")


# 16################################################
import math
num = int(input("Enter a number: "))
while num == 10:
    print(math.pow(num, 2))
    num = int(input("Enter a number: "))
if num != 10:
    print("Try again")


# 17################################################
num = 1
while num < 20:
    if num % 2 != 0:
        print(num)
    num += 1


# 18################################################
User = input("Which number do you want: even / uneven ?")
num = int(input("Type a number: "))
for even in User:
    if num % 2 != 0:
        print(num)
        num += 1
    if num % 2 == 0:
        print(num)
        num += 1
print("Error")
