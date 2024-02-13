"""
import inputs

while True:
    events = inputs.get_key()
    print(events)
"""


"""
import inputs
import time

def main():
    # Initialize the gamepad
    devices = inputs.devices.gamepads
    if not devices:
        print("No gamepad found.")
        return

    gamepad = devices[0]
    print(f"Connected to Gamepad: {gamepad}")

    while True:
        events = inputs.get_key()
        for event in events:
            # checks for button input
            if event.ev_type == "Key" and event.ev_value == 1:
                handle_button_press(event.ev_code)

            # check for joystick input
            elif event.ev_type == "Absolute":
                handle_joystick_event(event.ev_type, event.ev_code, event.ev_value)

            # FIXME: figure out hat buttons
            elif event.ev_type == "Sync":
                hat_values = inputs.get_key()[0].ev_value
                handle_hat_event(hat_values)

        # Delay to reduce CPU usage
        time.sleep(0.01)

def handle_button_press(ev_code):
    print(f"Button {ev_code} pressed")
    # Add your custom actions based on the pressed button here

def handle_joystick_event(ev_type, ev_code, ev_value):
    print(f"Joystick event - Type: {ev_type}, Code: {ev_code}, Value: {ev_value}")
    # Add your custom actions based on the joystick event here

def handle_hat_event(hat_values):
    # Perform actions based on D-pad (hat) input
    if hat_values == (0, 1):
        print("D-pad pressed up")
    elif hat_values == (0, -1):
        print("D-pad pressed down")
    elif hat_values == (1, 0):
        print("D-pad pressed right")
    elif hat_values == (-1, 0):
        print("D-pad pressed left")

if __name__ == "__main__":
    main()
"""


import pygame
from pyautogui import press, hotkey
import inputs
import time

# Initialize Pygame and the joystick module
pygame.init()
pygame.joystick.init()

# Number of available gamepads
num_joysticks = pygame.joystick.get_count()


if num_joysticks == 0:
	print("No gamepad found.")
else:
	# Initialize the gamepad
	joystick = pygame.joystick.Joystick(0)
	joystick.init()
	print(f"Connected to Gamepad: {joystick.get_name()}")

	while True:
		for event in pygame.event.get():
			# checks for button input
			if event.type == pygame.JOYBUTTONDOWN:
				button = event.button

				# Perform actions based on the button pressed
				# A
				if button == 0:
					print("Button A pressed")
				# B
				if button == 1:  
					print("Button B pressed")
				# X
				if button == 2:  
					print("Button X pressed")
				# Y
				if button == 3:  
					print("Button Y pressed")
				# LB
				if button == 4:  
					print("Button LB pressed")
				# RB
				if button == 5:  
					print("Button RB pressed")
				# Back
				if button == 6:  
					print("Back button pressed")
				# Start
				if button == 7:  
					print("Start button pressed")
				# Left toggle
				if button == 8:  
					print("Left toggle pressed")
				# Right toggle
				if button == 9:  
					print("Right toggle pressed")


			# check for joystick input
			elif event.type == pygame.JOYAXISMOTION:
				axis = event.axis
				value = event.value

				# left joystick
				# X-axis
				if axis == 0:
					# print(f"Left X-axis value: {value}")
					# check the joystick angle
					if value > 0.5:
						print("Left joystick angle to the right")
					if value < -0.5:
						print("Left joystick angle to the left")
				# Y-axis
				elif axis == 1:
					# print(f"Left Y-axis value: {value}")
					if value < -0.5:
						print("Left joystick angle up")
					if value > 0.5:
						print("Left joystick angle down")

				# right joystick
				# X-axis
				elif axis == 2:
					# print(f"Right X-axis value: {value}")
					if value > 0.5:
						print("Right joystick angle to the right")
					if value < -0.5:
						print("Right joystick angle to the left")
				# Y-axis
				elif axis == 3:  # Y-axis (right joystick)
					# print(f"Right Y-axis value: {value}")
					if value < -0.5:
						print("Right joystick angle up")
					if value > 0.5:
						print("Right joystick angle down")

				# Triggers
				# Left trigger
				elif axis == 4:
					# print(f"Left Trigger value: {value}")
					if value > 0.5:
						print("Left trigger pressed")
				# Right trigger
				elif axis == 5:
					# print(f"Right Trigger value: {value}")
					if value > 0.5:
						print("Right trigger pressed")

			#FIXME: figure out hat buttons
			elif event.type == pygame.JOYHATMOTION:
				hat = event.hat
				value = event.value

				# Perform actions based on D-pad (hat) input
				if hat == 0:  # Hat 0
					# print(f"D-pad (Hat 0) value: {value}")
					if value == (0,1):
						print("D-pad pressed up")
					elif value == (0,-1):
						print("D-pad pressed down")
					elif value == (1,0):
						print("D-pad pressed right")
					elif value == (-1,0):
						print("D-pad pressed left")


		# Delay to reduce CPU usage
		time.sleep(0.01)


# Cleanup
pygame.quit()

