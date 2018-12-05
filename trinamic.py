class Trinamic():
    def __init__(self, read_register, write_register):
        self.read_register = read_register
        self.write_register = write_register

        self._IHOLD_IRUN = None  # 0x10 W
        self._VACTUAL = None  # 0x21 R
        self._VSTART = None  # 0x23 W
        self._AMAX = None  # 0x26 W
        self._VMAX = None  # 0x27 W
        self.reset_drive()

        # Easy Config
        s2 = [0x6C, bytes([0x00, 0x01, 0x00, 0xC3])]  # Chopper Mode
        s3 = [0x10, bytes([0x00, 0x06, 0x03, 0x0A])]  # Hold/run Current
        s4 = [0x20, bytes([0x00, 0x00, 0x00, 0x01])]  # Velocity Mode
        s5 = [0x26, bytes([0x00, 0x01, 0x23, 0x45])]  # ACceleration
        stuff = [s2, s3, s4, s5]

        for msg in stuff:
            self.write_register(msg[0], msg[1])

    # VACTUAL Register
    @property
    def VACTUAL(self):
        register = 0x21
        data = self.read_register(register)
        self._VACTUAL = struct.unpack(">I", data)[0]
        return self._VACTUAL

    # VSTART Register
    @property
    def VSTART(self):
        return self._VSTART

    @VSTART.setter
    def VSTART(self, val):
        register = 0x23
        valb = struct.pack(">i", val)
        self.write_register(register, valb)
        self._VSTART = val

    # VMAX Register
    @property
    def VMAX(self):
        return self._VMAX

    @VMAX.setter
    def VMAX(self, vel):
        register = 0x27
        velb = struct.pack(">i", vel)
        self.write_register(register, velb)
        self._VMAX = vel

    # AMAX Register
    @property
    def AMAX(self):
        return self._AMAX

    @AMAX.setter
    def AMAX(self, val):
        register = 0x26
        valb = struct.pack(">i", val)
        self.write_register(register, valb)
        self._AMAX = val

    # Send Reset Drive Command
    def reset_drive(self):
        self.write_register(0x01, bytes([0x00, 0x00, 0x00, 0x00]))