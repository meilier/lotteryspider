'''启动360浏览器'''
# -*- coding: UTF-8 -*-
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchFrameException
from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
import os
import csv

class StartCrawler(object):


	list1=[]
	list2=[]
	allot_data_list=[]

	def __init__(self):
		pass
		
	def TODO(self):
		print("beacause a img element is including in <a> element , we need to send enter to make it work")
		print("how can we get exactly time we need to sleep??????we can wait not too long or short")
		
		
	def start_drive(self):
		#打开浏览器
		self.browser = webdriver.Ie()
		self.browser.get('https://3.13.1.10/loginnew.html')

		#输入PIN码
		pin_code= self.browser.find_element_by_name("pinCode")
		pin_code.clear()
		pin_code.send_keys("11111111")

		#点击登录按钮
		login_button = self.browser.find_element_by_xpath("/html/body/form/div/table/tbody/tr[2]/td/table[2]/tbody/tr/td/input[1]").click()

		#Xpath
		# jikaiyewu= /html/frameset[1]/frame/html/body/div/div/div[4]/ul/li[18]/a
		# jikaiyewu = /html/frameset[@id='mainFrameset']/frame[@id='topFrame']/html/body/div[@id='top']/div/div[4]/ul[@id='nav']/li[@id='31000000']/a

		time.sleep(10)
		
		
	def switch_which_frame(self, frame_name):
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
		
	def instant_business(self):
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
		time.sleep(1)
		self.statement_management()
		# back to root frame
		self.browser.switch_to.parent_frame()
	
	# call autoit automatically click save button
	def autoit_click(self):
		os.system("click_save.exe")
	
	def statement_management(self):
		#定位报表管理
		js_BaoBiaoGuanLi = "if(top.checkUmpBlock()){clearBack();switchModule('31140000','报表管理', 'ilms', '20');}else{return false;}"
		# js_BaoBiaoGuanLi ='{clearBack();switchModule('31140000','报表管理', 'ilms', '20')}'
		self.browser.execute_script(js_BaoBiaoGuanLi)
		time.sleep(1)


	def get_JX201(self):
	
		#1. 定位ZAFFIL报表WEB展现
		# js_ZAFIL = "if(top.checkUmpBlock()){clearBack();clickSubMenu('报表管理','',this.innerHTML);}else{return false}"
		# self.browser.execute_script(js_ZAFIL)

		#self.browser.find_element_by_xpath("/frame#leftFrame/html/body.imgbody/div.menubox/div.lnavbg1/a").click 	



		self.switch_which_frame("leftFrame")

		Xpath_ZAFFIL = "/html/body[@class='imgbody']/div[@class='leftbox']/div[@class='menubox']/div[@class='lnavbg1']/a[@menuId='31140900']"
		# self.browser.find_element_by_xpath(Xpath_ZAFFIL).click()
		self.browser.find_element_by_xpath(Xpath_ZAFFIL).send_keys(Keys.ENTER)
		# self.browser.execute_script( self.browser.find_element_by_xpath(Xpath_ZAFFIL).style  )

		print("Finish ZAFFIL")

		time.sleep(2)
		#2. 定位JX201
		Xpath_JX201 = "/html/body[@class='imgbody']/div[@class='leftbox']/div[@class='menubox']/ul[@id='content8']/li[@sizset='76']/a[@menuId='31140915']"
		self.browser.find_element_by_xpath(Xpath_JX201).click()
		print("Finish find JX201")
		self.browser.switch_to.parent_frame()


		# switch to mainFrame
		self.switch_which_frame("mainFrame")
		# 3. 查询
		time.sleep(2)
		js_Query = "queryRecord()"
		self.browser.execute_script(js_Query)

		time.sleep(2)

		# 4. download jx201 csv file
		self.switch_which_frame("report")
		# js_DownLoadJX201 = "javascript:resultOut('csv',resultForm)"
		# self.browser.execute_script(js_DownLoadJX201)
		#Xpath_JX201_csv = "/html[@class='dj_ie dj_ie7 dj_contentbox']/body[@class='unieap']/form[@name='resultForm']/div[@id='exportBar']/ul/li[@id='csvTag']/img[@id='csv']"
		#self.browser.find_element_by_xpath(Xpath_JX201_csv).click()
		
		#download B402 csv file
		js_DownLoadJX201 = "javascript:resultOut('csv',resultForm)"
		self.browser.execute_script(js_DownLoadJX201)
		# Alert(self.browser).accept()
		
		#5. click save and exit
		self.autoit_click()
		#back to main frame
		self.browser.switch_to.parent_frame()
		#back to root
		self.browser.switch_to.parent_frame()

		pass

	def get_B402(self):

		# 1.get in left frame for sales and claiming
		self.switch_which_frame("leftFrame")
		
		time.sleep(5)
		xpath_sales = "/html/body[@class='imgbody']/div[@class='leftbox']/div[@class='menubox']/div[@class='lnavbg1']/a[@menuId='31140500']"
		self.browser.find_element_by_xpath(xpath_sales).send_keys(Keys.ENTER)
		print("Finish get sales and claiming")
		
		# 2. locating B402
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
		
		# 4. download B402 csv file
		self.switch_which_frame("report")
		# js_DownLoadJX201 = "javascript:resultOut('csv',resultForm)"
		# self.browser.execute_script(js_DownLoadJX201)
		#Xpath_B402_csv = "/html[@class='dj_ie dj_ie7 dj_contentbox']/body[@class='unieap']/form[@name='resultForm']/div[@id='exportBar']/ul/li[@id='csvTag']/img[@id='csv']"
		#self.browser.find_element_by_xpath(Xpath_B402_csv).click()
		js_DownLoadB402 = "javascript:resultOut('csv',resultForm)"
		self.browser.execute_script(js_DownLoadB402)
		# Alert(self.browser).accept()
		
		#5. click save and exit
		self.autoit_click()
		#back to main frame
		self.browser.switch_to.parent_frame()
		#back to root
		self.browser.switch_to.parent_frame()
		

	def get_A205(self):
		# 1.get in left frame for inventory
		self.switch_which_frame("leftFrame")
		
		time.sleep(5)
		xpath_sales = "/html/body[@class='imgbody']/div[@class='leftbox']/div[@class='menubox']/div[@class='lnavbg1']/a[@menuId='31140300']"
		self.browser.find_element_by_xpath(xpath_sales).send_keys(Keys.ENTER)
		print("Finish get inventory")
		
		# 2. locating A205
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
		
		
		#Xpath_A205_lookup = "/html[@class='dj_ie dj_ie7 dj_iequirks']/body[@class='unieap']/div[@class='cmhead']/div[@id='queryPanel']/form[@id='queryForm']/table[@id='queryFormContent]/tbody/tr/td/table/tbody/tr/td/div[@class='lookuptextbox lookuptextboxReadOnly']/div[@class='u-lookupIcon']"
		Xpath_A205_lookup = "/html/body/div[3]/div/form/table/tbody/tr/td[4]/table/tbody/tr/td[2]/div/div[@class='u-lookupIcon']"
		self.browser.find_element_by_xpath(Xpath_A205_lookup).click()
		
		# move to iframe
		# xpath_A205_iframe = "/html[@class='dj_ie dj_ie7 dj_iequirks']/body[@class='unieap mainbody']/div[@class='x-dlg-proxy']/div[@class='x-dlg']/table[@id='unieap_innerTable_0']/tbody/tr/td/table/tbody/tr/td/div[@class='dialogBody']/iframe"
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

		# small button
		#xpath_A205_small = "/html[@class='dj_ie dj_ie7 dj_iequirks']/body[@class='unieap mainbody']/div[@id='dataGrid']/div[@class='dojoxGrid-master-view']/div[@id='unieap_widget_grid_RowView_0']/div[@class='dojoxGrid-scrollbox']/div[@class='dojoxGrid-content']/div[@id='page-0']/div[@class='dojoxGrid-rowbar dojoxGrid-rowbar-over']/table[@class='u-grid-rowbar-table']/tbody/tr/td/input"
		name_A205_small = "singledataGrid"
		self.browser.find_element_by_name(name_A205_small).click()
		
		# back to mainFrame , move to confirm frame
		#self.browser.switch_to.parent_frame()
		time.sleep(2)
		self.browser.find_element_by_id('confirmBtn_label').click()
		print("click confirm key")
		
		# back to mainFrame is already closed? I can not know where i am ,so i switch to deauflt
		self.browser.switch_to.default_content()
		self.switch_which_frame("mainFrame")
		#self.browser.switch_to.parent_frame()
		# 查询
		time.sleep(3)
		js_Query = "queryRecord()"
		self.browser.execute_script(js_Query)
		time.sleep(45)
		
		# 4. download A205 csv file
		self.switch_which_frame("report")
		js_DownLoadA205 = "javascript:resultOut('csv',resultForm)"
		self.browser.execute_script(js_DownLoadA205)
		# Alert(self.browser).accept()
		
		#5. click save and exit
		self.autoit_click()
		#back to main frame
		self.browser.switch_to.parent_frame()
		#back to root
		self.browser.switch_to.parent_frame()
		
	def get_Q102(self):
		# 1.get in left frame for sales and claiming
		self.switch_which_frame("leftFrame")
		
		time.sleep(3)
		# maybe name is ok menuTwoWithoutHref .Test when completed.
		# img_path = "/html/body/div/div[2]/div[2]/div[@class='lnavbg2']/a/img"
		# img_path.click()
		#xpath_sales = "/html/body[@class='imgbody']/div[@class='leftbox']/div[@class='menubox']/div[@class='lnavbg1']/a[@menuId='31140500']"
		xpath_query = "/html/body[@class='imgbody']/div[@class='leftbox']/div[@class='menubox']/div[@class='lnavbg1']/a[@menuId='31141000']"
		self.browser.find_element_by_xpath(xpath_query).send_keys(Keys.ENTER)
		print("Finish get statement query")
		
		# 2. locating Q102
		Xpath_Q102 = "/html/body[@class='imgbody']/div[@class='leftbox']/div[@class='menubox']/ul[@id='content9']/li[@sizset='82']/a[@menuId='31141002']"
		self.browser.find_element_by_xpath(Xpath_Q102).click()
		print("Finish find Q102")
		self.browser.switch_to.parent_frame()
		time.sleep(5)

		
		# 3. 查询
		# switch to mainFrame
		self.switch_which_frame("mainFrame")
		time.sleep(3)
		
		
		# click sr
		self.browser.find_element_by_id('awardType3').click()
		time.sleep(2)
		# click query
		js_Query = "queryRecord()"
		self.browser.execute_script(js_Query)
		time.sleep(30)
		
		# 4. download Q102 csv file
		self.switch_which_frame("report")
		# js_DownLoadJX201 = "javascript:resultOut('csv',resultForm)"
		# self.browser.execute_script(js_DownLoadJX201)
		#Xpath_B402_csv = "/html[@class='dj_ie dj_ie7 dj_contentbox']/body[@class='unieap']/form[@name='resultForm']/div[@id='exportBar']/ul/li[@id='csvTag']/img[@id='csv']"
		#self.browser.find_element_by_xpath(Xpath_B402_csv).click()
		js_DownLoadB402 = "javascript:resultOut('csv',resultForm)"
		self.browser.execute_script(js_DownLoadB402)
		# Alert(self.browser).accept()
		
		#5. click save and exit
		self.autoit_click()
		#back to main frame
		self.browser.switch_to.parent_frame()
		#back to root
		self.browser.switch_to.parent_frame()

	def get_AllotData(self):
		#focus on topFrame
		self.switch_which_frame("topFrame")
				
		#locate allot management
		time.sleep(1)
		allot_management = "if(top.checkUmpBlock()){clearBack();switchModule('31030000','调拨管理', 'ilms', '20');}else{return false;}"
		self.browser.execute_script(allot_management)
		time.sleep(1)

		# back to root frame
		self.browser.switch_to.parent_frame()
		
		
		# normal allot
		# 1.get in left frame for normal allot data
		self.switch_which_frame("leftFrame")
		
		time.sleep(3)
		xpath_normal = "/html/body[@class='imgbody']/div[@class='leftbox']/div[@class='menubox']/div[@class='lnavbg1']/a[@menuId='31030200']"
		self.browser.find_element_by_xpath(xpath_normal).send_keys(Keys.ENTER)
		print("Finish get normal allot")
		
		# 2. locating allot order query
		Xpath_allot_data = "/html/body[@class='imgbody']/div[@class='leftbox']/div[@class='menubox']/ul[@id='content2']/li[@sizset='9']/a[@menuId='31030205']"
		self.browser.find_element_by_xpath(Xpath_allot_data).click()
		print("Finish find allot order query")
		self.browser.switch_to.parent_frame()
		time.sleep(3)
		
		
		# 第一个页面有如下数据： 调拨单号	发货仓库	收货仓库	创建日期	调拨箱数	调拨散包数	调拨总包数	状态
		# 点击调拨单号会有：游戏编码	游戏名称游戏面值 调拨金额
		# 我们的表：ID，调拨单号	发货仓库	收货仓库	游戏编码	游戏名称	游戏面值 	调拨箱数	调拨散包数	调拨总包数 调拨总金额 创建日期
		# 根据情况重新设计：ID，调拨单号	发货仓库	收货仓库	游戏编码	游戏名称 调拨箱数	调拨散包数	调拨总包数 游戏面值 调拨总金额 创建日期
		
		# 获取当前日期：
		# 列表1：调拨单号	发货仓库	收货仓库
		# 列表2：调拨箱数	调拨散包数	调拨总包数
		# 列表3：游戏编码	游戏名称 游戏面值 调拨金额
		# 根据当前日期，在第一个页面获取调拨单号，进入获取数据。数据拼接格式： 列表1+列表3+列表2+日期
		
		# 重新设计
		# 列表1：调拨单号	发货仓库	收货仓库
		# 列表2 ：游戏编码	游戏名称 调拨箱数	调拨散包数	调拨总包数 游戏面值 调拨总金额
		# 数据拼接格式： 列表1+列表2+日期
		# switch to mainFrame
		self.switch_which_frame("mainFrame")
		time.sleep(2)
		#xpath_allot_number= ""/html/body/div[@class='cm']/div[@id='dataGrid']/div[@class='dojoxGrid-master-view']/div[@id='dojox_GridView_0']/div[@class='dojoxGrid-scrollbox']/div[@class='dojoxGrid-content']""
		# xpath_allot_number = "/html/body/div[@class='cm']/div[@id='dataGrid']/div[2]/div[2]/div/div/div/"
		# 采用相对定位，服了，相对定位非常ok
		#xpath_main_page = "//div[@id='page-0']/div[1]"
		xpath_allot_number = "//div[@id='page-0']/div[1]/table[@class='dojoxGrid-row-table']/tbody/tr/td[1]/nobr/div"
		#xpath_outbound_warehouse = "//div[@id='page-0']/div[1]/table[@class='dojoxGrid-row-table']/tbody/tr/td[2]/nobr"
		#xpath_inbound_warehouse = "//div[@id='page-0']/div[1]/table[@class='dojoxGrid-row-table']/tbody/tr/td[3]/nobr"
		#xpath_create_date = "//div[@id='page-0']/div[1]/table[@class='dojoxGrid-row-table']/tbody/tr/td[4]/nobr"
		#xpath_allot_case_number = "//div[@id='page-0']/div[1]/table[@class='dojoxGrid-row-table']/tbody/tr/td[5]/nobr"
		#xpath_scattered_package = "//div[@id='page-0']/div[1]/table[@class='dojoxGrid-row-table']/tbody/tr/td[6]/nobr"
		#xpath_total_package = "//div[@id='page-0']/div[1]/table[@class='dojoxGrid-row-table']/tbody/tr/td[7]/nobr"
		#xpath_allot_state = "//div[@id='page-0']/div[1]/table[@class='dojoxGrid-row-table']/tbody/tr/td[8]/nobr"
		print(self.browser.find_element_by_xpath(xpath_allot_number).text)
		xpath_part1="//div[@id='page-0']/div["
		xpath_part2="]/table[@class='dojoxGrid-row-table']/tbody/tr/td["
		xpath_part3="]/nobr"
		xpath_part3div= "]/nobr/div"
		
		current_date=time.strftime('%Y-%m-%d',time.localtime(time.time()))
		#查找page-0 中10项，等于当前日期的项
		i = 1
		#list save allot date items which date equals current date  ,such as list=[1,2]
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
		#join list1 
		for i in list:
			text = self.browser.find_element_by_xpath(xpath_part1+str(i)+xpath_part2+'1'+xpath_part3div).text
			self.list1 = self.list1+[[text]]
		for i in list:
			for j in range(2,4):
				text=self.browser.find_element_by_xpath(xpath_part1+str(i)+xpath_part2+str(j)+xpath_part3).text
				self.list1[i-1]=self.list1[i-1]+[text]
				
		print(self.list1)
		
		########### join list2
		#for i in list:
		#	for j in range(5,8):
		#		text=self.browser.find_element_by_xpath(xpath_part1+i+xpath_part2+j+xpath_part3).text
		#		list[i-1]=list[i-1]+[text]
		for i in list:
			time.sleep(3)
			self.get_order(i-1)
			# click backbtn
			self.browser.find_element_by_id('backBtn').click()
			
		# back to root frame
		print(self.allot_data_list)
		self.browser.switch_to.parent_frame()
		with open('./csv/allotdata.csv','w') as f:
			f_csv = csv.writer(f)
			f_csv.writerows(self.allot_data_list)
		
		
	def get_order(self,order_num):
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
		
		
		# get total game num
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
		# add game code
		i = 1
		while i <= game_count:
			xpath_game_code=xpath_info_part1+str(i)+xpath_info_part2+'1'+xpath_info_part3div
			self.list2=self.list2+[[self.browser.find_element_by_xpath(xpath_game_code).text]]
			i=i+1
		
		print(self.list2)
		# add game info
		i=1
		while i<=game_count:
			for j in range(2,8):
				xpath_game=xpath_info_part1+str(i)+xpath_info_part2+str(j)+xpath_info_part3
				text=self.browser.find_element_by_xpath(xpath_info_part1+str(i)+xpath_info_part2+str(j)+xpath_info_part3).text
				self.list2[i-1]+=[text]
			i=i+1
		
		print(self.list2)
		# get first order list,put list info into list2
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
	#Crawler.get_JX201()
	#Crawler.get_B402()
	#Crawler.get_A205()
	#Crawler.get_Q102()
	Crawler.get_AllotData()


