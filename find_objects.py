"""Detect objects coming from the game.

	Required 3rd party libraries:
		- numpy
		- pillow (PIL)
		- opencv-python (cv2)
		- pyautogui
		- matplotlib

	Game window must be placed in the top left corner of the screen for this to application 
	to function correctly.
"""
import os
import numpy as np
from PIL import ImageGrab
import cv2
import pyautogui
from matplotlib import pyplot as plt
from aspect_ratio import return_aspect_ratio

# monster_found = False
aspect_ratio_x, aspect_ratio_y = return_aspect_ratio()

def find_objects(img_bgr):
	"""
		Take the original image, look for objects matching the template, and draw 
	rectangles around the object.
	"""

	# Convert the brg formatted picture to gray scale to simplify pixel identification.
	img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)


	# Determine the aspect ration of monitor to choose correct images.
	if aspect_ratio_x == 4 and aspect_ratio_y == 3:
		root = './Images/4-3images'
	elif aspect_ratio_x == 16 and aspect_ratio_y == 9:
		root = './Images/16-9images'

	# Default location of images if no object is found
	object_location = (404, 404)

	# For each image in the images folder, create a template, set a threshold for that template, and draw a green rectangle
	# around each object found.
	for rootdir, dirs, files in os.walk(root):
		for file in files:
			if '.JPG' in file or '.jpg' in file:
				file = os.path.join(rootdir, file)
				print(file)
				template = cv2.imread(file, 0)
				w, h = template.shape[::-1]

				res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
				threshold = 0.6
				if 'Player' in file:
					threshold = .65
				loc = np.where( res >= threshold)

				for pt in zip(*loc[::-1]):
					cv2.rectangle(img_bgr, pt, (pt[0] + w, pt[1] + h), (0,255,0), 2)
					object_location = pt

					# If the object is a monster, return it's type and location.
					if 'Monster' in file:
						return 'Monster', object_location

	# If no object is found, return default parameters.
	if object_location == (404, 404):
		return 'NOOB', object_location

	# Return player type and location.
	return 'Player', object_location



def screen_record(): 
	"""Gets and records screen by taking multiple images"""

	while True:

		# Determines what screen to print (ImageGrab.grab(bbox=(0,40,800,640))) for custom bounds.
		if aspect_ratio_x == 4 and aspect_ratio_y == 3:
			capture_window_positions = {'top_left_x': 0,
										'top_left_y': 0,
										'bottom_right_x': 960,
										'bottom_right_y': 510,}
		else:
			capture_window_positions = {'top_left_x': 0,
										'top_left_y': 0,
										'bottom_right_x': 976,
										'bottom_right_y': 519,}

		printscreen =  np.array(ImageGrab.grab(bbox = 
											  (capture_window_positions['top_left_x'],
											   capture_window_positions['top_left_y'],
											   capture_window_positions['bottom_right_x'],
											   capture_window_positions['bottom_right_y'])))

		# Process the image and find objects
		object_type, object_location= find_objects(printscreen)
		# print(object_type, object_location)

		# cv2.imshow displays the image of window name, 'window' and the image coming from printscreen.
		window_name = 'window'
		image = printscreen
		cv2.imshow(window_name, image)

		# Wait for a pressed key ('q'), then destroy the window, and end the program.
		if cv2.waitKey(25) & 0xFF == ord('q'):
			cv2.destroyAllWindows()
			break

# Start displaying the screen.
if __name__ =='__main__':
	screen_record()