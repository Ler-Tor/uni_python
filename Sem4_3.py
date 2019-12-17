symbol = 's'
height = 3
width = 3
counter = 3

def dec1(f):
    global counter
    print("Число вызовов функции func():", counter)
    counter = counter + 1
    return f

def dec2(f):
    global symbol, width, height
    if len(symbol) != 1:
        raise Exception( "Переменная symbol должна быть односимвольной строкой" )
    if width <= 2:
        raise Exception( "Значение width должно превышать 2" )
    if height <= 2:
        raise Exception( "Значение height должно превышать 2" )
    return f
@dec1
@dec2
def f():
    return 2

