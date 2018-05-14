'''启动360浏览器'''
# -*- coding: UTF-8 -*-
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchFrameException
# from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
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
		# self.browser.find_element_by_xpath("/frame[@name='topFrame']/html/body/div[@id='top']/div[@class='topgb']/div[@class='navmenu']/ul[@id='nav']/li[@id='31000000']/a").click
		# jikaiyewu = "/html/frameset[@id='mainFrameset']/frame[@id='topFrame']/html/body/div[@id='top']/div[@class='topbg']/div[@class='navmenu']/ul[@id='nav']/li[@id='31000000']/a"
		

		# jikaiyewu = "/html/body/div[@id='top']/div[@class='topbg']/div[@class='navmenu']/ul[@id='nav']/li[@id='31000000']/a"
		# JIKAI = self.browser.find_element_by_xpath(jikaiyewu)
		# actions.move_to_element(JIKAI)
		# actions.double_click(JIKAI)
		# actions.perform()
		time.sleep(10)

		js = "if('31000000'=='55999999'){window.location.href = '/ump/system/toELPSystem.action'}else{if(top.checkUmpBlock()){clearBack();switchModule('31000000','即开业务', 'ilms', '10');}else{return false;}}"

		self.browser.execute_script(js)

		# self.browser.find_element_by_id("31000000").click()
		time.sleep(1)
		#定位报表管理
		#self.browser.find_element_by_id("31140000").click
		time.sleep(1)
		#定位ZAFFIL报表WEB展现

		#self.browser.find_element_by_xpath("/frame#leftFrame/html/body.imgbody/div.menubox/div.lnavbg1/a").click 	
		
		time.sleep(10)
		#定位JX201



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


