class Driver():

	def __init__(self, id_s, sur, id_o): 
	
		self.__ID_S = id_s
		self.__Surname = sur
		self.__ID_O = id_o

	def get_id_s(self):
		return self.__ID_S

	def get_id_o(self):
		return self.__ID_O

	def get_sur(self):
		return self.__Surname

class AvtoPark():

	def __init__(self, id_o, name, sot_list): 
	
		self.__ID_O = id_o
		self.__Name = name
		self.__Lst = sot_list

	def get_id_0(self):
		return self.__ID_O

	def get_name(self):
		return self.__Name

	def get_sot_list(self):
		return self.__Lst

class Rabotnik_AvtoParka():

	def __init__(self, id, id_p): 

		self.__ID_V = id
		self.__ID_P = id_p

	def get_id_v(self):
		return self.__ID_V

	def get_id_p(self):
		return self.__ID_P

def formspisok1():
	driver1 = Driver(1, "Vodila", 1)
	driver2 = Driver(2, "TaxiDriv", 1)
	driver3 = Driver(3, "Sta", 1)
	spisok = [driver1, driver2, driver3]
	return spisok

def formspisok2():
	driver4 = Driver(4, "IvanovPetr", 2)
	driver5 = Driver(5, "PetrovIvan", 2)
	driver6 = Driver(6, "Kachul", 2)
	driver33 = Driver(12, "Lebed", 2)
	spisok = [driver4, driver5, driver6, driver33]
	return spisok

def formspisok3():
	driver7 = Driver(7, "Gagarin", 3)
	driver8 = Driver(8, "Lebedev", 3)
	driver9 = Driver(9, "Trubitcyn", 3)
	driver10 = Driver(10, "Postykov", 3)
	driver11 = Driver(11, "Aewn", 3)
	spisok = [driver7, driver8, driver9, driver10, driver11]
	return spisok

def form_main_spisok():
	avtopark1 = AvtoPark(1, "AvtoparkNomer1", formspisok1())
	avtopark2 = AvtoPark(2, "AvtoparkNomer2", formspisok2())
	avtopark3 = AvtoPark(3, "AvtoparkNomer3", formspisok3())
	spisok = [avtopark1, avtopark3, avtopark2]
	return spisok
