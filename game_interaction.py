"""Interact with the game and the game window directly."""
import win32gui
import win32api
import win32con
from rect import rect_t
import time
from pynput.keyboard import Controller
from color import color_t
from vec2 import vec2_t
import ctypes

def focus_window(name):
	"""Focus on the game window."""
	def check_window_enums(hWnd, name):
		if name == str(win32gui.GetWindowText(hWnd)):
			win32gui.SetForegroundWindow(hWnd)

	win32gui.EnumWindows(check_window_enums, name)

def get_window_info():
	"""Get information about the game window."""
	details = rect_t(0, 0, 0, 0)

	def callback(hWnd, extra):
		"""Callback funtion."""
		rect = win32gui.GetWindowRect(hWnd)

		if win32gui.GetWindowText(hWnd) == "Cave Runner Actual Sharp Hustle":
			crect = ctypes.wintypes.RECT()
			DWMWA_EXTENDED_FRAME_BOUNDS = 9
			ctypes.windll.dwmapi.DwmGetWindowAttribute(
				hWnd,
				ctypes.wintypes.DWORD(DWMWA_EXTENDED_FRAME_BOUNDS),
				ctypes.byref(crect),
				ctypes.sizeof(crect))

			if crect.left >= 0:
				extra.left = crect.left + 1
				extra.top = crect.top + 1 + 30
				extra.right = crect.right - 1
				extra.bot = crect.bottom - 1

	win32gui.EnumWindows(callback, details)

	return(details)

def get_pixel(x, y):
	"""Get the pixel at the location x, y."""
	pos = local_to_global(vec2_t(x,y))
	x = pos.x
	y = pos.y

	desktop_window = win32gui.GetDesktopWindow()
	window_dc = win32gui.GetWindowDC(desktop_window)
	color = int( win32gui.GetPixel(window_dc, x, y))

	return(color_t
		 ((color & 0xFF), # Red
		 ((color >> 8 ) & 0xFF), # Green
		 ((color >> 16 ) & 0xFF))) # Blue

def click_at(x, y):
	"""Leftclick mouse at specified location."""
	new_pos = local_to_global(vec2_t(x, y))
	x = new_pos.x
	y = new_pos.y

	# win32api.SetCursorPos((x, y))
	win32api.mouse_event(win32con.MOUSEEVENTF_MOVE |
		win32con.MOUSEEVENTF_ABSOLUTE,
		int(x / win32api.GetSystemMetrics( 0 ) * 65535.0),
		int(y / win32api.GetSystemMetrics( 1 ) * 65535.0))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
	time.sleep(1.0 / 60.0)  # This makes the buttons actually work.
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

def click_start():
	"""Click the games start button (must add fix for aspect ratio nonsense."""
	click_at(200, 400)

def press_key(key):
	"""Press key"""
	press_key.kbd = Controller()

	press_key.kbd.press(key)
	time.sleep(1.0 / 60.0)
	press_key.kbd.release(key)

def press_jump():
	"""Press jump key."""
	press_key('w')

def press_dash():
	"""Docstring..."""
	press_key( 'd' )

def local_to_global( vec2 ):
	"""Convert local coordinates to global coordinates."""
	local_to_global.window_rect = get_window_info()
	x = vec2.x + local_to_global.window_rect.left
	y = vec2.y + local_to_global.window_rect.top
	return(vec2_t(x, y))

if __name__ == '__main__':
	# Get the window specifications.
	print(get_window_info())

	# Click the games start button (Looks like this is also effected by aspect ratio.)
	click_start()

	# Processes finished successfully.
	print("Processes finished.")
