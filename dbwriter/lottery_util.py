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

#this function compare total claim prize money between JX201 add Q102 and B402 
def compare_total_claim_money():
	with open(wd+'\\JX201.csv') as f:
		reader = csv.reader(f)
		contents = [i for i in reader]
	data = contents[5:]
	JX201_total_claim_money = sum([row[9] for row in data])
	with open(wd+'\\Q102.csv') as f:
		reader = csv.reader(f)
		contents = [i for i in reader]
	data = contents[4:]
	Q102_total_claim_money = sum([row[17] for row in data])
	with open(wd+'\\B402.csv') as f:
		reader = csv.reader(f)
		contents = [i for i in reader]
	B402_total_confirm_money = contents[-1][10]
	if(JX201_total_claim_money + Q102_total_claim_money == B402_total_confirm_money):
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
	
	
	
	



