
"""Exrcise from w3resource website"""

#EX6#############################################
num = input("Type numbers with comma: ")
list = num.split(",")
tuple = tuple(list)
print("list: ", list)
print("Tuple: ", tuple)

#EX9##############################################
date = (11, 12, 2014)
print("The date is:  %i - %i - %i" % date)


#EX12#############################################
import calendar
year = int(input("Type a year: "))
month = int(input("Type a month: "))
print(calendar.month(year, month))

#EX21##############################################
num = int(input("type "))
if num % 2 == 0:
    print("Even")
else:
    print("Not even")

#EX30###############################################
base = int(input("Type the base : "))
height = int(input("Type the height : "))

area = base*height/2

print("area = ", area)

#EX48################################################
n = input("Type an integer: ")
print(float(n))
print(int(float(n)))

#EX58##################################################
n = int(input("Input a number: "))
sum_num = (n * (n + 1)) / 2
print("Sum of the first", n, "positive integers:", sum_num)

#EX59############################################################################
choice = input("Type which convert you would like to change? foot / centimeters")
centimeters = 30.480000
if 'centimeters' in choice:
    height_centim = float(input("Type your height in 'centimeters': "))
    foot = height_centim / centimeters
    print("Your height in foot: ", foot)
else:
    height_foot = int(input("Type your height in 'foot': "))
    centim = height_foot * centimeters
    print("Your height in centimeters: ", centim)

#EX68########################################################################
num = int(input("Input a four digit numbers: "))
x = num // 1000
x1 = (num - x*1000)//100
x2 = (num - x*1000 - x1*100)//10
x3 = num - x*1000 - x1*100 - x2*10
print("The sum of digits in the number is", x+x1+x2+x3)

#EX69########################################################################
num = input("Input a three digit numbers: ")
list = sorted(num)
print(list)

#EX81############################################################
list_colors = ["pink", "orange", "white"]
colors = '-'.join(list_colors)
print(colors)

#EX84############################################################
sentence = input("Enter a sentence: ")
print("the number of times 'e' occured: ", sentence.count("e"))

#EX88#################################################################
num = int(input("Input a number: "))
num2 = int(input("Input a number: "))
sum = num + num2
print("x = ", num)
print("y = ", num2)
print(num, "+", num2, "=", sum)

#EX89##################################################################
n=30
if n == 30:
   print("\nlast day of a Month!")
print()

#EX98####################################################################
import time
print()
print(time.ctime())
print()

#other_option######################
import datetime
print(datetime.datetime.now())

#EX109######################################################################
num = int(input("Type a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Equal to zero")


#EX110######################################################################
list = [15, 25, 45, 90]
for i in range(len(list) - 1):
    if list[i] % 15 != 0:
        del list[i]
        new_list = list
print(new_list)

#EX112#####################################################################
ls = ["blue", "white", "black", "orange"]
print("List of colors: ", ls)
del ls[0]
print("List of colors after removing 'blue': ", ls)

#EX113####################################################################
while True:
    try:
        a = int(input("Input a number: "))
        break
    except ValueError:
        print("\nThis is not a number. Try again...")
        print()

#EX114######################################################################
ls = [5, -9, -7, 8, 10, -200]
newls = list(filter(lambda x: x > 0, ls))
print(newls)

#EX19#######################################################################
order_amt = 212.374
print('\nThe total order amount comes to %f' % order_amt)
print('The total order amount comes to %.2f' % order_amt)
print()

#EX120######################################################################
str_num = "1234567890"
print("Original string:",str_num)
print('%.6s' % str_num)
print('%.9s' % str_num)
print('%.10s' % str_num)

#EX31#######################################################################
var_list = ['a', 'b', 'c', 'd', 'e']
v, w, x, y, z = var_list
print(v, w, x, y, z)

#EX147######################################################################
def divide(num, num1):
    if num % num1 == 0:
        print("divide")
    else:
        print("not dividing")


divide(int(input("Type a number: ")), int(input("Type a number: ")))




