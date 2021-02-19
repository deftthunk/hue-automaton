import phue
import sensor
import time
import setup


d = setup.Setup()
print("completed setup.Setup")




'''
while True:
#def test():
    raw_sensors = b.get_sensor()
    for sensor in raw_sensors.values():
        if sensor.get("type").find("ZLL") != -1:
            if sensor["type"] == "ZLLPresence":
                state = sensor["state"]
                if state["presence"] == True:
                    print(sensor["name"])
    
    time.sleep(1)

#test()
'''


