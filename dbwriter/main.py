from lottery_databaes import LotteryDatabase
from table import JX201Table, B402Table, A205Table, Q102Table, AllotDataTable
import lottery_util

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

#call sipder



#check csv files exist in dir or not
while(not lottery_util.check_csv_files()):
	#call spider again

print('check success')

lottery_util.change_files_name() 
print('rename success')

#there we have some conditions when we insert data to database because data my not ready for)
if(lottery_util.compare_total_money() and lottery_util.compare_total_claim_money()):
	print('prepare to insert data')
	ld.insert_data()
	lottery_util.delete_csv_files()
else:
	#call this py in crontab next hour
	#delete csv files
	lottery_util.delete_csv_files()