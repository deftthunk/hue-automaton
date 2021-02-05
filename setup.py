import phue
import sys
import configparser
import time
from room import Room
from sensor import Sensor
from pprint import PrettyPrinter


def Read_Config():
  config = configparser.ConfigParser()
  ret = config.read("config.ini")
  if ret == []:
    print("unable to find 'config.ini', exiting")
    sys.exit(1)

  return config


def Connect(config):
  bridge_ip = config["settings"]["bridge"]
  b = phue.Bridge(bridge_ip)
  b.connect()
  return b


def Build_Rooms(b):
  rooms = {}
  groups = b.get_group()
  lights = b.get_light_objects("id")

  for i in groups.keys():
    room_data = groups[i]

    ## get room's light objects
    light_data = {}
    light_indexes = room_data["lights"]

    for j in light_indexes:
      l_id = int(j)
      light_data[lights[l_id].name] = lights[l_id]

    ## create new room object
    new_room = Room(room_data, light_data, b)
    rooms[new_room.name] = new_room

  return rooms


def Build_Sensors(b):
  sensors = {}
  raw_sensors = b.get_sensor()
  
  for key in raw_sensors.keys():
    raw_data = raw_sensors[key]
    if raw_data.get("type").find("ZLLPresence") != -1:
      uuid = raw_data["uniqueid"]
      name = raw_data["name"]
      
      new_sensor = Sensor(name, uuid)
      sensors[name] = new_sensor
    
  return sensors


def start():
  pp = PrettyPrinter()
  config = Read_Config()
  b = Connect(config)

  sensors = Build_Sensors(b)
  rooms = Build_Rooms(b)

  for s in sensors.keys():
    print("{} ({})".format(s, str(type(sensors[s]))))

  for r in rooms.keys():
    print("{} ({})".format(r, str(type(rooms[r]))))
    for l in rooms[r].Get_Lights():
      print("\t{}".format(str(l)))



start()


'''
  def sensors():
    sensors = Build_Sensors(b)


  def rooms():
    rooms = Build_Rooms(b)

    den = rooms["Den"]
    print("Den: ", den.Is_Any_On())
    print("number of lights: ", den.Get_Num_Lights())
    bri = den.Get_Brightness()
    print("bright: ", str(bri))
  
    from time import sleep
    den.Set_Brightness(254)
    sleep(2)
    print("bri: ", str(den.Get_Brightness()))
    sleep(1)
    print("resetting...")
    den.Set_Brightness(bri)
    sleep(2)
    print("bri: ", str(den.Get_Brightness()))
'''




