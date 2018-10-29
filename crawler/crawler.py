# -*- coding: UTF-8 -*-

import os, time
import datetime
from ie import StartCrawler
import crawler_util
import traceback
import threading


class Crawler(object):
    def __init__(self):

        self.work_list = {
            "B402": False,
            "JX201": False,
            "A205": False,
            # "Q102_STORE": False,
            # "Q102_SR": False,
            # "Q102_CENTER": False,
            # "Q102_CCLIENT": False,
            "AllotData": False,
            # -"BigCustomerData": False,
            # "DaiBiaoXinXiData": False,
            "MenDianXinXiData": False
            }
        pass
    
    def start(self):
        while True:

            try:
                start_work = self.check_work()
                # 是否开始工作
            except Exception as e:
                traceback.print_exc()
                time.sleep(20)
                continue

            if start_work:

                self.clear_work_list() #清空work_list
                self.delete_csv_files() #清空下载文件夹

                except_count = 0
                while True:
                    try:
                        if self.work_all_done():
                            self.write_control(self.yesterday)
                            break
                        else:
                            self.go_to_work()
                    except Exception as e:
                        traceback.print_exc()
                        except_count = except_count + 1
                        time.sleep(20)
                        if except_count > 2:
                            break
            else:
                time.sleep(3600)
                
    def clear_work_list(self):
        """
        清空work_list
        """
        for work in self.work_list.keys():
            self.work_list[work] = False
    
    def work_all_done(self):
        """
        检测所有的扒取是否干完
        """
        result = True
        for work in self.work_list.keys():
            result = result and self.work_list[work]
        return result

    def go_to_work(self):
        """
        扒取文件
        """
        # Crawler = StartCrawler()
        # Crawler.autoit_close_all_ie() #关闭所有IE网页
        # Crawler.log_in() #登录
        # Crawler.autoit_close() # 关闭多于页
        # Crawler.get_download_page() #进入下载页
        # Crawler.instant_business() #进入二代系统
        # Crawler.statement_management() #进入报表管理

        for work in self.work_list.keys():

            if self.work_list[work] == False:

                Crawler = StartCrawler()
                Crawler.autoit_close_all_ie() #关闭所有IE网页
                Crawler.log_in() #登录
                Crawler.autoit_close() # 关闭多于页
                Crawler.get_download_page() #进入下载页
                Crawler.instant_business() #进入二代系统
                Crawler.statement_management() #进入报表管理

                crawler_result = False
                if work == "B402":
                    crawler_result=Crawler.get_B402()
                if work == "JX201":
                    crawler_result=Crawler.get_JX_201()
                if work == "A205":
                    crawler_result=Crawler.get_A205()
                if work == "Q102_STORE":
                    crawler_result=Crawler.get_Q102_store()
                if work == "Q102_SR":
                    crawler_result=Crawler.get_Q102_sr()
                if work == "Q102_CENTER":
                    crawler_result=Crawler.get_Q102_center()
                if work == "Q102_CCLIENT":
                    crawler_result=Crawler.get_Q102_cclient()
                if work == "AllotData":
                    crawler_result=Crawler.get_AllotData()
                if work == "BigCustomerData":
                    crawler_result=Crawler.get_BigCustomerData()
                if work == "DaiBiaoXinXiData":
                    crawler_result=Crawler.get_DaiBiaoXinXiData()
                if work == "MenDianXinXiData":
                    crawler_result=Crawler.get_MenDianXinXiData()
                self.work_list[work] = crawler_result #修改work_list 状态
                print(self.work_list)

                Crawler.close_Express() #关闭插件
            else:
                continue

    def get_begin_date(self):
        begine_date = StartCrawler().get_begin_date()
        return begine_date


    def check_work(self):
        self.yesterday = self.get_yesterday()
        print("Yesterday date is :" + str(self.yesterday))
        begin_date = self.get_begin_date()
        #时间条件是否满足
        t_date = False
        if self.yesterday == begin_date:
            t_date = True

        #日志时间是否满足
        t_control = False

        current_path = os.getcwd()
        parent_path = os.path.dirname(current_path)
        file_path = os.path.join(parent_path, "control.cfg")

        with open(file_path,"r") as f:
            date=f.readline()
            if not begin_date==date:
                t_control = True

        #是否为工作时间
        hour_time = ["06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22"]
        work_hour = self.get_current_time()
        print(work_hour)
        work_time = False

        if work_hour in hour_time:
            work_time = True

        print("T_data : "+ str(t_date))
        print("T_control : "+ str(t_control))
        print("Work time :" +str(work_time))

        result = t_control and t_date and work_time

        return result

    def get_yesterday(self):
        """
        得到前一天的信息
        """
        today=datetime.date.today() 
        oneday=datetime.timedelta(days=1) 
        yesterday=today-oneday  
        return yesterday.strftime('%Y-%m-%d')

    def get_current_data(self):
        """
        得到当前的日期
        """
        data_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        current_data = data_time[0:10]
        print(current_data)
        return current_data
    
    def get_current_time(self):
        """
        得到当前时间
        """
        data_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        current_time = data_time[11:13]
        print(current_time)
        return current_time 
    

    def delete_csv_files(self):
        """
        清空CSV文件
        """
        wd = os.getcwd()
        parent_path = os.path.dirname(wd)
        # parent_2_path = os.path.dirname(parent_path)
        wdcsv = parent_path +'\\csv\\'

        for filename in os.listdir(wdcsv):
            filepath = wdcsv+filename
            os.remove(filepath)

    def write_control(self,begin_data):
        current_path = os.getcwd()
        parent_path = os.path.dirname(current_path)
        file_path = os.path.join(parent_path, "control.cfg")

        with open(file_path,"w") as f:
            f.write(begin_data)
        print("Have write control : " + begin_data)



if __name__ == "__main__":
    C = Crawler()
    # C.get_current_time()
    C.start()
    
