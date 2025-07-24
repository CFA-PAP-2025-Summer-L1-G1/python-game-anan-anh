from game_funcs import *
import game_engine
import random

#Set this first to decide the world dimensions
set_game_size(1600, 900)
#Below is where most of your code will be written

#title code
title = print_text("Welcome to Challenger! Click on monsters to defeat them", 60)
place_element(title, 300, 30)

#background code
background_color("black")
add_background('game_background.png') 

# initialize and print scores
player_hp = 500
monster_hp = 1000
p_score_text = print_text('Player HP: '+str(player_hp), 70)
m_score_text = print_text('Monster HP: '+str(monster_hp), 70)
place_element(p_score_text, 60, 350)
place_element(m_score_text, 850, 200)

#helper functions
def extinction():
    global player_hp
    player_hp = player_hp - 1
    update_text(p_score_text, 'Player HP: '+str(player_hp))
    if player_hp == 0 or monster_hp == 0:
        scoreboard()
    play_audio("player-explosion.mp3")

def fight(target):
    global monster_hp
    monster_hp = monster_hp - 30
    update_text(m_score_text, 'Monster HP: '+str(monster_hp))
    play_audio("player-haven-score.mp3")
    if player_hp == 0 or monster_hp <= 0:
        scoreboard()

def scoreboard():
    clear()
    if monster_hp <= 0:
        print_heading("You win", 100) 
        play_audio("win.mp3") 
    else:
        print_heading('Monster wins', 100)         
        play_audio("lose.mp3")

#initialize player and monsters
player = add_image("player.png", 300)
place_element(player, 60, 500)

monster1 = add_image("monster1.png", 500)
place_element(monster1, 800, 350)

#player animation
set_collider(player, width = 150, offset_x = 100)
set_solid(player)
place_element(player, 40, 500)
jump(player, 900, 1)
wasd_move(player, ['w', 's'], speed = 600)
arrows_move(player, ['up', 'down'], speed = 600)
detect_collision(player, monster1, extinction)

click(monster1, fight)


#fireballs
fireballs = []
def spawn_fireballs(i):
  image = add_image('fireball.png', 80)
  fireballs.append(image)
  place_element(image, 1200, random.choice([465, 465, 465]))
  animate_x(image, 900, -200, 2, False, 450)
  detect_collision(player, image, extinction)
  if player_hp == 0 or monster_hp == 0:
        scoreboard()
set_interval(spawn_fireballs, 2.5, range(0, 10))

    
# WARNING: For advanced students/game requirements
# Called once per frame (there are 60 frames per second)
# DO NOT CHANGE FUNCTION NAME
def update():
    pass

#DO NOT EDIT BELOW 
game_engine.start(update)
