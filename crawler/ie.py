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

		time.sleep(20)

	def get_JX201(self):
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



		i = 0
		while True:
			try:
				self.browser.switch_to.frame("topFrame")
			except NoSuchFrameException:
				time.sleep(1) 
				print(str(i))
				i = i +1
			else:
				print("Find this topFrame")
				break


		#定位即开业务‘
		time.sleep(2)
		js_JiKai = "if('31000000'=='55999999'){window.location.href = '/ump/system/toELPSystem.action'}else{if(top.checkUmpBlock()){clearBack();switchModule('31000000','即开业务', 'ilms', '10');}else{return false;}}"
		self.browser.execute_script(js_JiKai)
		time.sleep(1)

		#定位报表管理
		js_BaoBiaoGuanLi = "if(top.checkUmpBlock()){clearBack();switchModule('31140000','报表管理', 'ilms', '20');}else{return false;}"
		# js_BaoBiaoGuanLi ='{clearBack();switchModule('31140000','报表管理', 'ilms', '20')}'
		self.browser.execute_script(js_BaoBiaoGuanLi)
		time.sleep(1)



		#定位ZAFFIL报表WEB展现
		# js_ZAFIL = "if(top.checkUmpBlock()){clearBack();clickSubMenu('报表管理','',this.innerHTML);}else{return false}"
		# self.browser.execute_script(js_ZAFIL)

		#self.browser.find_element_by_xpath("/frame#leftFrame/html/body.imgbody/div.menubox/div.lnavbg1/a").click 	

		self.browser.switch_to.parent_frame()

		i = 0
		while True:
			try:
				self.browser.switch_to.frame("leftFrame")
			except NoSuchFrameException:
				time.sleep(1) 
				print(str(i))
				i = i +1
			else:
				print("Find this leftFrame")
				break

		time.sleep(5)

		Xpath_ZAFFIL = "/html/body[@class='imgbody']/div[@class='leftbox']/div[@class='menubox']/div[@class='lnavbg1']/a[@menuId='31140900']"
		# self.browser.find_element_by_xpath(Xpath_ZAFFIL).click()
		self.browser.find_element_by_xpath(Xpath_ZAFFIL).send_keys(Keys.ENTER)
		# self.browser.execute_script( self.browser.find_element_by_xpath(Xpath_ZAFFIL).style  )

		print("Finish ZAFFIL")

		time.sleep(5)
		#定位JX201
		Xpath_JX201 = "/html/body[@class='imgbody']/div[@class='leftbox']/div[@class='menubox']/ul[@id='content8']/li[@sizset='76']/a[@menuId='31140915']"
		self.browser.find_element_by_xpath(Xpath_JX201).click()
		print("Finish find JX201")
		self.browser.switch_to.parent_frame()




		i = 0
		while True:
			try:
				self.browser.switch_to.frame("mainFrame")
			except NoSuchFrameException:
				time.sleep(1) 
				print(str(i))
				i = i +1
			else:
				print("Find this mainFrame")
				break
		#查询
		time.sleep(5)
		js_Query = "queryRecord()"
		self.browser.execute_script(js_Query)

		time.sleep(10)


		self.browser.switch_to.frame("report")
		# js_DownLoadJX201 = "javascript:resultOut('csv',resultForm)"
		# self.browser.execute_script(js_DownLoadJX201)
		Xpath_JX201_csv = "/html[@class='dj_ie dj_ie7 dj_contentbox']/body[@class='unieap']/form[@name='resultForm']/div[@id='exportBar']/ul/li[@id='csvTag']/img[@id='csv']"
		self.browser.find_element_by_xpath(Xpath_JX201_csv).click()
		js_DownLoadJX201 = "javascript:resultOut('csv',resultForm)"
		self.browser.execute_script(js_DownLoadJX201)
		time.sleep(2)
		# Alert(self.browser).accept()
		os.system("click_save.exe")

		time.sleep(3)


		pass

	def get_B402(self):
		pass

	def get_A205(self):
		pass

	def get_DiaoBoDan(self):
		pass






if __name__ =="__main__":
	Crawler = StartCrawler()
	Crawler.start_drive()
	Crawler.get_JX201()


