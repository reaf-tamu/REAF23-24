
import time
from adafruit_servokit import ServoKit
#import adafruit_motor.servo
#import keyboard
from pynput import keyboard

kit = ServoKit(channels = 16)

A1 = kit.servo[0].angle = 90
A2 = kit.servo[1].angle = 90
A3 = kit.servo[2].angle = 90
A4 = kit.servo[3].angle = 90
M1 = kit.servo[7].angle = 90
M2 = kit.servo[9].angle = 90
M3 = kit.servo[10].angle = 90
M4 = kit.servo[13].angle = 90

def set_speed(speed, motor):
	kit.servo[motor].angle = speed
	return

class Motor:
	def __init__(self, name):
		self.name = name
		self.speed = 90
		self.prev_speed = self.speed
	def setSpeed(self, speed):
		self.speed = speed

	def run(self):
		if self.prev_speed != self.speed:
			print("boop")
			kit.servo[self.name].angle = self.speed
			self.prev_speed = self.speed
		else:
			return
	def stop(self):
		kit.servo[name] = 90

A1 = Motor(0)
A2 = Motor(1)
A3 = Motor(2)
A4 = Motor(3)
M1 = Motor(7)
M2 = Motor(9)
M3 = Motor(10)
M4 = Motor(13)

M4.setSpeed(90)
M4.run()
M3.setSpeed(90)
M3.run()
M2.setSpeed(90)
M2.run()
M1.setSpeed(90)
M1.run()
A4.setSpeed(90)
A4.run()
A3.setSpeed(90)
A3.run()
A2.setSpeed(90)
A2.run()
A1.setSpeed(90)
A1.run()

print("ready")
def on_key_release(key):
	if key == keyboard.Key.esc:
		return False  # Stop the listener
	try:
		if key.char == 'a':
			print("right")
			"""
			M4.setSpeed(100)
			M4.run()
			
			A4.setSpeed(80)
			A4.run()
			"""
		if key.char == "s":
			print("left")
			"""
			M4.setSpeed(80)
			M4.run()

			A4.setSpeed(100)
			A4.run()
			"""
		if key.char == "d":
			"""
			print("stop")
			M4.setSpeed(90)
			M4.run()

			A4.setSpeed(90)
			A4.run()
			"""
	except AttributeError:
		pass

# Collect events until released
with keyboard.Listener(on_release=on_key_release) as listener:
	listener.join()



# this code works
# thanks chatGPT
"""
from pynput import keyboard

def on_key_release(key):
    if key == keyboard.Key.esc:
        return False  # Stop the listener
    try:
        if key.char == 'a':
            print("You pressed 'a'.")
    except AttributeError:
        pass

# Collect events until released
with keyboard.Listener(on_release=on_key_release) as listener:
    listener.join()
"""
"""
print("starting")

def f1():
	print("speed 1")
def f2():
	print("speed 2")
def b1():
	print("back it up")
def stop():
	print("I'm tired of this grandpa")

print("ready")
keyboard.add_hotkey("a", lambda: print("works"))
keyboard.add_hotkey("s", f2)
keyboard.add_hotkey("d", b1)
keyboard.add_hotkey("x", stop)

print("still ready")
keyboard.wait()

print("oops")
"""


"""
on = True
print("ready")

# testing one thruster in bucket
while on == True:
	print("start")
	if keyboard.read_key() == "a":
		print("speed 1")
		# M4.setSpeed(100)
		#M4.run()
	elif keyboard.read_key() == "s":
		print("speed 2")
		#M4.setSpeed(105)
		#M4.run()
	elif keyboard.read_key() == "f":
		print("backward")
		#M4.setSpeed(80)
		#M4.run()
	elif keyboard.read_key() == "o":
		print("stopping")
		#M4.setSpeed(90)
		#M4.run()
	print("oops")
"""

"""
def test():
	#while True:
	#	M4.setSpeed(95)
	#	M4.run()
	print("running")

def stop():
	M4.setSpeed(90)
	M4.run()
	M3.setSpeed(90)
	M3.run()
	M2.setSpeed(90)
	M2.run()
	M1.setSpeed(90)
	M1.run()
	A4.setSpeed(90)
	A4.run()
	A3.setSpeed(90)
	A3.run()
	A2.setSpeed(90)
	A2.run()
	A1.setSpeed(90)
	A1.run()

keyboard.add_hotkey('e',test())
keyboard.add_hotkey("s",stop())
keyboard.wait()
"""

"""
while True:
	if keyboard.is_pressed('e'):
		test()
		print('e is pressed')
	elif keyboard.is_pressed('s'):
		stop()
"""
