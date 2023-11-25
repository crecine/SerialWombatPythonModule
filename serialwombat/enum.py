NEUTRAL_BYTE = 0x55

SW_LOW = 0
SW_HIGH = 1
SW_INPUT = 2

class SerialWombatDataSource():
  SW_DATA_SOURCE_PIN_0 	= 0 # 16 bit public data provided by Pin 0
  SW_DATA_SOURCE_PIN_1 	= 1 # 16 bit public data provided by Pin 1
  SW_DATA_SOURCE_PIN_2 	= 2 # 16 bit public data provided by Pin 2
  SW_DATA_SOURCE_PIN_3 	= 3 # 16 bit public data provided by Pin 3
  SW_DATA_SOURCE_PIN_4 	= 4 # 16 bit public data provided by Pin 4
  SW_DATA_SOURCE_PIN_5 	= 5 # 16 bit public data provided by Pin 5
  SW_DATA_SOURCE_PIN_6 	= 6 # 16 bit public data provided by Pin 6
  SW_DATA_SOURCE_PIN_7 	= 7 # 16 bit public data provided by Pin 7
  SW_DATA_SOURCE_PIN_8 	= 8 # 16 bit public data provided by Pin 8
  SW_DATA_SOURCE_PIN_9 	= 9 # 16 bit public data provided by Pin 9
  SW_DATA_SOURCE_PIN_10 	= 10 # 16 bit public data provided by Pin 10
  SW_DATA_SOURCE_PIN_11 	= 11 # 16 bit public data provided by Pin 11
  SW_DATA_SOURCE_PIN_12 	= 12 # 16 bit public data provided by Pin 12
  SW_DATA_SOURCE_PIN_13 	= 13 # 16 bit public data provided by Pin 13
  SW_DATA_SOURCE_PIN_14 	= 14 # 16 bit public data provided by Pin 14
  SW_DATA_SOURCE_PIN_15 	= 15 # 16 bit public data provided by Pin 15
  SW_DATA_SOURCE_PIN_16 	= 16 # 16 bit public data provided by Pin 16
  SW_DATA_SOURCE_PIN_17 	= 17 # 16 bit public data provided by Pin 17
  SW_DATA_SOURCE_PIN_18 	= 18 # 16 bit public data provided by Pin 18
  SW_DATA_SOURCE_PIN_19 	= 19 # 16 bit public data provided by Pin 19
  SW_DATA_SOURCE_INCREMENTING_NUMBER 	= 65 # An number that increments each time it is accessed.
  SW_DATA_SOURCE_1024mvCounts 	= 66 # The number of ADC counts that result from a 1.024V reading
  SW_DATA_SOURCE_FRAMES_RUN_LSW 	= 67 # The number of frames run since reset, least significant 16 bits
  SW_DATA_SOURCE_FRAMES_RUN_MSW 	= 68 # The number of frames run since reset, most significant 16 bits
  SW_DATA_SOURCE_OVERRUN_FRAMES 	= 69 # The number of frames that ran more than 1mS
  SW_DATA_SOURCE_TEMPERATURE 	= 70 #The internal core temperature expressed in 100ths deg C
  SW_DATA_SOURCE_PACKETS_RECEIVED 	= 71 # The nubmer of incoming CMD packets that have been processed since reset rolls over at 65535 #
  SW_DATA_SOURCE_ERRORS 	= 72 #The number of incoming packets that have caused errors since reset rolls over at 65535 #
  SW_DATA_SOURCE_DROPPED_FRAMES 	= 73 # The number of times since reset that a frame ran so far behind that it crossed two subsequent 1ms boundaries, causing a permanent lost frame
  SW_DATA_SOURCE_SYSTEM_UTILIZATION 	= 74 # A number between 0 and 65535 that scales to the average length of pin processing frames between 0 and 1000mS
  SW_DATA_SOURCE_VCC_mVOLTS 	= 75 # The system source voltage in mV
  SW_DATA_SOURCE_VBG_COUNTS_VS_VREF 	= 76 # A/D conversion of VBG against VRef . Used for mfg calibration
  SW_DATA_SOURCE_LFSR 	= 78 # A Linear Feedback Shift Register that produces a Pseudo random sequence of 16 bit values
  SW_DATA_SOURCE_PIN_0_MV 	= 100 # Pin 0 public output expressed in mV for analog modes only #
  SW_DATA_SOURCE_PIN_1_MV 	= 101 # Pin 1 public output expressed in mV for analog modes only #
  SW_DATA_SOURCE_PIN_2_MV 	= 102 # Pin 2 public output expressed in mV for analog modes only #
  SW_DATA_SOURCE_PIN_3_MV 	= 103 # Pin 3 public output expressed in mV for analog modes only #
  SW_DATA_SOURCE_PIN_4_MV 	= 104 # Pin 4 public output expressed in mV for analog modes only #
  SW_DATA_SOURCE_PIN_16_MV 	= 116 # Pin 16 public output expressed in mV for analog modes only #
  SW_DATA_SOURCE_PIN_17_MV 	= 117 # Pin 17 public output expressed in mV for analog modes only #
  SW_DATA_SOURCE_PIN_18_MV 	= 118 # Pin 18 public output expressed in mV for analog modes only #
  SW_DATA_SOURCE_PIN_19_MV 	= 119 # Pin 19 public output expressed in mV for analog modes only #
  SW_DATA_SOURCE_2HZ_SQUARE 	= 164 # Square wave that alternates between 0 and 65535 every 256 frames
  SW_DATA_SOURCE_2HZ_SAW 	= 165 # Sawtooth wave that goes from 0 to 65535 to 0 every 512 frames
  SW_DATA_SOURCE_1HZ_SQUARE 	= 167 # Square wave that alternates between 0 and 65535 every 512 frames
  SW_DATA_SOURCE_1HZ_SAW 	= 168 # Sawtooth wave that goes from 0 to 65535 to 0 every 1024 frames
  SW_DATA_SOURCE_2SEC_SQUARE 	= 170 #Square wave that alternates between 0 and 65535 every 1024 frames
  SW_DATA_SOURCE_2SEC_SAW 	= 171 #Sawtooth wave that goes from 0 to 65535 to 0 every 2048 frames
  SW_DATA_SOURCE_8SEC_SQUARE 	= 173 #Square wave that alternates between 0 and 65535 every 4096 frames
  SW_DATA_SOURCE_8SEC_SAW 	= 174 #Sawtooth wave that goes from 0 to 65535 to 0 every 8192 frames
  SW_DATA_SOURCE_65SEC_SQUARE 	= 176 # Square wave that alternates between 0 and 65535 every 32768 frames
  SW_DATA_SOURCE_65SEC_SAW 	= 177  SW_#Sawtooth wave that goes from 0 to 65535 to 0 every 65536 frames

ERROR_HOST_INCORRECT_NUMBER_BYTES_WRITTEN = 0x10000 # Write routine returned wrong number of bytes
ERROR_HOST_DATA_TOO_LONG = 0x10001  # endTransmission returned data too long
ERROR_HOST_NACK_ADDRESS = 0x10002  # endTransmission returned address NACK
ERROR_HOST_NACK_DATA = 0x10003   # endTransmission returned data NACK
ERROR_HOST_OTHER_I2C_ERROR = 0x10004 # endTransmission returned other error

WOMBAT_MAXIMUM_PINS = 20

class SerialWombatCommands():
  CMD_ECHO 	= '!'
  CMD_READ_BUFFER_ASCII 	= 'G'
  CMD_ASCII_SET_PIN 	= 'P'
  CMD_RESET 	= 'R'
  CMD_SET_BUFFER_ASCII 	= 'S'
  CMD_RESYNC 	= 'U'
  CMD_VERSION 	= 'V'
  CMD_SUPPLYVOLTAGE 	= 'v'
  COMMAND_BINARY_READ_PIN_BUFFFER 	= 0x81
  COMMAND_BINARY_SET_PIN_BUFFFER 	= 0x82
  COMMAND_BINARY_READ_USER_BUFFER 	= 0x83
  COMMAND_BINARY_WRITE_USER_BUFFER 	= 0x84
  COMMAND_BINARY_WRITE_USER_BUFFER_CONTINUE 	= 0x85
  COMMAND_BINARY_QUEUE_INITIALIZE 	= 0x90
  COMMAND_BINARY_QUEUE_ADD_BYTES 	= 0x91
  COMMAND_BINARY_QUEUE_ADD_7BYTES 	= 0x92
  COMMAND_BINARY_QUEUE_READ_BYTES 	= 0x93
  COMMAND_BINARY_QUEUE_INFORMATION 	= 0x94
  COMMAND_BINARY_CFG 	= 0x9F
  COMMAND_BINARY_READ_RAM 	= 0xA0
  COMMAND_BINARY_READ_FLASH 	= 0xA1
  COMMAND_BINARY_READ_EEPROM 	= 0xA2
  COMMAND_BINARY_WRITE_RAM 	= 0xA3
  COMMAND_BINARY_WRITE_FLASH 	= 0xA4
  COMMAND_CALIBRATE_ANALOG 	= 0xA5
  COMMAND_ENABLE_2ND_UART 	= 0xA6
  COMMAND_READ_LAST_ERROR_PACKET 	= 0xA7
  COMMAND_UART0_TX_7BYTES 	= 0xB0
  COMMAND_UART0_RX_7BYTES 	= 0xB1
  COMMAND_UART1_TX_7BYTES 	= 0xB2
  COMMAND_UART1_RX_7BYTES 	= 0xB3
  CONFIGURE_PIN_MODE0 	= 200
  CONFIGURE_PIN_MODE1 	= 201
  CONFIGURE_PIN_MODE2 	= 202
  CONFIGURE_PIN_MODE3 	= 203
  CONFIGURE_PIN_MODE4 	= 204
  CONFIGURE_PIN_MODE5 	= 205
  CONFIGURE_PIN_MODE6 	= 206
  CONFIGURE_PIN_MODE7 	= 207
  CONFIGURE_PIN_MODE8 	= 208
  CONFIGURE_PIN_MODE9 	= 209
  CONFIGURE_PIN_MODE10 	= 210
  CONFIGURE_PIN_OUTPUTSCALE 	= 210
  CONFIGURE_PIN_INPUTPROCESS 	= 211
  CONFIGURE_PIN_MODE_HW_0 	= 220
  CONFIGURE_CHANNEL_MODE_HW_1 	= 221
  CONFIGURE_CHANNEL_MODE_HW_2 	= 222
  CONFIGURE_CHANNEL_MODE_HW_3 	= 223

PIN_MODE_DIGITALIO = 0
PIN_MODE_CONTROLLED = 1
PIN_MODE_ANALOG_INPUT = 2
PIN_MODE_SERVO = 3
PIN_MODE_THROUGHPUT_CONSUMER = 4
PIN_MODE_QUADRATURE_ENC = 5
PIN_MODE_WATCHDOG = 7
PIN_MODE_PROTECTEDOUTPUT = 8
PIN_MODE_DEBOUNCE = 10
PIN_MODE_TM1637 = 11
PIN_MODE_MODEWS2812 = 12
PIN_MODE_SW_UART = 13
PIN_MODE_INPUT_PROCESSOR = 14
PIN_MODE_MATRIX_KEYPAD = 15
PIN_MODE_PWM = 16
PIN_MODE_PULSE_TIMER = 18
PIN_MODE_UART_TXRX = 17
PIN_MODE_FRAME_TIMER = 21
PIN_MODE_SW18AB_CAPTOUCH = 22
PIN_MODE_UART1_RX_TX = 23
PIN_MODE_RESISTANCEINPUT = 24
PIN_MODE_PULSE_ON_CHANGE = 25
PIN_MODE_HS_SERVO = 26
PIN_MODE_ULTRASONIC_DISTANCE = 27
PIN_MODE_LIQUIDCRYSTAL = 28
PIN_MODE_HS_CLOCK = 29
PIN_MODE_HS_COUNTER = 30
PIN_MODE_VGA = 31
PIN_MODE_PS2KEYBOARD = 32
PIN_MODE_UNKNOWN = 0xFF