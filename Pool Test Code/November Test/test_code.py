from brping import Ping1D
import ms5837
from vnpy import *

"""
# connect to pinger
myPing = Ping1D()
myPing.connect_serial("/dev/ttyUSB1", 115200)
if myPing.initialize() is False:
    print("Failed to initialize Ping!")
    exit(1)
# suggestions to improve accuracy
# set_gain_index did not exist
myPing.set_ping_interval(29)
myPing.set_speed_of_sound(1500)
# myPing.set_gain_index(2)
"""

# connect to  pressure sensor
sensor = ms5837.MS5837_02BA()
# We must initialize the sensor before reading it
if not sensor.init():
        print("Sensor could not be initialized")
        exit(1)
# We have to read values from sensor to update pressure and temperature
if not sensor.read():
    print("Sensor read failed!")
    exit(1)
pressure = sensor.pressure(ms5837.UNITS_psi)
freshwaterDepth = sensor.depth() # default is freshwater
sensor.setFluidDensity(ms5837.DENSITY_SALTWATER)
saltwaterDepth = sensor.depth() # No nead to read() again
sensor.setFluidDensity(1000) # kg/m^3


# connect to vnav
s = VnSensor()
s.connect("/dev/ttyUSB0",115200)

# in function
below = myPing.get_distance_simple()
top = freshwaterDepth
orientation = s.read_yaw_pitch_roll()
print("below = ", below)
print("top = ", top)
print("gyro = ", orientation)
print()

