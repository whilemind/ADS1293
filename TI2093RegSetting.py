'''
/************************************************************
* TI ADS1293 REGISTER SET INITIALIZATION VALUES
************************************************************/
'''

TI_ADS1293_FLEX_CH1_CN_REG_VALUE          = (0x11)  #/* Flex Routing Swich Control for Channel 1 */
TI_ADS1293_FLEX_CH2_CN_REG_VALUE          = (0x19)  #/* Flex Routing Swich Control for Channel 2 */
TI_ADS1293_FLEX_CH3_CN_REG_VALUE          = (0x2E)  #/* Flex Routing Swich Control for Channel 3 */
TI_ADS1293_FLEX_PACE_CN_REG_VALUE         = (0x00)  #/* Flex Routing Swich Control for Pace Channel */
TI_ADS1293_FLEX_VBAT_CN_REG_VALUE         = (0x00)  #/* Flex Routing Swich Control for Battery Monitoriing */

TI_ADS1293_LOD_CN_REG_VALUE               = (0x08)  #/* Lead Off Detect Control */
TI_ADS1293_LOD_EN_REG_VALUE               = (0x00)  #/* Lead Off Detect Enable */
TI_ADS1293_LOD_CURRENT_REG_VALUE          = (0x00)  #/* Lead Off Detect Current */
TI_ADS1293_LOD_AC_CN_REG_VALUE            = (0x00)  #/* AC Lead Off Detect Current */

TI_ADS1293_CMDET_EN_REG_VALUE             = (0x07)  #/* Common Mode Detect Enable */
TI_ADS1293_CMDET_CN_REG_VALUE             = (0x00)  #/* Commond Mode Detect Control */
TI_ADS1293_RLD_CN_REG_VALUE               = (0x04)  #/* Right Leg Drive Control */

TI_ADS1293_WILSON_EN1_REG_VALUE           = (0x01)  #/* Wilson Reference Input one Selection */
TI_ADS1293_WILSON_EN2_REG_VALUE           = (0x02)  #/* Wilson Reference Input two Selection */
TI_ADS1293_WILSON_EN3_REG_VALUE           = (0x03)  #/* Wilson Reference Input three Selection */
TI_ADS1293_WILSON_CN_REG_VALUE            = (0x01)  #/* Wilson Reference Input Control */

TI_ADS1293_REF_CN_REG_VALUE              =  (0x00)  #/* Internal Reference Voltage Control */

TI_ADS1293_OSC_CN_REG_VALUE              =  (0x04)  #/* Clock Source and Output Clock Control */

TI_ADS1293_AFE_RES_REG_VALUE             =  (0x00)  #/* Analog Front-End Frequency and Resolution */
TI_ADS1293_AFE_SHDN_CN_REG_VALUE         =  (0x00)  #/* Analog Front-End Shutdown Control */
TI_ADS1293_AFE_FAULT_CN_REG_VALUE        =  (0x00)  #/* Analog Front-End Fault Detection Control */
TI_ADS1293_AFE_DITHER_EN_REG_VALUE       =  (0x00)  #/* Enable Dithering in Signma-Delta */
TI_ADS1293_AFE_PACE_CN_REG_VALUE         =  (0x05)  #/* Analog Pace Channel Output Routing Control */

TI_ADS1293_ERROR_LOD_REG_VALUE           =  (0x00)  #/* Lead Off Detect Error Status */
TI_ADS1293_ERROR_STATUS_REG_VALUE        =  (0x72)  #/* Other Error Status */
TI_ADS1293_ERROR_RANGE1_REG_VALUE        =  (0x12)  #/* Channel 1 Amplifier Out of Range Status */
TI_ADS1293_ERROR_RANGE2_REG_VALUE        =  (0x12)  #/* Channel 1 Amplifier Out of Range Status */
TI_ADS1293_ERROR_RANGE3_REG_VALUE        =  (0x36)  #/* Channel 1 Amplifier Out of Range Status */
TI_ADS1293_ERROR_SYNC_REG_VALUE          =  (0x00)  #/* Synchronization Error */


TI_ADS1293_R2_RATE_REG_VALUE             =  (0x02)  #/* R2 Decimation Rate */
TI_ADS1293_R3_RATE1_REG_VALUE            =  (0x02)  #/* R3 Decimation Rate for Channel 1 */
TI_ADS1293_R3_RATE2_REG_VALUE            =  (0x02)  #/* R3 Decimation Rate for Channel 2 */
TI_ADS1293_R3_RATE3_REG_VALUE            =  (0x02)  #/* R3 Decimation Rate for Channel 3 */
TI_ADS1293_P_DRATE_REG_VALUE             =  (0x00)  #/* 2x Pace Data Rate for all channels */
TI_ADS1293_DIS_EFILTER_REG_VALUE         =  (0x00)  #/* ECG Filters Disabled */
TI_ADS1293_DRDYB_SRC_REG_VALUE           =  (0x08)  #/* Data Ready Pin Source */
TI_ADS1293_SYNCOUTB_SRC_REG_VALUE        =  (0x00)  #/* Sync Out Pin Source */
TI_ADS1293_MASK_DRDYB_REG_VALUE          =  (0x00)  #/* Optional Mask Control for DRDYB Output */
TI_ADS1293_MASK_ERR_REG_VALUE            =  (0x00)  #/* Mask Error on ALARMB Pin */

TI_ADS1293_ALARM_FILTER_REG_VALUE        =  (0x33)  #/* Digital Filter for Analog Alarm Signals */
TI_ADS1293_CH_CNFG_REG_VALUE             =  (0x70)  #/* Configure Channel for Loop Read Back Mode */

TI_ADS1293_DATA_STATUS_REG_VALUE         =  (0x00)  #/* ECG and Pace Data Ready Status */
TI_ADS1293_DATA_CH1_PACE_H_REG_VALUE     =  (0x00)  #/* Channel1 Pace Data High [15:8] */
TI_ADS1293_DATA_CH1_PACE_L_REG_VALUE     =  (0x00)  #/* Channel1 Pace Data Low [7:0] */
TI_ADS1293_DATA_CH2_PACE_H_REG_VALUE     =  (0x00)  #/* Channel2 Pace Data High [15:8] */
TI_ADS1293_DATA_CH2_PACE_L_REG_VALUE     =  (0x00)  #/* Channel2 Pace Data Low [7:0] */
TI_ADS1293_DATA_CH3_PACE_H_REG_VALUE     =  (0x00)  #/* Channel3 Pace Data High [15:8] */
TI_ADS1293_DATA_CH3_PACE_L_REG_VALUE     =  (0x00)  #/* Channel3 Pace Data Low [7:0] */
TI_ADS1293_DATA_CH1_ECG_H_REG_VALUE      =  (0x00)  #/* Channel1 ECG Data High [23:16] */
TI_ADS1293_DATA_CH1_ECG_M_REG_VALUE      =  (0x00)  #/* Channel1 ECG Data Medium [15:8] */
TI_ADS1293_DATA_CH1_ECG_L_REG_VALUE      =  (0x00)  #/* Channel1 ECG Data Low [7:0] */
TI_ADS1293_DATA_CH2_ECG_H_REG_VALUE      =  (0x00)  #/* Channel2 ECG Data High [23:16] */
TI_ADS1293_DATA_CH2_ECG_M_REG_VALUE      =  (0x00)  #/* Channel2 ECG Data Medium [15:8] */
TI_ADS1293_DATA_CH2_ECG_L_REG_VALUE      =  (0x00)  #/* Channel2 ECG Data Low [7:0] */
TI_ADS1293_DATA_CH3_ECG_H_REG_VALUE      =  (0x00)  #/* Channel3 ECG Data High [23:16] */
TI_ADS1293_DATA_CH3_ECG_M_REG_VALUE      =  (0x00)  #/* Channel3 ECG Data Medium [15:8] */
TI_ADS1293_DATA_CH3_ECG_L_REG_VALUE      =  (0x00)  #/* Channel3 ECG Data Low [7:0] */

TI_ADS1293_REVID_REG_VALUE               =  (0x40)  #/* Revision ID */
TI_ADS1293_DATA_LOOP_REG_VALUE           =  (0x50)  #/* Loop Read Back Address */

#Useful definitions
ADS1293_START_CONV                       =  (0x01)  #// Start Conversion Bit

