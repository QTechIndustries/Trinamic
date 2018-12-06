# NOTATION OF R/W FIELD
# R - Read only
# W - Write only
# R/W - Read- and writable register
# R+C - Clear upon read

# 4.1.2 SPI Status Bits
# BACKWARDS FLIP ALL THE DATA BITS
class SPI_STATUS():
	def __init__(self):
		self.address = None
		self.bytes = bytearray(1)
		# Data type =
		self.status_stop_r = None
		self.status_stop_l = None
		self.position_reached = None
		self.velocity_reached = None
		self.standstill = None
		self.sg2 = None
		self.driver_error = None
		self.reset_flag = None

# Register Classes

class GCONF():
	def __init__(self):
		self.address = 0x00
		self.type = 'RW'
		self.bytes = bytearray(4)
		# Data type =
		self.recalibrate = False
		self.fasstandstill = False
		self.en_pwm_mode = False
		self.multistep_filt = False
		self.shaft = False
		self.diag0_error = False #only with SD_MODE = 1
		self.diag0_optw = False
		self.diag0_stall = False
		self.diag0_step = False
		self.diag1_stall = False
		self.diag1_step = False
		self.diag1_index = False
		self.diag1_onstate = False
		self.diag1_steps_skipped = False
		self.diag0_int_pushpull = False
		self.diag1_poscomp_pushpull = False
		self.small_hysteresis = False
		self.stop_enable = False
		self.direct_mode = False
		self.test_mode = False

class GSTAT():
	def __init__(self):
		self.address = 0x01
		self.type = 'R+WC'
		# Bits
		self.reset = False
		self.drv_err = False
		self.uv_cp = False

class IFCNT():
	def __init__(self):
		self.address = 0x02
		self.type = 'R'
		self.bytes = bytearray(4)
		#
		self.IFCNT = None

class SLAVECONF():
    def __init__(self):
        self.address = 0x03
        self.type = 'W'
        self.bytes = bytearray(4)
        #
        self.SLAVEADDR = None
        self.SENDDELAY = None

class IOIN():
    def __init__(self):
        self.address = 0x04
        self.type = 'R'
        self.bytes = bytearray(4)
        #
        self.REFL_STEP = None
        self.REFR_DIR = None
        self.ENCB_DCEN_CFG4 = None
        self.ENCA_DCEN_CFG5 = None
        self.DRV_ENN = None
        self.ENC_N_DCO_CFG6 = None
        self.SD_MODE = None
        self.SWCOMP_IN = None
        self.VERSION = None

class OUTPUT():
    def __init__(self):
        self.address = 0x04
        self.type = 'W'
        self.bytes = bytearray(4)
        #
        self.OUTPUT = None

class X_COMPARE():
    def __init__(self):
        self.address = 0x05
        self.type = 'W'
        self.bytes = bytearray(4)
        #
        self.X_COMPARE = None

class OTP_PROG():
    def __init__(self):
        self.address = 0x06
        self.type = 'W'
        self.bytes = bytearray(4)
        #
        self.OTPBIT = None
        self.OTPBYTE = None
        self.OTPMAGIC = None

class OTP_READ():
    def __init__(self):
        self.address = 0x07
        self.type = 'R'
        self.bytes = bytearray(4)
        #
        self.OTP0 = None

class FACTORY_CONF():
    def __init__(self):
        self.address = 0x08
        self.type = 'RW'
        self.bytes = bytearray(4)
        #
        self.FCLKTRIM = None

class CoolConf:
	def __init__(self):
		self.address = 0x6D
		self.type = 'W'
		self.bytes = bytearray(4)
		#
		self.semin = None
		self.seup = None
		self.semax = None
		self.sedn = None
		self.seimin = None # bool
		self.sgt = None
		self.sfilt = None # bool

class DcCtrl:
	def __init__(self):
		self.address = 0x6E
		self.type = 'W'
		self.bytes = bytearray(3)
		#
		self.dc_time = None # 0-1023
		self.sc_sg = None # 0-255

class Drv_Status:
	def __init__(self):
		self.address = 0x6F
		self.type = 'R'
		self.bytes = bytearray(4)
		#
		self.sg_result = None # 0-1023
		self.s2vsa = None # bool
		self.s2vsb = None # bool
		self.stealth = None # bool
		self.fsactive = None # bool
		self.csactual = None # 0-31
		self.stallguard = None # bool
		self.ot = None # bool
		self.otpw = None # bool
		self.s2ga = None # bool
		self.s2gb = None # bool
		self.ola = None # bool
		self.olb = None # bool

class PwmConf:
	def __init__(self):
		self.address = 0x70
		self.type = 'W'
		self.bytes = bytearray(4)
		#
		self.pwm_ofs = 0xE # 0-255
		self.pwm_grad = 0x1 # 0-255
		self.pwm_freq = 0x0 # 0-3
		self.pwm_autoscale = False
		self.pwm_autograd =False
		self.freewheel =0x0 # 0-3
		self.pwm_reg = 0x4 # 1-15
		self.pwm_lim = 0xC # 0-15

class Pwm_Scale:
	def __init__(self):
		self.address = 0x71
		self.type = 'R'
		self.bytes = bytearray(3)
		#
		self.pwm_scale_sum = None # 0-255
		self.pwm_scale_auto = None # -255-255

class Pwm_Auto:
	def __init__(self):
		self.address = 0x72
		self.type = 'R'
		self.bytes = bytes(1)
		#
		self.pwm_auto = None # 0-255

class Lost_Steps:
	def __init__(self):
		self.address = 0x73
		self.type = 'R'
		self.bytes = bytearray(4)
		#
		self.lost_steps = None # 0-0xFFFFFFFF