import arcade
import os
import timeit

import entities
import settings

settings = settings.settings_load()

# INIT DATA A LOT OFF SETINGS
SCENES = ['INTRO', 'MAIN', 'OPTIONS', 'PAUSE', 'GAME_OVER', 'VICTORY', 'INTRODUCTION', 'LOAD', 'SCORES']
SET_TITLE = settings['GAME']['TITLE']
SET_SAVE_SLOTS = int(settings['DEFAULTS']['SAVE_SLOTS'])
DEFAULT_BG = arcade.color.WHITE
DEFAULT_FONT = arcade.color.BLACK
SET_MUSIC_VOLUME = settings['AUDIO']['MUSIC_VOL']
SET_SOUND_VOLUME = settings['AUDIO']['SOUND_VOL']
if int(settings['VIDEO']['FULL_RESOLUTION']) == 1:
    SET_FULL = True
    SET_WIDTH = int(settings['DEFAULTS']['WINDOW_WIDTH'])
    SET_HEIGHT = int(settings['DEFAULTS']['WINDOW_HEIGHT'])
    UI_SCALING = float(settings['DEFAULTS']['UI_SCALING'])
else:
    SET_FULL = False
    SET_WIDTH = int(settings['VIDEO']['WINDOW_WIDTH'])
    SET_HEIGHT = int(settings['VIDEO']['WINDOW_HEIGHT'])
    UI_SCALING = float(settings['VIDEO']['UI_SCALING'])
# DEVELOPER MODE
if int(settings['DEFAULTS']['SKIP_INTRO']) == 1:
    SET_SKIP_INTRO = 1
    CURRENT_SCENE = SCENES[1]
else:
    SET_SKIP_INTRO = 0
    CURRENT_SCENE = SCENES[0]

SET_DEVELOPER = int(settings['DEFAULTS']['DEVELOPER_MODE'])


class IntroView(arcade.View):
    def __init__(self):
        super().__init__()
        self.wait_sec = 0

    def on_show(self):
        arcade.set_background_color(DEFAULT_BG)

    def on_draw(self):
        arcade.start_render()
        if self.wait_sec >= 4:
            entities.draw_title(color='orange', window=self.window)

        arcade.draw_lrwh_rectangle_textured(self.window.width/2-entities.intro_team.width/4,
                                            self.window.height/2-entities.intro_team.height/4,
                                            entities.intro_team.width/2, entities.intro_team.height/2, entities.intro_team)
        if self.wait_sec >= 1:
            arcade.draw_text("PRESENTS", self.window.width/2,
                             self.window.height/2-entities.intro_team.height/4-60,
                             DEFAULT_FONT, font_size=20, anchor_x="center")
        if self.wait_sec >= 2:
            arcade.draw_text("PyWeek 30 Entry", self.window.width/2,
                             self.window.height/2-entities.intro_team.height/4-150,
                             DEFAULT_FONT, font_size=25, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        menu_view = MenuView()
        self.window.show_view(menu_view)

    def update(self, delta_time):
        self.wait_sec += delta_time


class MenuView(arcade.View):
    def __init__(self):
        super().__init__()
        self.button_start = entities.Button(x=self.window.width/2, y=self.window.height*2/6,
                                            width=200, height=50,
                                            texture_idle='start',
                                            texture_hover='start_hover')
        self.button_exit = entities.Button(x=self.window.width / 2, y=self.window.height*1/6,
                                           width=200, height=50,
                                           texture_idle='exit',
                                           texture_hover='exit_hover')
        self.background = entities.DynamicBackground(x=self.window.width/2, y=self.window.height/2,
                                                     res_width=self.window.width,
                                                     res_height=self.window.height)

    def on_update(self, delta_time: float):
        self.background.on_update()
        self.button_start.detect_mouse(self.window.cursor)
        self.button_exit.detect_mouse(self.window.cursor)

    def on_draw(self):
        arcade.start_render()
        self.background.on_draw()
        entities.draw_title(color='blue', window=self.window)
        self.button_start.draw()
        self.button_exit.draw()

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        if self.button_start.current_state == 'hover':
            start_game_view = StageView(background=self.background, wave=1, slot=1, sun_time=840)
            # start_game_view = StartGame(background = self.background)
            self.window.show_view(start_game_view)
        if self.button_exit.current_state == 'hover':
            self.window.close()


# class StartGame(arcade.View):
#     def __init__(self, background):
#         super().__init__()
#         self.background = background
#         self.slot_buttons = []
#         self.slot_buttons_restart = []
#         self.margin = self.window.width/4
#
#         for slot in range(1, SET_SAVE_SLOTS+1):
#             _slot_button = entities.Button(x=self.margin*slot, y=self.window.height/3,
#                                            width=150, height=35,
#                                            texture_idle='slot'+str(slot),
#                                            texture_hover='slot'+str(slot)+'_hover',
#                                            slot=slot)
#             _slot_restart_button = entities.Button(x=self.margin*slot, y=self.window.height/4,
#                                                    width=150, height=35,
#                                                    texture_idle='restart'+str(slot),
#                                                    texture_hover='restart'+str(slot)+'_hover',
#                                                    slot=slot)
#             self.slot_buttons.append(_slot_button)
#             self.slot_buttons_restart.append(_slot_restart_button)
#
#     def on_update(self, delta_time: float):
#         self.background.on_update()
#         for button in self.slot_buttons:
#             button.detect_mouse(self.window.cursor)
#         for button in self.slot_buttons_restart:
#             button.detect_mouse(self.window.cursor)
#
#     def on_draw(self):
#         arcade.start_render()
#         self.background.on_draw()
#         entities.draw_title(color='blue', window=self.window)
#         for button in self.slot_buttons:
#             button.draw()
#         for button in self.slot_buttons_restart:
#             button.draw()
#
#     def on_mouse_press(self, _x, _y, _button, _modifiers):
#         for button in self.slot_buttons:
#             if button.current_state == 'hover':
#                 stage_view = StageView(background=self.background, wave=1, slot=button.slot)
#                 self.window.show_view(stage_view)
#         for button in self.slot_buttons_restart:
#             if button.current_state == 'hover':
#                 stage_view = StageView(background=self.background, wave=1, slot=button.slot)
#                 self.window.show_view(stage_view)


class StageView(arcade.View):
    def __init__(self, background, wave, slot, sun_time=840):
        super().__init__()
        self.wave = wave
        self.slot = slot
        self.sun_time = sun_time
        self.button_exit = entities.Button(x=self.window.width*0.4 - 100, y=self.window.height*1/6,
                                           width=200, height=50,
                                           texture_idle='exit',
                                           texture_hover='exit_hover')
        self.button_wave = entities.Button(x=self.window.width*0.8 - 100, y=self.window.height*1/6,
                                           width=200, height=50,
                                           texture_idle='wave',
                                           texture_hover='wave_hover')
        self.background = background

    def on_update(self, delta_time: float):
        self.background.on_update()
        self.button_exit.detect_mouse(self.window.cursor)
        self.button_wave.detect_mouse(self.window.cursor)

    def on_draw(self):
        arcade.start_render()
        self.background.on_draw()
        entities.draw_title(color='blue', window=self.window)
        arcade.draw_text('WAVE ' + str(self.wave), self.window.width / 2,
                         self.window.height * 0.25,
                         DEFAULT_FONT, font_size=25, anchor_x="center")
        self.button_exit.draw()
        self.button_wave.draw()

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        if self.button_exit.current_state == 'hover':
            self.window.close()
        if self.button_wave.current_state == 'hover':
            game_view = GameView(background=self.background, wave=self.wave, slot=self.slot, sun_time=self.sun_time)
            self.window.show_view(game_view)


class GameView(arcade.View):
    def __init__(self, background, wave, slot, sun_time):
        super().__init__()
        # Environment
        self.background = background
        self.time_taken = 0
        self.sun_time = sun_time
        # Gameplay
        self.stage = wave
        self.slot = slot
        self.victory = False
        self.wait_after_victory = 0
        # Hero
        self.hero = entities.Hero(self.window.width/2, self.window.height*0.42)
        self.hero_action = 'idle'
        self.wait_after_failure = False
        self.game_over = False
        self.wait_sec = 0

        # Developer mode
        self.developer_mode = SET_DEVELOPER
        self.processing_time = 0
        self.draw_start_time = 0
        self.draw_time = 0
        self.frame_count = 0
        self.fps_start_timer = None
        self.fps = None

        # Enemies:
        self.score = 0
        self.bird_list = []
        self.bird_list = arcade.SpriteList()

        # Physic system
        self.coco_system = entities.CocoSystem(screen_width=self.window.width, screen_height=self.window.height,
                                               coco_x=self.window.width/2, coco_y=self.window.height/2)

    def on_victory(self):
        next_stage = self.stage + 1
        game_hour = (int(self.sun_time) // 60) % 24
        next_stage_view = StageView(background=entities.DynamicBackground(x=self.window.width/2,
                                                                          y=self.window.height/2,
                                                                          res_width=self.window.width,
                                                                          res_height=self.window.height,
                                                                          game_hour=game_hour),
                                    wave=next_stage,
                                    slot=self.slot,
                                    sun_time=self.sun_time)
        self.window.show_view(next_stage_view)

    def on_failure(self):
        next_stage = self.stage
        game_hour = (int(self.sun_time) // 60) % 24
        restart_stage_view = StageView(background=entities.DynamicBackground(x=self.window.width/2,
                                                                             y=self.window.height/2,
                                                                             res_width=self.window.width,
                                                                             res_height=self.window.height,
                                                                             game_hour=game_hour),
                                       wave=next_stage,
                                       slot=self.slot,
                                       sun_time=self.sun_time)
        self.window.show_view(restart_stage_view)

    def instruction(self):
        if int(self.wait_sec) in range(2,30):
            arcade.draw_text("PRESS W,D to move", self.window.width/2,
                             self.window.height-60,
                             DEFAULT_FONT, font_size=20, anchor_x="center")
        if int(self.wait_sec) in range(5, 30):
            arcade.draw_text("Use mouse to shoot cocos at seagulls", self.window.width/2,
                             self.window.height-120,
                             DEFAULT_FONT, font_size=20, anchor_x="center")
        if int(self.wait_sec) in range(7, 30):
            arcade.draw_text("Press S to start or W to stop building raft", self.window.width/2,
                             self.window.height-180,
                             DEFAULT_FONT, font_size=20, anchor_x="center")

    def developer_mode_pre_render(self):
        if self.developer_mode:
            # Start timing how long this takes
            self.draw_start_time = timeit.default_timer()
            if self.frame_count % 60 == 0:
                if self.fps_start_timer is not None:
                    total_time = timeit.default_timer() - self.fps_start_timer
                    self.fps = 60 / total_time
                self.fps_start_timer = timeit.default_timer()
            self.frame_count += 1

    def developer_mode_post_render(self):
        if self.developer_mode:
            # Display timings
            output = f"Processing time: {self.processing_time:.3f}"
            arcade.draw_text(output, 20, self.window.height - 20, arcade.color.BLACK, 16)

            output = f"Drawing time: {self.draw_time:.3f}"
            arcade.draw_text(output, 20, self.window.height - 40, arcade.color.BLACK, 16)

            # Calculate time
            minutes = int(self.time_taken) // 60
            seconds = int(self.time_taken) % 60
            time_output = f"Time: {minutes:02d}:{seconds:02d}"

            # Output the timer text.
            arcade.draw_text(time_output, 20, self.window.height - 60, arcade.color.BLACK, 16)

            if self.fps is not None:
                output = f"FPS: {self.fps:.0f}"
                arcade.draw_text(output, 20, self.window.height - 80, arcade.color.BLACK, 16)

        # Below code has to be at the end of rendering
            self.draw_time = timeit.default_timer() - self.draw_start_time

    def on_draw(self):
        if self.developer_mode:
            self.developer_mode_pre_render()

        arcade.start_render()
        self.background.draw_sea_and_sky()
        self.background.draw()
        self.coco_system.on_draw()
        self.background.draw_leafs()
        self.background.draw_raft()
        self.hero.draw()
        self.hero.on_draw_cocos()
        self.bird_list.draw()
        if self.stage == 1:
            self.instruction()

        if self.developer_mode:
            self.developer_mode_post_render()

    def on_update(self, delta_time):
        self.time_taken += delta_time
        self.sun_time += delta_time
        self.hero.update()
        self.hero.change_position(island_width=self.background.width, island_height=self.window.height*0.42)
        self.hero.update_animation()
        self.hero.sprite_top_coco_right.update()
        self.hero.sprite_top_coco_left.update()
        self.background.building_raft(self.hero.current_state, 0.001)
        self.coco_system.on_update(player_list=self.hero)

        self.wait_sec += delta_time

        # Birds:
        self.bird_list.update()
        for bird in self.bird_list:
            bird.on_update()
            bird.follow_hero(self.hero[0])
        birds_hit_list_1 = arcade.check_for_collision_with_list(self.hero[0], self.bird_list)

        entities.spawn_birds(wave=self.stage, bird_list=self.bird_list, screen_width=self.window.width,
                             screen_height=self.window.height)

        self.background.on_update()
        self.background.update_hour(int(self.sun_time) // 60)

        # Victory
        if self.background.victory:
            self.wait_after_victory += delta_time
            if self.wait_after_victory >= 2:
                self.on_victory()
        # Game over
        for bird in birds_hit_list_1:
            bird.kill()
        for coco in self.coco_system.fire_coco_list:
            coco_hit_list = arcade.check_for_collision_with_list(coco, self.bird_list)
            for cocos in coco_hit_list:
                cocos.kill()
            for bird in self.bird_list:
                bird_hit_list = arcade.check_for_collision_with_list(bird, self.coco_system.fire_coco_list)
                for bird in bird_hit_list:
                    bird.kill()

        if len(birds_hit_list_1) >= 1:
            self.game_over = True
        if self.game_over:
            self.wait_after_failure += delta_time
            self.hero.change_state(state='die')
            if self.wait_after_failure >= 1:
                self.on_failure()

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):

        # Hero:
        self.hero.flip_horizontaly(mouse_x=x)
        self.hero.update_hero_angle(x, y)

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ESCAPE:
            # pass self, the current view, to preserve this view's state
            pause = PauseView(paused_game_state=self, background=self.background)
            self.window.show_view(pause)
        if key == arcade.key.TAB:
            # pass self, the current view, to preserve this view's state
            if self.developer_mode:
                self.developer_mode = False
            else:
                self.developer_mode = True
        if self.developer_mode:
            if key == arcade.key.L:
                self.hero.change_state('die')
        if not self.hero.dying:
            self.hero.on_key_press(key)

    def on_key_release(self, key, _modifiers):
        self.hero.on_key_release(key)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        if self.hero.has_coco_right:
            self.hero.change_state(state='throw')
            self.coco_system.shoot_two_cocos = True
        elif self.hero.has_coco_left:
            self.hero.change_state(state='throw')
            self.coco_system.shoot_one_cocos = True

    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        pass


class PauseView(arcade.View):
    def __init__(self, paused_game_state, background):
        super().__init__()
        self.background = background
        self.paused_game_state = paused_game_state
        self.button_resume = entities.Button(x=self.window.width/2, y=self.window.height*3/6,
                                             width=200, height=50,
                                             texture_idle='resume',
                                             texture_hover='resume_hover')
        self.button_menu = entities.Button(x=self.window.width/2, y=self.window.height*2/6,
                                           width=200, height=50,
                                           texture_idle='menu',
                                           texture_hover='menu_hover')
        self.button_exit = entities.Button(x=self.window.width / 2, y=self.window.height*1/6,
                                           width=200, height=50,
                                           texture_idle='exit',
                                           texture_hover='exit_hover')

    def on_update(self, delta_time: float):
        self.button_resume.detect_mouse(self.window.cursor)
        self.button_exit.detect_mouse(self.window.cursor)
        self.button_menu.detect_mouse(self.window.cursor)

    def on_draw(self):
        arcade.start_render()
        self.background.on_draw()
        entities.draw_title(color='blue', window=self.window)
        self.button_resume.draw()
        self.button_exit.draw()
        self.button_menu.draw()

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        if self.button_resume.current_state == 'hover':
            self.window.show_view(self.paused_game_state)
        if self.button_menu.current_state == 'hover':
            menu_view = MenuView()
            self.window.show_view(menu_view)
        if self.button_exit.current_state == 'hover':
            self.window.close()


class Island(arcade.Window):
    def __init__(self):
        super().__init__(width=SET_WIDTH, height=SET_HEIGHT, title=SET_TITLE, fullscreen=SET_FULL)
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Entities (lists of sprites)
        self.cursor = entities.Cursor()

        # Start viewport
        if SET_SKIP_INTRO == 1:
            self.start_view = MenuView()
        if SET_SKIP_INTRO == 0:
            self.start_view = IntroView()

        self.show_view(self.start_view)

        # Start Resources Managers
        self.music_mng = entities.MusicManager(SET_MUSIC_VOLUME)

    def setup(self):
        self.music_mng.setup()

    def on_update(self, delta_time: float):
        self.music_mng.on_update(delta_time)

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.cursor.update()

    def update_resolution(self):
        width, height = self.get_size()
        self.set_viewport(0, width, 0, height)

    def on_mouse_motion(self, x, y, _dx, _dy):
        """
        Called whenever the mouse moves.
        """
        self.cursor.get_position(x, y)

    def on_show(self):
        arcade.set_background_color(DEFAULT_BG)

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if SET_DEVELOPER:
            if key == arcade.key.P:
                # User hits f. Flip between full and not full screen.
                self.set_fullscreen(not self.fullscreen)

                # Get the window coordinates. Match viewport to window coordinates
                # so there is a one-to-one mapping.
                width, height = self.get_size()
                self.set_viewport(0, width, 0, height)

            if key == arcade.key.O:
                # User hits s. Flip between full and not full screen.
                self.set_fullscreen(not self.fullscreen)

                # Instead of a one-to-one mapping, stretch/squash window to match the
                # constants. This does NOT respect aspect ratio. You'd need to
                # do a bit of math for that.
                self.set_viewport(0, SET_WIDTH, 0, SET_HEIGHT)

    def on_draw(self):
        # Draw all the sprites.
        self.cursor.draw()


def main():
    game = Island()
    # Initial all global managers:
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()