import sys
import time
import ads1293 as ecg
from TI2093RegList import *
from TI2093RegSetting import *
import matplotlib.pyplot as plt
import numpy as np

read_date= np.zeros((1,1))
xs = [0, 0]
ys = [1, 1]
i = 0
valve = 800

if __name__ == "__main__":
  print("Starting ECG ADS1293 library testing...")

  # 随机函数和系统时间的准备
  time_date = time.strftime('%Y-%m-%d', time.gmtime())  # 字符串文件

  # 启动文件对象和写入文件头
  try:  # 若文件存在 追加写
    file = open("/home/pi/Desktop/date/date_{}.csv".format(time_date), "r")  # 文件不存在的异常
    file = open("/home/pi/Desktop/date/date_{}.csv".format(time_date), "a+")
  except FileNotFoundError:  # 若文件不存在 从头开始写
    print("文件不存在，但是已经创建")
    file = open("/home/pi/Desktop/date/date_{}.csv".format(time_date), "w+")
    file.write("膈肌数据,时间:," + time_date + '\n')


  try:
    ads = ecg.ADS1293( leads=ecg.ECG_LEAD_TYPE.LEAD_05)
    ads.init_channel_setting()
    ads.spi_write_reg(TI_ADS1293_CONFIG_REG, ads.TI_ADS1293_CONFIG_REG_VALUE | ADS1293_START_CONV)
    ads.spi_0.xfer2([TI_ADS1293_ERROR_STATUS_REG|TI_ADS1293_ERROR_STATUS_REG,0x00]) # detect error status, 1Byte
    plt.ion()#display plot simutenidously run next
    time.sleep(0.05)#wait data balance
    print("Loading date")
    startTime = time.time()
    while(1):
      if i >= valve:
        print('Using code date:{}'.format(time.time()-startTime))
        #read_date = ads.data_read
        file.write(','.join('%s' %id for id in read_date) + '\n')  # 遍历列表元素，并把其转为字符串
        plt.plot(read_date)
        plt.axis([0,valve,0,1.2e7])
        plt.xlabel("1.2ms/pot")
        plt.ylabel("uv")
        plt.show()
        ads.reset_data_ready()
        break
      else:
        i = ads.is_data_ready
        read_date = ads.data_read
        time.sleep(0.01)#wait data balance

        read_date=np.append(ads.data_read,0)

        print("Loading date : {:.2%}".format(i/valve))#display progress bar

      #dongtaixianshi********
      '''
      xs[0] = xs[1]
      ys[0] = ys[1]
      xs[1] = i
      ys[1] = a[0]
      plt.plot(xs, ys, "b")
      plt.xlim(xs[1]-i, xs[1]+1)
      plt.ylim(0, 1.75e7)
      plt.pause(0.0000000001)
      plt.xlabel("1.2ms/pot")
      plt.ylabel("uv")
      '''
      #********************


  except Exception as e:
    print("Exception occured {}".format(e))
  finally:
    ads.close()
    ads.reset_data_ready()
