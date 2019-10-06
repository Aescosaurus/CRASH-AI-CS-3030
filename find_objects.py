"""Detect objects coming from the game.

	Required 3rd party libraries:
		- numpy
		- pillow (PIL)
		- opencv-python (cv2)
		- pyautogui
		- matplotlib

	Game window must be placed in the top left corner of the screen for this to application to function correctly.
"""
import numpy as np
from PIL import ImageGrab
import cv2
import pyautogui
from matplotlib import pyplot as plt

def find_objects(img_bgr):
	"""Take the original image, look for objects matching the template, and draw rectangles around the object."""

	# Convert the brg formatted picture to gray scale to simplify pixel identification.
	img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

	# List of jpeg names to create templates from (multiple images are used to increase the accuracy of finding the images.)
	template_images = ['Monster.jpg',
					   'Monster1.jpg',
					   'Monster2.jpg',
					   'Monster3.jpg',
					   'Player1.jpg',
					   'Player2.jpg',
					   'Player3.jpg',
					   'Player4.jpg']

	# For each image supplied, create a template, set a threshold for that template, and draw a green rectangle
	# around each object found.
	for image in template_images:
		template = cv2.imread(image,0)
		w, h = template.shape[::-1]

		res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
		threshold = 0.6
		if 'Player' in image:
			threshold = .65
		loc = np.where( res >= threshold)

		for pt in zip(*loc[::-1]):
			cv2.rectangle(img_bgr, pt, (pt[0] + w, pt[1] + h), (0,255,0), 2)

	# 


def screen_record(): 
	"""Gets and records screen by taking multiple images"""

	while True:

		# Determines what screen to print (ImageGrab.grab(bbox=(0,40,800,640))) for custom bounds.
		capture_window_positions = {'top_left_x': 0,
									'top_left_y': 30,
									'bottom_right_x': 960,
									'bottom_right_y': 510,}
		printscreen =  np.array(ImageGrab.grab(bbox = 
											  (capture_window_positions['top_left_x'],
											   capture_window_positions['top_left_y'],
											   capture_window_positions['bottom_right_x'],
											   capture_window_positions['bottom_right_y'])))

		# Process the image and find objects
		find_objects(printscreen)

		# cv2.imshow displays the image of window name, 'window' and the image coming from printscreen.
		window_name = 'window'
		image = printscreen
		cv2.imshow(window_name, image)

		# Wait for a pressed key ('q'), then destroy the window, and end the program.
		if cv2.waitKey(25) & 0xFF == ord('q'):
			cv2.destroyAllWindows()
			break

# Start displaying the screen.
screen_record()