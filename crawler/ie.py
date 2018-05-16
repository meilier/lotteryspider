'''启动360浏览器'''
# -*- coding: UTF-8 -*-
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchFrameException
# from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
import os

class StartCrawler(object):

	def __init__(self):
		pass
		
	def TODO(self):
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
		pass

	def get_DiaoBoDan(self):
		pass






if __name__ =="__main__":
	Crawler = StartCrawler()
	Crawler.start_drive()
	Crawler.TODO()
	Crawler.instant_business()
	#Crawler.get_JX201()
	#Crawler.get_B402()
	Crawler.get_A205()


