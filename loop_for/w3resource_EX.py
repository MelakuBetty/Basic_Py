"""Exrcise from w3resource website"""


#EX22###############################################
def count_list(nums):
    count = 0
    for i in nums:
        if i == 4:
            count += 1
    return count


print(count_list([3, 8, 4, 6, 4]))
print(count_list([1, 2, 3, 5, 6]))

#EX27###############################################
def concatenate(list):
    count = 0
    result = ''
    for i in list:
        result += str(i)
    return result


print(concatenate([1, 2, 3, 4, 5]))


#EX50##################################################
for i in range(0, 10):
    print('*', end="")
print("\n")
