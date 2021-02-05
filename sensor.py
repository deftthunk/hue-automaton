class Sensor:
  '''
  Represents a HUE motion sensor device
  '''
  def __init__(self, name, uuid):
    self.name = name
    self.uuid = uuid
    self.light_level = None
    self.temp = None
    self.presence = None


  def Get_Light_Level(self):
    '''
    Returns a tuple with the values of 'daylight' and 'light level' (bool, int)
    
    To get lux from light level, use the following:
    lux = 10 ^ ((lightlevel - 1) / 10000)
    '''
    return self.light_level


  def Get_Temperature(self):
    '''
    Returns degrees celcius with two precision decimal places
    '''
    return (self.temp / 100)


  def Get_Presence(self):
    '''
    Returns bool, indicating if sensor has been tripped or not
    '''
    return self.presence


  def Update(self, raw_sensor_data):
    '''
    Used by an external mechanism to consistently push new sensor data to any/all sensor
    objects. HUE does not provide a callback function for when sensor data changes, so 
    this external mechanism will constantly poll the HUE bridge for all sensor data 
    ("raw_sensor_data"), and then each sensor object can pick out the relevant info to
    make available to the "Get_XXX()" functions.
    '''
    for key in raw_sensors.keys():
      raw_data = raw_sensors[key]
      
      if raw_data.get("type").find("ZLL") != -1:
        if self.check_uuid(raw_data["uniqueid"]):
          instrument = raw_data["type"]
          
          if instrument == "ZLLLightLevel":
            self.set_light_level(raw_data["state"])
          elif instrument == "ZLLTemperature":
            self.set_temp(raw_data["state"])
          elif instrument == "ZLLPresence":
            self.set_presence(raw_data["state"])
          else:
            print("Odd ERROR: Found instrument type {}".format(instrument))


  def check_uuid(self, test_uuid):
    '''
    Each physical sensor has several internal sensors (temp, light level, daylight) which
    get assigned seemingly random key IDs in 'raw_sensors'. More than one physical 
    sensor will create multiples of these internal sensors, making it hard to
    differentiate which instrument came from which sensor.
    
    Thankfully, the individual instruments share a common UUID base number, so we can
    track who belongs to what.
    '''
    return self.uuid == test_uuid[:-8]


  def set_light_level(self, state):
    '''
    Sets a tuple up containing the values of 'daylight' and 'lightlevel'
    
    Example of structure:
    State: {'dark': True, 'daylight': False, 
    'lastupdated': '2021-01-10T05:31:38', 'lightlevel': 8936}
    '''
    daylight = state["daylight"]
    level = state["lightlevel"]
    self.light_level = (daylight, level)


  def set_temp(self, state):
    '''
    Sets instance value for reported temperature
    
    Example of structure:
    State: {'lastupdated': '2021-01-10T05:33:40', 'temperature': 1899}
    '''
    temp = state["temperature"]
    self.temp = temp


  def set_presence(self, state):
    '''
    Sets instance value for reported presence indication
    
    Example of structure:
    State: ('lastupdated': '2021-01-10T05:33:50', 'presence': False}
    '''
    presence = state["presence"]
    self.presence = presence




