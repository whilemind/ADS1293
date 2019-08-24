import sys
import time
import ads1293 as ecg
from TI2093RegList import *
from TI2093RegSetting import *


def main():
  print("Starting ECG ADS1293 library testing...")
  num_chunk = 5

  try:
    ads = ecg.ADS1293(maxpoint=10, leads=ECG_LEAD_TYPE.LEAD_05)
    ads.init_channel_setting()
    ads.spi_write_reg(TI_ADS1293_CONFIG_REG, ads.TI_ADS1293_CONFIG_REG_VALUE | ADS1293_START_CONV)

    i = 0
    while(1):
      if(ads.is_data_ready == 1):
        data_bytes = ads.spi_stream_read_reg(LEAD_05_CHAN_1_DATA_SIZE * num_chunk)
        print("Data is {}".format(data_bytes))
        ads.reset_data_ready()
        # break
      else:
        time.sleep(ads.data_ready_sleep_interval)  
        i = i + 1

      print("Sleeping {}".format(i))
      
      if(i == 15):
        break

  except Exception, e:
    print("Exception occured {}".format(e))
  finally:
    ads.close()


if __name__ == "__main__":
  main()