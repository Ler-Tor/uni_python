#Вариант 4
counter = 1
def deco(f):
    global counter
    print("Число вызовов функции func():", counter)
    counter = counter + 1
    return f
def func(x):
    return x * 2
i = 0
while i < 14:
    print(deco(func)(i))
    i += 1
