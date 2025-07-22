from game_funcs import *
import game_engine

#Set this first to decide the world dimensions
set_game_size(1600, 900)
#Below is where most of your code will be written

#title code
title = print_text("Welcome to Challenger! Click on monsters to defeat them", 60)
place_element(title, 300, 30)

#background code
background_color("black")
add_background('game_background.png') 

#player and monsters
player = add_image("player.png", 300)
place_element(player, 60, 500)

monster1 = add_image("monster1.png", 500)
place_element(monster1, 800, 350)

# WARNING: For advanced students/game requirements
# Called once per frame (there are 60 frames per second)
# DO NOT CHANGE FUNCTION NAME
def update():
    pass

#DO NOT EDIT BELOW 
game_engine.start(update)
