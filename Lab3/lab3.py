#Лабораторная работа 3
import os, sys


def main():
    while (1):
        files = file_search()


def file_search():
    dirs = os.listdir(".")
    lsts = filter(lambda x: x.endswith('.lst'), dirs)
    print(lsts)
    i = 1
    print("Список файлов: ")
    
    for file in lsts:
        if  lsts == 1: #####Переписать
            print("Файлы с искомым расширением не найдены \n")
        else:
            print(str(i) + ". " + file + "\n")
            i += 1

file_search()