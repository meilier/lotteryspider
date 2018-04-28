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
wdcsv = wd+'\\csv\\'



# replace commma (',') in number column with nothing ('')
def delete_comma(commadata):
	for i ,item in enumerate(commadata):
		for j, item2 in enumerate(item):
			if(j <=3):
				continue
			if(re.match('.*,.*',commadata[i][j],flags=0)):
				commadata[i][j]=commadata[i][j].replace(',','')
	return commadata




# this function compare the total actived money and confirmed money between JX201 and B402
def comprare_total_money():
	with open(wdcsv+'JX201.csv') as f:
		reader = csv.reader(f)
		contents = [i for i in reader]
	data = contents[5:]
	JX201_total_active_money = sum([row[5] for row in data])
	JX201_total_confirm_money = sum([row[7] for row in data])
	with open(wdcsv+'B402.csv') as f:
		reader = csv.reader(f)
		contents = [i for i in reader]
	B402_total_active_money = contents[-1][4]
	B402_total_confirm_money = contents[-1][7]
	if((JX201_total_active_money == B402_total_active_money) and (JX201_total_confirm_money == B402_total_confirm_money)):
		return True;
	else:
		return False;

#this function compare total claim prize money between JX201 add Q102 and B402 
def compare_total_claim_money():
	with open(wdcsv+'JX201.csv') as f:
		reader = csv.reader(f)
		contents = [i for i in reader]
	data = contents[5:]
	JX201_total_claim_money = sum([row[9] for row in data])
	with open(wdcsv+'Q102.csv') as f:
		reader = csv.reader(f)
		contents = [i for i in reader]
	data = contents[4:]
	Q102_total_claim_money = sum([row[17] for row in data])
	with open(wdcsv+'B402.csv') as f:
		reader = csv.reader(f)
		contents = [i for i in reader]
	B402_total_confirm_money = contents[-1][10]
	if(JX201_total_claim_money + Q102_total_claim_money == B402_total_confirm_money):
		return True;
	else:
		return False;
	


#change files name  in directory
def change_files_name():
	#if(((platform == 'Windows') and (filedir[-1] != '\\'))):
	#	filedir = filedir + '\\'
	#elif(((platform == 'Linux' and (filedir[-1] != '\\'))):
	#	filedir = filedir + '/'
	for files in os.listdir(wdcsv):
		if re.match('A205', files , flags=0):
			A205_name = re.match('A205.*', files , flags=0).group()
		if re.match('B402', files , flags=0):
			B402_name = re.match('B402.*', files , flags=0).group()
		if re.match('JX201', files , flags=0):
			JX201_name = re.match('JX201.*', files, flags=0).group()
		if re.match('Q102', files , flags=0):
			Q102_name = re.match('Q102.*', files, flags=0).group()
	os.rename(wdcsv+A205_name,'A205.csv')
	os.rename(wdcsv+B402_name,'B402.csv')
	os.rename(wdcsv+JX201_name,'JX201.csv')
	os.rename(wdcsv+Q102_name,'Q102.csv')

# check csv files if completely or not
def check_csv_files():
	#if(((platform == 'Windows') and (filedir[-1] != '\\'))):
	#	filedir = filedir + '\\'
	#elif(((platform == 'Linux' and (filedir[-1] != '\\'))):
	#	filedir = filedir + '/'
	#A205_count = B402_count = JX201_count = Q102_cout = ALLOTDATA_count = 0
	for files in os.listdir(wdcsv):
		if re.match('ALLOTDATA', files , flags=0):
			ALLOTDATA_name = re.match('ALLOT.*', files, flags=0).group()
			ALLOTDATA_count = ALLOTDATA_count + 1
		if re.match('A205', files , flags=0):
			A205_name = re.match('A205.*', files , flags=0).group()
			A205_count = A205_count + 1
		if re.match('B402', files , flags=0):
			B402_name = re.match('B402.*', files , flags=0).group()
			B402_count = B402_count + 1
		if re.match('JX201', files , flags=0):
			JX201_name = re.match('JX201.*', files, flags=0).group()
			JX201_count = JX201_count + 1
		if re.match('Q102', files , flags=0):
			JX201_name = re.match('Q102.*', files, flags=0).group()
			Q102_count = Q102_count + 1
	if (A205_count == 1 and  B402_count == 1 and JX201_count == 1 and Q102_cout == 1 and ALLOTDATA_count == 1):
		return True
	else:
		return False
	
def delete_csv_files():
	for filename in os.listdir(wdcsv):
		filepath = wdcsv+filename
		os.remove(filepath)
	



