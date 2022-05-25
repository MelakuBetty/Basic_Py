
# 1#############################################################
User = input("Enter 2 numbers: ")
new_num = int(User[0])
new_num2 = int(User[1])
if new_num > new_num2:
    print(new_num, ",is bigger then", new_num2)
else:
    print(new_num2, ",is bigger then", new_num)


# 2#############################################################
User = input("Enter 2 numbers: ")
new_num = int(User[0])
new_num2 = int(User[1])
if new_num//new_num2 == 0 and new_num % 2 == 0:
    print("djbv")


# 3#############################################################
Fullname = input("Fullname: ")
Address = input("Address: ")
School = input("School: ")
Age = int(input("Age: "))
User1 = Fullname, Address, School, Age
User2 = Fullname, Address, School, Age
User3 = Fullname, Address, School, Age
if User1 < User2 or User1 < User3:
    print(User1, "is big")
if User1 < User1 or User2 < User3:
    print(User2, "is big")
if User3 < User1 or User3 < User2:
    print(User3, "is big")
