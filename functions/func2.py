
# EX1##########################################################

def get_num(num):
    if num % 2 == 0:
        print("0")
    else:
        print("1")


def main():
    num = int(input("please enter number"))
    get_num(num)


main()


# EX2##########################################################
def get_nums_avg(n):
    sum = 0
    for i in range(n):
        numbers = int(input("Enter the number: "))
        sum += numbers
    print(sum/n)


get_nums_avg(int(input("Enter number of elements : ")))


# EX3##########################################################
def get_num():
    num = int(input("Type a number: "))
    while True:
        if num == -999:
            break
        else:
            z = len(str(num))
            print(z)
            num = input("Type a number: ")


get_num()


# EX4##########################################################
def change():
    money = int(input("Type your money: "))
    bill20 = money // 20
    bill10 = (money - (bill20 * 20)) // 10
    bill5 = (money - (bill20 * 20) - 10) // 5
    bill1 = (money - (bill20 * 20) - 10 - 5) // 1
    print(bill20)


change()
