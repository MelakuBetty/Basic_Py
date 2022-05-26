
"""Exrcise from w3resource website"""


#EX18#############################################
def sum_num(x, y, z):
    sum = x + y + z

    if x == y == z:
        sum = sum * 3
    return sum


print(sum_num(4, 6, 7))
print(sum_num(7, 7, 7))


#EX33###############################################
def sum(a, b, c):
    if a == b or b == c or a == c:
        sum = 0
    else:
        sum = a + b + c
    return sum


print(sum(2, 1, 2))
print(sum(3, 2, 2))
print(sum(2, 2, 2))
print(sum(1, 2, 3))


#EX34################################################
def numbers(a, b):
    sum = a + b
    if sum in range(a, b):
        print("20")
    else:
        return sum


print(numbers(10, 7))
print(numbers(9, 1))


# EX124################################################
def multiple_variables_equality(* vars):
   for x in vars:
       if x != vars[0]:
           return "All variables have not same value."
   return "All variables have same value."


print(multiple_variables_equality(2, 3, 2, 2, 2, 2))
print(multiple_variables_equality(10, 10, 10, 10))
print(multiple_variables_equality(-3, -3, -3, -3))
