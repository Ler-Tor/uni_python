#Лабораторная работа 4

class Books():
	
	def __init__(self, id_book, book_name, id_knizn):
		self.id_book = id_book
		self.book_name = book_name
		self.id_knizn = id_knizn

	def get_id_book(self):
		return self.id_book

	def get_book_name(self):
		return self.book_name

	def get_id_knizn(self):
		return self.id_knizn

class Kizn_mag():

	def __init__(self, id_knizn, knizn_name, knig_list):
		self.__id_knizn = id_knizn
		self.__knizn_name = knizn_name
		self.__knig_list = knig_list

	def get_id_kniznogo(self):
		return self.__id_knizn

	def get_knizn_name(self):
		return self.__knizn_name

	def get_knig_list(self):
		return self.__knig_list

class Knigi_Kniz():

	def __init__(self, id_book, id_knizn):
		self.__id_book = id_book
		self.__id_knizn = id_knizn

	def get_id_boook(self):
		return self.__id_book

	def get_id_kniznoogo(self):
		return self.__id_knizn

def test_1():
	Book_1 = Books(1, 'Ew', 1)
	Book_2 = Books(2, 'qwv', 1)
	Book_3 = Books(3, 'Swerto', 1)
	spisok = [Book_1, Book_2, Book_3]
	return spisok

def test_2():
	Book_4 = Books(4, 'Kova', 2)
	Book_5 = Books(5, 'Lot', 2)
	Book_6 = Books(6, 'Not', 2)
	spisok = [Book_4, Book_5, Book_6]
	return spisok

def test_3():
	Book_7 = Books(7, 'Rem', 3)
	Book_8 = Books(8, 'Set', 3)
	Book_9 = Books(9, 'Wow', 3)
	spisok = [Book_7, Book_8, Book_9]
	return spisok

def create_test_data_otdel():
	knizn_1 = Kizn_mag(1, "Первый", test_1())
	knizn_2 = Kizn_mag(2, "Второй", test_2())
	knizn_3 = Kizn_mag(3, "Третий", test_3())
	knizn_list = [knizn_1, knizn_2, knizn_3]
	return knizn_list

def zaprosy_zadanie():
	bd = create_test_data_otdel()
	
	def Spisok_po_Kniznomu(bd): 
		vp = [el.get_knizn_name() for el in bd]
		ks = [len(el.get_knig_list()) for el in bd]
		for i in range(len(vp)):
			print(vp[i], ks[i])

	def Spisok_po_A(bd):
		spisok = [o.get_book_name() for el in bd for o in el.get_knig_list() if o.get_book_name()[0] == 'A']
		print(*spisok)

	def vse_kniz_s_A(bd):
		for obj in bd:
			ch = 0
			for el in obj.get_knig_list():
				if el.get_book_name()[0] == 'A':
					ch += 1
					if len(obj.get_knig_list()) == ch:
						print(obj.get_knizn_name())

	def vse_kniz_s_a_h(bd):
		pr = set([obj.get_knizn_name() for obj in bd for el in obj.get_knig_list() if el.get_book_name()[0] == 'A'])
		print(*pr)

	def print_sort_po_kniznim(bd):
		s_o_n = [ob.get_knizn_name() for ob in bd]
		s_o = [ob for ob in bd]
		for i in sorted(s_o_n):
			for l in s_o:
				if l.get_knizn_name() == i:
					print(i);
					f = l.get_knig_list()
					for el in f:
						print(el.get_book_name(), sep=',,,', end=' ')
					print('\n')
				else:
					continue
	
	Spisok_po_Kniznomu(bd)
	Spisok_po_A(bd)
	vse_kniz_s_A(bd)
	vse_kniz_s_a_h(bd)
	print_sort_po_kniznim(bd)


zaprosy_zadanie()
















