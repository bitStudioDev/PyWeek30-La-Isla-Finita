import arcade
# to be cross-platform:
from pathlib import Path

UI_SCALING = 0.5
BG_SCALING = 0.5
SKY_SCALING = 1
UNIT_SCALING = 1


def path_to_string(directory, file):
    return str(Path.cwd().joinpath(directory, file).resolve())


# TITLE
game_title_orange = arcade.load_texture(path_to_string('gfx', 'bg_title1.png'))
game_title_blue = arcade.load_texture(path_to_string('gfx', 'bg_title2.png'))


# INTRO
intro_authors = arcade.load_texture(path_to_string('gfx', 'intro_team_white.png'))

# UI
player_cursor_idle = arcade.Sprite(path_to_string('gfx', 'cursor_idle.png'), UI_SCALING)
player_cursor_hover = arcade.Sprite(path_to_string('gfx', 'cursor_hover.png'), UI_SCALING)
player_cursor_select = arcade.Sprite(path_to_string('gfx', 'cursor_select.png'), UI_SCALING)

# UI BUTTONS
button_save_idle = arcade.Sprite(path_to_string('gfx', 'ui_button_save.png'), UI_SCALING)
button_save_hover = arcade.Sprite(path_to_string('gfx', 'ui_button_save_hover.png'), UI_SCALING)
button_wave_idle = arcade.Sprite(path_to_string('gfx', 'ui_button_wave.png'), UI_SCALING)
button_wave_hover = arcade.Sprite(path_to_string('gfx', 'ui_button_wave_hover.png'), UI_SCALING)
button_idle = arcade.Sprite(path_to_string('gfx', 'ui_button.png'), UI_SCALING)
button_hover = arcade.Sprite(path_to_string('gfx', 'ui_button_hover.png'), UI_SCALING)
button_start_idle = arcade.Sprite(path_to_string('gfx', 'ui_button_start.png'), UI_SCALING)
button_start_hover = arcade.Sprite(path_to_string('gfx', 'ui_button_start_hover.png'), UI_SCALING)
button_exit_idle = arcade.Sprite(path_to_string('gfx', 'ui_button_exit.png'), UI_SCALING)
button_exit_hover = arcade.Sprite(path_to_string('gfx', 'ui_button_exit_hover.png'), UI_SCALING)
button_resume_idle = arcade.Sprite(path_to_string('gfx', 'ui_button_resume.png'), UI_SCALING)
button_resume_hover = arcade.Sprite(path_to_string('gfx', 'ui_button_resume_hover.png'), UI_SCALING)
button_restart_idle = arcade.Sprite(path_to_string('gfx', 'ui_button_restart.png'), UI_SCALING)
button_restart_hover = arcade.Sprite(path_to_string('gfx', 'ui_button_restart_hover.png'), UI_SCALING)
button_restart1_idle = arcade.Sprite(path_to_string('gfx', 'ui_button_restart.png'), UI_SCALING)
button_restart1_hover = arcade.Sprite(path_to_string('gfx', 'ui_button_restart_hover.png'), UI_SCALING)
button_restart2_idle = arcade.Sprite(path_to_string('gfx', 'ui_button_restart.png'), UI_SCALING)
button_restart2_hover = arcade.Sprite(path_to_string('gfx', 'ui_button_restart_hover.png'), UI_SCALING)
button_restart3_idle = arcade.Sprite(path_to_string('gfx', 'ui_button_restart.png'), UI_SCALING)
button_restart3_hover = arcade.Sprite(path_to_string('gfx', 'ui_button_restart_hover.png'), UI_SCALING)
button_slot1_idle = arcade.Sprite(path_to_string('gfx', 'ui_button_slot1.png'), UI_SCALING)
button_slot1_hover = arcade.Sprite(path_to_string('gfx', 'ui_button_slot1_hover.png'), UI_SCALING)
button_slot2_idle = arcade.Sprite(path_to_string('gfx', 'ui_button_slot2.png'), UI_SCALING)
button_slot2_hover = arcade.Sprite(path_to_string('gfx', 'ui_button_slot2_hover.png'), UI_SCALING)
button_slot3_idle = arcade.Sprite(path_to_string('gfx', 'ui_button_slot3.png'), UI_SCALING)
button_slot3_hover = arcade.Sprite(path_to_string('gfx', 'ui_button_slot3_hover.png'), UI_SCALING)
button_menu_idle = arcade.Sprite(path_to_string('gfx', 'ui_button_menu.png'), UI_SCALING)
button_menu_hover = arcade.Sprite(path_to_string('gfx', 'ui_button_menu_hover.png'), UI_SCALING)

button_textures = {"start": button_start_idle,
                   "start_hover": button_start_hover,
                   "exit": button_exit_idle,
                   "exit_hover": button_exit_hover,
                   "resume": button_resume_idle,
                   "resume_hover": button_resume_hover,
                   "restart": button_restart_idle,
                   "restart_hover": button_restart_hover,
                   "slot1": button_slot1_idle,
                   "slot1_hover": button_slot1_hover,
                   "restart1": button_restart1_idle,
                   "restart1_hover": button_restart1_hover,
                   "slot2": button_slot2_idle,
                   "slot2_hover": button_slot2_hover,
                   "restart2": button_restart2_idle,
                   "restart2_hover": button_restart2_hover,
                   "slot3": button_slot3_idle,
                   "slot3_hover": button_slot3_hover,
                   "restart3": button_restart3_idle,
                   "restart3_hover": button_restart3_hover,
                   "menu": button_menu_idle,
                   "menu_hover": button_menu_hover,
                   "wave": button_wave_idle,
                   "wave_hover": button_wave_hover,
                   "save": button_save_idle,
                   "save_hover": button_save_hover
}

# BACKGROUND
dynamic_background_frames = []
dynamic_background_leafs = []
dynamic_background_sky_by_hour = []

for x in range(1,7,1):
    background = arcade.Sprite(path_to_string('gfx', 'bg_full_island'+str(x)+'.png'), BG_SCALING)
    leafs = arcade.load_texture(file_name=path_to_string('gfx', 'bg_full_island_leafs' + str(x) + '.png'))
    dynamic_background_frames.append(background)
    dynamic_background_leafs.append(leafs)

# SKY

for x in range(1,25,1):
    sky = arcade.load_texture(path_to_string('gfx', 'sky'+str(x)+'.png'))
    dynamic_background_sky_by_hour.append(sky)

# SEA
sea = arcade.load_texture(path_to_string('gfx', 'bg_see.png'))

# Hero
hero_bottom_idle = []
hero_bottom_run = []
hero_bottom_throw = []
hero_bottom_build = []
hero_top_idle = []
hero_top_run = []
hero_top_throw = []
hero_top_build = []
hero_die = []
hero_top = (hero_top_idle, hero_top_run, hero_top_throw, hero_top_build)
hero_bottom = (hero_bottom_idle, hero_bottom_run, hero_bottom_throw, hero_bottom_build)
hero_all = (hero_top_idle, hero_top_run, hero_top_throw, hero_top_build, hero_bottom_idle, hero_bottom_run, hero_bottom_throw, hero_bottom_build)

# Blue Fish
blue_fish = []
for x in range(1,5,1):
    blue_fish_texture = arcade.load_texture(path_to_string('gfx', 'blue_fish'+str(x)+'.png'))
    blue_fish.append(blue_fish_texture)

# White Bird
white_bird = []
white_bird_filename = path_to_string('gfx', 'bird'+str(x)+'.png')
for x in range(1,7,1):
    white_bird_texture = arcade.load_texture(path_to_string('gfx', 'bird'+str(x)+'.png'))
    white_bird_texture_right = arcade.load_texture(path_to_string('gfx', 'bird'+str(x)+'.png'),
                                                   flipped_horizontally=True)
    white_bird.append((white_bird_texture, white_bird_texture_right))

# Idle 2 frames
for x in range(1,3,1):
    _hero_bottom_idle = arcade.load_texture(file_name=path_to_string('gfx', 'hero_bottom_idle'+str(x)+'.png'))
    _hero_bottom_idle_left = arcade.load_texture(file_name=path_to_string('gfx', 'hero_bottom_idle'+str(x)+'.png'),
                                                 flipped_horizontally=True)
    hero_bottom_idle.append((_hero_bottom_idle, _hero_bottom_idle_left,))
    _hero_top_idle = arcade.load_texture(file_name=path_to_string('gfx', 'hero_top_idle'+str(x)+'.png'))
    _hero_top_idle_left = arcade.load_texture(file_name=path_to_string('gfx', 'hero_top_idle'+str(x)+'.png'),
                                              flipped_horizontally=True)
    _hero_top_idle_coco = arcade.load_texture(file_name=path_to_string('gfx', 'hero_top_idle_coco'+str(x)+'.png'))
    _hero_top_idle_coco_left = arcade.load_texture(file_name=path_to_string('gfx', 'hero_top_idle_coco'+str(x)+'.png'),
                                                   flipped_horizontally=True)
    hero_top_idle.append((_hero_top_idle, _hero_top_idle_left, _hero_top_idle_coco, _hero_top_idle_coco_left))

# Run 4 frames
for x in range(1,5,1):
    _hero_bottom_run = arcade.load_texture(file_name=path_to_string('gfx', 'hero_bottom_run'+str(x)+'.png'))
    _hero_bottom_run_left = arcade.load_texture(file_name=path_to_string('gfx', 'hero_bottom_run'+str(x)+'.png'),
                                                flipped_horizontally=True)
    hero_bottom_run.append((_hero_bottom_run, _hero_bottom_run_left))
    _hero_top_run = arcade.load_texture(file_name=path_to_string('gfx', 'hero_top_run'+str(x)+'.png'))
    _hero_top_run_left = arcade.load_texture(file_name=path_to_string('gfx', 'hero_top_run'+str(x)+'.png'),
                                             flipped_horizontally=True)
    hero_top_run.append((_hero_top_run, _hero_top_run_left))

# Run 4 frames
    _hero_bottom_build_left = arcade.load_texture(file_name=path_to_string('gfx', 'hero_bottom_build1.png'))
    _hero_bottom_build = arcade.load_texture(file_name=path_to_string('gfx', 'hero_bottom_build1.png'),
                                             flipped_horizontally=True)
    hero_bottom_build.append((_hero_bottom_run, _hero_bottom_run_left))
    _hero_top_build_left = arcade.load_texture(file_name=path_to_string('gfx', 'hero_top_build1.png'))
    _hero_top_build = arcade.load_texture(file_name=path_to_string('gfx', 'hero_top_build1.png'),
                                          flipped_horizontally=True)
    hero_top_build.append((_hero_top_build, _hero_top_build_left))

# Throw 3 frames
for x in range(1,4,1):
    _hero_bottom_throw = arcade.load_texture(file_name=path_to_string('gfx', 'hero_bottom_throw'+str(x)+'.png'))
    _hero_bottom_throw_left = arcade.load_texture(file_name=path_to_string('gfx', 'hero_bottom_throw'+str(x)+'.png'),
                                                  flipped_horizontally=True)
    hero_bottom_throw.append((_hero_bottom_throw, _hero_bottom_throw_left))
    _hero_top_throw = arcade.load_texture(file_name=path_to_string('gfx', 'hero_top_throw'+str(x)+'.png'))
    _hero_top_throw_left = arcade.load_texture(file_name=path_to_string('gfx', 'hero_top_throw'+str(x)+'.png'),
                                               flipped_horizontally=True)
    hero_top_throw.append((_hero_top_throw, _hero_top_throw_left))

# DIE 6 frames
for x in range(1,7,1):
    _hero_die = arcade.load_texture(file_name=path_to_string('gfx', 'hero_die'+str(x)+'.png'))
    hero_die.append(_hero_die)

dynamic_background_raft = []
# RAFT 6 frames
for x in range(1,7,1):
    _raft = arcade.load_texture(file_name=path_to_string('gfx', 'raft'+str(x)+'.png'))
    dynamic_background_raft.append(_raft)

coco_filename = path_to_string('gfx', 'coco.png')
coco_texture = arcade.load_texture(file_name=coco_filename)

# MUSIC
track01 = path_to_string('music', 'track01.mp3')
track02 = path_to_string('music', 'track02.mp3')
songs_list = [track01, track02]
