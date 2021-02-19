class Expression:
    def __init__(self,left,op,right):
        self.left = left
        self.right = right
        self.op = op


class Test(Expression):
    pass


class Assignment(Expression):
    pass


class Directory:
    def __init__(self, bridge, rooms, sensors, lights):
        self.bridge = bridge
        self.rooms = rooms
        self.sensors = sensors
        self.events = None
        self.lights = lights
        self.obj_lookup = {
                "room"          : {},   ## normalized_name : object
                "sensor"        : {},
                "light"         : {},
        }
        self.api_lookup = {
                "sensor"        : sensor_api_lookup,
                "room"          : room_api_lookup,
                "light"         : light_api_lookup,
                "time"          : time_api_lookup,
                "date"          : date_api_lookup,
        }
        self.changelog = {}


    def Get_Sensor_Names(self):
        return self.sensors.keys()
    
    
    def Get_Room_Names(self):
        return self.rooms.keys()


    def Get_Light_Names(self):
        return self.lights.keys()



## lookup tables
sensor_api_lookup = {
    "daylight"      : ("Get_Light_Level", (bool, int)),
    "temp"          : ("Get_Temperature", float),
    "motion"        : ("Get_Presence", bool),
}

room_api_lookup = {
    "level"         : ("Brightness", int),
    "colortemp"     : ("Color_Temperature", int),
}

light_api_lookup = {
    "level"         : ("Brightness", int),
    "colortemp"     : ("Color_Temperature", int),
    "saturation"    : ("Saturation", int),
    "colorxy"       : ("ColorXY", (float, float)),
    "hue"           : ("Hue", int),
}

time_api_lookup = {
    "wait"          : ("placeholder", int),
    "now"           : ("placeholder", str),
    "sunrise"       : ("placeholder", bool),
    "sunset"        : ("placeholder", bool),
}

date_api_lookup = {
    "today"         : ("plateholder", str),
    "daydate"       : ("placeholder", int),
    "dayofweek"     : ("placeholder", str),
}











