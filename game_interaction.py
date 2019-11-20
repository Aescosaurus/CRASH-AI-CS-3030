import win32gui
import win32api
import win32con
from rect import rect_t
import time

def get_window_info():
    details = rect_t( 0,0,0,0 )
    def callback( hWnd,extra ):
        rect = win32gui.GetWindowRect( hWnd )
        x = rect[0]
        y = rect[1]
        w = rect[2] - x
        h = rect[3] - y
        if win32gui.GetWindowText( hWnd ) == "Cave Runner Actual Sharp Hustle":
            extra.left = x
            extra.top = y
            extra.right = x + w
            extra.bot = y + h

    win32gui.EnumWindows( callback,details )

    return( details )

def click_at( x,y ):
    win32api.SetCursorPos( ( x,y ) )
    win32api.mouse_event( win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0 )
    win32api.mouse_event( win32con.MOUSEEVENTF_LEFTUP,x,y,0,0 )

def click_start():
    window_rect = get_window_info()
    click_at( window_rect.left + 215,window_rect.top + 520 )

print( get_window_info() )
time.sleep( 5 )
click_start()
print( "done" )