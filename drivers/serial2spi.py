import serial, struct

class Serial2Spi:
	def __init__(self):
		self.s = None

	def connect(self, port):
		self.s = serial.Serial(port, 115200)

	def disconnect(self):
		if self.s:
			self.s.close()

	def write_reg(self, reg, val):
		if self.s:
			self.s.write(struct.pack('>BI', reg | 0x80, val))
			return self.s.read(1)

	def read_reg(self, reg):
		self.s.write(struct.pack('>B', reg & 0x7F))
		return self.s.read(1), self.s.read(4)