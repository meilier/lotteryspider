#!/usr/bin/python
import csv
import os
import re
import platform

"""
this python scprit include some utils function when 
transporting the .csv files to the oracle database
"""

os.environ['NLS_LANG']='AMERICAN_AMERICA.ZHS16GBK'
wd = os.getcwd()

# get title column and data from JX201.csv
def get_JX201data():
	with open(wd+'\\JX201.csv') as f:
		reader = csv.reader(f)
		contents = [i for i in reader]
	#title = contents[4]
	date = contents[2][1][:10]
	data = contents[5:]
	for i ,item in enumerate(data):
		for j, item2 in enumerate(item):
			if(j <=3):
				continue
			if(re.match('.*,.*',data[i][j],flags=0)):
				data[i][j]=data[i][j].replace(',','')
	data_and_date = [i+[date] for i in data]
	return data_and_date

# get title column and data from B402.csv
def get_B402data():
	with open(wd+'\\B402.csv') as f:
		reader = csv.reader(f)
		contents = [i for i in reader]
	#title = contents[7]
	date = contents[4][2][:10]
	data = contents[-18:-1]
	#append date to data we got 
	data_and_date = [i+[date] for i in data]
	return data_and_date

# get data from A205.csv 
def get_A205data():
	with open(wd+'\\A205.csv') as f:
		reader = csv.reader(f);
		contents = [i for i in reader]
	#waiting for completed

# add data column to data

# this function compare the total actived money and confirmed money between JX201 and B402
def comprare_total_money():
	with open(wd+'\\JX201.csv') as f:
		reader = csv.reader(f)
		contents = [i for i in reader]
	data = contents[5:]
	JX201_total_active_money = sum([row[5] for row in data])
	JX201_total_confirm_money = sum([row[7] for row in data])
	with open(wd+'\\B402.csv') as f:
		reader = csv.reader(f)
		contents = [i for i in reader]
	B402_total_active_money = contents[-1][4]
	B402_total_confirm_money = contents[-1][7]
	if((JX201_total_active_money == B402_total_active_money) and (JX201_total_confirm_money == B402_total_confirm_money)):
		return True;
	else:
		return False;

#change files name  in directory
def change_files_name(filedir):
	if(((platform == 'Windows') and (filedir[-1] != '\\'))):
		filedir = filedir + '\\'
	else:
		filedir = filedir + '/'
	for files in os.listdir(filedir):
		if re.match('A205', files , flags=0):
			A205_name = re.match('A205.*', files , flags=0).group()
		if re.match('B402', files , flags=0):
			B402_name = re.match('B402.*', files , flags=0).group()
		if re.match('JX201', files , flags=0):
			JX201_name = re.match('JX201.*', files, flags=0).group()
	os.rename(filedir+A205_name,'A205.csv')
	os.rename(filedir+B402_name,'B402.csv')
	os.rename(filedir+JX201_name,'JX201.csv')
	
	
	
	



