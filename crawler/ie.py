'''启动360浏览器'''
# -*- coding: UTF-8 -*-
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchFrameException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import JavascriptException
# from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
import os
import csv

class StartCrawler(object):


	#爬取时间
	#begin_date = '' 
	# 列表1：调拨单号	发货仓库	收货仓库
	# 列表2 ：游戏编码	游戏名称 调拨箱数	调拨散包数	调拨总包数 游戏面值 调拨总金额
	list1=[]
	list2=[]
	# 最终的地市调拨数据拼接列表
	allot_data_list=[]

	def __init__(self):
		pass
		
	def TODO(self):
		print("beacause a img element is including in <a> element , we need to send enter to make it work")
		print("how can we get exactly time we need to sleep??????we can wait not too long or short")
		
		
	def start_drive(self):
		"""
		自动登录模块
		"""
		#打开浏览器
		self.browser = webdriver.Ie()
		self.browser.get('https://3.13.1.10/loginnew.html')

		#输入PIN码
		pin_code= self.browser.find_element_by_name("pinCode")
		pin_code.clear()
		pin_code.send_keys("11111111")  # 默认PIN码
		#点击登录按钮
		login_button = self.browser.find_element_by_xpath("/html/body/form/div/table/tbody/tr[2]/td/table[2]/tbody/tr/td/input[1]").click()
		time.sleep(10)
		
	
	def switch_which_frame(self, frame_name):
		"""
		切换Frame
		"""
		i = 0
		while True:
			try:
				self.browser.switch_to.frame(frame_name)
			except NoSuchFrameException:
				time.sleep(1) 
				print(str(i))
				i = i +1
			else:
				print("Find this "+frame_name)
				break
	

	def download_csv(self):
		i = 0
		while True:
			try:
				js_DownLoad = "javascript:resultOut('csv',resultForm)"
				self.browser.execute_script(js_DownLoad)
			except JavascriptException:
				time.sleep(2) 
				print(str(i))
				i = i +1
			else:
				print("click download csv successfully")
				break
	# def find_which_element(self, element_name):
	# 	"""
	# 	切换Frame
	# 	"""
	# 	i = 0
	# 	while True:
	# 		try:
	# 			self.browser.switch_to.frame(frame_name)
	# 		except NoSuchFrameException:
	# 			time.sleep(1) 
	# 			print(str(i))
	# 			i = i +1
	# 		else:
	# 			print("Find this "+frame_name)
	# 			break
		
	def instant_business(self):
		"""
		点击即开业务
		"""
		#得到网页
		# self.browser.get("https://3.13.1.20:/ump/index.html")
		i = 0
		for handler in self.browser.window_handles:
			print(str(i))
			print(len(self.browser.window_handles))
			url = self.browser.current_url
			print(str(url))
			if str(url) == "https://3.13.1.20/ump/index.html":
				self.browser.switch_to.window(handler)
				print("Focus into this page")
				break
			else:
				continue
		print("All page have print")
		print(self.browser.current_url)

		#focus on topFrame
		self.switch_which_frame("topFrame")

		#定位即开业务‘
		time.sleep(1)
		js_JiKai = "if('31000000'=='55999999'){window.location.href = '/ump/system/toELPSystem.action'}else{if(top.checkUmpBlock()){clearBack();switchModule('31000000','即开业务', 'ilms', '10');}else{return false;}}"
		self.browser.execute_script(js_JiKai)
		# back to root frame
		self.browser.switch_to.parent_frame()
	
	# call autoit automatically click save button
	def autoit_click(self):
		"""
		自动点击下载
		"""
		os.system("click_save.exe")

	def autoit_click_30(self):
		"""
		自动点击下载,下载等待30s
		"""
		os.system("click_save_30.exe")
	
	def statement_management(self):
		"""
		点击报表管理
		"""
		#定位报表管理
		time.sleep(2)
		js_BaoBiaoGuanLi = "if(top.checkUmpBlock()){clearBack();switchModule('31140000','报表管理', 'ilms', '20');}else{return false;}"
		self.browser.execute_script(js_BaoBiaoGuanLi)
		time.sleep(2)


	def get_begin_data(self):
		"""
		得到当前的有效数据时间
		"""
		#1. 定位报表管理
		#focus on topFrame
		self.switch_which_frame("topFrame")
		time.sleep(1)
		self.statement_management() #点击报表管理
		# back to root frame
		self.browser.switch_to.parent_frame()
		#2. 定位ZAFFIL报表WEB展现
		self.switch_which_frame("leftFrame")
		Xpath_ZAFFIL = "/html/body[@class='imgbody']/div[@class='leftbox']/div[@class='menubox']/div[@class='lnavbg1']/a[@menuId='31140900']"

		i = 0
		while True:
			try:
				self.browser.find_element_by_xpath(Xpath_ZAFFIL).send_keys(Keys.ENTER)
			except NoSuchElementException:
				time.sleep(1) 
				print(str(i))
				i = i +1
			else:
				print("Find this element ")
				break
		# self.browser.find_element_by_xpath(Xpath_ZAFFIL).send_keys(Keys.ENTER)
		print("Finish ZAFFIL")

		time.sleep(2)
		#3. 定位JX201
		Xpath_JX201 = "/html/body[@class='imgbody']/div[@class='leftbox']/div[@class='menubox']/ul[@id='content8']/li[@sizset='76']/a[@menuId='31140915']"
		self.browser.find_element_by_xpath(Xpath_JX201).click()
		print("Finish find JX201")
		self.browser.switch_to.parent_frame()

		# switch to mainFrame
		self.switch_which_frame("mainFrame")
		#4. 得到时间
		time.sleep(2)
		elem = self.browser.find_element_by_id("BEGIN_DATE")
		begine_data = elem.get_attribute("value")
		#click statement management again
		self.browser.switch_to.parent_frame()
		#focus on topFrame
		self.switch_which_frame("topFrame")
		time.sleep(1)
		self.statement_management() #点击报表管理
		time.sleep(2)
		self.browser.switch_to.parent_frame()
		return begine_data

	def get_JX201(self):
		"""
		下载JX_201报表到共享文件夹/csv 文件目录中
		"""
	
		#1. 定位ZAFFIL报表WEB展现
		time.sleep(1)
		self.switch_which_frame("leftFrame")
		time.sleep(1)
		Xpath_ZAFFIL = "/html/body[@class='imgbody']/div[@class='leftbox']/div[@class='menubox']/div[@class='lnavbg1']/a[@menuId='31140900']"
		self.browser.find_element_by_xpath(Xpath_ZAFFIL).send_keys(Keys.ENTER)
		print("Finish ZAFFIL")

		time.sleep(2)
		#2. 定位JX201
		Xpath_JX201 = "/html/body[@class='imgbody']/div[@class='leftbox']/div[@class='menubox']/ul[@id='content8']/li[@sizset='76']/a[@menuId='31140915']"
		self.browser.find_element_by_xpath(Xpath_JX201).click()
		print("Finish find JX201")
		self.browser.switch_to.parent_frame()

		# switch to mainFrame
		self.switch_which_frame("mainFrame")
		# 3. 获取全局 爬取时间，然后查询
		# time.sleep(2)
		# elem = self.browser.find_element_by_id("BEGIN_DATE")
		# self.begin_date = elem.get_attribute("value")
		time.sleep(2)
		js_Query = "queryRecord()"
		self.browser.execute_script(js_Query)
		time.sleep(2)

		# 4. 下载文件 jx201 csv file
		self.switch_which_frame("report")
		
		self.download_csv()
		
		#5. 点击下载保存 click save and exit
		self.autoit_click()
		#back to main frame
		self.browser.switch_to.parent_frame()
		#back to root
		self.browser.switch_to.parent_frame()

		pass

	def get_B402(self):
		"""
		下载B_402报表到共享文件夹/csv 文件目录中
		"""
		# 1. 点击销售兑奖 get in left frame for sales and claiming
		self.switch_which_frame("leftFrame")
		
		time.sleep(5)
		xpath_sales = "/html/body[@class='imgbody']/div[@class='leftbox']/div[@class='menubox']/div[@class='lnavbg1']/a[@menuId='31140500']"
		self.browser.find_element_by_xpath(xpath_sales).send_keys(Keys.ENTER)
		print("Finish get sales and claiming")
		
		# 2. 定位B402报表locating B402
		Xpath_B402 = "/html/body[@class='imgbody']/div[@class='leftbox']/div[@class='menubox']/ul[@id='content4']/li[@sizset='45']/a[@menuId='31140505']"
		self.browser.find_element_by_xpath(Xpath_B402).click()
		print("Finish find B402")
		self.browser.switch_to.parent_frame()
		time.sleep(5)

		
		# 3. 查询
		# switch to mainFrame
		self.switch_which_frame("mainFrame")
		time.sleep(5)
		js_Query = "queryRecord()"
		self.browser.execute_script(js_Query)
		time.sleep(5)
		
		# 4. 下载文件download B402 csv file
		self.switch_which_frame("report")

		self.download_csv()

		
		#5. 点击下载保存click save and exit
		self.autoit_click()
		#back to main frame
		self.browser.switch_to.parent_frame()
		#back to root
		self.browser.switch_to.parent_frame()
		

	def get_A205(self):
		"""
		下载A_205报表到共享文件夹/csv 文件目录中
		"""
		# 1. 点击库存 get in left frame for inventory
		self.switch_which_frame("leftFrame")
		
		time.sleep(5)
		xpath_sales = "/html/body[@class='imgbody']/div[@class='leftbox']/div[@class='menubox']/div[@class='lnavbg1']/a[@menuId='31140300']"
		self.browser.find_element_by_xpath(xpath_sales).send_keys(Keys.ENTER)
		print("Finish get inventory")
		
		# 2. 定位A205 报表 locating A205
		Xpath_A205 = "/html/body[@class='imgbody']/div[@class='leftbox']/div[@class='menubox']/ul[@id='content2']/li[@sizset='10']/a[@menuId='31140305']"
		self.browser.find_element_by_xpath(Xpath_A205).click()
		print("Finish find A205")
		self.browser.switch_to.parent_frame()
		time.sleep(3)
		
		# 3. 查询
		# switch to mainFrame
		self.switch_which_frame("mainFrame")
		# chose storehouse
		time.sleep(3)
		
		
		Xpath_A205_lookup = "/html/body/div[3]/div/form/table/tbody/tr/td[4]/table/tbody/tr/td[2]/div/div[@class='u-lookupIcon']"
		self.browser.find_element_by_xpath(Xpath_A205_lookup).click()
		
		# 因为iframe没有 name 或者 id，找到iframe切换进入move to iframe
		xpath_A205_iframe = "/html/body/div[@class='x-dlg-proxy']/div[@class='x-dlg']/table/tbody/tr[2]/td/table/tbody/tr/td[2]/div/iframe"
		iframe = self.browser.find_element_by_xpath(xpath_A205_iframe)
		i = 0
		while True:
			try:
				self.browser.switch_to.frame(iframe)
			except NoSuchFrameException:
				time.sleep(1) 
				print(str(i))
				i = i +1
			else:
				print("Find this iframe")
				break

		# 点击查找仓库 small button
		time.sleep(2)
		name_A205_small = "singledataGrid"
		self.browser.find_element_by_name(name_A205_small).click()
		
		# back to mainFrame , move to confirm frame
		time.sleep(2)
		self.browser.find_element_by_id('confirmBtn_label').click()
		print("click confirm key")
		
		# 再次从最基础切换到mainframe中back to mainFrame is already closed? I can not know where i am ,so i switch to deauflt
		self.browser.switch_to.default_content()
		self.switch_which_frame("mainFrame")
		#self.browser.switch_to.parent_frame()
		# 查询
		time.sleep(3)
		js_Query = "queryRecord()"
		self.browser.execute_script(js_Query)
		time.sleep(2)
		
		# 4. 下载A205报表 download A205 csv file
		self.switch_which_frame("report")
		self.download_csv()
		# Alert(self.browser).accept()
		
		#5. 点击保存 click save and exit
		self.autoit_click()
		#back to main frame
		self.browser.switch_to.parent_frame()
		#back to root
		self.browser.switch_to.parent_frame()
		
	def get_Q102(self):
		"""
		下载Q_102报表到共享文件夹/csv 文件目录中
		"""
		# 1.点击查询报表 get in left frame for quering report 
		self.switch_which_frame("leftFrame")
		
		time.sleep(3)
		xpath_query = "/html/body[@class='imgbody']/div[@class='leftbox']/div[@class='menubox']/div[@class='lnavbg1']/a[@menuId='31141000']"
		self.browser.find_element_by_xpath(xpath_query).send_keys(Keys.ENTER)
		print("Finish get statement query")
		
		# 2. 点击Q102报表  locating Q102
		Xpath_Q102 = "/html/body[@class='imgbody']/div[@class='leftbox']/div[@class='menubox']/ul[@id='content9']/li[@sizset='82']/a[@menuId='31141002']"
		self.browser.find_element_by_xpath(Xpath_Q102).click()
		print("Finish find Q102")
		self.browser.switch_to.parent_frame()
		time.sleep(5)

		
		# 3. 查询
		# switch to mainFrame
		self.switch_which_frame("mainFrame")
		time.sleep(3)
		# 3.1 门店数据click store 
		self.browser.find_element_by_id('awardType2').click()
		time.sleep(2)
		# click query
		js_Query = "queryRecord()"
		self.browser.execute_script(js_Query)
		time.sleep(3)
		
		# . 下载Q102 报表 download Q102 csv file
		self.switch_which_frame("report")
		self.download_csv()
		
		# click save and exit
		self.autoit_click_30()

		#back to main frame
		self.browser.switch_to.default_content()

		time.sleep(3)
		# 1.点击查询报表 get in left frame for quering yreport 
		self.switch_which_frame("leftFrame")
		time.sleep(3)
		
		# 2. 点击Q102报表  locating Q102
		Xpath_Q102 = "/html/body[@class='imgbody']/div[@class='leftbox']/div[@class='menubox']/ul[@id='content9']/li[@sizset='82']/a[@menuId='31141002']"
		self.browser.find_element_by_xpath(Xpath_Q102).click()
		print("Finish find Q102")
		self.browser.switch_to.parent_frame()
		time.sleep(5)



		self.switch_which_frame("mainFrame")
		time.sleep(2)

		# 3.2 sr数据click sr 
		self.browser.find_element_by_id('awardType3').click()
		time.sleep(2)
		# click query
		js_Query = "queryRecord()"
		self.browser.execute_script(js_Query)
		time.sleep(3)
		
		#  下载Q102 报表 download Q102 csv file
		self.switch_which_frame("report")
		self.download_csv()
		
		# click save and exit
		self.autoit_click()
		#back to main frame
		self.browser.switch_to.default_content()

		time.sleep(3)
		# 1.点击查询报表 get in left frame for quering yreport 
		self.switch_which_frame("leftFrame")
		time.sleep(3)	
		
		# 2. 点击Q102报表  locating Q102
		Xpath_Q102 = "/html/body[@class='imgbody']/div[@class='leftbox']/div[@class='menubox']/ul[@id='content9']/li[@sizset='82']/a[@menuId='31141002']"
		self.browser.find_element_by_xpath(Xpath_Q102).click()
		print("Finish find Q102")
		self.browser.switch_to.parent_frame()
		time.sleep(5)

		self.switch_which_frame("mainFrame")

		# 3.3 center数据click center
		self.browser.find_element_by_id('awardType4').click()
		time.sleep(2)
		# click query
		js_Query = "queryRecord()"
		self.browser.execute_script(js_Query)
		time.sleep(3)
		
		# . 下载Q102 报表 download Q102 csv file
		self.switch_which_frame("report")
		self.download_csv()
		
		# click save and exit
		self.autoit_click()
		#back to main frame
		self.browser.switch_to.default_content()


		time.sleep(3)
		# 1.点击查询报表 get in left frame for quering yreport 
		self.switch_which_frame("leftFrame")
		
		time.sleep(3)
		
		# 2. 点击Q102报表  locating Q102
		Xpath_Q102 = "/html/body[@class='imgbody']/div[@class='leftbox']/div[@class='menubox']/ul[@id='content9']/li[@sizset='82']/a[@menuId='31141002']"
		self.browser.find_element_by_xpath(Xpath_Q102).click()
		print("Finish find Q102")
		self.browser.switch_to.parent_frame()
		time.sleep(5)

		self.switch_which_frame("mainFrame")

		# 3.4 cclient数据click cclient
		self.browser.find_element_by_id('awardType5').click()
		time.sleep(2)
		# click query
		js_Query = "queryRecord()"
		self.browser.execute_script(js_Query)
		time.sleep(3)
		
		# . 下载Q102 报表 download Q102 csv file
		self.switch_which_frame("report")
		self.download_csv()
		
		# click save and exit
		self.autoit_click()
		#back to main frame
		self.browser.switch_to.parent_frame()

		#back to root
		self.browser.switch_to.parent_frame()

	def get_AllotData(self):
		"""
		拼接地市调拨数据
		"""
		#focus on topFrame
		self.switch_which_frame("topFrame")
				
		#点击调拨管理 locate allot management
		time.sleep(1)
		allot_management = "if(top.checkUmpBlock()){clearBack();switchModule('31030000','调拨管理', 'ilms', '20');}else{return false;}"
		self.browser.execute_script(allot_management)
		time.sleep(1)

		# back to root frame
		self.browser.switch_to.parent_frame()
		
		
		# normal allot
		# 1. 点击普通调拨get in left frame for normal allot data
		self.switch_which_frame("leftFrame")
		
		time.sleep(3)
		xpath_normal = "/html/body[@class='imgbody']/div[@class='leftbox']/div[@class='menubox']/div[@class='lnavbg1']/a[@menuId='31030200']"
		self.browser.find_element_by_xpath(xpath_normal).send_keys(Keys.ENTER)
		print("Finish get normal allot")
		
		# 2. 点击调拨单查询 locating allot order query
		Xpath_allot_data = "/html/body[@class='imgbody']/div[@class='leftbox']/div[@class='menubox']/ul[@id='content2']/li[@sizset='9']/a[@menuId='31030205']"
		self.browser.find_element_by_xpath(Xpath_allot_data).click()
		print("Finish find allot order query")
		self.browser.switch_to.parent_frame()
		time.sleep(3)
		
		

		# 根据情况重新设计：ID，调拨单号	发货仓库	收货仓库	游戏编码	游戏名称 调拨箱数	调拨散包数	调拨总包数 游戏面值 调拨总金额 创建日期
		
		# 获取当前日期
		# 重新设计
		# 列表1：调拨单号	发货仓库	收货仓库
		# 列表2 ：游戏编码	游戏名称 调拨箱数	调拨散包数	调拨总包数 游戏面值 调拨总金额
		# 数据拼接格式： 列表1+列表2+日期
		# switch to mainFrame
		self.switch_which_frame("mainFrame")
		time.sleep(2)
		
		# 采用相对定位
		xpath_allot_number = "//div[@id='page-0']/div[1]/table[@class='dojoxGrid-row-table']/tbody/tr/td[1]/nobr/div"
		print(self.browser.find_element_by_xpath(xpath_allot_number).text)

		# 拼接元素查找路径
		xpath_part1="//div[@id='page-0']/div["
		xpath_part2="]/table[@class='dojoxGrid-row-table']/tbody/tr/td["
		xpath_part3="]/nobr"
		xpath_part3div= "]/nobr/div"
		
		current_date=time.strftime('%Y-%m-%d',time.localtime(time.time()))
		#查找page-0 中10项，等于当前日期的项
		i = 1
		#保存当前日志调拨单的数量 list save allot date items which date equals current date  ,such as list=[1,2]
		list=[]
		time.sleep(2)
		while i <=10:
			xpath_create_date = "//div[@id='page-0']/div["+str(i)+"]/table[@class='dojoxGrid-row-table']/tbody/tr/td[4]/nobr"
			create_date = self.browser.find_element_by_xpath(xpath_create_date).text
			print(create_date)
			if(current_date == create_date):
				list = list + [i]
				i=i+1
			else:
				break
		
		time.sleep(2)

		#拼接list1：join list1 
		for i in list:
			text = self.browser.find_element_by_xpath(xpath_part1+str(i)+xpath_part2+'1'+xpath_part3div).text
			self.list1 = self.list1+[[text]]
		for i in list:
			for j in range(2,4):
				text=self.browser.find_element_by_xpath(xpath_part1+str(i)+xpath_part2+str(j)+xpath_part3).text
				self.list1[i-1]=self.list1[i-1]+[text]
				
		print(self.list1)
		
		#join list2

		for i in list:
			time.sleep(3)
			self.get_order(i-1)
			# click backbtn
			self.browser.find_element_by_id('backBtn').click()
			
		# back to root frame
		print(self.allot_data_list)
		self.browser.switch_to.parent_frame()

		# 将得到的拼接数据写入到csv文件中
		with open('./csv/ALLOTDATA.csv','w',newline='') as f:
			f_csv = csv.writer(f)
			f_csv.writerows(self.allot_data_list)
		
		
	def get_order(self,order_num):
		"""
		获取每个具体调拨单的数据
		"""
		# execute js,move to first order info
		time.sleep(1)
		allot_code = "viewARecord("+str(order_num)+",\"ama_ALLOCATE_CODE\")"
		self.browser.execute_script(allot_code)
		time.sleep(1)
		self.list2=[]
		#join list2
		xpath_info_part1="//div[@id='page-0']/div["
		xpath_info_part2="]/table[@class='dojoxGrid-row-table']/tbody/tr/td["
		xpath_info_part3= "]"
		xpath_info_part3div= "]/div"
		
		
		# 获取游戏的数量 get total game num
		time.sleep(2)
		i=1
		game_count = 0
		while True:
			try:
				xpath_game_code=xpath_info_part1+str(i)+xpath_info_part2+'1'+xpath_info_part3div
				print(self.browser.find_element_by_xpath(xpath_game_code).text)
				game_count = game_count+1
				i=i+1
			except NoSuchElementException:
				break
		
		print(game_count)
		# 添加游戏编号add game code
		i = 1
		while i <= game_count:
			xpath_game_code=xpath_info_part1+str(i)+xpath_info_part2+'1'+xpath_info_part3div
			self.list2=self.list2+[[self.browser.find_element_by_xpath(xpath_game_code).text]]
			i=i+1
		
		print(self.list2)
		# 添加游戏其他信息 add game info
		i=1
		while i<=game_count:
			for j in range(2,8):
				xpath_game=xpath_info_part1+str(i)+xpath_info_part2+str(j)+xpath_info_part3
				text=self.browser.find_element_by_xpath(xpath_info_part1+str(i)+xpath_info_part2+str(j)+xpath_info_part3).text
				self.list2[i-1]+=[text]
			i=i+1
		
		print(self.list2)
		# 拼接list2 get first order list,put list info into list2
		current_date=time.strftime('%Y-%m-%d',time.localtime(time.time()))
		i=1
		while i<=game_count:
			self.allot_data_list+=[self.list1[order_num]+self.list2[i-1]+[current_date]]
			i=i+1


if __name__ =="__main__":
	Crawler = StartCrawler()
	Crawler.start_drive()
	Crawler.TODO()
	Crawler.instant_business()
	# Crawler.get_JX201()
	# Crawler.get_B402()
	# Crawler.get_A205()
	Crawler.get_Q102()
	# Crawler.get_AllotData()
	# Crawler.get_begin_data()


