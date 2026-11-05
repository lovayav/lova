#-----------1------------
from math import*
x = float(input('x:'))
if x <= -3:
    y = sin(x**2)
elif -3 < x < 5:
    y = 1 + exp(-x)
else: y = log(x**2)/(3+4*x)

print(f"y = {y}")

#---------------2---------------------
age = int(input("от 20 до 40:"))
if age < 20 or age > 40:
    print("не подходит!")
else:
    word10 = {2: "двадцать", 3: "тридцать", 4: "сорок"}
    word1 = {1: "один", 2: "два", 3: "три", 4: "четыре", 5: "пять", 6: "шесть",\
             7: "семь", 8: "восемь", 9: "девять"}

    desyat = age//10
    odin = age%10

    if odin == 0:
        slovo = word10[desyat]
        word = "лет"
    else:
        slovo = f"{word10[desyat]} {word1[odin]}"
        if odin == 1:
            word = "год"
        elif 2 <= odin <= 4:
            word = "года"
        else: word = "лет"
    print(f"{age} - {slovo} {word}")

















