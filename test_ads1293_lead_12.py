import sys
import time
from datetime import datetime
import ads1293 as ecg
from TI2093RegList import *
from TI2093RegSetting import *


def main():
  print("Starting ECG ADS1293 library testing...")
  num_chunk = 1
  duration_secs = 1.0
  num_data_points = 1000

  try:
    print(">> Trying to read {} data points within {} secs.\n".format(num_data_points, duration_secs))

    ads = ecg.ADS1293(leads=ecg.ECG_LEAD_TYPE.LEAD_12)
    
    ads.init_channel_setting()

    ads.spi_write_reg(TI_ADS1293_CONFIG_REG, ads.TI_ADS1293_CONFIG_REG_VALUE | ADS1293_START_CONV, ECG_CHAN_1)
    ads.spi_write_reg(TI_ADS1293_CONFIG_REG, ads.TI_ADS1293_CONFIG_REG_VALUE | ADS1293_START_CONV, ECG_CHAN_2)
    ads.spi_write_reg(TI_ADS1293_CONFIG_REG, ads.TI_ADS1293_CONFIG_REG_VALUE | ADS1293_START_CONV, ECG_CHAN_3)

    i = 0
    data_bytes = None
    startTime = time.time()
    while(1):
      if(ads.is_data_ready > 0):
        data_bytes = ads.spi_stream_read_reg(LEAD_12_CHAN_1_DATA_SIZE * num_chunk, ECG_CHAN_1)
        # print("Chan 1 Data is {}".format(data_bytes))
        data_bytes = ads.spi_stream_read_reg(LEAD_12_CHAN_2_DATA_SIZE * num_chunk, ECG_CHAN_2)
        # print("Chan 2 Data is {}".format(data_bytes))
        data_bytes = ads.spi_stream_read_reg(LEAD_12_CHAN_3_DATA_SIZE * num_chunk, ECG_CHAN_3)
        # print("Chan 3 Data is {}".format(data_bytes))

        ads.reset_data_ready()
        i = i + 1

        endTime = time.time()
        diff = endTime - startTime

        if(diff >= duration_secs):
          print("<< {} secs required to read {} data points.".format(diff, (i * num_chunk)))
          break

      else:
        # print("Sleeping is_data_ready {} and i {}.".format(ads.is_data_ready, i))
        time.sleep(ads.data_ready_sleep_interval)  

      if(i == num_data_points):
        endTime = time.time()
        diff = endTime - startTime

        print("<< {} secs required to read {} data points.".format(diff, (i * num_chunk)))
        break

  except Exception as e:
    print("Exception occured {}".format(e))
  finally:
    ads.close()


if __name__ == "__main__":
  main()