import sqlite3 as baza
import start as lab4

def start_db():
	try:
		print("Database opened")
		soedinenie = baza.connect("test.db")
		curs = soedinenie.cursor()
	except baza.DatabaseError:
		print("Error")
	return soedinenie, curs

def close_db(soedinenie, curs):
	try:
		print("Database closed")
		soedinenie.close
		curs.close
	except baza.DatabaseError:
		print("Error")

def make_t_db1(curs):
	curs.execute("""create table if not exists Drivers(id_v integer, surname_v text, id_p integer)""")

def make_t_db2(curs):
	curs.execute("""create table if not exists Avtopark (id_p integer, name_p text, spis_sotr text)""")

def dob_t_db1(curs, soed, main_lst):
	for el in main_lst:
		lst_sot = el.get_sot_list()
		for sot in lst_sot:
			name = sot.get_sur()
			id = sot.get_id_s()
			id_p = sot.get_id_o()
			curs.execute( "INSERT INTO Drivers VALUES ('%d','%s', '%d')" % (id, name, id_p))
			soed.commit()

def dob_t_db2(curs, soed, main_lst):
	for el in main_lst:
		name = el.get_name()
		id = el.get_id_0()
		lst_sot = el.get_sot_list()
		lst_sot_name = ""
		for sot in lst_sot:
			lst_sot_name += sot.get_sur() + ', '
		curs.execute( "INSERT INTO Avtopark VALUES ('%d','%s', '%s')" % (id, name, lst_sot_name))
		soed.commit()

def db_print(kurs, soed):
	try:
		print("-" * 100)
		kurs.execute('''SELECT * FROM Avtopark''')
		res = kurs.fetchall()
		for i in range(len(res)):
			print("Taxi ID - %d, Taxi name - %s, Taxi Drivers %s" %(res[i][0], res[i][1], res[i][2]))
		print('Number of changes - %d' % soed.total_changes)
	except baza.DatabaseError:
		print("Error")
	print("-" * 100)
	try:
		kurs.execute('''SELECT * FROM Drivers''')
		res = kurs.fetchall()
		for i in range(len(res)):
			print("Driver ID - %d, Driver Name - %s, Taxi ID %d" %(res[i][0], res[i][1], res[i][2]))
		print('Number of changes - %d' % soed.total_changes)
		print("-" * 100)
	except baza.DatabaseError:
		print("Error")

def del_table(kurs, soed):
	kurs.execute('DROP table if exists Drivers')
	soed.commit()
	kurs.execute('DROP table if exists Avtopark')
	soed.commit()

def main():
	main_lst = lab4.form_main_spisok()
	soed, kurs = start_db()
	make_t_db1(kurs)
	make_t_db2(kurs)
	dob_t_db1(kurs, soed, main_lst)
	dob_t_db2(kurs, soed, main_lst)
	db_print(kurs, soed)
	del_table(kurs, soed)
	close_db(soed, kurs)

main()
