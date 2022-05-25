#1#############################################
for num in range(1,20):
    if num % 2 != 0:
        print(num)


#2##############################################
num = int(input("Type a number: "))
for num in range(1,num):
    if num % 2 != 0:
        print(num)


#3##############################################
sum = 0
for i in range(1,13):
    sum += 1
    print(i)


#4##############################################
for i in range(100, 5000, 4):
    print(i)


#5##############################################
for i in range(5,2500):
    if i % 6 == 0:
        print(i)


#6##############################################
user = input("Type a sentence: ")
n = len(user)
for i in range(n):
    print(user[i], end=" ")


#7##############################################
num = input("Type a number with 5 digits: ")
num1 = input("Type a number with 5 digits: ")
for i in range(len(num)):
    if num[i] == num1[i]:
        print(num[i])
        num = input("Type a number with 5 digits: ")
        num1 = input("Type a number with 5 digits:: ")
print(num[i])


#8##############################################
for i in range(1, 101):
    for j in range(i,1):
        if i % j == 0:
            break
    print(i)


#9############################################
i = int(input("Type a number between 100-500: "))
for i in range(100, 500):
    if i != 287:
        i = int(input("Type a number between 100-500: "))
        if i == 287:
            break
print("Good guess")

for i in range(10, 20 + 1):
    if i == 13:
        continue
    print(i)


#10##############################################
x = int(input("Type a number: "))
y = x - 4
for i in range(x):
    for j in range(y):
        print('*', end=' ')
    print()
