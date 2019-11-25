import game_interaction as game
import time

window_name = "Cave Runner Actual Sharp Hustle"

def start():
    game.focus_window( window_name )
    time.sleep( 0.2 )
    game.click_start()
    # game.click_at( 0,0 )

start()

