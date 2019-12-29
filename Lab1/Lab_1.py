import random

random.seed(5)

def init_file_one():

	while(True):
		try:
			filepath = input("Введите название файла: \n" ) + ".txt"
			break
		except:
			pass
	
	while(True):
		try:
			size = int(input( "Введите кол-во строк вашего файла: \n" ))
			break
		except:
			print( "Ошибка ввода \n" )

	while(True):
		try:
			First_dot = int(input( "Введите начальную точку: \n" ))
			break
		except:
			print( "Ошибка ввода \n" )
	
	while(True):
		try:
			Second_dot = int(input( "Введите конечную точку: \n" ))
			break
		except:
			print( "Ошибка ввода \n" )

	def my_rand(Up, Down):

		return round(random.uniform(Up, Down), 2)

	with open(filepath, 'w') as f:

		for i in range(size):

			[x1, y1, x2, y2] = [float(my_rand(First_dot, Second_dot)), float(my_rand(First_dot, Second_dot)), float(my_rand(First_dot, Second_dot)), float(my_rand(First_dot, Second_dot))]

			f.write( f'{x1:>9.2f} {y1:>9.2f} {x2:>9.2f} {y2:>9.2f}\n' )

	print( f'\nПуть файла: {filepath}',

		f'\nКол-во строк в файле: {size}',

		f'\nДиапазон точек: от {First_dot} до {Second_dot}')

	Slov = {'filename': filepath,

			'size': size,

			'range': [First_dot, Second_dot] }

	with open(filepath) as f:
		i = 1
		for line in f:
			print(str(i) + ".",line)
			i +=1

	return Slov

file_one = init_file_one()
print(file_one)

def init_file_two(file_one, size, filename_two="out_file.txt"):

	Tochki = []

	with open(file_one) as f:
		count = 1
		for line in f:
			Tochki.append(line[:-1].split(" "))

	#Tochki = [x for x in Tochki if len(x) != 0]
	try:
		with open(filename_two, 'w') as f:
			for i in Tochki:
				i = [x for x in i if len(x) != 0]
				N = list(map(lambda x: float(x), i))
				[x1, y1, x2, y2] = N
				dist = ( (x1 - x2) ** 2 + (y1 - y2) ** 2 ) ** 0.5
				f.write( f'{dist}\n' )

	except ValueError:
		print()

init_file_two(file_one['filename'], file_one['size'])

def out_file_two(filename_two = "out_file.txt"):

        with open(filename_two) as f:
                for line in f:
                        print(line)

out_file_two()

def out_file_two_mean(filename_two="out_file.txt"):
	#Подсчет среднего значения
	summ = 0
	count = 0

	with open(filename_two) as f:
		for line in f:
			summ += float(line)	
			count += 1
	print( "Среднее по файлу: ",summ/count )

out_file_two_mean()



