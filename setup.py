import phue
import sys
import configparser
from room import Room


def read_config():
  config = configparser.ConfigParser()
  ret = config.read("config.ini")
  if ret == []:
    print("unable to find 'config.ini', exiting")
    sys.exit(1)

  return config


def connect(config):
  bridge_ip = config["settings"]["bridge"]
  b = phue.Bridge(bridge_ip)
  b.connect()
  return b


def build_rooms(b):
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


def main():
  config = read_config()
  b = connect(config)
  rooms = build_rooms(b)


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



main()
