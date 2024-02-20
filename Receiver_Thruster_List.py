import socket
from std_msgs.msg import String
from adafruit_servokit import ServoKit
import time


# [M4, M1, A3, A1]
forward = [100,100,100,100]

# [M4, M1, A3, A1]
backward = [80,80,80,80]

# [M4, M1, A3, A1]
left = [100,100,80,80]

# [M4, M1, A3, A1]
right = [80,80,100,100]

# [A4, A2]
up = [100, 100]

# [A4, A2]
down = [80, 75]


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

# Set up the server on the Jetson
server_ip = '0.0.0.0'  # Listen on all available interfaces
server_port = 12345  # Choose an available port
buffer_size = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
  server_socket.bind((server_ip, server_port))
  server_socket.listen()

  print(f"Listening for connections on {server_ip}:{server_port}")
  
  # Wait for a client to connect
  client_socket, client_address = server_socket.accept()
  print(f"Connection established with {client_address}")
  
  while True:
  	# all forward thrusters

    # Receive data from the client
    data = client_socket.recv(buffer_size).decode('utf-8')
    
    if not data:
    break  # Break the loop if no data is received
    
    #Thruster code based on controller input
    if info == "Left joystick angle up":
      print("forward")
      M4.setSpeed(forward[0])
      M1.setSpeed(forward[1])
      A3.setSpeed(forward[2])
      A1.setSpeed(forward[3])
      M4.run()
      M1.run()
      A3.run()
      A1.run()
    
    if info == "Left joystick angle to the left":
      print("left")
      M4.setSpeed(left[0])
      M4.run()
      M1.setSpeed(left[1])
      M1.run()
      A3.setSpeed(left[2])
      A3.run()
      A1.setSpeed(left[3])
      A1.run()
    
    		
    if info == "Left joystick angle to the right":
    	print("right")
      A3.setSpeed(right[2])
      A1.setSpeed(right[3])
      M4.setSpeed(right[0])
      M1.setSpeed(right[1])
      A3.run()
      A1.run()
      M4.run()
      M1.run()
    
    
    if info == "Left joystick angle down":
      print("backward")
      M4.setSpeed(backward[0])
      M1.setSpeed(backward[1])
      A3.setSpeed(backward[2])
      A1.setSpeed(backward[3])
      M4.run()
      M1.run()
      A3.run()
      A1.run()
    
    
    if info == "Right joystick angle up":
      print("up")
      A4.setSpeed(up[0])
      A2.setSpeed(up[1])
      A4.run()
      A2.run()
    
    if info == "Right joystick angle down":
      print("down")
      A4.setSpeed(down[0])
      A2.setSpeed(down[1])
      A4.run()
      A2.run()
      
    if info == "Button B pressed":
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
    
    
    time.sleep(0.1)


print("Connection closed.")
