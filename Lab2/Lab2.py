# Лабораторная работа 2

	#1 - Читаем files.txt
	#2 - Выписываем их в кортеж
	#3 - Создаем список numbers и append его после каждой иттерации по считыванию файла ---лучше написать в отдельную функцию-0
	#4 - Отдельная функция по подсчету статистических данных и их вывод
#import collections
import math

def file_reader():
	#Предположим что все файлы находятся в одной директории
	try:
		f = open('files.txt','r', encoding='ascii') # Файл с ссылками на другие файлы
		mylist = f.read().split() 
	except:
		print("Файла нет \n")
	
	numbers = [] # Список с числами полученными из файлов

	try:

		for i in mylist:
			with open(i, encoding = 'ascii') as f_in:
				numbers_file_in = f_in.read().split()  #Временный список чисел из читаемого файла
				numbers.extend(numbers_file_in)
	except:
		print("Файл из списка не найден \n")

	try:
		numbers = [int(item) for item in numbers]
	
	except:
		print("Найдено не число (NaN) \n")

	def list_sum(numList):
		theSum = 0
		for i in numList:
			theSum = theSum + i
		return theSum
	
	def mediana(numList):
		numList = sorted(numList)
		if len(numList) % 2 == 1:
			return numList[len(numList) // 2]
		else:
			return 0.5 * float((numList[len(numList) // 2 - 1] + numList[len(numList) // 2]))

	def find_popular_numbers(numList):
		#c = collections.Counter(numList)
		#out.append(c.most_common()[0][0])
		#out.append(c.most_common()[0][1])
		#out = c.most_common(3)
		#return out
		slovar = {}
		mod = []
		ch = 0
		for el in numList:
			try:
				slovar[el] += 1
				if ch < slovar[el]:
					ch = slovar[el]
			except KeyError:
				slovar[el] = 1
		ss = sorted(slovar.items(), key = lambda kv: kv[1], reverse = True)
		k = 0
		for e in ss:
			if k < 3:
				mod.append(e[0])
				k += 1
		return mod

	def std_otkl(numList):
		Sum = 0
		n = len(numList)
		sr_znach = list_sum(numbers)/n
		for i in numbers:
			temp = pow(sr_znach + i, 2)
			Sum += temp
		return((math.sqrt(Sum))/(n-1))	

	print("Количество элементов: ", len(numbers), "\n")
	print("Общая сумма: ", list_sum(numbers),"\n")
	print("Медиана: ", mediana(numbers), "\n")
	print("Наиболее часто встречающиеся:  ", find_popular_numbers(numbers), "\n")
	print("Стандартное отклонение: ", std_otkl(numbers), "\n")

	''' TEST Data '''
	#print(mylist)
	#print(numbers)

file_reader()