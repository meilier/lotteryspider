from lottery_database import LotteryDatabase
from table import JX201Table, B402Table, A205Table, Q102Table, AllotDataTable
import lottery_util
import time, datetime

ld = LotteryDatabase()
jxt = JX201Table()
bt = B402Table()
at = A205Table()
qt = Q102Table()
adt = AllotDataTable()

ld.add_table(jxt)
ld.add_table(bt)
ld.add_table(at)
ld.add_table(qt)
ld.add_table(adt)

#call sipder


def get_yesterday():
	"""
	得到前一天的信息
	"""
	today=datetime.date.today() 
	oneday=datetime.timedelta(days=1) 
	yesterday=today-oneday  
	return yesterday.strftime('%Y-%m-%d')

def start_dbwriter(control_date):
	"""
	开始写入今天的数据
	"""
	if(not lottery_util.check_csv_files()):#call spider again, say another words ,set control.cfg none
		with open("control.cfg","w") as f:
			f.write('')
		print('reset successfully')
		time.sleep(300)
	else:
		#core logic
		print('check success')
		lottery_util.change_files_name() 
		print('rename success')
		#there we have some conditions when we insert data to database because data my not ready for)
		#if(lottery_util.compare_total_money() and lottery_util.compare_total_claim_money()):
		if(lottery_util.compare_total_money()):
			print('prepare to insert data')
			ld.insert_data()
			lottery_util.delete_csv_files()
			with open("flag.cfg","w") as f:
				f.write(control_date)
		else:
			#call this py in crontab next hour
			#delete csv files
			print("two check failed exit(0)")
			exit(0)
			lottery_util.delete_csv_files()
			with open("control.cfg","w") as f:
				f.write('')
			print('reset successfully')
			time.sleep(300)

#check csv files exist in dir or not
while True:
	#检查数据是否发布
	with open("control.cfg","r") as f:
		current_control_date = f.readline()
	with open("flag.cfg", "r") as fl:
		flag_date = fl.readline()
	
	if not flag_date == current_control_date:
		start_dbwriter(current_control_date)

	else:
		time.sleep(300)	


