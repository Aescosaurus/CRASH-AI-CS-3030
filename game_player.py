import game_interaction as game
import time
from vec2 import vec2_t

window_name = "Cave Runner Actual Sharp Hustle"

def start():
    game.focus_window( window_name )
    time.sleep( 0.2 )
    game.click_start()
    pos = vec2_t( 0,350 ) # 8,352
    print( game.get_pixel( pos.x,pos.y ) )
    game.click_at( pos.x,pos.y )

start()

