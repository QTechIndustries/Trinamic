class SPI_STATUS():
	self.address = None
	self.type = ''
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

class GCONF():

	self.address = 0x00
	self.type = 'RW'
	self.bytes = bytearray(1)
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
	self.address = 0x01
	self.type = 'R+WC'
	# Bits
	self.reset = False
	self.drv_err = False
	self.uv_cp = False


