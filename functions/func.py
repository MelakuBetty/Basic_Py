import math

# 1########################################################
def square(a):
    s = math.pow(a, 2)
    p = 4 * a
    print("square:  side = ", a)
    print("area: ", s)
    print("perimeter: ", p)


def rectangle(a, b):
    s = a * b
    p = 2 * (a + b)
    print("square:  side1 =", a, ",side2 =", b)
    print("area: ", s)
    print("perimeter: ", p)


def main():
    choice = int(input("הקלד 1 לריבוע,2 למלבן"))
    side = int(input("אורך צלע -->"))
    if choice == 1:
        square(side)
    else:
        rectangle(side, 2 * side)


main()


# 2######################################################
def get_positive_num():
    num = int(input(" <-- הקלד מספר חיובי"))
    while num <= 0:
        print("שגיאה! המספר אינו חיובי. נסה שוב!")
        num = int(input(" <-- הקלד מספר חיובי"))
    return num


def summ(a, b):
    return a + b


def main():
    # get_positive_num()
    a = int(input("Type a number: "))
    b = int(input("Type a number: "))
    print(summ(a, b))


main()


# 3#############################################################
#---פעולה שקולטת ומחזירה מספר שלם---


def get_num():
    num = int(input("הקש מספר ארוך, שלם וחיובי: "))

    while num <= 0:
        print("המספר אינו חיובי")
        num = int(input("הקש מספר שלם וחיובי: "))
    return num

#--- פעולה הקולטת ומחזירה מספר חד ספרתי לא שלילי ---


def get_digit():
    num = int(input("הקש מספר: "))

    while num < 0 or num > 9:
        print("זו אינה ספרה, נסה שוב")
        num = int(input("הקש מספר: "))
    return num


#--- פעולה המקבלת כפרמטר מספר וספרה ---
#--- סופרת ומחזירה כמה פעמים הופיעה הספרה במספר ---
def count_digit(num, digit):
    count = 0
    while num > 0:
        d = num % 10            # האחדות ספרת
        if d == digit:
            count = count + 1
        num = num // 10
    return count


def main():
    num = get_num()
    digit = get_digit()
    count = count_digit(num, digit)
    print("digit ", digit, " appears in ", num, ": ", end=" ")
    print(count , " times")


main()
