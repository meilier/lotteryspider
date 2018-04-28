from lottery_databaes import LotteryDatabase
from table import JX201Table, B402Table, A205Table, Q102Table, AllotDataTable

ld = LotteryDatabase()
jxt = JX201Table()
bt = B402Table()
at = A205Table()
qt = Q102Table()
adt = AllotDataTable()

ld.addTable(jxt)
ld.addTable(bt)
ld.addTable(at)
ld.addTable(qt)
ld.addTable(adt)


if(#there we have some conditions when we insert data to database because data my not ready for):
	ld.insert_data()

