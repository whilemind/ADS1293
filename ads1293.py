from TI2093RegList import *
from TI2093RegSetting import *
import spidev
import time
import RPi.GPIO as GPIO
from enum import Enum


class ECG_LEAD_TYPE(Enum):
  LEAD_03 = 3
  LEAD_05 = 5
  LEAD_12 = 12


class ADS1293(object):

  def __init__(self, maxpoint = 1000, leads=ECG_LEAD_TYPE.LEAD_12, max_speed_hz=15000000):
    self._DATA_READY_SLEEP_INTERVAL   = 0.009 #raspberry pi zero w required sleep mainly initially
    self.TI_ADS1293_CONFIG_REG_VALUE  = (0x00)
    self.GPIO_INPUT_PIN               = 27

    self.counter = 0
    self.maxpoint = maxpoint
    self.leads = leads
    self.adc_data_ready = 0

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.GPIO_INPUT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    self.spi_0 = None
    self.spi_1 = None
    self.spi_2 = None

    if(leads == ECG_LEAD_TYPE.LEAD_05):
      self.spi_0 = spidev.SpiDev()
      self.spi_0.open(0, 0)
      self.spi_0.max_speed_hz = max_speed_hz
    elif (leads == ECG_LEAD_TYPE.LEAD_12):
      self.spi_0 = spidev.SpiDev()
      self.spi_0.open(1, 0)
      self.spi_0.max_speed_hz = max_speed_hz

      self.spi_1 = spidev.SpiDev()
      self.spi_1.open(1, 1)
      self.spi_1.max_speed_hz = max_speed_hz

      self.spi_2 = spidev.SpiDev()
      self.spi_2.open(1, 2)
      self.spi_2.max_speed_hz = max_speed_hz
      
    GPIO.add_event_detect(self.GPIO_INPUT_PIN, GPIO.FALLING, callback=self.gpio_callback)
    self.isConnected = True


  def gpio_callback(self, channel):
    # print("Called GPIO callback method.")
    self.adc_data_ready = self.adc_data_ready + 1


  def close(self):
    self.spi_write_reg(TI_ADS1293_CONFIG_REG, self.TI_ADS1293_CONFIG_REG_VALUE)
    
    if(self.leads == ECG_LEAD_TYPE.LEAD_05):
      self.spi_0.close()
    elif (self.leads == ECG_LEAD_TYPE.LEAD_12):
      self.spi_0.close()
      self.spi_1.close()
      self.spi_2.close()

    GPIO.cleanup()
    self.isConnected = False


  @property
  def is_data_ready(self):
    return self.adc_data_ready


  def reset_data_ready(self):
    if(self.adc_data_ready > 0):
      self.adc_data_ready = self.adc_data_ready - 1


  @property
  def is_connected(self):
    return self.isConnected


  @property
  def data_ready_sleep_interval(self):
    return self._DATA_READY_SLEEP_INTERVAL


  def spi_write_reg(self, addr, value, channel=0):
    command = ADS1293_WRITE_BIT & addr
    result = None

    if (channel == 0):
      result = self.spi_0.xfer2([command, value])
    elif (channel == 1):
      result = self.spi_1.xfer2([command, value])
    elif (channel == 2):
      result = self.spi_2.xfer2([command, value])

    return result

  def init_channel_setting(self):
    if(self.leads == ECG_LEAD_TYPE.LEAD_05):
      self.init_channel_lead5()
    elif (self.leads == ECG_LEAD_TYPE.LEAD_12):
      self.init_channel_lead12()


  def init_channel_lead5(self, channel=0):
    self.spi_write_reg(TI_ADS1293_CONFIG_REG, self.TI_ADS1293_CONFIG_REG_VALUE, channel)
    self.spi_write_reg(TI_ADS1293_FLEX_CH1_CN_REG, 0x11, channel)
    self.spi_write_reg(TI_ADS1293_FLEX_CH2_CN_REG, 0x19, channel)
    self.spi_write_reg(TI_ADS1293_FLEX_CH3_CN_REG, 0x2E, channel)
    
    self.spi_write_reg(0x0A, 0x07, channel)
    self.spi_write_reg(0x0C, 0x04, channel)
    self.spi_write_reg(0x0D, 0x01, channel)
    self.spi_write_reg(0x0E, 0x02, channel)
    self.spi_write_reg(0x0F, 0x03, channel)
    self.spi_write_reg(0x10, 0x01, channel)

    self.spi_write_reg(0x12, 0x04, channel)

    self.spi_write_reg(TI_ADS1293_AFE_SHDN_CN_REG, 0x00, channel)

    self.spi_write_reg(TI_ADS1293_R2_RATE_REG, 0x02, channel)
    self.spi_write_reg(TI_ADS1293_R3_RATE1_REG, 0x02, channel)
    self.spi_write_reg(TI_ADS1293_R3_RATE2_REG, 0x02, channel)
    self.spi_write_reg(TI_ADS1293_R3_RATE3_REG, 0x02, channel)

    self.spi_write_reg(0x27, 0x08, channel)
    self.spi_write_reg(0x2F, 0x70, channel)


  def init_channel_lead12(self):
    self.spi_write_reg(TI_ADS1293_CONFIG_REG, self.TI_ADS1293_CONFIG_REG_VALUE, ECG_CHAN_1)
    self.spi_write_reg(TI_ADS1293_FLEX_CH1_CN_REG, 0x11, ECG_CHAN_1)
    self.spi_write_reg(TI_ADS1293_FLEX_CH2_CN_REG, 0x19, ECG_CHAN_1)
    
    self.spi_write_reg(TI_ADS1293_CMDET_EN_REG, 0x07, ECG_CHAN_1)
    self.spi_write_reg(TI_ADS1293_RLD_CN_REG, 0x04, ECG_CHAN_1)

    self.spi_write_reg(TI_ADS1293_WILSON_EN1_REG, 0x01, ECG_CHAN_1)
    self.spi_write_reg(TI_ADS1293_WILSON_EN2_REG, 0x02, ECG_CHAN_1)
    self.spi_write_reg(TI_ADS1293_WILSON_EN3_REG, 0x03, ECG_CHAN_1)
    
    self.spi_write_reg(TI_ADS1293_OSC_CN_REG, 0x05, ECG_CHAN_1)
    
    self.spi_write_reg(TI_ADS1293_AFE_SHDN_CN_REG, 0x24, ECG_CHAN_1)
    
    self.spi_write_reg(TI_ADS1293_R2_RATE_REG, 0x02, ECG_CHAN_1)
    self.spi_write_reg(TI_ADS1293_R3_RATE1_REG, 0x02, ECG_CHAN_1)
    self.spi_write_reg(TI_ADS1293_R3_RATE2_REG, 0x02, ECG_CHAN_1)
    
    self.spi_write_reg(TI_ADS1293_DRDYB_SRC_REG, 0x08, ECG_CHAN_1)
    
    self.spi_write_reg(TI_ADS1293_SYNCOUTB_SRC_REG, 0x08, ECG_CHAN_1)
    
    self.spi_write_reg(TI_ADS1293_CH_CNFG_REG, 0x30, ECG_CHAN_1)
    
    self.__init_channel_lead12(ECG_CHAN_2)
    self.__init_channel_lead12(ECG_CHAN_3)


  def __init_channel_lead12(self, channel):
    self.spi_write_reg(TI_ADS1293_CONFIG_REG, self.TI_ADS1293_CONFIG_REG_VALUE, channel)
    self.spi_write_reg(TI_ADS1293_FLEX_CH1_CN_REG, 0x0C, channel)
    self.spi_write_reg(TI_ADS1293_FLEX_CH2_CN_REG, 0x14, channel)
    self.spi_write_reg(TI_ADS1293_FLEX_CH3_CN_REG, 0x1C, channel)

    self.spi_write_reg(TI_ADS1293_OSC_CN_REG, 0x06, channel)

    self.spi_write_reg(TI_ADS1293_AFE_SHDN_CN_REG, 0x00, channel)

    self.spi_write_reg(TI_ADS1293_R2_RATE_REG, 0x02, channel)
    self.spi_write_reg(TI_ADS1293_R3_RATE1_REG, 0x02, channel)
    self.spi_write_reg(TI_ADS1293_R3_RATE2_REG, 0x02, channel)
    self.spi_write_reg(TI_ADS1293_R3_RATE3_REG, 0x02, channel)

    self.spi_write_reg(TI_ADS1293_DRDYB_SRC_REG, 0x00, channel)
    self.spi_write_reg(TI_ADS1293_SYNCOUTB_SRC_REG, 0x40, channel)
    
    self.spi_write_reg(TI_ADS1293_CH_CNFG_REG, 0x70, channel)


  def spi_read_reg(self, addr, channel=0):
    command = ADS1293_READ_BIT | addr
    
    result = []
    if (channel == 0):
      result = self.spi_0.xfer2([command, 0x00])
    elif (channel == 1):
      result = self.spi_1.xfer2([command, 0x00])
    elif (channel == 2):
      result = self.spi_2.xfer2([command, 0x00])

    return result


  def spi_stream_read_reg(self, count, channel=0):
    data = []
    cmd = ADS1293_READ_BIT | TI_ADS1293_DATA_LOOP_REG
    commands = ([cmd] + [0x00] * count)

    if (channel == 0):
      data = self.spi_0.xfer2(commands)
    elif (channel == 1):
      data = self.spi_1.xfer2(commands)
    elif (channel == 2):
      data = self.spi_2.xfer2(commands)

    return data   

  