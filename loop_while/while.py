
# 1###########################################################
i = 1
while i < 20:
    if i % 2 != 0:
        print(i)
    i += 1

# 2############################################################
i = int(input("Type: 1-uneven, 2-even "))
y = int(input("Type a number "))
while i > 0:
    if i % 2 != 0:
        if y % 2 != 0:
            print(y)
        y += 1
print("Error")

# 3############################################################
guess = 10
user = int(input("guess a number: "))
while i < 1000:
    if user > guess:
        print("Your number is: ",user)

# 4############################################################
guessnum = int(input("guess a number between 1-1000: "))
start = 1
end = 1000
ran = (start+end)//2
while guessnum != ran:
    if guessnum > ran:
        start = end // 2
        ran = (start+end) // 2
        print(ran,start)
    else:
        end = end // 2
        ran = (start + end) // 2
        print(ran,end)
print("found", guessnum)

# 5############################################################
sum = 0
count = 0
i = input("Type number: ")
while i != 'q':
    num = int(i)
    print(i)
    sum += num
    count += 1
    i = input("Type number: ")
Avg = sum / count
print(Avg)


# 6############################################################
count = 0
sum = 0
user = input("Type a number: ")
while user != 'done':
    num = int(user)
    print(user)
    sum += num
    count += 1
    user = input("Type a number: ")
print("avg: ", sum / count,"\n", "Big: ", max(user))
