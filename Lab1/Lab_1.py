#Лабороторная работа 1

import random
import sys
random.seed(5)
def first_file_init(): 
    while(True):
        try:
            file1  = "/Users/vm/Desktop/Лабы/Lab1/" + input("Введите имя файла \n") + '.txt'
        except:
            print("Неверное имя \n")
            sys.exit(0)
        break
    while(True):
        try:
            rows = int(input("Введите число строк\n"))
        except:
            print("Не целое число\n")
            sys.exit(0)
        break
    while(True):
        try:
            A = float(input("Введите минимум\n"))
        except:
            print("Ошибка ввода\n")
            sys.exit(0)
        break
    while(True):
        try:
            B = int(input("Введите максимум\n"))
        except:
            print("Ошибка ввода \n")
            sys.exit(0)
        break
    def my_round(A, B):
        return round(random.uniform(A, B), 2)
    with open(file1, 'w') as f:
        for i in range(rows):
            [x1, y1, x2, y2] = [my_round(A,B), my_round(A,B), my_round(A,B), my_round(A,B)]
            f.write(f'{i + 1}. {x1} {y1} {x2} {y2} \n')
    

    

first_file_init()


        



