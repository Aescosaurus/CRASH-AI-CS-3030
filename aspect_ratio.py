from win32api import GetSystemMetrics

screen_width = GetSystemMetrics(0)
screen_height = GetSystemMetrics(1)


def return_aspect_ratio():
	if screen_width== 1920 and screen_height == 1080:
		return (16, 9)
	elif screen_width == 1280 and screen_height == 720:
		return (4, 3)
	else:
		raise Exception('The aspect ratio of the monitor in focus is not supported.')

