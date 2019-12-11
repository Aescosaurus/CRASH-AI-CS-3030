"""Main file to control implementation."""
import threading
import os

import open_game
import game_interaction
import game_player

# Open the game window.
open_window_t = threading.Thread(target=open_game.open_game_window, daemon=False)
open_window_t.start()

# Move the game window.
open_game.move_game_window()

# Change directory and start playing the game.
os.chdir('..')
game_player.start_playing()
