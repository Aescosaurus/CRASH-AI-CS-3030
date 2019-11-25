import pygetwindow
import subprocess
import os
import sys
import threading
from time import sleep

def open_game_window():

	# Look for the game.exe
	for root, dirs, files in os.walk('.'):
		for file in files:
			if '.exe' in file:
				path = os.path.abspath(os.path.join(root, file))
				if path.endswith('.exe'):
					path = path[:-11]
				os.chdir(path)
				os.system("{}/{}".format(path, file))

def move_game_window():

	while True:
		try:
			game_window = pygetwindow.getWindowsWithTitle('Cave Runner Actual Sharp Hustle')[0]
			break
		except IndexError:    
			pass
	game_window.moveTo(0, 0)

if __name__ == '__main__':
	open_window_thread = threading.Thread(target=open_game_window, daemon=False)
	open_window_thread.start()
	move_game_window()

