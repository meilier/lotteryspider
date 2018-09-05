#!/usr/bin/python3
import cx_Oracle
import os
import time
from table import JX201Table, B402Table, A205Table, Q102StoreTable, Q102SrTable, Q102CenterTable, Q102CclientTable, AllotDataTable

class LotteryDatabase:

	__conn = 0

	__cursor = 0

	#Table list stroing tables add to this class
	__table_list =[]

	#init object
	def init(self):
		self.__conn = cx_Oracle.connect('sports_lottery_data/demo123@172.19.112.11/orcl')
		self.__cursor = self.__conn.cursor()

	#add table to database class
	def add_table(self, table):
		self.__table_list.append(table)

	#insert data to oracle database
	def insert_data(self):
		self.init()
		print("init success,sleep 3s and start to insert data")
		time.sleep(3)
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
			print("commit success")
		self.close()
		print("close success,sleep 3s and exit")
		
 
	# release object 
	def close(self):
		self.__conn.close()
		print("close success")

if __name__ == "__main__":
	ld = LotteryDatabase()
	#jxt = JX201Table()
	#bt = B402Table()
	#at = A205Table()
	#qtst = Q102StoreTable()
	#qtsr = Q102SrTable()
	#qtce = Q102CenterTable()
	#qtcc = Q102CclientTable()
	adt = AllotDataTable()

	#ld.add_table(jxt)
	#ld.add_table(bt)
	#ld.add_table(at)
	#ld.add_table(qtst)
	#ld.add_table(qtsr)
	#ld.add_table(qtce)
	#ld.add_table(qtcc)
	ld.add_table(adt)
	ld.insert_data()
