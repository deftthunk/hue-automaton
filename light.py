class Light:
    def __init__(self, light_data, bridge):
        self.name = light_data["name"]
        self.light_data = light_data
        self.bridge = bridge
        
    
    def Is_On(self):
        state = self.light_data["state"]
        return state["on"]
    

    def Brightness(self, value=None):
        '''
        Range: 0 - 254 (0 is not off)
        If user specifies '0', interpret as "off"
        '''
        if value == None:
            state_dict = self.light_data["state"]
            return state_dict["bri"]
        elif type(value) == int and 0 <= value <= 254:
            self.bridge.set_light(self.name, "bri", value)
            return value
        else:
            print("WARN: invalid value for {} brightness level (0-254)".format(self.name))
            return None


    def Hue(self, value=None):
        '''
        Range: 0 - 65535
        '''
        if value == None:
            state_dict = self.light_data["state"]
            return state_dict["bri"]
        elif type(value) == int and 0 <= value <= 254:
            self.bridge.set_light(self.name, "hue", value)
        return state_dict["hue"]


    def Colormode(self, value=None):
        '''
        Get the color mode of the light [hs|xy|ct]
        '''
        pass


    def Saturation(self):
        '''
        Range: 0 - 254 (0 is white, 254 is most saturated)
        '''
        state_dict = self.light_data["state"]
        return state_dict["sat"]


    def Color_Temperature(self, value=None):
        '''
        color temp
        range: 154 (cold) to 500 (warm)
        '''
        if value == None:
            state_dict = self.light_data["state"]
            return state_dict["ct"]
        elif type(value) == int and 154 <= value <= 500:
            self.bridge.set_light(self.name, "ct", value)
            return value
        else:
            print("WARN: invalid value for {} colortemp (154-500)".format(self.name))
            return None


