#!/usr/bin/python3
import cx_Oracle
import lottery_util
import os

class LotteryDatabase:

	__conn = 0
	__cursor = 0
	JX201SQL = "INSERT INTO T_PHONE_LOTTERY_TICKET_ALL (SITE_CODE, SITE_NAME, SPORTS_LOTTERY_CODE, SPORTS_LOTTERY_NAME, ACTIVE_NUMBER, ACTIVE_MONEY, SURE_NUMBER, SURE_MONEY, DUIJIANG_NUMBER, DUIJIANG_MONEY, MANAGE_DATE) VALUES "
	JX201GETMAXIDSQL = 'SELECT ID FROM T_PHONE_LOTTERY_TICKET_ALL WHERE ID=(SELECT MAX(ID) FROM T_PHONE_LOTTERY_TICKET_ALL)'
	B402SQL = "INSERT INTO SALES_ALL (CITY_CODE, CITY_NAME, CONFIRM_PACKAGE, CONFIRM_MONEY , CONFIRM_PROPORTION , ACTIVE_PACKAGE, ACTIVE_MONEY , ACTIVE_PROPORTION , DUIJIANG_NUMBER , DUIJIANG_MONEY , DUIJIANG_PROPORTION, MANAGE_DATE) VALUES "
	A205SQL = "INSERT INTO INVENTORY_INFO_ALL (FACE_VALUE, GAME_CODE, GAME_NAME, II_JIANGZU, II_CASE, II_PACKAGE, II_MONEY, INBOUND_JIANGZU, INBOUND_CASE, INBOUND_PACKAGE, INBOUND_MONEY, OUTBOUND_JIANGZU, OUTBOUND_CASE, OUTBOUND_PACKAGE, OUTBOUND_MONEY, EI_JIANGZU, EI_CASE, EI_PACKAGE, EI_MONEY, MANAGE_DATE) VALUES "
	Q102SQL = "INSERT INTO CLAIM_PRIZE_INFO_ALL (PROVINCE_CODE, PROVINCE_NAME, CITY_CODE, CITY_NAME, COUNTRY_CODE, COUNTRY_NAME, ORGANIZATION_TYPE, ORGANIZATION_CODE, ORGANIZATION_NAME, CLAIM_DATE, GAME_CODE, GAME_NAME, TERMINAL_CODE, FACE_VALUE, PACKAGE_NUMBER, TICKET_NUMBER, PRIZE_CLASS, PRIZE_MONEY, STORE_CODE, ACTIVE_TIME, PACKAGE_STATE) VALUES "
	ALLOT_DATASQL = "INSERT INTO ALLOT_DATA_ALL (ALLOT_NUMBER, OUTBOUND_WAREHOUSE, INBOUND_WAREHOUSE, GAME_CODE, GAME_NAME, GAME_FACE_VALUE, ALLOT_CASE_NUMBER, ALLOT_SCATTERED_PACKAGE, ALLOT_TOTAL_PACKAGE, ALLOT_TOTAL_MONEY) VALUES "
	def __init__(self):
		self.__conn = cx_Oracle.connect('sports_lottery_data/demo123@172.19.112.11/orcl')
		self.__cursor = self.__conn.cursor()
		os.environ['NLS_LANG']='AMERICAN_AMERICA.ZHS16GBK'


	# get database connection
	def get_connection(self):
		return self.__conn

	# get connection cursor
	def get_cursor(self):
		return self.__conn.cursor()

	# insert data to database	
	def insert_data(self, filename):
		if(filename == 'JX201'):
			data = lottery_util.get_JX201data()
			sql = self.JX201SQL
		elif(filename == 'B402'):
			data = lottery_util.get_B402data()
			sql = self.B402SQL
		elif(filename == 'A205'):
			data = lottery_util.get_A205data()
			sql = self.A205SQL
		elif(filename == 'Q102'):
			data = lottery_util.get_Q102data()
			sql = self.Q102SQL
		elif(filename == 'ALLOT_DATASQL'):
			data = lottery
		#current_id = int(self.get_max_id())
		for da in data :
			#current_id = current_id +1
			print(da)
			#sqldata = sql+str(tuple(([str(current_id)]+da)))
			sqldata = sql+str(tuple(da))
			print(sqldata)
			self.__cursor.execute(sqldata)
		self.__conn.commit();
	
	def __del__(self):
		self.__conn.close()
	# used for insert id increase but now when use default sys_guid() its useless
	def get_max_id(self):
		rs = self.__cursor.execute(self.JX201GETMAXIDSQL).fetchall()
		if(rs == []):
			maxid = 0
		else:
			maxid=rs[0][0]
		return maxid
