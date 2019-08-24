ECG_CHAN_1                      = 0
ECG_CHAN_2                      = 1
ECG_CHAN_3                      = 2  
 
LEAD_05_CHAN_1_DATA_SIZE        = 9

LEAD_12_CHAN_1_DATA_SIZE        = 6
LEAD_12_CHAN_2_DATA_SIZE        = 9
LEAD_12_CHAN_3_DATA_SIZE        = 9


TI_ADS1293_CONFIG_REG           = 0x00    #/* Main Configuration */

TI_ADS1293_FLEX_CH1_CN_REG      = 0x01    #/* Flex Routing Swich Control for Channel 1 */
TI_ADS1293_FLEX_CH2_CN_REG      = 0x02    #/* Flex Routing Swich Control for Channel 2 */
TI_ADS1293_FLEX_CH3_CN_REG      = 0x03    #/* Flex Routing Swich Control for Channel 3 */
TI_ADS1293_FLEX_PACE_CN_REG     = 0x04    #/* Flex Routing Swich Control for Pace Channel */
TI_ADS1293_FLEX_VBAT_CN_REG     = 0x05    #/* Flex Routing Swich Control for Battery Monitoriing */

TI_ADS1293_LOD_CN_REG           = 0x06    #/* Lead Off Detect Control */
TI_ADS1293_LOD_EN_REG           = 0x07    #/* Lead Off Detect Enable */
TI_ADS1293_LOD_CURRENT_REG      = 0x08    #/* Lead Off Detect Current */
TI_ADS1293_LOD_AC_CN_REG        = 0x09    #/* AC Lead Off Detect Current */

TI_ADS1293_CMDET_EN_REG         = 0x0A    #/* Common Mode Detect Enable */
TI_ADS1293_CMDET_CN_REG         = 0x0B    #/* Commond Mode Detect Control */
TI_ADS1293_RLD_CN_REG           = 0x0C    #/* Right Leg Drive Control */

TI_ADS1293_WILSON_EN1_REG       = 0x0D    #/* Wilson Reference Input one Selection */
TI_ADS1293_WILSON_EN2_REG       = 0x0E    #/* Wilson Reference Input two Selection */
TI_ADS1293_WILSON_EN3_REG       = 0x0F    #/* Wilson Reference Input three Selection */
TI_ADS1293_WILSON_CN_REG        = 0x10    #/* Wilson Reference Input Control */

TI_ADS1293_REF_CN_REG           = 0x11    #/* Internal Reference Voltage Control */

TI_ADS1293_OSC_CN_REG           = 0x12    #/* Clock Source and Output Clock Control */

TI_ADS1293_AFE_RES_REG          = 0x13    #/* Analog Front-End Frequency and Resolution */
TI_ADS1293_AFE_SHDN_CN_REG      = 0x14    #/* Analog Front-End Shutdown Control */
TI_ADS1293_AFE_FAULT_CN_REG     = 0x15    #/* Analog Front-End Fault Detection Control */
TI_ADS1293_AFE_DITHER_EN_REG    = 0x16    #/* Enable Dithering in Signma-Delta */
TI_ADS1293_AFE_PACE_CN_REG      = 0x17    #/* Analog Pace Channel Output Routing Control */

TI_ADS1293_ERROR_LOD_REG        = 0x18    #/* Lead Off Detect Error Status */
TI_ADS1293_ERROR_STATUS_REG     = 0x19    #/* Other Error Status */
TI_ADS1293_ERROR_RANGE1_REG     = 0x1A    #/* Channel 1 Amplifier Out of Range Status */
TI_ADS1293_ERROR_RANGE2_REG     = 0x1B    #/* Channel 1 Amplifier Out of Range Status */
TI_ADS1293_ERROR_RANGE3_REG     = 0x1C    #/* Channel 1 Amplifier Out of Range Status */
TI_ADS1293_ERROR_SYNC_REG       = 0x1D    #/* Synchronization Error */


TI_ADS1293_R2_RATE_REG          = 0x21    #/* R2 Decimation Rate */
TI_ADS1293_R3_RATE1_REG         = 0x22    #/* R3 Decimation Rate for Channel 1 */
TI_ADS1293_R3_RATE2_REG         = 0x23    #/* R3 Decimation Rate for Channel 2 */
TI_ADS1293_R3_RATE3_REG         = 0x24    #/* R3 Decimation Rate for Channel 3 */
TI_ADS1293_P_DRATE_REG          = 0x25    #/* 2x Pace Data Rate */
TI_ADS1293_DIS_EFILTER_REG      = 0x26    #/* ECG Filter Disable */
TI_ADS1293_DRDYB_SRC_REG        = 0x27    #/* Data Ready Pin Source */
TI_ADS1293_SYNCOUTB_SRC_REG     = 0x28    #/* Sync Out Pin Source */
TI_ADS1293_MASK_DRDYB_REG       = 0x29    #/* Optional Mask Control for DRDYB Output */
TI_ADS1293_MASK_ERR_REG         = 0x2A    #/* Mask Error on ALARMB Pin */

TI_ADS1293_ALARM_FILTER_REG     = 0x2E    #/* Digital Filter for Analog Alarm Signals */
TI_ADS1293_CH_CNFG_REG          = 0x2F    #/* Configure Channel for Loop Read Back Mode */

TI_ADS1293_DATA_STATUS_REG      = 0x30    #/* ECG and Pace Data Ready Status */
TI_ADS1293_DATA_CH1_PACE_H_REG  = 0x31    #/* Channel1 Pace Data High [15:8] */
TI_ADS1293_DATA_CH1_PACE_L_REG  = 0x32    #/* Channel1 Pace Data Low [7:0] */
TI_ADS1293_DATA_CH2_PACE_H_REG  = 0x33    #/* Channel2 Pace Data High [15:8] */
TI_ADS1293_DATA_CH2_PACE_L_REG  = 0x34    #/* Channel2 Pace Data Low [7:0] */
TI_ADS1293_DATA_CH3_PACE_H_REG  = 0x35    #/* Channel3 Pace Data High [15:8] */
TI_ADS1293_DATA_CH3_PACE_L_REG  = 0x36    #/* Channel3 Pace Data Low [7:0] */
TI_ADS1293_DATA_CH1_ECG_H_REG   = 0x37    #/* Channel1 ECG Data High [23:16] */
TI_ADS1293_DATA_CH1_ECG_M_REG   = 0x38    #/* Channel1 ECG Data Medium [15:8] */
TI_ADS1293_DATA_CH1_ECG_L_REG   = 0x39    #/* Channel1 ECG Data Low [7:0] */
TI_ADS1293_DATA_CH2_ECG_H_REG   = 0x3A    #/* Channel2 ECG Data High [23:16] */
TI_ADS1293_DATA_CH2_ECG_M_REG   = 0x3B    #/* Channel2 ECG Data Medium [15:8] */
TI_ADS1293_DATA_CH2_ECG_L_REG   = 0x3C    #/* Channel2 ECG Data Low [7:0] */
TI_ADS1293_DATA_CH3_ECG_H_REG   = 0x3D    #/* Channel3 ECG Data High [23:16] */
TI_ADS1293_DATA_CH3_ECG_M_REG   = 0x3E    #/* Channel3 ECG Data Medium [15:8] */
TI_ADS1293_DATA_CH3_ECG_L_REG   = 0x3F    #/* Channel3 ECG Data Low [7:0] */

TI_ADS1293_REVID_REG            = 0x40    #/* Revision ID */
TI_ADS1293_DATA_LOOP_REG        = 0x50    #/* Loop Read Back Address */


#Useful definitions
ADS1293_READ_BIT                = 0x80
ADS1293_WRITE_BIT               = 0x7F