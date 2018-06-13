#!/usr/bin/python3
import csv
import re
import datetime
from abc import ABC, abstractmethod
from lottery_util import wdcsv


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
		return "INSERT INTO T_PHONE_LOTTERY_TICKET_ALL (SITE_CODE, SITE_NAME, SPORTS_LOTTERY_CODE, SPORTS_LOTTERY_NAME, ACTIVE_NUMBER, ACTIVE_MONEY, SURE_NUMBER, SURE_MONEY, DUIJIANG_NUMBER, DUIJIANG_MONEY, MANAGE_DATE) VALUES "

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
		return "INSERT INTO SALES_ALL (CITY_CODE, CITY_NAME, CONFIRM_PACKAGE, CONFIRM_MONEY , CONFIRM_PROPORTION , ACTIVE_PACKAGE, ACTIVE_MONEY , ACTIVE_PROPORTION , DUIJIANG_NUMBER , DUIJIANG_MONEY , DUIJIANG_PROPORTION, MANAGE_DATE) VALUES "
	
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
		return "INSERT INTO INVENTORY_INFO_ALL (FACE_VALUE, GAME_CODE, GAME_NAME, II_JIANGZU, II_CASE, II_PACKAGE, II_MONEY, INBOUND_JIANGZU, INBOUND_CASE, INBOUND_PACKAGE, INBOUND_MONEY, OUTBOUND_JIANGZU, OUTBOUND_CASE, OUTBOUND_PACKAGE, OUTBOUND_MONEY, EI_JIANGZU, EI_CASE, EI_PACKAGE, EI_MONEY, MANAGE_DATE) VALUES "
	
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
		return "INSERT INTO CLAIM_PRIZE_INFO_STORE (PROVINCE_CODE, PROVINCE_NAME, CITY_CODE, CITY_NAME, COUNTRY_CODE, COUNTRY_NAME, ORGANIZATION_TYPE, ORGANIZATION_CODE, ORGANIZATION_NAME, CLAIM_DATE, GAME_CODE, GAME_NAME, TERMINAL_CODE, FACE_VALUE, PACKAGE_NUMBER, TICKET_NUMBER, PRIZE_CLASS, PRIZE_MONEY, STORE_CODE, ACTIVE_TIME, PACKAGE_STATE, MANAGE_DATE) VALUES "
	
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
		return "INSERT INTO CLAIM_PRIZE_INFO_SR (PROVINCE_CODE, PROVINCE_NAME, CITY_CODE, CITY_NAME, COUNTRY_CODE, COUNTRY_NAME, ORGANIZATION_TYPE, ORGANIZATION_CODE, ORGANIZATION_NAME, CLAIM_DATE, GAME_CODE, GAME_NAME, TERMINAL_CODE, FACE_VALUE, PACKAGE_NUMBER, TICKET_NUMBER, PRIZE_CLASS, PRIZE_MONEY, STORE_CODE, ACTIVE_TIME, PACKAGE_STATE, MANAGE_DATE) VALUES "
	
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
		return "INSERT INTO CLAIM_PRIZE_INFO_CENTER (PROVINCE_CODE, PROVINCE_NAME, CITY_CODE, CITY_NAME, COUNTRY_CODE, COUNTRY_NAME, ORGANIZATION_TYPE, ORGANIZATION_CODE, ORGANIZATION_NAME, CLAIM_DATE, GAME_CODE, GAME_NAME, TERMINAL_CODE, FACE_VALUE, PACKAGE_NUMBER, TICKET_NUMBER, PRIZE_CLASS, PRIZE_MONEY, STORE_CODE, ACTIVE_TIME, PACKAGE_STATE, MANAGE_DATE) VALUES "
	
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
		return "INSERT INTO CLAIM_PRIZE_INFO_CCLIENT (PROVINCE_CODE, PROVINCE_NAME, CITY_CODE, CITY_NAME, COUNTRY_CODE, COUNTRY_NAME, ORGANIZATION_TYPE, ORGANIZATION_CODE, ORGANIZATION_NAME, CLAIM_DATE, GAME_CODE, GAME_NAME, TERMINAL_CODE, FACE_VALUE, PACKAGE_NUMBER, TICKET_NUMBER, PRIZE_CLASS, PRIZE_MONEY, STORE_CODE, ACTIVE_TIME, PACKAGE_STATE, MANAGE_DATE) VALUES "
	
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
		return "INSERT INTO ALLOT_DATA (ALLOT_NUMBER, OUTBOUND_WAREHOUSE, INBOUND_WAREHOUSE, GAME_CODE, GAME_NAME, GAME_FACE_VALUE, ALLOT_CASE_NUMBER, ALLOT_SCATTERED_PACKAGE, ALLOT_TOTAL_PACKAGE, ALLOT_TOTAL_MONEY, MANAGE_DATE) VALUES "
	
	def get_data(self):
		print('hello')
		with open(wdcsv+self.filename) as f:
			reader = csv.reader(f)
			contents =[i for i in reader]
		data = contents
		if data[0][0] == "":
			return None
		today=datetime.date.today()
		date=today.strftime('%Y-%m-%d')
		data_and_date = [i+[date] for i in data]
		return data_and_date
