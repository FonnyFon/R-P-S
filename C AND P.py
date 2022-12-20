import random


def checkFaCtOrS():   # 1
    newList = []
    numbers = range(1500, 2701)
    for num in numbers:
        if num % 7 == 0 and num % 5 == 0:
            newList.append(num)
    return (newList)

active = True # 3
num = range(1, 10)
while active:
    computer = random.randrange(10)
    user_input = int(input("Enter your number:"))
    if user_input == computer:
        print("Well Guessed")
        active = False
    else:
        active = True


def stringReverse(word):  # 4
    print(word[::-1])


stringReverse('Farrhan')
stringReverse('Fareed')

def checkDiGiTs():   # 1
    newList = []
    numbers = range(100, 401)
    for num in numbers:
        if num % 2 == 0 and num % 2 == 0:
            newList.append(num)
    return (newList)

print(checkDiGiTs())
