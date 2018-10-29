# -*- coding: UTF-8 -*-
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import crawler_util
from selenium.common.exceptions import NoSuchFrameException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import JavascriptException
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
# from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
import os
import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import re


class StartCrawler(object):


    def __init__(self):

        #爬取时间
        #begin_date = '' 
        # 列表1：调拨单号	发货仓库	收货仓库
        # 列表2 ：游戏编码	游戏名称 调拨箱数	调拨散包数	调拨总包数 游戏面值 调拨总金额
        self.list1=[]
        self.list2=[]
        # 最终的地市调拨数据拼接列表
        self.allot_data_list=[]

        self.ToDo()


    def ToDo(self):
        print("We are starting to crawler data.")

    def log_in(self):
        """
		自动登录模块
		"""
		#打开浏览器
        self.browser = webdriver.Ie(capabilities={ 'ignoreZoomSetting':True})
        self.browser.implicitly_wait(15)
        self.browser.maximize_window()  #最大化窗口
        self.browser.get('https://3.13.1.10/loginnew.html') #打开登录界面
        #输入PIN码
        pin_code= self.browser.find_element_by_name("pinCode")
        pin_code.clear()
        pin_code.send_keys("11111111")  # 默认PIN码
        #点击登录按钮
        login_button = self.browser.find_element_by_xpath("/html/body/form/div/table/tbody/tr[2]/td/table[2]/tbody/tr/td/input[1]").click()
        self.browser.maximize_window()  #最大化窗口

    def get_download_page(self):
        """
        定位到下载页
        """
        current_handle = self.browser.current_window_handle
        if self.browser.current_url == "https://3.13.1.20/ump/index.html":
            print("Focus into download page")
            flag = True
            return flag

        for handler in self.browser.window_handles:
            print(len(self.browser.window_handles)) #当前handle个数
            #切换handle
            self.browser.switch_to_window(handler)
            if len(self.browser.current_url) < 4: #没有URL
                self.browser.close()
                continue
            url = self.browser.current_url  #得到当前URL
            # print(str(url))
            if str(url) == "https://3.13.1.20/ump/index.html":
                print("Focus into download page")
                flag = True
                break
            else:
                self.browser.close()
                print("Not download page close")
                flag = False
                continue
        return flag
    
    def instant_business(self):
        """
        点击即开业务进入二代系统
        """
        #focus on topFrame
        self.switch_which_frame("topFrame")
        #定位即开业务‘
        time.sleep(3)
        js_JiKai = "if('31000000'=='55999999'){window.location.href = '/ump/system/toELPSystem.action'}else{if(top.checkUmpBlock()){clearBack();switchModule('31000000','即开业务', 'ilms', '10');}else{return false;}}"
        self.browser.execute_script(js_JiKai)
        # back to root frame
        self.browser.switch_to.parent_frame()

    def statement_management(self):
        """
        点击报表管理
        """
        #定位报表管理
        self.switch_which_frame("topFrame")
        time.sleep(2)
        js_BaoBiaoGuanLi = "if(top.checkUmpBlock()){clearBack();switchModule('31140000','报表管理', 'ilms', '20');}else{return false;}"
        self.browser.execute_script(js_BaoBiaoGuanLi)
        time.sleep(2)
        self.browser.switch_to.parent_frame()

    def switch_which_frame(self, frame_name):
        """
        切换Frame
        """
        i = 0
        while True:
            try:
                # self.browser.switch_to.frame(frame_name)
                WebDriverWait(self.browser,15).until(EC.frame_to_be_available_and_switch_to_it(frame_name))
            except TimeoutException:
                time.sleep(1) 
                print(str(i))
                i = i +1
                if i >3:
                    raise TimeoutException
            else:
                print("Find this "+frame_name)
                break


    def get_B402(self):
        """
		下载B_402报表到共享文件夹/csv 文件目录中
		"""
        self.autoit_ontop()

        # 1. 点击销售兑奖 get in left frame for sales and claiming
        self.switch_which_frame("leftFrame")

        xpath_sales = "/html/body[@class='imgbody']/div[@class='leftbox']/div[@class='menubox']/div[@class='lnavbg1']/a[@menuId='31140500']"
        self.browser.find_element_by_xpath(xpath_sales).send_keys(Keys.ENTER)
        print("Finish get sales and claiming")

        # 2. 定位B402报表locating B402
        Xpath_B402 = "/html/body[@class='imgbody']/div[@class='leftbox']/div[@class='menubox']/ul[@id='content3']/li[@sizset='28']/a[@menuId='31140505']"
        # self.browser.find_element_by_xpath(Xpath_B402).click()
        # self.browser.find_element_by_xpath(Xpath_B402).double_click()

        WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.XPATH, Xpath_B402)))
        # click_B402.click()
        time.sleep(2)
        self.browser.find_element_by_xpath(Xpath_B402).click()
        # self.autoit_ontop()
        
        print("Finish find B402")
        time.sleep(5)   #可能会下B001D
        self.browser.switch_to.parent_frame()

        # 3. 查询
        # switch to mainFrame
        self.switch_which_frame("mainFrame")
        time.sleep(5)
        js_Query = "queryRecord()"
        self.browser.execute_script(js_Query)
        time.sleep(5)

        # 4. 下载文件download B402 csv file
        download_result = self.download_file("B402")

        #back to main frame
        self.browser.switch_to.parent_frame()
        #back to root
        self.browser.switch_to.parent_frame()

        return download_result

    
    def get_JX_201(self):
        """
		下载JX_201报表到共享文件夹/csv 文件目录中
		"""
        self.autoit_ontop() #网页放在最前面

		#1. 定位ZAFFIL报表WEB展现
        self.switch_which_frame("leftFrame")
        Xpath_ZAFFIL = "/html/body[@class='imgbody']/div[@class='leftbox']/div[@class='menubox']/div[@class='lnavbg1']/a[@menuId='31140900']"
        self.browser.find_element_by_xpath(Xpath_ZAFFIL).send_keys(Keys.ENTER)
        print("Finish ZAFFIL")

        #2. 定位JX201
        Xpath_JX201 = "/html/body[@class='imgbody']/div[@class='leftbox']/div[@class='menubox']/ul[@id='content5']/li[@sizset='47']/a[@menuId='31140915']"
        WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.XPATH,Xpath_JX201)))
        self.browser.find_element_by_xpath(Xpath_JX201).click()
        print("Finish find JX201")
        self.browser.switch_to.parent_frame()

        #3. 查询
        # switch to mainFrame

        self.switch_which_frame("mainFrame")
        time.sleep(5)
        js_Query = "queryRecord()"
        self.browser.execute_script(js_Query)
        time.sleep(5)

        # 4. 下载文件 jx201 csv file

        download_result = self.download_file("JX201")

        #back to main frame
        self.browser.switch_to.parent_frame()
        #back to root
        self.browser.switch_to.parent_frame()

        return download_result


    def get_A205(self):
        """
		下载A_205报表到共享文件夹/csv 文件目录中
		"""

        print("Start getting A205")
        self.autoit_ontop() #网页放在最前面
		
        # 1. 点击库存 get in left frame for inventory
        self.switch_which_frame("leftFrame")

        xpath_sales = "/html/body[@class='imgbody']/div[@class='leftbox']/div[@class='menubox']/div[@class='lnavbg1']/a[@menuId='31140300']"
        self.browser.find_element_by_xpath(xpath_sales).send_keys(Keys.ENTER)
        print("Finish get inventory")

        # 2. 定位A205 报表 locating A205
        Xpath_A205 = "/html/body[@class='imgbody']/div[@class='leftbox']/div[@class='menubox']/ul[@id='content2']/li[@sizset='10']/a[@menuId='31140305']"
        WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.XPATH,Xpath_A205)))
        self.browser.find_element_by_xpath(Xpath_A205).click()
        print("Finish find A205")
        self.browser.switch_to.parent_frame()

        # 3. 查询
        # switch to mainFrame
        self.switch_which_frame("mainFrame")
        # chose storehouse

        Xpath_A205_lookup = "/html/body/div[3]/div/form/table/tbody/tr/td[4]/table/tbody/tr/td[2]/div/div[@class='u-lookupIcon']"
        WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.XPATH,Xpath_A205_lookup)))
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
                if i > 3:
                    raise NoSuchFrameException
            else:
                print("Find this iframe")
                break

        # 点击查找仓库 small button
        name_A205_small = "singledataGrid"
        WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.NAME,name_A205_small)))
        self.browser.find_element_by_name(name_A205_small).click()

        # back to mainFrame , move to confirm frame
        WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.ID,"confirmBtn_label")))
        self.browser.find_element_by_id('confirmBtn_label').click()
        print("click confirm key")

        # 再次从最基础切换到mainframe中back to mainFrame is already closed? I can not know where i am ,so i switch to deauflt
        self.browser.switch_to.default_content()
        self.switch_which_frame("mainFrame")
        #self.browser.switch_to.parent_frame()
        # 修改日期
        yday = crawler_util.get_yesterday()
        #yday ="2018-07-04"
        print(str(yday))

        #self.browser.find_element_by_id('DATE').__setattr__("value",yday)
        input_date = self.browser.find_element_by_id('DATE')
        self.browser.execute_script("arguments[0].setAttribute('value', arguments[1])", input_date, yday)

        A205_search_date = self.browser.find_element_by_id('DATE').get_property("value")
        print(str(A205_search_date))
        self.browser.find_element_by_id('DATE').send_keys(Keys.ENTER)
        # A205_calender_path = "//td[@id='td1']/div/div[2]"
        # self.browser.find_element_by_xpath(A205_calender_path).send_keys("2018-07-04")

        # 查询
        time.sleep(5)
        js_Query = "queryRecord()"
        self.browser.execute_script(js_Query)
        time.sleep(3)
        # 4. 下载文件A205
        download_result = self.download_file("A205")

        #back to main frame
        self.browser.switch_to.parent_frame()
        #back to root
        self.browser.switch_to.parent_frame()

        return download_result


    def get_Q102(self):
        self.get_Q102_store()
        self.get_Q102_sr()
        self.get_Q102_center()
        self.get_Q102_cclient()

    def get_Q102_store(self):

        print("Start getting Q102 store")
        self.autoit_ontop() #网页放在最前面

        # 1.点击查询报表 get in left frame for quering report 
        self.switch_which_frame("leftFrame")

        xpath_query = "/html/body[@class='imgbody']/div[@class='leftbox']/div[@class='menubox']/div[@class='lnavbg1']/a[@menuId='31141000']"
        self.browser.find_element_by_xpath(xpath_query).send_keys(Keys.ENTER)
        print("Finish get statement query")

        # 2. 点击Q102报表  locating Q102
        Xpath_Q102 = "/html/body[@class='imgbody']/div[@class='leftbox']/div[@class='menubox']/ul[@id='content6']/li[@sizset='55']/a[@menuId='31141002']"
        WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.XPATH,Xpath_Q102)))
        self.browser.find_element_by_xpath(Xpath_Q102).click()
        print("Finish find Q102")
        self.browser.switch_to.parent_frame()

        # 3. 查询
        # switch to mainFrame
        self.switch_which_frame("mainFrame")

        # 3.1 门店数据click store 
        WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.ID,"awardType2")))
        self.browser.find_element_by_id('awardType2').click()
        # time.sleep(2)
        # click query
        time.sleep(5)
        js_Query = "queryRecord()"
        self.browser.execute_script(js_Query)
        time.sleep(5)

        # .4 下载Q102 报表 门店数据 download Q102 csv file

        download_result = self.download_file("Q102_STORE")

        #back to main frame
        self.browser.switch_to.default_content()
        #back to root frame
        self.browser.switch_to.parent_frame()

        return download_result

    def get_Q102_sr(self):

        print("Start getting Q102 sr")
        self.autoit_ontop() #网页放在最前面

        # 1.点击查询报表 get in left frame for quering report 
        self.switch_which_frame("leftFrame")
        xpath_query = "/html/body[@class='imgbody']/div[@class='leftbox']/div[@class='menubox']/div[@class='lnavbg1']/a[@menuId='31141000']"
        self.browser.find_element_by_xpath(xpath_query).send_keys(Keys.ENTER)
        print("Finish get statement query")

        # 2. 点击Q102报表  locating Q102
        Xpath_Q102 = "/html/body[@class='imgbody']/div[@class='leftbox']/div[@class='menubox']/ul[@id='content6']/li[@sizset='55']/a[@menuId='31141002']"
        WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.XPATH,Xpath_Q102)))
        self.browser.find_element_by_xpath(Xpath_Q102).click()
        print("Finish find Q102")
        self.browser.switch_to.parent_frame()

        # 3. 查询
        # switch to mainFrame
        self.switch_which_frame("mainFrame")

        # 3.1 门店数据click store 
        WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.ID,"awardType3")))
        self.browser.find_element_by_id('awardType3').click()
        # time.sleep(2)
        # click query
        time.sleep(5)
        js_Query = "queryRecord()"
        self.browser.execute_script(js_Query)
        time.sleep(5)

        # .4 下载Q102 报表 门店数据 download Q102 csv file

        download_result = self.download_file("Q102_SR")

        #back to main frame
        self.browser.switch_to.default_content()
        #back to root frame
        self.browser.switch_to.parent_frame()

        return download_result

    def get_Q102_center(self):

        print("Start getting Q102 center")
        self.autoit_ontop() #网页放在最前面

        # 1.点击查询报表 get in left frame for quering report 
        self.switch_which_frame("leftFrame")
        xpath_query = "/html/body[@class='imgbody']/div[@class='leftbox']/div[@class='menubox']/div[@class='lnavbg1']/a[@menuId='31141000']"
        self.browser.find_element_by_xpath(xpath_query).send_keys(Keys.ENTER)
        print("Finish get statement query")

        # 2. 点击Q102报表  locating Q102
        Xpath_Q102 = "/html/body[@class='imgbody']/div[@class='leftbox']/div[@class='menubox']/ul[@id='content6']/li[@sizset='55']/a[@menuId='31141002']"
        WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.XPATH,Xpath_Q102)))
        self.browser.find_element_by_xpath(Xpath_Q102).click()
        print("Finish find Q102")
        self.browser.switch_to.parent_frame()

        # 3. 查询
        # switch to mainFrame
        self.switch_which_frame("mainFrame")

        # 3.1 门店数据click store 
        WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.ID,"awardType4")))
        self.browser.find_element_by_id('awardType4').click()
        # time.sleep(2)
        # click query
        time.sleep(5)
        js_Query = "queryRecord()"
        self.browser.execute_script(js_Query)
        time.sleep(5)

        # .4 下载Q102 报表 门店数据 download Q102 csv file

        download_result = self.download_file("Q102_CENTER")

        #back to main frame
        self.browser.switch_to.default_content()
        #back to root frame
        self.browser.switch_to.parent_frame()

        return download_result

    def get_Q102_cclient(self):

        print("Start getting Q102 c client")
        self.autoit_ontop() #网页放在最前面

        # 1.点击查询报表 get in left frame for quering report 
        self.switch_which_frame("leftFrame")
        xpath_query = "/html/body[@class='imgbody']/div[@class='leftbox']/div[@class='menubox']/div[@class='lnavbg1']/a[@menuId='31141000']"
        self.browser.find_element_by_xpath(xpath_query).send_keys(Keys.ENTER)
        print("Finish get statement query")

        # 2. 点击Q102报表  locating Q102
        Xpath_Q102 = "/html/body[@class='imgbody']/div[@class='leftbox']/div[@class='menubox']/ul[@id='content6']/li[@sizset='55']/a[@menuId='31141002']"
        WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.XPATH,Xpath_Q102)))
        self.browser.find_element_by_xpath(Xpath_Q102).click()
        print("Finish find Q102")
        self.browser.switch_to.parent_frame()

        # 3. 查询
        # switch to mainFrame
        self.switch_which_frame("mainFrame")

        # 3.1 门店数据click store 
        WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.ID,"awardType5")))
        self.browser.find_element_by_id('awardType5').click()
        # time.sleep(2)
        # click query
        time.sleep(5)
        js_Query = "queryRecord()"
        self.browser.execute_script(js_Query)
        time.sleep(5)

        # .4 下载Q102 报表 门店数据 download Q102 csv file

        download_result = self.download_file("Q102_CCLIENT")

        #back to main frame
        self.browser.switch_to.default_content()
        #back to root frame
        self.browser.switch_to.parent_frame()

        return download_result

    def get_AllotData(self):
        """
        拼接地市调拨数据
        """
        print("Start getting AllotData")
        self.autoit_ontop() #网页放在最前面

        #focus on topFrame
        self.switch_which_frame("topFrame")
                
        #点击调拨管理 locate allot management
        time.sleep(3)
        allot_management = "if(top.checkUmpBlock()){clearBack();switchModule('31030000','调拨管理', 'ilms', '20');}else{return false;}"
        self.browser.execute_script(allot_management)
        time.sleep(3)

        # back to root frame
        self.browser.switch_to.parent_frame()
        
        
        # normal allot
        # 1. 点击普通调拨get in left frame for normal allot data
        self.switch_which_frame("leftFrame")
        
        xpath_normal = "/html/body[@class='imgbody']/div[@class='leftbox']/div[@class='menubox']/div[@class='lnavbg1']/a[@menuId='31030200']"
        self.browser.find_element_by_xpath(xpath_normal).send_keys(Keys.ENTER)
        print("Finish get normal allot")
        
        # 2. 点击调拨单查询 locating allot order query
        Xpath_allot_data = "/html/body[@class='imgbody']/div[@class='leftbox']/div[@class='menubox']/ul[@id='content2']/li[@sizset='5']/a[@menuId='31030205']"
        WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.XPATH,Xpath_allot_data)))
        self.browser.find_element_by_xpath(Xpath_allot_data).click()
        print("Finish find allot order query")
        self.browser.switch_to.parent_frame()
        
        

        # 根据情况重新设计：ID，调拨单号	发货仓库	收货仓库	游戏编码	游戏名称 调拨箱数	调拨散包数	调拨总包数 游戏面值 调拨总金额 创建日期
        
        # 获取当前日期
        # 重新设计
        # 列表1：调拨单号	发货仓库	收货仓库
        # 列表2 ：游戏编码	游戏名称 调拨箱数	调拨散包数	调拨总包数 游戏面值 调拨总金额
        # 数据拼接格式： 列表1+列表2+日期
        # switch to mainFrame
        self.switch_which_frame("mainFrame")
        
        # waiting for details arise
        time.sleep(8)
        # 修改日期
        # yday = crawler_util.get_yesterday()
        yday ="2018-10-22"
        print(str(yday))

        #self.browser.find_element_by_id('DATE').__setattr__("value",yday)
        input_date = self.browser.find_element_by_id('ama_CREATED_DATE_B')
        self.browser.execute_script("arguments[0].setAttribute('value', arguments[1])", input_date, yday)

        A205_search_date = self.browser.find_element_by_id('ama_CREATED_DATE_B').get_property("value")
        print(str(A205_search_date))
        self.browser.find_element_by_id('ama_CREATED_DATE_B').send_keys(Keys.ENTER)

        input_date = self.browser.find_element_by_id('ama_CREATED_DATE_D')
        self.browser.execute_script("arguments[0].setAttribute('value', arguments[1])", input_date, yday)

        A205_search_date = self.browser.find_element_by_id('ama_CREATED_DATE_D').get_property("value")
        print(str(A205_search_date))
        self.browser.find_element_by_id('ama_CREATED_DATE_D').send_keys(Keys.ENTER)
        

        # 查询
        time.sleep(5)
        js_Query = "queryRecord()"
        self.browser.execute_script(js_Query)
        time.sleep(3)

        #set items per page 
        self.browser.find_element_by_xpath("//div[@id='navigate']/table/tbody/tr[1]/td/table/tbody/tr/td[2]/table/tbody/tr/td[2]/select/option[10]").click()


        # for test
        self.browser.find_element_by_id('navigategotoPageNO').click()
        self.browser.find_elements_by_xpath("//div[@id='navigate']/table/tbody/tr[1]/td/table/tbody/tr/td[3]/a[3]")
        xpath_create_date = "//div[@id='page-" + str(0) + "']/div[" + str(
            1) + "]/table[@class='dojoxGrid-row-table']/tbody/tr/td[4]/nobr"
        print("aaa" + xpath_create_date)
        create_date_test = self.browser.find_element_by_xpath(xpath_create_date).text
        print("aaa" + create_date_test)
        xpath_create_date = "//div[@id='page-" + str(1) + "']/div[" + str(
            1) + "]/table[@class='dojoxGrid-row-table']/tbody/tr/td[4]/nobr"
        print(xpath_create_date)
        create_date_test1 = self.browser.find_element_by_xpath(xpath_create_date).text
        print("bbb" + create_date_test1)
        exit(0)


        # big loop for all pages
        for page_num in range(10):
            if page_num != 1:
                continue
            # 采用相对定位
            #xpath_allot_number = "//div[@id='page-0']/div[1]/table[@class='dojoxGrid-row-table']/tbody/tr/td[1]/nobr/div"
            #print(self.browser.find_element_by_xpath(xpath_allot_number).text)

            # 拼接元素查找路径
            xpath_part1="//div[@id='page-"
            xpath_part1_extra = "']/div["
            xpath_part2="]/table[@class='dojoxGrid-row-table']/tbody/tr/td["
            xpath_part3="]/nobr"
            xpath_part3div= "]/nobr/div"

            #current_date=time.strftime('%Y-%m-%d',time.localtime(time.time()))
            #allot_yesterday = crawler_util.get_yesterday()
            allot_yesterday = yday

            self.browser.switch_to.default_content()
            self.switch_which_frame("mainFrame")

            #查找page-0 中30项，等于当前日期的项
            i = 1
            #保存当前日志调拨单的数量 list save allot date items which date equals current date  ,such as crawl_list=[1,2]
            crawl_list = []
            while i <= 30:
                print("i is " + str(i))
                xpath_create_date = "//div[@id='page-" + str(0) + "']/div["+str(i)+"]/table[@class='dojoxGrid-row-table']/tbody/tr/td[4]/nobr"
                print("aaa"+xpath_create_date)
                create_date_test = self.browser.find_element_by_xpath(xpath_create_date).text
                print("aaa"+create_date_test)
                xpath_create_date = "//div[@id='page-" + str(page_num) + "']/div["+str(i)+"]/table[@class='dojoxGrid-row-table']/tbody/tr/td[4]/nobr"
                print(xpath_create_date)
                try:
                    create_date = self.browser.find_element_by_xpath(xpath_create_date).text
                except NoSuchElementException:
                    break
                print(create_date)
                if(allot_yesterday ==  create_date):
                    crawl_list = crawl_list + [i]
                    i = i + 1
                else:
                    break
            print("the list is " + str(crawl_list))

            # one problem is that when should we turn to the next page ?

            #拼接list1：join list1
            for i in crawl_list:
                text = self.browser.find_element_by_xpath(xpath_part1+str(page_num)+xpath_part1_extra+str(i)+xpath_part2+'1'+xpath_part3div).text
                self.list1 = self.list1+[[text]]
            for i in crawl_list:
                for j in range(2,4):
                    text=self.browser.find_element_by_xpath(xpath_part1+str(page_num)+xpath_part1_extra+str(i)+xpath_part2+str(j)+xpath_part3).text
                    self.list1[i-1]=self.list1[i-1]+[text]

            print(self.list1)

            #join list2

            for i in crawl_list:
                self.get_order(i-1,page_num)
                # click backbtn
                WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.ID,"backBtn")))
                self.browser.find_element_by_id('backBtn').click()
                self.browser.switch_to.default_content()
                self.switch_which_frame("mainFrame")
                self.browser.find_element_by_xpath(
                    "//div[@id='navigate']/table/tbody/tr[1]/td/table/tbody/tr/td[2]/table/tbody/tr/td[2]/select/option[10]").click()
            
        # back to root frame
        print(self.allot_data_list)
        self.browser.switch_to.parent_frame()

        # 将得到的拼接数据写入到csv文件中

        wd = os.getcwd()
        parent_path = os.path.dirname(wd)
        wdcsv = parent_path +'\\csv\\'
        
        allot_file_path = os.path.join(wdcsv,"ALLOTDATA.csv")
        with open(allot_file_path,'w',newline='') as f:
            f_csv = csv.writer(f)
            f_csv.writerows(self.allot_data_list)
        return True
        # self.already_download_list['ALLOTDATA'] = True
				
    def get_order(self,order_num,page_num):
        """
        获取每个具体调拨单的数据
        """
        # execute js,move to first order info
        time.sleep(3)
        allot_code = "viewARecord("+str(order_num)+",\"ama_ALLOCATE_CODE\")"
        self.browser.execute_script(allot_code)
        time.sleep(3)
        self.list2=[]
        #join list2
        xpath_info_part1="//div[@id='page-"
        xpath_info_part1_extra="']/div["
        xpath_info_part2="]/table[@class='dojoxGrid-row-table']/tbody/tr/td["
        xpath_info_part3= "]"
        xpath_info_part3div= "]/div"
		
		
        # 获取游戏的数量 get total game num
        i=1
        game_count = 0
        while True:
            try:
                xpath_game_code=xpath_info_part1+str(page_num)+xpath_info_part1_extra+str(i)+xpath_info_part2+'1'+xpath_info_part3div
                print(self.browser.find_element_by_xpath(xpath_game_code).text)
                game_count = game_count+1
                i=i+1
            except NoSuchElementException:
                break
		
        print(game_count)
        # 添加游戏编号add game code
        i = 1
        while i <= game_count:
            xpath_game_code=xpath_info_part1+str(page_num)+xpath_info_part1_extra+str(i)+xpath_info_part2+'1'+xpath_info_part3div
            self.list2=self.list2+[[self.browser.find_element_by_xpath(xpath_game_code).text]]
            i=i+1

        print(self.list2)
        # 添加游戏其他信息 add game info
        i=1
        while i<=game_count:
            for j in range(2,8):
                xpath_game=xpath_info_part1+str(page_num)+xpath_info_part1_extra+str(i)+xpath_info_part2+str(j)+xpath_info_part3
                text=self.browser.find_element_by_xpath(xpath_info_part1+str(page_num)+xpath_info_part1_extra+str(i)+xpath_info_part2+str(j)+xpath_info_part3).text
                self.list2[i-1]+=[text]
            i=i+1
		
        print(self.list2)
        # 拼接list2 get first order list,put list info into list2
        # current_date=time.strftime('%Y-%m-%d',time.localtime(time.time()))
        yesterday = crawler_util.get_yesterday()
        i=1
        while i<=game_count:
            self.allot_data_list+=[self.list1[order_num]+self.list2[i-1]+[yesterday]]
            i=i+1


    def get_begin_date(self):
        count = 0
        for count in range(1,3): 

            begin_date = self.get_begin_date_B402()
            if len(begin_date) > 2:
                # begin_date = self.get_begin_date_B402()
                print("The B402 date is:" + str(begin_date))
                break
            # JX201_date = self.get_begin_date_JX201()
            # if len(JX201_date) > 2:
            #     begin_date = self.get_begin_date_JX201()
            #     print("The JX201 date is:" + str(begin_date))
            #     break

            else:
                begin_date = self.get_begin_date_JX201()
                if len(begin_date) > 2:
                    # begin_date = self.get_begin_date_JX201()
                    print("The JX201 date is:" + str(begin_date))
                    break
                # B402_date = self.get_begin_date_B402()
                # if len(B402_date) > 2:
                #     begin_date = self.get_begin_date_B402()
                #     print("The B402 date is:" + str(begin_date))
                #     break
                else:
                    print("Can not find begine date " + str(count) + " times." )
        return begin_date


    def get_begin_date_B402(self):

        self.autoit_close_all_ie() #关闭所有IE网页
        self.log_in() #登录
        self.autoit_close() # 关闭多于页
        self.get_download_page() #进入下载页
        self.instant_business() #进入二代系统
        self.statement_management() #进入报表管理

        self.autoit_ontop() #当前页置最前

        # 1. 点击销售兑奖 get in left frame for sales and claiming
        self.switch_which_frame("leftFrame")

        xpath_sales = "/html/body[@class='imgbody']/div[@class='leftbox']/div[@class='menubox']/div[@class='lnavbg1']/a[@menuId='31140500']"
        self.browser.find_element_by_xpath(xpath_sales).send_keys(Keys.ENTER)
        print("Finish get sales and claiming")

        # 2. 定位B402报表locating B402
        Xpath_B402 = "/html/body[@class='imgbody']/div[@class='leftbox']/div[@class='menubox']/ul[@id='content3']/li[@sizset='28']/a[@menuId='31140505']"
        WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.XPATH, Xpath_B402)))

        self.browser.find_element_by_xpath(Xpath_B402).click()
        print("Finish find B402")
        time.sleep(5)   #可能会下B001D
        self.browser.switch_to.parent_frame()

        # 3. switch to mainFrame
        self.switch_which_frame("mainFrame")
        time.sleep(5)

        #4. 得到时间
        elem = self.browser.find_element_by_id("DATE")
        begine_date = elem.get_attribute("value")

        return begine_date   


    def get_begin_date_JX201(self):

        self.autoit_close_all_ie() #关闭所有IE网页
        self.log_in() #登录
        self.autoit_close() # 关闭多于页
        self.get_download_page() #进入下载页
        self.instant_business() #进入二代系统
        self.statement_management() #进入报表管理

        self.autoit_ontop() #网页放在最前面

		#1. 定位ZAFFIL报表WEB展现
        self.switch_which_frame("leftFrame")
        Xpath_ZAFFIL = "/html/body[@class='imgbody']/div[@class='leftbox']/div[@class='menubox']/div[@class='lnavbg1']/a[@menuId='31140900']"
        self.browser.find_element_by_xpath(Xpath_ZAFFIL).send_keys(Keys.ENTER)
        print("Finish ZAFFIL")

        #2. 定位JX201
        Xpath_JX201 = "/html/body[@class='imgbody']/div[@class='leftbox']/div[@class='menubox']/ul[@id='content8']/li[@sizset='76']/a[@menuId='31140915']"
        WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.XPATH,Xpath_JX201)))
        self.browser.find_element_by_xpath(Xpath_JX201).click()
        print("Finish find JX201")
        self.browser.switch_to.parent_frame()

        # switch to mainFrame
        self.switch_which_frame("mainFrame")
		#4. 得到时间
        elem = self.browser.find_element_by_id("BEGIN_DATE")
        begine_date = elem.get_attribute("value")

        return begine_date
	
	
    def get_BigCustomerData(self):
        """
        下载基础数据-大客户数据
        """
        print("Start getting BigCustomer")
        self.autoit_ontop()
		
        self.switch_which_frame("topFrame")
        time.sleep(3)
        
        #点击基础数据
        bigCustomer_management="if(top.checkUmpBlock()){clearBack();switchModule('31120000','基础数据', 'ilms', '20');}else{return false;}"
        self.browser.execute_script(bigCustomer_management)
        time.sleep(3)

        self.browser.switch_to.parent_frame()

        # 1. 点击渠道管理
        self.switch_which_frame("leftFrame")

        # xpath_bigCustomer = "/html/body[@class='imgbody']/div[@class='leftbox']/div[@class='menubox']/div[@class='lnavbg2']/a[@menuId='31120200']"
        # self.browser.find_element_by_xpath(xpath_bigCustomer).send_keys(Keys.ENTER)
        # print("Finish get BigCustomerData")
        # time.sleep(3)

        # 2. 点击大客户
        xpath_bigCustomer_data="/html/body[@class='imgbody']/div[@class='leftbox']/div[@class='menubox']/ul[@id='content1']/li[@sizset='1']/a[@menuId='31120203']"
        WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.XPATH,xpath_bigCustomer_data)))
        self.browser.find_element_by_xpath(xpath_bigCustomer_data).click()
        print("Finish find BigCustomerData")
        time.sleep(3)
        
        self.browser.switch_to.parent_frame()
        
        #先找到frame，再找到iframe
        self.switch_which_frame("mainFrame")
        i = 1
        while True:
            try:
                self.browser.switch_to.frame("rightBusinessFrame")
            except NoSuchFrameException:
                time.sleep(1) 
                print(str(i))
                i = i +1
                if i > 4:
                    raise NoSuchFrameException
            else:
                print("Find this iframe")
                break
                
        #set items per page 
        self.browser.find_element_by_xpath("//div[@id='navigate']/table/tbody/tr[1]/td/table/tbody/tr/td[2]/table/tbody/tr/td[2]/select/option[3]").click()
        time.sleep(3)

        #拼接元素查找路径
        xpath_bigCustomer_part="/html[@class='dj_ie dj_ie7 dj_iequirks']/body[@class='unieap mainbody']/div[@class='cm']/div[@class='dojoxGrid']/div[@class='dojoxGrid-master-view']/div[@id='dojox_GridView_0']/div[@class='dojoxGrid-scrollbox']/div[@class='dojoxGrid-content']"
        xpath_bigCustomer_part1="/div[@id='page-0']/div["
        xpath_bigCustomer_part2="]/table[@class='dojoxGrid-row-table']/tbody/tr/td["
        xpath_bigCustomer_part3="]/nobr"
        xpath_bigCustomer_part3div= "]/nobr/div"
        
        #方法1. 找到序号对比
        #xpath_bigCustomer_num="//div[@id='page-0']/div[0]/table[@class='u-grid-rowbar-table']/tbody/tr[0]/td"
        #print("xpath_bigCustomer_num is :"+xpath_bigCustomer_num)
        
        #方法2. 找一共几行
        bigCustomer_num_text = self.browser.find_element_by_xpath("//div[@id='navigate']/table/tbody/tr[1]/td/table/tbody/tr/td[1]/div").text
        #print(bigCustomer_num_text)
        bigCustomer_num = re.search('\d+',bigCustomer_num_text).group()
        print("条数为："+bigCustomer_num)
        
        bigCustomer_list=[]
        while i<= int(bigCustomer_num):
            print("i is "+ str(i))
            bigCustomer_list = bigCustomer_list + [i]
            i = i + 1
        print("the list is :"+str(bigCustomer_list))
        
        
        for i in bigCustomer_list:
            text = self.browser.find_element_by_xpath(xpath_bigCustomer_part+xpath_bigCustomer_part1+str(i)+xpath_bigCustomer_part2+'1'+xpath_bigCustomer_part3div).text
            print(str(i)+":"+text)
            self.list1 = self.list1+[[text]]
        
        for i in bigCustomer_list:
            for j in range(2,11):
                text=self.browser.find_element_by_xpath(xpath_bigCustomer_part+xpath_bigCustomer_part1+str(i)+xpath_bigCustomer_part2+str(j)+xpath_bigCustomer_part3).text
                print(str(i-1)+":"+text)
                self.list1[i-1]=self.list1[i-1]+[text]
        print(self.list1)
        
        self.browser.switch_to.parent_frame()
        
        #将得到的拼接数据写入到csv文件中
        wd = os.getcwd()
        parent_path = os.path.dirname(wd)
        wdcsv = parent_path + '\\csv\\'
        
        bigCustomer_file_path = os.path.join(wdcsv,"BIGCUSTOMER.csv")
        with open(bigCustomer_file_path,'w',newline='') as f:
            f_csv = csv.writer(f)
            f_csv.writerows(self.list1)

        return True
	

    def get_DaiBiaoXinXiData(self):
        """
        下载基础数据-销售代表数据
        """
        print("Start getting DaiBiaoXinXi")
        self.autoit_ontop()#网页放在最前面
		
        self.switch_which_frame("topFrame")
		
        #点击基础数据
        time.sleep(3)
        DaiBiaoXinXi_management="if(top.checkUmpBlock()){clearBack();switchModule('31120000','基础数据', 'ilms', '20');}else{return false;}"
        self.browser.execute_script(DaiBiaoXinXi_management)
        time.sleep(3)
		
        self.browser.switch_to.parent_frame()
		
        #1. 点击渠道管理
        self.switch_which_frame("leftFrame")

        # xpath_DaiBiaoXinXi = "/html/body[@class='imgbody']/div[@class='leftbox']/div[@class='menubox']/div[@class='lnavbg1']/a[@menuId='31120200']"
        # self.browser.find_element_by_xpath(xpath_DaiBiaoXinXi).send_keys(Keys.ENTER)
        # print("Finish get BigCustomerData")

		#2. 点击销售代表
        xpath_DaiBiaoXinXi_data="/html/body[@class='imgbody']/div[@class='leftbox']/div[@class='menubox']/ul[@id='content1']/li[@sizset='1']/a[@menuId='31120204']"
        WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.XPATH,xpath_DaiBiaoXinXi_data)))
        self.browser.find_element_by_xpath(xpath_DaiBiaoXinXi_data).click()
        print("Finish find DaiBiaoXinXi")
        self.browser.switch_to.parent_frame()
        
        #先找到frame，再找到iframe
        self.switch_which_frame("mainFrame")
        i = 1
        while True:
            try:
                self.browser.switch_to.frame("rightBusinessFrame")
            except NoSuchFrameException:
                time.sleep(1) 
                print(str(i))
                i = i +1
                if i > 4:
                    raise NoSuchFrameException
            else:
                print("Find this iframe")
                break
                
        #点击查询按钮
        js_Query = "queryRecord()"
        self.browser.execute_script(js_Query)
        time.sleep(5)
        
        #点击批量导出
        xpath_DaiBiaoXinXi_exportBtn="/html/body/div[@class='cm']/h3/span[@class='cr']/button[@id='exportBtn']/span[@id='exportBtn_label']"
        self.browser.find_element_by_xpath(xpath_DaiBiaoXinXi_exportBtn).click()
        print("Finish find xpath_DaiBiaoXinXi_exportBtn")
        time.sleep(3)
        
        #选择全选        
        xpath_DaiBiaoXinXi_selectAll="//*[@name='selectAll']"
        self.browser.find_element_by_xpath(xpath_DaiBiaoXinXi_selectAll).click()
        print("Finish find xpath_DaiBiaoXinXi_selectAll")
        time.sleep(3)
        
        #下载文件 DaiBiaoXinXiData xlsx file
        download_result = self.download_file_xlsx("DaiBiaoXinXi")
        
        #back to main frame
        self.browser.switch_to.parent_frame()
        #back to root
        self.browser.switch_to.parent_frame()
        print("download_result:"+str(download_result))
        return download_result
        
    
    def get_MenDianXinXiData(self):
        """
        下载基础数据-门店数据
        """
        print("Start getting MenDianXinXi")
        self.autoit_ontop()#网页放在最前面
		
        self.switch_which_frame("topFrame")

        # 点击基础数据
        time.sleep(3)
        MenDianXinXi_management="if(top.checkUmpBlock()){clearBack();switchModule('31120000','基础数据', 'ilms', '20');}else{return false;}"
        self.browser.execute_script(MenDianXinXi_management)
        time.sleep(3)

        self.browser.switch_to.parent_frame()

        #1. 点击渠道管理
        self.switch_which_frame("leftFrame")

        # xpath_MenDianXinXi = "/html/body[@class='imgbody']/div[@class='leftbox']/div[@class='menubox']/div[@class='lnavbg1']/a[@menuId='31120200']"
        # self.browser.find_element_by_xpath(xpath_MenDianXinXi).send_keys(Keys.ENTER)
        # print("Finish get BigCustomerData")

        #2. 点击门店
        xpath_MenDianXinXi_data="/html/body[@class='imgbody']/div[@class='leftbox']/div[@class='menubox']/ul[@id='content1']/li[@sizset='2']/a[@menuId='31120205']"
        WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.XPATH,xpath_MenDianXinXi_data)))
        self.browser.find_element_by_xpath(xpath_MenDianXinXi_data).click()
        print("Finish find MenDianXinXi")
        self.browser.switch_to.parent_frame()
        
        #先找到frame，再找到iframe
        self.switch_which_frame("mainFrame")
        i = 1
        while True:
            try:
                self.browser.switch_to.frame("rightBusinessFrame")
            except NoSuchFrameException:
                time.sleep(1) 
                print(str(i))
                i = i +1
                if i > 4:
                    raise NoSuchFrameException
            else:
                print("Find this iframe")
                break
                
        #点击查询按钮
        js_Query = "queryRecord()"
        self.browser.execute_script(js_Query)
        time.sleep(5)
        
        #点击批量导出
        xpath_MenDianXinXi_exportBtn="/html/body/div[@class='cm']/h3/span[@class='cr']/button[@id='exportBtn']/span[@id='exportBtn_label']"
        self.browser.find_element_by_xpath(xpath_MenDianXinXi_exportBtn).click()
        print("Finish find xpath_MenDianXinXi_exportBtn")
        time.sleep(3)
        
        #选择全选        
        xpath_MenDianXinXi_selectAll="//*[@name='selectAll']"
        self.browser.find_element_by_xpath(xpath_MenDianXinXi_selectAll).click()
        print("Finish find xpath_MenDianXinXi_selectAll")
        time.sleep(3)
        
        #下载文件 MenDianXinXiData xlsx file
        download_result = self.download_file_xlsx("MenDianXinXi")
        
        #back to main frame
        self.browser.switch_to.parent_frame()
        #back to root
        self.browser.switch_to.parent_frame()
        print("download_result:"+str(download_result))
        return download_result
        

	
    def download_file(self,file_name):
        #切换到reportFrame
        self.switch_which_frame("report")
        time.sleep(5)

        download_count = 0
        check_count = 0
        while True:
            #退出其他提示框
            # self.autoit_click_exit()
            #点击下载文件
            time.sleep(2)
            js_success = self.click_download_csv()
            time.sleep(2)
            if(js_success == True):
                #点击下载保存 click save and exit
                self.autoit_click()
                #检测文件是否存在
                time.sleep(8)
            else:
                #首先模拟点击csv下载
                print("download by mouse click")
                self.autoit_click_backup()
                time.sleep(8)
            while True:
                download = False #标记是否正常下载并改名
                file_exist = crawler_util.check_file(file_name)
                if(file_exist == True):
                    print("Successfully downdload file " + str(file_name) )
                    crawler_util.change_file_name(file_name)
                    download = True
                    break
                else:
                    time.sleep(10)
                    check_count = check_count +1
                    print("Download waiting :"+ str(10*check_count))
                    if(check_count > 12): #等待时间2分钟
                        download =False
                        break
            if(download == True):
                return True 
            download_count = download_count +1
            if(download_count >2 ): #最多下载三次
                return False

    def click_download_csv(self):
        i = 0
        while True:
            try:
                #下载按钮相对定位
                #download_img = "//form[@id='resultForm']/div[1]/ul/li[4]/img"
                js_DownLoad = "javascript:resultOut('csv',resultForm)"
                self.browser.execute_script(js_DownLoad)
                #self.switch_which_frame("printIFrame")
                #self.browser.find_element_by_id("printIFrame").click()
            except JavascriptException:
                time.sleep(2) 
                print(str(i))
                i = i +1
                #if i > 150: # 等待时间超过5分钟，下载不完善，重新下载
                if i > 150: # 等待时间超过10s，下载不完善，重新下载，无论第一次执行js是否成功，第二次执行js一定失败。
                    #raise JavascriptException 已经处理异常不再抛出
                    return False
            else:
                print("click download csv successfully")
                return True
             
    
    def download_file_xlsx(self,file_name):
        time.sleep(5)
        download_count = 0
        check_count = 0
        while True:
            #退出其他提示框
            # self.autoit_click_exit()
            #点击下载文件
            time.sleep(2)
            js_success = self.click_download_xlsx()
            time.sleep(15)
            if(js_success == True):
                #点击下载保存 click save and exit
                self.autoit_click()
                print("js_success")
                #检测文件是否存在
                time.sleep(8)
            else:
                #首先模拟点击csv下载
                print("download by mouse click")
                self.autoit_click_backup()
                time.sleep(8)
            while True:
                download = False #标记是否正常下载
                #转换格式
                #crawler_util.change_file_name(file_name)
                
                file_exist = crawler_util.check_file(file_name)
                print("file_exist ："+str(file_exist))
                if(file_exist == True):
                    print("Successfully downdload file " + str(file_name) )
                    crawler_util.change_file_name(file_name)
                    download = True
                    break
                else:
                    time.sleep(10)
                    check_count = check_count +1
                    print("Download waiting :"+ str(10*check_count))
                    if(check_count > 12): #等待时间2分钟
                        download =False
                        break
            if(download == True):
                return True
            download_count = download_count +1
            if(download_count >2 ): #最多下载三次
                return False
    
    
    
    def click_download_xlsx(self):
        i = 0
        while True:
            try:
                #下载按钮相对定位
                #download_img = "//form[@id='resultForm']/div[1]/ul/li[4]/img"
                js_DownLoad = "exportExcel()"
                self.browser.execute_script(js_DownLoad)
                print("click exportBtn successfully")
                #self.switch_which_frame("printIFrame")
                #self.browser.find_element_by_id("printIFrame").click()
            except JavascriptException:
                time.sleep(2) 
                print(str(i))
                i = i +1
                #if i > 150: # 等待时间超过5分钟，下载不完善，重新下载
                if i > 150: # 等待时间超过10s，下载不完善，重新下载，无论第一次执行js是否成功，第二次执行js一定失败。
                    #raise JavascriptException 已经处理异常不再抛出
                    return False
            else:
                print("click download xlsx successfully")
                return True
    

    def autoit_click(self):
        """
        自动点击下载
        """
        dirs = os.getcwd()
        file_root = os.path.join(dirs,"autoit_exe")
        file_path = os.path.join(file_root,"alts.exe" )
        os.system(file_path)
    def autoit_click_backup(self):
        """
        鼠标模拟点击csv下载，然后点击下载
        """
        dirs = os.getcwd()
        file_root = os.path.join(dirs,"autoit_exe")
        file_path = os.path.join(file_root,"click_click_new.exe" )
        os.system(file_path)
        #os.system("click_click_new.exe")
    
    def autoit_click_exit(self):
        """
        自动点击下载
        """
        dirs = os.getcwd()
        file_root = os.path.join(dirs,"autoit_exe")
        file_path = os.path.join(file_root,"click_exit.exe" )
        os.system(file_path)
        # os.system("click_exit.exe")

    def autoit_ontop(self):
        """
        窗口最前面
        """
        dirs = os.getcwd()
        file_root = os.path.join(dirs,"autoit_exe")
        file_path = os.path.join(file_root,"ontop.exe" )
        os.system(file_path)
        #os.system("ontop.exe")  
    
    def autoit_close(self):
        """
        关闭多于页
        """
        dirs = os.getcwd()
        file_root = os.path.join(dirs,"autoit_exe")
        file_path = os.path.join(file_root,"page_close.exe" )
        os.system(file_path)
        #os.system("page_close.exe")
    
    def autoit_close_all_ie(self):
        """
        关闭所有IE
        """
        dirs = os.getcwd()
        file_root = os.path.join(dirs,"autoit_exe")
        file_path = os.path.join(file_root,"close_all_ie.exe" )
        os.system(file_path)
        #os.system("close_all_ie.exe")

    def close_Express(self):
        os.popen("taskkill /im lava.exe -f")
        print("kill Express")



if __name__ == "__main__":
    Crawler = StartCrawler()
    Crawler.autoit_close_all_ie() #关闭所有IE网页
    Crawler.log_in() #登录
    Crawler.autoit_close() # 关闭多于页
    Crawler.get_download_page() #进入下载页
    Crawler.instant_business() #进入二代系统
    Crawler.statement_management() #进入报表管理

    # B402 =  Crawler.get_B402()
    # print("The B402 result is : "+str(B402))

    # JX201 = Crawler.get_JX_201()
    # print("The JX201 result is : "+ str(JX201))

    # A205 = Crawler.get_A205()
    # print("The A205 result is :" + str(A205))

    # Q102_STORE =Crawler.get_Q102_store()
    # print("The Q102 store result is :" +str(Q102_STORE))

    # Q102_SR =Crawler.get_Q102_sr()
    # print("The Q102 sr result is :" +str(Q102_SR))

    # Q102_CENTER =Crawler.get_Q102_center()
    # print("The Q102 center result is :" +str(Q102_CENTER))

    # Q102_CCLIENT =Crawler.get_Q102_cclient()
    # print("The Q102 C client result is :" +str(Q102_CCLIENT))

    Allot_DATA = Crawler.get_AllotData()
    print("The result of Allot_DATA is : " + str(Allot_DATA))

    # BigCustomerData = Crawler.get_BigCustomerData()
    # print("The BigCustomerData result is :"+str(BigCustomerData))
    
    # DaiBiaoXinXiData = Crawler.get_DaiBiaoXinXiData()
    # print("The DaiBiaoXinXiData result is :"+str(DaiBiaoXinXiData))
    
    # MenDianXinXiData = Crawler.get_MenDianXinXiData()
    # print("The MenDianXinXiData result is :"+str(MenDianXinXiData))

    # Crawler.close_Express() #关闭插件
    # print("End of this file")
