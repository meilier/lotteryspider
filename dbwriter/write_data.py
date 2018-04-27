#!/usr/bin/python3
import cx_Oracle
import lottery_util
import os

os.environ['NLS_LANG']='AMERICAN_AMERICA.ZHS16GBK'


JX201SQL = "INSERT INTO T_PHONE_LOTTERY_TICKET_ALL (ID, SITE_CODE, SITE_NAME, SPORTS_LOTTERY_CODE, SPORTS_LOTTERY_NAME, ACTIVE_NUMBER, ACTIVE_MONEY, SURE_NUMBER, SURE_MONEY, DUJIANG_NUMBER, DUIJIANG_MONEY, MANEGE_DATE) VALUES "
B402SQL = "INSERT INTO TABLE () VALUES"

#connect to the database	
conn = cx_Oracle.connect('sports_lottery_data/demo123@172.19.112.11/orcl')

cursor = conn.sursor()

# filename
def insert_data(filename, sql):
	if(filename = 'JX201'):
		data = lottery_util.get_JX201data()
	elif(filename = 'B402')
		date = lottery_util.get_B402data()

	for da in data
		sqldata = sql+str(da)
		cursor.execute(sql)
	conn.commit();
	
		




