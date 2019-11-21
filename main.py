"""Main file to control implementation."""
import threading
import os

import open_game
import game_interaction
import find_objects

# Open the game window.
open_window_t = threading.Thread(target=open_game.open_game_window, daemon=False)
open_window_t.start()

# Move the game window.
open_game.move_game_window()

# Get the coordinates of the game window.
window_specs = game_interaction.get_window_info()
print(window_specs)

# Start the window capture.
os.chdir('..')
print(os.getcwd())
object_tracking_t = threading.Thread(target=find_objects.screen_record())
object_tracking_t.start()

# Click the start button