import os
import re



wd = os.getcwd()
parent_path = os.path.dirname(wd)
wdcsv = parent_path +'\\csv\\'

def check_csv_files():
	#if(((platform == 'Windows') and (filedir[-1] != '\\'))):
	#	filedir = filedir + '\\'
	#elif(((platform == 'Linux' and (filedir[-1] != '\\'))):
	#	filedir = filedir + '/'
	#A205_count = B402_count = JX201_count = Q102_cout = ALLOTDATA_count = 0
	A205_count = 0
	B402_count = 0
	JX201_count = 0
	Q102_store_count = 0
	Q102_sr_count = 0
	Q102_center_count = 0 
	Q102_c_count = 0
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
	file_list_count = [A205_count,B402_count,JX201_count,Q102_count,ALLOTDATA_count]

def check_B402_file():
	for files in os.listdir(wdcsv):
		if re.match('B402', files , flags=0):
			return True
	return False
def check_A205_file():
	for files in os.listdir(wdcsv):
		if re.match('A205', files , flags=0):
			return True
	return False
def check_JX201_file():
	for files in os.listdir(wdcsv):
		if re.match('JX201', files , flags=0):
			return True
	return False
def check_Q102_store_file():
	for files in os.listdir(wdcsv):
		if re.match('Q102', files , flags=0):
			Q102_name = re.match('Q102.*', files, flags=0).group()
			if(re.search('.*.partial', Q102_name, flags=0)):
				continue
			if(Q102_name != 'Q102_SR.csv' and Q102_name != 'Q102_CENTER.csv' and Q102_name != 'Q102_CCLIENT.csv'):
				return True
	return False
def check_Q102_sr_file():
	for files in os.listdir(wdcsv):
		if re.match('Q102', files, flags=0):
			Q102_name = re.match('Q102.*', files, flags=0).group()
			if(re.search('.*.partial', Q102_name, flags=0)):
				continue
			if(Q102_name != 'Q102_STORE.csv' and Q102_name != 'Q102_CENTER.csv' and Q102_name != 'Q102_CCLIENT.csv'):
				return True
	return False
def check_Q102_center_file():
	for files in os.listdir(wdcsv):
		if re.match('Q102', files , flags=0):
			Q102_name = re.match('Q102.*', files, flags=0).group()
			if(re.search('.*.partial', Q102_name, flags=0)):
				continue
			if(Q102_name != 'Q102_STORE.csv' and Q102_name != 'Q102_SR.csv' and Q102_name != 'Q102_CCLIENT.csv'):
				return True
	return False
def check_Q102_cclient_file():
	for files in os.listdir(wdcsv):
		if re.match('Q102', files , flags=0):
			Q102_name = re.match('Q102.*', files, flags=0).group()
			if(re.search('.*.partial', Q102_name, flags=0)):
				continue
			if(Q102_name != 'Q102_STORE.csv' and Q102_name != 'Q102_SR.csv' and Q102_name != 'Q102_CENTER.csv'):
				return True
	return False



def change_A205_name():
	for root, dirs, filenames in os.walk(wdcsv):
		for files in filenames:
			if re.match('A205', files , flags=0):
				A205_name = re.match('A205.*', files , flags=0).group()
	A205_old_name = os.path.join(root,A205_name)
	A205_new_name = os.path.join(root,"A205.csv")
	os.rename(A205_old_name,A205_new_name)

def change_B402_name():
	for root, dirs, filenames in os.walk(wdcsv):
		for files in filenames:
			if re.match('B402', files , flags=0):
				B402_name = re.match('B402.*', files , flags=0).group()
	B402_old_name = os.path.join(root,B402_name)
	B402_new_name = os.path.join(root,"B402.csv")
	os.rename(B402_old_name,B402_new_name)

def change_JX201_name():
	for root, dirs, filenames in os.walk(wdcsv):
		for files in filenames:
			if re.match('JX201', files , flags=0):
				JX201_name = re.match('JX201.*', files , flags=0).group()
	JX201_old_name = os.path.join(root,JX201_name)
	JX201_new_name = os.path.join(root,"JX201.csv")
	os.rename(JX201_old_name,JX201_new_name)

def change_Q102_store_name():
	for root, dirs, filenames in os.walk(wdcsv):
		for files in filenames:
			if re.match('Q102', files , flags=0):
				Q102_name = re.match('Q102.*', files, flags=0).group()
				if(Q102_name != 'Q102_SR.csv' and Q102_name != 'Q102_CENTER.csv' and Q102_name != 'Q102_CCLIENT.csv'):
					Q102_name = re.match('Q102.*', files , flags=0).group()

	Q102_store_old_name = os.path.join(root,Q102_name)
	Q102_store_new_name = os.path.join(root,"Q102_STORE.csv")
	os.rename(Q102_store_old_name,Q102_store_new_name)
def change_Q102_sr_name():
	for root, dirs, filenames in os.walk(wdcsv):
		for files in filenames:
			if re.match('Q102', files , flags=0):
				Q102_name = re.match('Q102.*', files, flags=0).group()
				if(Q102_name != 'Q102_STORE.csv' and Q102_name != 'Q102_CENTER.csv' and Q102_name != 'Q102_CCLIENT.csv'):
					Q102_name = re.match('Q102.*', files , flags=0).group()

	Q102_store_old_name = os.path.join(root,Q102_name)
	Q102_store_new_name = os.path.join(root,"Q102_SR.csv")
	os.rename(Q102_store_old_name,Q102_store_new_name)
def change_Q102_center_name():
	for root, dirs, filenames in os.walk(wdcsv):
		for files in filenames:
			if re.match('Q102', files , flags=0):
				Q102_name = re.match('Q102.*', files, flags=0).group()
				if(Q102_name != 'Q102_STORE.csv' and Q102_name != 'Q102_SR.csv' and Q102_name != 'Q102_CCLIENT.csv'):
					Q102_name = re.match('Q102.*', files , flags=0).group()

	Q102_store_old_name = os.path.join(root,Q102_name)
	Q102_store_new_name = os.path.join(root,"Q102_CENTER.csv")
	os.rename(Q102_store_old_name,Q102_store_new_name)
def change_Q102_cclient_name():
	for root, dirs, filenames in os.walk(wdcsv):
		for files in filenames:
			if re.match('Q102', files , flags=0):
				Q102_name = re.match('Q102.*', files, flags=0).group()
				if(Q102_name != 'Q102_STORE.csv' and Q102_name != 'Q102_SR.csv' and Q102_name != 'Q102_CENTER.csv'):
					Q102_name = re.match('Q102.*', files , flags=0).group()

	Q102_store_old_name = os.path.join(root,Q102_name)
	Q102_store_new_name = os.path.join(root,"Q102_CCLIENT.csv")
	os.rename(Q102_store_old_name,Q102_store_new_name)


def check_file(file_name):
	result = False
	if file_name == "B402":
		result = check_B402_file()
	if file_name == "JX201":
		result = check_JX201_file()
	if file_name == "A205":
		result = check_A205_file()
	if file_name == "Q102_STORE":
		result = check_Q102_store_file()
	if file_name == "Q102_SR":
		result = check_Q102_sr_file()
	if file_name == "Q102_CENTER":
		result = check_Q102_center_file()
	if file_name == "Q102_CCLIENT":
		result = check_Q102_cclient_file()
		
	return result


def change_file_name(file_name):
	if file_name == "B402":
		change_B402_name()
	if file_name == "JX201":
		change_JX201_name()
	if file_name == "A205":
		change_A205_name()
	if file_name == "Q102_STORE":
		change_Q102_store_name()
	if file_name == "Q102_SR":
		change_Q102_sr_name()
	if file_name == "Q102_CENTER":
		change_Q102_center_name()
	if file_name == "Q102_CCLIENT":
		change_Q102_cclient_name()

