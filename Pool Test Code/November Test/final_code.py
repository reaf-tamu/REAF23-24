# imports
import time
from adafruit_servokit import ServoKit
# import adafruit_motor.servo
# import keyboard
import cv2			#Import the cv2 library to gather camera images
from pynput import keyboard


# initiate thrusters
kit = ServoKit(channels = 16)

# Turn OFF all thrusters
A1 = kit.servo[0].angle = 90
A2 = kit.servo[1].angle = 90
A3 = kit.servo[2].angle = 90
A4 = kit.servo[3].angle = 90
M1 = kit.servo[7].angle = 90
M2 = kit.servo[9].angle = 90
M3 = kit.servo[10].angle = 90
M4 = kit.servo[13].angle = 90

# servo.angle == 90

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
			#print("boop")
			kit.servo[self.name].angle = self.speed
			self.prev_speed = self.speed
		else:
			return
	def stop(self):
		kit.servo[name] = 90

# set thruster pins
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

"""
cap = cv2.VideoCapture(0)	#Set the camera to record using the default camera

# FIXME: figure out where to put this in the code
while True: 		#To show camera feed continuously, use an infinite while loop
    ret,img=cap.read()		#Capture the video frame by frame
    cv2.imshow('Video', img)	# Display the resulting frame

    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break
"""

print("ready")
def on_key_release(key):
	if key == keyboard.Key.esc:
		return False  # Stop the listener
	try:
		# forward
		if key.char == "w":
			print("forward")
			M4.setSpeed(100)
			M1.setSpeed(100)
			A3.setSpeed(100)
			A1.setSpeed(100)
			M4.run()
			M1.run()
			A3.run()
			A1.run()
		
		# backward
		if key.char == "s":
			print("backward")
			M4.setSpeed(80)
			M1.setSpeed(80)
			A3.setSpeed(80)
			A1.setSpeed(80)
			M4.run()
			M1.run()
			A3.run()
			A1.run()
		
		# up
		if key.char == "p":
				print("up")
				A4.setSpeed(100)
				A2.setSpeed(80)
				A4.run()
				A2.run()
		
		# down
		if key.char == "l":
				print("down")
				A4.setSpeed(100)
				A2.setSpeed(75)
				A4.run()
				A2.run()
		
		# left
		if key.char == "a":
				print("left")
				M4.setSpeed(100)
				M4.run()
				M1.setSpeed(100)
				M1.run()

				A3.setSpeed(80)
				A3.run()
				A1.setSpeed(80)
				A1.run()

		# right
		if key.char == 'd':
				print("right")
				A3.setSpeed(100)
				A1.setSpeed(100)
				M4.setSpeed(80)
				M1.setSpeed(80)
				A3.run()
				A1.run()
				M4.run()
				M1.run()

		# stop
		if key.char == "x":
				print("stopping")
				M4.setSpeed(90)
				M1.setSpeed(90)
				A1.setSpeed(90)
				A2.setSpeed(90)
				A3.setSpeed(90)
				A4.setSpeed(90)
				M4.run()
				M1.run()
				A1.run()
				A2.run()
				A3.run()
				A4.run()

	except AttributeError:
		pass

# Collect events until released
with keyboard.Listener(on_release=on_key_release) as listener:
	listener.join()
