#!/usr/bin/python3
import csv
import re
import datetime
from abc import ABC, abstractmethod
from lottery_util import wdcsv

def get_yesterday():
	"""
	得到前一天的信息
	"""
	today=datetime.date.today() 
	oneday=datetime.timedelta(days=1) 
	yesterday=today-oneday  
	return yesterday.strftime('%Y-%m-%d')

class Table(ABC):
	@property
	@abstractmethod
	def filename(self):
		pass

	@property
	@abstractmethod
	def insert_sql(self):
		pass

	@abstractmethod
	def get_data(self):
		pass

class JX201Table(Table):
	@property
	def filename(self):
		return 'JX201.csv'

	@property
	def insert_sql(self):
		return "INSERT INTO JS_T_PHONE_LOTTERY_TICKET_ALL (SITE_CODE, SITE_NAME, SPORTS_LOTTERY_CODE, SPORTS_LOTTERY_NAME, ACTIVE_NUMBER, ACTIVE_MONEY, SURE_NUMBER, SURE_MONEY, DUIJIANG_NUMBER, DUIJIANG_MONEY, MANAGE_DATE) VALUES "

	# get title column and data from JX201.csv
	def get_data(self):
		with open(wdcsv+self.filename) as f:
			reader = csv.reader(f)
			contents = [i for i in reader]
		#title = contents[4]
		date = contents[2][1][:10]
		#15 item for test
		data = contents[5:]
		for i ,item in enumerate(data):
			for j, item2 in enumerate(item):
				if(j <=3):
					continue
				if(re.match('.*,.*',data[i][j],flags=0)):
					data[i][j]=data[i][j].replace(',','')
		data_and_date = [i+[date] for i in data]
		return data_and_date

class B402Table(Table):
	@property
	def filename(self):
		return 'B402.csv'
	@property
	def insert_sql(self):
		return "INSERT INTO JS_T_LOTTERY_TICKET_DUIJIANG (CITY_CODE, CITY_NAME, CONFIRM_PACKAGE, CONFIRM_MONEY , CONFIRM_PROPORTION , ACTIVE_PACKAGE, ACTIVE_MONEY , ACTIVE_PROPORTION , DUIJIANG_NUMBER , DUIJIANG_MONEY , DUIJIANG_PROPORTION, MANAGE_DATE) VALUES "

	def get_data(self):
		with open(wdcsv+self.filename) as f:
			reader = csv.reader(f)
			contents = [i[1:] for i in reader]
		#title = contents[7]
		date = contents[4][1][:10]
		data = contents[8:-2]
		for i ,item in enumerate(data):
			for j, item2 in enumerate(item):
				if(j ==0 or j==1 or j==4 or j==7 or j== 10):
					continue
				if(re.match('.*,.*',data[i][j],flags=0)):
					data[i][j]=data[i][j].replace(',','')
		#append date to data we got 
		data_and_date = [i+[date] for i in data]
		return data_and_date

class A205Table(Table):
	@property
	def filename(self):
		return 'A205.csv'
	@property
	def insert_sql(self):
		return "INSERT INTO JS_T_PROVINCE_STOCK (FACE_VALUE, GAME_CODE, GAME_NAME, II_JIANGZU, II_CASE, II_PACKAGE, II_MONEY, INBOUND_JIANGZU, INBOUND_CASE, INBOUND_PACKAGE, INBOUND_MONEY, OUTBOUND_JIANGZU, OUTBOUND_CASE, OUTBOUND_PACKAGE, OUTBOUND_MONEY, EI_JIANGZU, EI_CASE, EI_PACKAGE, EI_MONEY, MANAGE_DATE) VALUES "
	
	def get_data(self):
		with open(wdcsv+self.filename) as f:
			reader = csv.reader(f)
			contents = [i for i in reader]
		date = contents[3][2][:10]
		tmpdata = contents[7:]
		data = []
		for i in tmpdata:
			if(i[0].isdigit()):
				data = data+[i]
		for i ,item in enumerate(data):
			for j, item2 in enumerate(item):
				if(j ==0 or j==1 or j==2):
					continue
				if(re.match('.*,.*',data[i][j],flags=0)):
					data[i][j]=data[i][j].replace(',','')
		data_and_date = [i+[date] for i in data]
		return data_and_date

class Q102StoreTable(Table):
	@property
	def filename(self):
		return 'Q102_STORE.csv'
	@property
	def insert_sql(self):
		return "INSERT INTO JS_T_SITE_DUIJIANG (PROVINCE_CODE, PROVINCE_NAME, CITY_CODE, CITY_NAME, COUNTRY_CODE, COUNTRY_NAME, ORGANIZATION_TYPE, ORGANIZATION_CODE, ORGANIZATION_NAME, CLAIM_DATE, GAME_CODE, GAME_NAME, TERMINAL_CODE, FACE_VALUE, PACKAGE_NUMBER, TICKET_NUMBER, PRIZE_CLASS, PRIZE_MONEY, STORE_CODE, ACTIVE_TIME, PACKAGE_STATE, MANAGE_DATE) VALUES "
	
	def get_data(self):
		with open(wdcsv+self.filename) as f:
			reader = csv.reader(f)
			contents =[i for i in reader]
		date = contents[2][0][5:15]
		data = contents[4:]
		data_and_date = [i+[date] for i in data]
		return data_and_date

class Q102SrTable(Table):
	@property
	def filename(self):
		return 'Q102_SR.csv'
	@property
	def insert_sql(self):
		return "INSERT INTO JS_T_SR_DUIJIANG (PROVINCE_CODE, PROVINCE_NAME, CITY_CODE, CITY_NAME, COUNTRY_CODE, COUNTRY_NAME, ORGANIZATION_TYPE, ORGANIZATION_CODE, ORGANIZATION_NAME, CLAIM_DATE, GAME_CODE, GAME_NAME, TERMINAL_CODE, FACE_VALUE, PACKAGE_NUMBER, TICKET_NUMBER, PRIZE_CLASS, PRIZE_MONEY, STORE_CODE, ACTIVE_TIME, PACKAGE_STATE, MANAGE_DATE) VALUES "
	
	def get_data(self):
		with open(wdcsv+self.filename) as f:
			reader = csv.reader(f)
			contents =[i for i in reader]
		date = contents[2][0][5:15]
		data = contents[4:]
		data_and_date = [i+[date] for i in data]
		return data_and_date

class Q102CenterTable(Table):
	@property
	def filename(self):
		return 'Q102_CENTER.csv'
	@property
	def insert_sql(self):
		return "INSERT INTO JS_T_CENTER_DUIJIANG (PROVINCE_CODE, PROVINCE_NAME, CITY_CODE, CITY_NAME, COUNTRY_CODE, COUNTRY_NAME, ORGANIZATION_TYPE, ORGANIZATION_CODE, ORGANIZATION_NAME, CLAIM_DATE, GAME_CODE, GAME_NAME, TERMINAL_CODE, FACE_VALUE, PACKAGE_NUMBER, TICKET_NUMBER, PRIZE_CLASS, PRIZE_MONEY, STORE_CODE, ACTIVE_TIME, PACKAGE_STATE, MANAGE_DATE) VALUES "
	
	def get_data(self):
		with open(wdcsv+self.filename) as f:
			reader = csv.reader(f)
			contents =[i for i in reader]
		data = contents[4:]
		if data[0][0] == "":
			return None
		date = contents[2][0][5:15]
		data_and_date = [i+[date] for i in data]
		return data_and_date

class Q102CclientTable(Table):
	@property
	def filename(self):
		return 'Q102_CCLIENT.csv'
	@property
	def insert_sql(self):
		return "INSERT INTO JS_T_CCLIENT_DUIJIANG (PROVINCE_CODE, PROVINCE_NAME, CITY_CODE, CITY_NAME, COUNTRY_CODE, COUNTRY_NAME, ORGANIZATION_TYPE, ORGANIZATION_CODE, ORGANIZATION_NAME, CLAIM_DATE, GAME_CODE, GAME_NAME, TERMINAL_CODE, FACE_VALUE, PACKAGE_NUMBER, TICKET_NUMBER, PRIZE_CLASS, PRIZE_MONEY, STORE_CODE, ACTIVE_TIME, PACKAGE_STATE, MANAGE_DATE) VALUES "
	
	def get_data(self):
		with open(wdcsv+self.filename) as f:
			reader = csv.reader(f)
			contents =[i for i in reader]
		data = contents[4:]
		if data[0][0] == "":
			return None
		date = contents[2][0][5:15]
		data_and_date = [i+[date] for i in data]
		return data_and_date



class AllotDataTable(Table):
	@property
	def filename(self):
		return 'ALLOTDATA.csv'
	@property
	def insert_sql(self):
		return "INSERT INTO JS_T_BIG_CITY_ALLOT (ALLOT_NUMBER, OUTBOUND_WAREHOUSE, INBOUND_WAREHOUSE, GAME_CODE, GAME_NAME, ALLOT_CASE_NUMBER, ALLOT_SCATTERED_PACKAGE, ALLOT_TOTAL_PACKAGE, GAME_FACE_VALUE, ALLOT_TOTAL_MONEY, MANAGE_DATE) VALUES "
	
	def get_data(self):
		print('hello')
		with open(wdcsv+self.filename) as f:
			reader = csv.reader(f)
			contents =[i for i in reader]
		data = contents
		if data == []:
			return None
		today=datetime.date.today()
		data_and_date = data
		return data_and_date

        
        
class BigCustomerTable():
	@property
	def filename(self):
		return 'BIGCUSTOMER.csv'
	@property
	def insert_sql(self):
		return "INSERT INTO JS_T_BIGCUSTOMER (CODE, NAME, SEND_PATTERN, TYPE, REGION_CODE, REGION_NAME, LINKMAN, PHONE, ADDRESS, EMS_CODE, STATES, MANAGE_DATE) VALUES "
	
	def get_data(self):
		print('getting BigCustomerTable Data')
		with open(wdcsv+self.filename) as f:
			reader = csv.reader(f)
			contents =[i for i in reader]
			date = get_yesterday()
			data = contents
		for i ,item in enumerate(data):
        		city_code = re.search("(\d+)",str(data[i][4])).group()
        		city_name = re.search("([\u4e00-\u9fa5]{2,4})",str(data[i][4])).group()
        		data[i].pop(4)
        		data[i].insert(4,city_code)
        		data[i].insert(5,city_name)
        		print(str(data[i]))
        		for j,item2 in enumerate(item):
        			if(j<=3):
        				continue
        			if(re.match('.*,.*',data[i][j],flags=0)):
        				data[i][j]=data[i][j].replace(',','')
		data_and_date = [i+[date] for i in data]
		print(str(data_and_date))
		return data_and_date

        
        
class DaiBiaoXinXiTable():
	@property
	def filename(self):
		return 'DaiBiaoXinXi.csv'

	@property
	def insert_sql(self):
		return "INSERT INTO JS_T_DAIBIAOXINXI (code, name, fullname, pro_name, city_name, county_name, city_division, county_division, relationship, sr_states, person_name, person_id, address, ems_code, phone, send_pattern, out_min_money, transfer_min_money, auto_collection, channel_1, channel_2, channel_3, distribution_1, distribution_2, distribution_3, order_warehouse, refund_ticket_permit, submit_order_permit, order_automatic_permit, sale_commission_proportion, sale_commission_modul, sale_commission_pay, duijiang_commission_proportion, duijiang_commission_modul, duijiang_commission_way, duijiang_commission_pay, manage_commission_proportion, manage_commission_modul, manage_commission_way, manage_commission_pay, duijiang_max_money, duijiang_min_money, duijiang_pay_sure_money, cycle, duijiang_times, clock_time, transfer_out_permit, transfer_in_permit, receive_person, receive_address, receive_phone, manage_date) VALUES "

	# get title column and data from JX201.csv
	def get_data(self):
		with open(wdcsv+self.filename,encoding = 'utf-8') as f:
			reader = csv.reader(f)
			contents = [i for i in reader]
		#title = contents[4]
		date = get_yesterday()
		#print(date)
		#15 item for test
		data = contents[3:]
		#print(data)
		for i ,item in enumerate(data):
			for j, item2 in enumerate(item):
				if(j <=3):
					continue
				if(re.match('.*,.*',data[i][j],flags=0)):
					data[i][j]=data[i][j].replace(',','')
		data_and_date = [i+[date] for i in data]
		print(str(data_and_date))
		return data_and_date
        
        
class MenDianXinXiTable():
	@property
	def filename(self):
		return 'MenDianXinXi.csv'

	@property
	def insert_sql(self):
		return "INSERT INTO JS_T_MENDIANXINXI (code, name, fullname, pro_name, city_name, county_name, city_division, county_division, business_type, site_states, person_name, person_id, address, phone, ems_code, out_min_money, transfer_min_money, relationship, site_level, channel_1, channel_2, channel_3, send_pattern, manage_sr, move_sr1, move_sr2, move_sr3, distribution_1, distribution_2, distribution_3, order_warehouse, refund_ticket_permit, submit_order_permit, sure_active_mony, manual_activation_permit, order_automatic_permit, sale_commission_proportion, sale_commission_modul, sale_commission_way, sale_commission_pay, duijiang_commission_proportion, duijiang_commission_modul, duijiang_commission_way, duijiang_commission_pay, duijiang_max_money, duijiang_min_money, duijiang_pay_sure_money, cycle, duijiang_times, clock_time, receive_person, receive_address, receive_phone, manage_date) VALUES "

	# get title column and data from JX201.csv
	def get_data(self):
		with open(wdcsv+self.filename,encoding = 'utf-8') as f:
			reader = csv.reader(f)
			contents = [i for i in reader]
		#title = contents[4]
		date = get_yesterday()
		#print(date)
		#15 item for test
		data = contents[3:]
		#print(data)
		for i ,item in enumerate(data):
			for j, item2 in enumerate(item):
				if(j <=3):
					continue
				if(re.match('.*,.*',data[i][j],flags=0)):
					data[i][j]=data[i][j].replace(',','')
		data_and_date = [i+[date] for i in data]
		print(str(data_and_date))
		return data_and_date