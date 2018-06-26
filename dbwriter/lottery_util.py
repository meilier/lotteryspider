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
parent_path = os.path.dirname(wd)
# parent_2_path = os.path.dirname(parent_path)
wdcsv = parent_path +'\\csv\\'


# replace commma (',') in number column with nothing ('')
def delete_comma(commadata):
	for i ,item in enumerate(commadata):
		for j, item2 in enumerate(item):
			if(j <=3):
				continue
			if(re.match('.*,.*',commadata[i][j],flags=0)):
				commadata[i][j]=commadata[i][j].replace(',','')
	return commadata

# replace  ('.') in number column with nothing ('')
def delete_dot(commadata):
	for i ,item in enumerate(commadata):
		for j, item2 in enumerate(item):
			if(j <=3):
				continue
			if(re.match('.*,.*',commadata[i][j],flags=0)):
				commadata[i][j]=commadata[i][j].replace(',','')
	return commadata




# this function compare the total actived money and confirmed money between JX201 and B402
def compare_total_money():
	with open(wdcsv+'JX201.csv') as f:
		reader = csv.reader(f)
		contents = [i for i in reader]
	data = contents[5:]
	without_comma_data = delete_comma(data)
	JX201_total_active_money = sum([int(row[5]) for row in without_comma_data])
	print(JX201_total_active_money)
	JX201_total_confirm_money = sum([int(row[7]) for row in without_comma_data])
	print(JX201_total_confirm_money)
	with open(wdcsv+'B402.csv') as f:
		reader = csv.reader(f)
		contents = [i for i in reader]
	print(contents)
	B402_total_active_money = contents[-2][7]
	B402_total_active_money = B402_total_active_money.replace(',','')
	print(B402_total_active_money)
	B402_total_confirm_money = contents[-2][4]
	B402_total_confirm_money = B402_total_confirm_money.replace(',','')
	print(B402_total_confirm_money)
	if((JX201_total_active_money == int(B402_total_active_money)) and (JX201_total_confirm_money == int(B402_total_confirm_money))):
		print("compare successfully")
		return True
	else:
		print("compare failed")
		return False


#this function compare total claim prize money between JX201 add Q102 and B402 
def compare_total_claim_money():
	with open(wdcsv+'JX201.csv') as f:
		reader = csv.reader(f)
		contents = [i for i in reader]
	data = contents[5:]
	without_comma_data = delete_comma(data)
	JX201_total_claim_money = sum([int(row[9]) for row in without_comma_data])
	print(JX201_total_claim_money)
	with open(wdcsv+'Q102.csv') as f:
		reader = csv.reader(f)
		contents = [i for i in reader]
	data = contents[4:]
	without_comma_data = delete_comma(data)
	Q102_total_claim_money = sum([int(float(row[17])) for row in without_comma_data])
	print(Q102_total_claim_money)
	with open(wdcsv+'B402.csv') as f:
		reader = csv.reader(f)
		contents = [i for i in reader]
	B402_total_confirm_money = contents[-2][10]
	B402_total_confirm_money = B402_total_confirm_money.replace(',','')
	print(B402_total_confirm_money)
	exit(0)
	if(JX201_total_claim_money + Q102_total_claim_money == B402_total_confirm_money):
		return True
	else:
		return False
	


#change files name  in directory
def change_files_name():
	#if(((platform == 'Windows') and (filedir[-1] != '\\'))):
	#	filedir = filedir + '\\'
	#elif(((platform == 'Linux' and (filedir[-1] != '\\'))):
	#	filedir = filedir + '/'
	Q102_List = [] # for sort
	for root, dirs, filenames in os.walk(wdcsv):
		for files in filenames:
			if re.match('A205', files , flags=0):
				A205_name = re.match('A205.*', files , flags=0).group()
			if re.match('B402', files , flags=0):
				B402_name = re.match('B402.*', files , flags=0).group()
			if re.match('JX201', files , flags=0):
				JX201_name = re.match('JX201.*', files, flags=0).group()
			if re.match('Q102', files , flags=0):
				Q102_name = re.match('Q102.*', files, flags=0).group()
				Q102_List = Q102_List + [Q102_name]

	Q102_List.sort()
	print(Q102_List)
	
	A205_old_name = os.path.join(root,A205_name)
	A205_new_name = os.path.join(root,"A205.csv")
	os.rename(A205_old_name,A205_new_name)

	B402_old_name = os.path.join(root,B402_name)
	B402_new_name = os.path.join(root,"B402.csv")
	os.rename(B402_old_name,B402_new_name)

	JX201_old_name = os.path.join(root,JX201_name)
	JX201_new_name = os.path.join(root,"JX201.csv")
	os.rename(JX201_old_name,JX201_new_name)

	
	Q102_store_old_name = os.path.join(root,Q102_List[0])
	Q102_store_new_name = os.path.join(root,"Q102_STORE.csv")
	os.rename(Q102_store_old_name,Q102_store_new_name)

	Q102_sr_old_name = os.path.join(root,Q102_List[1])
	Q102_sr_new_name = os.path.join(root,"Q102_SR.csv")
	os.rename(Q102_sr_old_name,Q102_sr_new_name)

	Q102_center_old_name = os.path.join(root,Q102_List[2])
	Q102_center_new_name = os.path.join(root,"Q102_CENTER.csv")
	os.rename(Q102_center_old_name,Q102_center_new_name)

	Q102_cclient_old_name = os.path.join(root,Q102_List[3])
	Q102_cclient_new_name = os.path.join(root,"Q102_CCLIENT.csv")
	os.rename(Q102_cclient_old_name,Q102_cclient_new_name)

	# for files in os.listdir(wdcsv):
	# 	if re.match('A205', files , flags=0):
	# 		A205_name = re.match('A205.*', files , flags=0).group()
	# 	if re.match('B402', files , flags=0):
	# 		B402_name = re.match('B402.*', files , flags=0).group()
	# 	if re.match('JX201', files , flags=0):
	# 		JX201_name = re.match('JX201.*', files, flags=0).group()
	# 	if re.match('Q102', files , flags=0):
	# 		Q102_name = re.match('Q102.*', files, flags=0).group()
	# os.rename(wdcsv+A205_name,'A205.csv')
	# os.rename(wdcsv+B402_name,'B402.csv')
	# os.rename(wdcsv+JX201_name,'JX201.csv')
	# os.rename(wdcsv+Q102_name,'Q102.csv')

# check csv files if completely or not
def check_csv_files():
	#if(((platform == 'Windows') and (filedir[-1] != '\\'))):
	#	filedir = filedir + '\\'
	#elif(((platform == 'Linux' and (filedir[-1] != '\\'))):
	#	filedir = filedir + '/'
	#A205_count = B402_count = JX201_count = Q102_cout = ALLOTDATA_count = 0
	A205_count = 0
	B402_count = 0
	JX201_count = 0
	Q102_count = 0
	ALLOTDATA_count = 0
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
			Q201_name = re.match('Q102.*', files, flags=0).group()
			Q102_count = Q102_count + 1
	if (A205_count == 1 and  B402_count == 1 and JX201_count == 1 and Q102_count == 4 and ALLOTDATA_count == 1):
		return True
	else:
		return False
	
def delete_csv_files():
	for filename in os.listdir(wdcsv):
		filepath = wdcsv+filename
		os.remove(filepath)
	



