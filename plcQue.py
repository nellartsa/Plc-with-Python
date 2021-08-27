from pymodbus.client.sync import ModbusTcpClient

# coils:
  # Y(0-255) : 0 - 255
  # X(0-255) : 1000 - 1255
  # M(0-2001): 2000 - 4001
  # S(0-999) : 6000 - 6999
  # T(0-255) : 9000 - 9255 (current_value=False)
  # C(0-255) : 9500 - 9755 (current_value=False)

# registers
  # R(0-4167)    : 0    - 4167
  # R(5000-5998) : 5000 - 5998 (holding or ror)
  # D(0-2998)    : 6000 - 8998
  # T(0-255)     : 9000 - 9255 (current_value = True)
  # C(0-199)     : 9500 - 9699 (16bit, current_value=True)
  # C(200-255)   : 9700 - 9811 (32bit, current_value=True) double offset

class GetSetPlcData():
  def __init__(self, ip, port, logger):
    self.client = ModbusTcpClient(host=ip, port=port)
    self.logger = logger
    self.client.connect()

  def get_coil(self, c):
    if c[:1].lower() == "x":
      try:
        if int(c[1:]) < 0 or int(c[1:]) > 255:
          self.logger.error("Fetch Coil Input is out or range")
        else:
          address = int(c[1:]) + 1000
          val = self.client.read_coils(address).bits[0]
          self.client.close()
          return val
      except Exception as e:
        self.logger.exception(e)
        self.logger.error("Cath Fetch Coil Input : %s" %c)

    elif c[:1].lower() == "m":
      try:
        if int(c[1:]) < 0 or int(c[1:]) > 2001:
          self.logger.error("Fetch Memory is out of range")
        else:
          address = int(c[1:]) + 2000
          val = self.client.read_coils(address).bits[0]
          self.client.close()
          return val
      except Exception as e:
        self.logger.exception(e)
        self.logger.error("Can't Fetch Memory %s" %c)

    elif c[:1].lower() == "y":
      try:
        if int(c[1:]) < 0  or int(c[1:]) > 255:
          self.logger.error("Fetch Coil Output is out of range")
        else:
          address = int(c[1:])
          val = self.client.read_coils(address).bits[0]
          self.client.close()
          return val
      except Exception as e:
        self.logger.exception(e)
        self.logger.error("Can't Fetch Coil Output %s" %c)

    else:
      self.logger.error("Fetch Coil has an Invalid Symbol : %s" %c)

  def set_coil(self, c, value):
    if c[:1].lower() == "x":
      try:
        if int(c[1:]) < 0 or int(c[1:]) > 255:
          self.logger.error("Set Coil Input is out of range")
        else:
          address = int(c[1:]) + 2000
          self.client.write_coil(address, int(value))
          self.client.close()
      except Exception as e:
        self.logger.exception(e)
        self.logger.error("Can't Set Coil Input %s" %c)

    elif c[:1].lower() == "m":
      try:
        if int(c[1:]) < 0 or int(c[1:]) > 2001:
          self.logger.error("Set Memory is out of range")
        else:
          address = int(c[1:]) + 2000
          self.client.write_coil(address, int(value))
          self.client.close()
      except Exception as e:
        self.logger.exception(e)
        self.logger.error("Can't Set Memory %s" %c)

    elif c[:1].lower() == "y":
      try:
        if int(c[1:]) < 0  or int(c[1:]) > 255:
          self.logger.error("Set Coil Output is out of range")
        else:
          address = int(c[1:])
          self.client.write_coil(address, int(value))
          self.client.close()
      except Exception as e:
        self.logger.exception(e)
        self.logger.error("Can't Set Coil Output %s" %c)
        
    else:
      self.logger.error("Set Coil has an Invalid Symbol : %s" %c)

  def get_register(self, r):
    if r[:1].lower() == "r":
      try:
        if int(r[1:]) < 0 or int(r[1:]) > 4167:
          self.logger.error("Fetch Register is out of range ")
        else:
          address = int(r[1:])
          val = self.client.read_holding_registers(address).registers[0]
          self.client.close()
          return val
      except Exception as e:
        self.logger.exception(e)
        self.logger.error("Can't Fetch Register %s" %r)
    else:
      self.logger.error("Fetch Register has invalid symbol : %s" %r)

  def set_register(self, r, value):
    if r[:1].lower() == "r":
      try:
        if int(r[1:]) < 0 or int(r[1:]) > 4167:
          self.logger.error("Set Register is out of range")
        else:
          address = int(r[1:])
          self.client.write_register(address, int(value))
          self.client.close()
      except Exception as e:
        self.logger.exception(e)
        self.logger.error("Can't Set Register %s" %r)
    else:
      self.logger.error("Set Register has invalid symbol : %s" %r)
