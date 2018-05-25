#!/usr/bin/python3
import cx_Oracle
import os

class LotteryDatabase:

	__conn = 0

	__cursor = 0

	#Table list stroing tables add to this class
	__table_list =[]

	def __init__(self):
		self.__conn = cx_Oracle.connect('sports_lottery_data/demo123@172.19.112.11/orcl')
		self.__cursor = self.__conn.cursor()

	#add table to database class
	def add_table(self, table):
		self.__table_list.append(table)

	#insert data to oracle database
	def insert_data(self):
		for table in self.__table_list:
			data = table.get_data()
			sql = table.insert_sql
			if data is None:
				continue
			for da in data:
				#print for testing
				print(da)
				sqldata = sql+str(tuple(da))
				print(sqldata)
				self.__cursor.execute(sqldata)
			self.__conn.commit()
 
	# release object 
	def __del__(self):
		self.__conn.close()
	
	# del data
	def def_JX201_data(self,table_name,date):
		"""
		传入表名以及日期参数,例如 "T_PHONE_LOTTERY_TICKET_ALL" "2018-05-23"
		"""
		sqldata = "DELETE FROM" + table_name + "WHERE MANAGE_DATE = " + date
		print(sqldata)
		self.__cursor.execute(sqldata)
		self.__cursor.commit()



		
