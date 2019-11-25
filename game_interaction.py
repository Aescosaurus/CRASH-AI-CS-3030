import win32gui
import win32api
import win32con
from rect import rect_t
import time
from pynput.keyboard import Controller
from color import color_t
from vec2 import vec2_t

def focus_window( name ):
    def check_window_enums( hWnd,name ):
        if name == str( win32gui.GetWindowText( hWnd ) ):
            win32gui.SetForegroundWindow( hWnd )

    win32gui.EnumWindows( check_window_enums,name )

def get_window_info():
<<<<<<< HEAD
    details = rect_t( 0,0,0,0 )
    def callback( hWnd,extra ):
        rect = win32gui.GetWindowRect( hWnd )
        if win32gui.GetWindowText( hWnd ) == "Cave Runner Actual Sharp Hustle":
            extra.left = rect[0]
            extra.top = rect[1]
            extra.right = rect[2]
            extra.bot = rect[3]
=======
    """Get information about the game window."""
    details = rect_t(0, 0, 0, 0)

    def callback(hWnd, extra):
        rect = win32gui.GetWindowRect(hWnd)
        x = rect[0]
        y = rect[1]
        w = rect[2] - x
        h = rect[3] - y
        if win32gui.GetWindowText(hWnd) == "Cave Runner Actual Sharp Hustle":
            extra.left = x
            extra.top = y
            extra.right = x + w
            extra.bot = y + h
>>>>>>> 7ebd6ac749f11dd7c71af1c7bac7ef0cff039d36

    win32gui.EnumWindows(callback, details)

    return details

<<<<<<< HEAD
def get_pixel( x,y ):
    new_pos = local_to_global( vec2_t( x,y ) )
    x = new_pos.x
    y = new_pos.y

    desktop_window = win32gui.GetDesktopWindow()
    window_dc = win32gui.GetWindowDC( desktop_window )
    color = int( win32gui.GetPixel( window_dc,x,y ) )
    return( color_t(
        ( color & 0xFF ), # Red
        ( ( color >> 8 ) & 0xFF ), # Green
        ( ( color >> 16 ) & 0xFF ) ) ) # Blue

def click_at( x,y ):
    new_pos = local_to_global( vec2_t( x,y ) )
    x = new_pos.x
    y = new_pos.y

    win32api.SetCursorPos( ( x,y ) )
    win32api.mouse_event( win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0 )
    time.sleep( 1.0 / 60.0 ) # This makes the buttons actually work.
    win32api.mouse_event( win32con.MOUSEEVENTF_LEFTUP,x,y,0,0 )

def click_start():
    click_at( 200,400 )

def press_key( key ):
    press_key.kbd = Controller()

    press_key.kbd.press( key )
    press_key.kbd.release( key )

def local_to_global( vec2 ):
    local_to_global.window_rect = get_window_info()
    x = vec2.x + local_to_global.window_rect.left
    y = vec2.y + local_to_global.window_rect.top
    return( vec2_t( x,y ) )

"""
window_rect = get_window_info()
focus_window( "Cave Runner Actual Sharp Hustle" )
time.sleep( 1 )
click_start()
print( "done" )
"""
=======
def click_at(x, y):
    """Leftclick mouse at specified location."""
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

def click_start():
    """Click the games start button (must add fix for aspect ratio nonsense."""
    window_rect = get_window_info()
    click_at(window_rect.left + 215, window_rect.top + 520)

if __name__ == '__main__':
    # Get the window specifications.
    print(get_window_info())

    # Click the games start button (Looks like this is also effected by aspect ratio.)
    click_start()

    # Processes finished successfully.
    print("Processes finished.")
>>>>>>> 7ebd6ac749f11dd7c71af1c7bac7ef0cff039d36
