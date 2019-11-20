import win32gui
import win32api
import win32con
import rect

def get_window_info():
    
    def callback( hWnd,extra ):
        rect = win32gui.GetWindowRect( hWnd )
        x = rect[0]
        y = rect[1]
        w = rect[2] - x
        h = rect[3] - y
        if win32gui.GetWindowText( hWnd ) == "Cave Runner Actual Sharp Hustle":
            extra.append( ( x,y ) )
            extra.append( ( w,h ) )

    win32gui.EnumWindows( callback,details )

    return( details )

def click_at( x,y ):
    win32api.SetCursorPos( x,y )
    win32api.mouse_event( win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0 )
    win32api.mouse_event( win32con.MOUSEEVENTF_LEFTUP,x,y,0,0 )

print( get_window_info() )