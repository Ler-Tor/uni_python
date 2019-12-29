import random
from math import fabs
import sys
import os
import string
strip = '\n' + "\"'"


def get_integer(message, name="целое число", default=None, minimum=0,
                maximum=100, allow_zero=True):

    class RangeError(Exception): pass

    message += ": " if default is None else " [{0}]: ".format(default)
    while True:
        try:
            line = input(message)
            if not line and default is not None:
                return default
            i = int(line)
            if i == 0:
                if allow_zero:
                    return i
                else:
                    raise RangeError("{0} не должен быть 0".format(name))
            if not (minimum <= i <= maximum):
                raise RangeError("{0} должен быть между {1} и {2} "
                        "включительно {3}".format(name, minimum, maximum,
                        (" (или 0)" if allow_zero else "")))
            return i
        except RangeError as err:
            print("ОШИБКА", err)
        except ValueError as err:
            print("ОШИБКА {0} должно быть целым числом".format(name))



def get_name_of_file():
    ls = os.listdir(".")
    lst_of_files = []
    for fl in ls:
        if (fl.find('.lst') != -1):
            lst_of_files.append(fl)
    print('Список файлов:')
    i = 1
    for names in lst_of_files:
        print(i, ':', names)
        i += 1
    name = ''
    while name == '':
        action = get_integer('Выберите номер файла (или 0 для создания нового файла)')
        if action == 0:
            name = input('Выберите имя файла: ')
            name = name + '.lst'
        else:
            try:
                name = lst_of_files[action - 1]
            except IndexError:
                print('Нет файла с указанным номером')
    return name


def read_file(name):
    str_of_file = []
    try:
        f = open(name, 'rt')
        for st in f:
            st = st.strip(strip)
            str_of_file.append(st)
        f.close()
    except IOError:
        f = open(name, "w")
        f.close()
    return str_of_file


def record_in_file(name, str_of_file):
    print('Сохранение ', len(str_of_file), ' строк в файл ', name)
    f = open(name, 'w')
    for st in str_of_file:
        f.write(st+'\n')
    f.close()


def add_in_lst(lst):
    new_lst = []
    a = input('Добавить строку: ')
    new_lst.append(a)
    new_lst.extend(lst)
    return new_lst


def print_lst(lst):
    if lst != []:
        print('Список строк:')
        i = 1
        for st in lst:
            print(i, ':', st)
            i += 1
    else:
        print('-- Список не содержит элементов --')


def delete_elem_in_lst(lst, number):
    a = lst.pop(number-1)
    return lst


def ask_save(file, lst):
    flag = 0
    while flag==0:
        action = input('Сохранить изменения (д/н) [д]: ')
        action.lower()
        if action == 'д' or action == 'l':
            record_in_file(file, lst)
            flag = 1
        elif action == 'н' or action == 'y':
            flag = 1
        else:
            print('Неккоректный ввод')


def big_menu_circle(f1, array_of_str):
    fg = 0
    fg1 = 0
    while fg == 0:
        if fg1 == 0:
            action = (input('[Д]обавить [У]далить [В]ыйти : '))
            action = action.lower()
            if action == 'д' or action == 'l':
                array_of_str = add_in_lst(array_of_str)
                print_lst(array_of_str)
                fg1 = 1
            elif action == 'в' or action == 'd':
                sys.exit(0)
            elif action == 'у' or action == 'e':
                fg2 = 0
                while fg2 == 0:
                    dele = get_integer('Введите номер строки для удаления (или 0 для выхода)')
                    if dele != 0:
                        try:
                            delete_elem_in_lst(array_of_str, dele)
                            print_lst(array_of_str)
                            fg2 = 1
                            fg1 = 1
                        except IndexError:
                            print('Нет такой строки')
                    else:
                        fg2 = 1
            else:
                print('Неккоректный ввод')
        elif fg1 == 1:
            action = input('[Д]обавить  [У]далить  [С]охранить  [В]ыйти : ')
            action = action.lower()
            if action == 'д' or action == 'l':
                array_of_str = add_in_lst(array_of_str)
                print_lst(array_of_str)
                fg1 = 1
            elif action == 'в' or action == 'd':
                ask_save(f1, array_of_str)
                sys.exit(0)
            elif action == 'с' or action == 'c':
                record_in_file(f1, array_of_str)
                fg1 = 0
            elif action == 'у' or action == 'e':
                fg2 = 0
                while fg2 == 0:
                    dele = get_integer('Введите номер строки для удаления (или 0 для выхода)')
                    if dele != 0:
                        try:
                            delete_elem_in_lst(array_of_str, dele)
                            print_lst(array_of_str)
                            fg2 = 1
                        except IndexError:
                            print('Нет такой строки')
                    else:
                        fg2 = 1
            else:
                print('Неккоректный ввод')


# MAIN
file1 = get_name_of_file()
print_lst(read_file(file1))
array = read_file(file1)
big_menu_circle(file1, array)
