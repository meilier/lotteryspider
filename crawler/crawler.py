# -*- coding: UTF-8 -*-

import os, time
import datetime
from ie import StartCrawler
import traceback
import threading

class Crawler(object):

    def __init__(self):
        pass

    def start(self):
        while True:
            try :
                n_crawler = StartCrawler()
                n_crawler.start_drive()
                n_crawler.TODO()
                n_crawler.instant_business()
                i = 0
                browser_time = 0
                while True:
                    try :
                        begin_data = n_crawler.get_begin_data()
                        if self.check_data(begin_data):
                            nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                            with open("Time.txt","w") as f:
                                f.write(nowTime)
                            print(nowTime)
                            self.delete_csv_files() #清空文件夹
                            n_crawler.get_B402()
                            n_crawler.get_JX201()
                            n_crawler.get_A205()
                            n_crawler.get_Q102()
                            n_crawler.get_AllotData()
                            self.write_control_date(begin_data) #写控制文件
                            i = 0
                        else:
                            browser_time = browser_time + 1
                            print("current time is : " + str(browser_time))
                            print("============Sleeping============")
                            time.sleep(10)
                    except Exception as e:
                        traceback.print_exc()
                        i = i+1
                        if i>3:
                            time.sleep(10)
                            break
                        else:
                            continue
            except Exception as e:
                traceback.print_exc()
                #time.sleep(300)
                print("thread start ")
                wait_thread = threading.Thread(target = self.start_sleep_thread,args=())
                wait_thread.start()
                wait_thread.join()
                print("Thread Stoped")
                continue


    def start_sleep_thread(self):
        i=0
        while i<5:
            print("sleep count" + str(i+1))
            i = i + 1
            time.sleep(3)


    def delete_csv_files(self):
        """
        清空CSV文件
        """
        wdcsv = "./csv/"
        for filename in os.listdir(wdcsv):
            filepath = wdcsv+filename
            os.remove(filepath)

    def write_control_date(self,begin_data):

        with open("control.cfg","w") as f:
            f.write(begin_data)
        print("Have write control : " + begin_data)

    def check_data(self, begin_data):
        yesterday = self.get_yesterday()

        print("Check date")
        print(type(yesterday))
        print(yesterday)
        print(type(begin_data))
        print(begin_data)
        #时间条件是否满足
        t_data = False
        if yesterday == begin_data:
            t_data = True

        #日志时间是否满足
        t_control = False
        with open("control.cfg","r") as f:
            data=f.readline()
            if not begin_data==data:
                t_control = True

        print("T_data : "+ str(t_data))
        print("T_control : "+ str(t_control))

        if t_data and t_control:
            result = True
        else:
            result = False
        print(result)
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
        current_time = data_time[11:]
        print(current_time)
        return current_time
        


if __name__ == "__main__":
    C = Crawler()
    # C.get_current_data()
    # C.get_current_time()
    C.start()
    
