from lottery_database import LotteryDatabase
from table import JX201Table, B402Table, A205Table, Q102StoreTable, Q102SrTable, Q102CenterTable, Q102CclientTable, AllotDataTable
import lottery_util
import time, datetime,os

ld = LotteryDatabase()
jxt = JX201Table()
bt = B402Table()
at = A205Table()
qtst = Q102StoreTable()
qtsr = Q102SrTable()
qtce = Q102CenterTable()
qtcc = Q102CclientTable()
adt = AllotDataTable()

ld.add_table(jxt)
ld.add_table(bt)
ld.add_table(at)
ld.add_table(qtst)
ld.add_table(qtsr)
ld.add_table(qtce)
ld.add_table(qtcc)
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
	if(lottery_util.compare_total_money()):
		print('prepare to insert data')
		ld.insert_data()
		# lottery_util.delete_csv_files()

		current_path = os.getcwd()
		parent_path = os.path.dirname(current_path)
		# control_file_path = os.path.join(parent_path, "control.cfg")
		flag_file_path = os.path.join(parent_path, "flag.cfg")
		with open(flag_file_path,"w") as f:
			f.write(control_date)
	else:
		#call this py in crontab next hour
		#delete csv files
		print("two check failed exit(0)")
		#exit(0)
		# lottery_util.delete_csv_files()

		current_path = os.getcwd()
		parent_path = os.path.dirname(current_path)
		control_file_path = os.path.join(parent_path, "control.cfg")
		# flag_file_path = os.path.join(parent_path, "flag.cfg")

		with open(control_file_path,"w") as f:
			f.write('')
		print('reset successfully')
		time.sleep(600)

#check csv files exist in dir or not
while True:
	#检查数据是否发布


	current_path = os.getcwd()
	parent_path = os.path.dirname(current_path)
	control_file_path = os.path.join(parent_path, "control.cfg")
	flag_file_path = os.path.join(parent_path, "flag.cfg")

	with open(control_file_path,"r") as f:
		current_control_date = f.readline()
	with open(flag_file_path, "r") as fl:
		flag_date = fl.readline()
	
	the_yesterday = get_yesterday()

	print("Controle date : " + str(current_control_date))
	print("The yesterday is :" + str(the_yesterday))
	
	if (not flag_date == current_control_date) and (current_control_date ==  the_yesterday):
		start_dbwriter(current_control_date)
		
	else:
		print("sleep 10 miniutes")
		time.sleep(600)	


