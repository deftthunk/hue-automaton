class Room:
  '''
  Represents a HUE "room" or "zone" object and all its HUE devices (lights, sensors, etc)
  '''
  def __init__(self, room_data, light_data, bridge):
    self.name = room_data["name"]
    self.room_data = room_data
    self.light_data = light_data
    self.bridge = bridge


  def Is_Any_On(self):
    '''
    Returns True if any devices are on
    '''
    state = self.room_data["state"]
    return state["any_on"]


  def Is_All_On(self):
    '''
    Returns True if all devices are on
    '''
    state = self.data["state"]
    return state["all_on"]


  def Room_Type(self):
    '''
    Returns "Room" or "Zone"
    '''
    return self.type


  def Get_Num_Lights(self):
    return len(self.light_data)


  def Get_Brightness(self):
    '''
    Range: 0 - 254 (0 is not off)
    '''
    action_dict = self.room_data["action"]
    return action_dict["bri"]


  def Set_Brightness(self, value=200):
    '''
    Range: 0 - 254 (0 is not off)
    '''
    if type(value) == int and 0 <= value <= 254:
      self.bridge.set_group(self.name, "bri", value)
      return value
    else:
      return -1



  def Get_Hue(self):
    action_dict = self.room_data["action"]
    return action_dict["hue"]


  def Get_Saturation(self):
    action_dict = self.room_data["action"]
    return action_dict["sat"]


  def Get_Color_Temp(self):
    '''
    color temp
    range: 154 (cold) to 500 (warm)
    '''
    action_dict = self.room_data["action"]
    return action_dict["ct"]


  def Set_Color_Temp(self, value=300):
    '''
    color temp
    range: 154 (cold) to 500 (warm)
    '''
    if type(value) == int and 154 <= value <= 500:
      self.bridge.set_group(self.name, "ct", value)
      return value
    else:
      return -1


  def Get_Lights(self):
    return self.Get_Light()


  def Get_Light(self, light=None):
    '''
    Returns a given light object (either by name or id)
    If no argument given, returns all light objects
    '''
    if light == None:
      return self.light_data
    elif type(light) == int:
      for v in self.light_data.values():
        if v.light_id == light:
          return v
    elif type(light) == str:
      return self.light_data[light]


  def Get_Light_Attribute(self, light, attribute):
    '''
    asdf
    '''
    l = self.Get_Light(light)


  




