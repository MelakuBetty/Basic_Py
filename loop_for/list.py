
# 1##################################################
for i in range(5):
    print("Love Python")


# 2##################################################
ls = []
for i in range(11):
    ls.append(i)
print(ls)


# 3##################################################
ls = []
for i in range(3):
    num = int(input("Type a number: "))
    ls.append(num)
print(ls)
x = sorted(ls)
print(x)


# 4##################################################
ls = []
newList =[]
countplus = 0
countminus = 0
maxn = 0
minn = 10000000
countEven = 0
countdivied3 = 0
for i in range(3):
    num = int(input("Type a number: "))
    ls.append(num)
    for i in ls:
        divide = i / 11
        newList.append(divide)
        if i > 10:
            countplus += 1
        if i < 10:
            countminus += 1
        if num > maxn:
            maxn = num
        if num < minn:
            minn = num
        if i % 2 == 0:
            countEven += 1
        if i % 3 == 0:
            countdivied3 += 1
x = sorted(ls)
print("Diveded by 11: ", newList)
print("List of numbers: ", ls)
print("list sorted: ", x)
print("Numbers bigger then 10: ", countplus)
print("Numbers smaller then 10: ", countminus)
print("max number: ", maxn)
print("min number: ", minn)
print("Even numbers: ", countEven)
print("numbers divied by 3: ", countdivied3)


# 5#################################################
data_numbers = []
for i in range(11):
    newnum = int(input("Type a number: "))
    num = newnum + 1
    if num != newnum:
        print(num, newnum)
