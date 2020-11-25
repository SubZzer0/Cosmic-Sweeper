
import pygame
import time
from pygame.locals import *
import os
import sys

from menu import *
from random import randint

os.environ['SDL_VIDEO_CENTERED'] = '1'

class Game():
    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 2, 512)
        pygame.init()
        pygame.display.set_caption("Cosmic Sweeper")
        self.icon = pygame.image.load('resources/icon.png')
        pygame.display.set_icon(self.icon)
        self.running, self.playing = True, False
        self.run_intro = True
        self.display_w, self.display_h = 800, 600
        self.mid_w, self.mid_h = self.display_w/2, self.display_h/2
        self.scale_x = self.display_w / 2441
        self.scale_y = self.display_h / 1827
        self.nx = 16
        self.ny = 16
        self.difficulty = 1
        self.matrix = [[0 for x in range(self.nx)]for y in range(self.ny)]
        self.mines = 40
        self.display = pygame.Surface ((self.display_w, self.display_h))
        self.window = pygame.display.set_mode((self.display_w, self.display_h))
        
        self.play_hover_sound = True
        self.play_press_sound = True
        self.play_win_sound = True
        self.play_face_sound = True

        self.button_hover_sound = pygame.mixer.Sound('sfx/button hover.wav')
        self.button_press_sound = pygame.mixer.Sound('sfx/button press.wav')
        self.tile_press_sound = pygame.mixer.Sound('sfx/tile press.wav')
        self.tile_flag_sound = pygame.mixer.Sound('sfx/tile flag.wav')
        self.mine_explode_sound = pygame.mixer.Sound('sfx/mine explode.wav')
        self.tile_reveal_sound = pygame.mixer.Sound('sfx/tile reveal.wav')
        self.game_win_sound = pygame.mixer.Sound('sfx/game win.wav')
        self.face_press_sound = pygame.mixer.Sound('sfx/face press.wav')

        self.background_orig = pygame.image.load('resources/menu_background.png').convert_alpha()
        self.game_background_orig = pygame.image.load('resources/game_background.png').convert_alpha()
        self.credits_background_orig = pygame.image.load('resources/credits_background.png').convert_alpha()
        self.fade_orig = pygame.image.load('resources/intro.png').convert()

        pygame.mixer.music.load('sfx/moonmen.mp3')
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play(-1)

        self.face_button_orig = pygame.image.load('resources/face.png').convert_alpha()
        self.face_pressed_orig = pygame.image.load('resources/face pressed.png').convert_alpha()
        self.face_sun_orig = pygame.image.load('resources/face sun.png').convert_alpha()
        self.face_moon_orig = pygame.image.load('resources/face moon.png').convert_alpha()

        self.mainmenu_game_orig = pygame.image.load('resources/main menu game.png').convert_alpha()
        self.mainmenu_game_hover_orig = pygame.image.load('resources/main menu game hover.png').convert_alpha()
        self.mainmenu_game_pressed_orig = pygame.image.load('resources/main menu game pressed.png').convert_alpha()
        self.mines_game_orig = pygame.image.load('resources/mines game.png').convert_alpha()
        self.timer_game_orig = pygame.image.load('resources/timer game.png').convert_alpha()

        self.no0_orig = pygame.image.load('numbers/0.png').convert_alpha()
        self.no1_orig = pygame.image.load('numbers/1.png').convert_alpha()
        self.no2_orig = pygame.image.load('numbers/2.png').convert_alpha()
        self.no3_orig = pygame.image.load('numbers/3.png').convert_alpha()
        self.no4_orig = pygame.image.load('numbers/4.png').convert_alpha()
        self.no5_orig = pygame.image.load('numbers/5.png').convert_alpha()
        self.no6_orig = pygame.image.load('numbers/6.png').convert_alpha()
        self.no7_orig = pygame.image.load('numbers/7.png').convert_alpha()
        self.no8_orig = pygame.image.load('numbers/8.png').convert_alpha()
        self.no9_orig = pygame.image.load('numbers/9.png').convert_alpha()
        self.sep_orig = pygame.image.load('numbers/sep.png').convert_alpha()

        self.play_button_orig = pygame.image.load('buttons/play button.png').convert_alpha()
        self.play_hover_orig = pygame.image.load('buttons/play hover.png').convert_alpha()
        self.play_pressed_orig = pygame.image.load('buttons/play pressed.png').convert_alpha()
        self.difficulty_button_orig = pygame.image.load('buttons/difficulty button.png').convert_alpha()
        self.difficulty_hover_orig = pygame.image.load('buttons/difficulty hover.png').convert_alpha()
        self.difficulty_pressed_orig = pygame.image.load('buttons/difficulty pressed.png').convert_alpha()
        self.settings_button_orig = pygame.image.load('buttons/settings button.png').convert_alpha()
        self.settings_hover_orig = pygame.image.load('buttons/settings hover.png').convert_alpha()
        self.settings_pressed_orig = pygame.image.load('buttons/settings pressed.png').convert_alpha()
        self.credits_button_orig = pygame.image.load('buttons/credits button.png').convert_alpha()
        self.credits_hover_orig = pygame.image.load('buttons/credits hover.png').convert_alpha()
        self.credits_pressed_orig = pygame.image.load('buttons/credits pressed.png').convert_alpha()
        self.exit_button_orig = pygame.image.load('buttons/exit button.png').convert_alpha()
        self.exit_hover_orig = pygame.image.load('buttons/exit hover.png').convert_alpha()
        self.exit_pressed_orig = pygame.image.load('buttons/exit pressed.png').convert_alpha()
        self.back_button_orig = pygame.image.load('buttons/back button.png').convert_alpha()
        self.back_hover_orig = pygame.image.load('buttons/back hover.png').convert_alpha()
        self.back_pressed_orig = pygame.image.load('buttons/back pressed.png').convert_alpha()

        self.beginner_button_orig = pygame.image.load('buttons/beginner button.png').convert_alpha()
        self.beginner_hover_orig = pygame.image.load('buttons/beginner hover.png').convert_alpha()
        self.beginner_pressed_orig = pygame.image.load('buttons/beginner pressed.png').convert_alpha()
        self.beginner_selected_orig = pygame.image.load('buttons/beginner selected.png').convert_alpha()
        self.beginner_expl_orig = pygame.image.load('buttons/beginner expl.png').convert_alpha()
        self.intermediate_button_orig = pygame.image.load('buttons/intermediate button.png').convert_alpha()
        self.intermediate_hover_orig = pygame.image.load('buttons/intermediate hover.png').convert_alpha()
        self.intermediate_pressed_orig = pygame.image.load('buttons/intermediate pressed.png').convert_alpha()
        self.intermediate_selected_orig = pygame.image.load('buttons/intermediate selected.png').convert_alpha()
        self.intermediate_expl_orig = pygame.image.load('buttons/intermediate expl.png').convert_alpha()
        self.expert_button_orig = pygame.image.load('buttons/expert button.png').convert_alpha()
        self.expert_hover_orig = pygame.image.load('buttons/expert hover.png').convert_alpha()
        self.expert_pressed_orig = pygame.image.load('buttons/expert pressed.png').convert_alpha()
        self.expert_selected_orig = pygame.image.load('buttons/expert selected.png').convert_alpha()
        self.expert_expl_orig = pygame.image.load('buttons/expert expl.png').convert_alpha()
        self.custom_button_orig = pygame.image.load('buttons/custom button.png').convert_alpha()
        self.custom_hover_orig = pygame.image.load('buttons/custom hover.png').convert_alpha()
        self.custom_pressed_orig = pygame.image.load('buttons/custom pressed.png').convert_alpha()
        self.custom_selected_orig = pygame.image.load('buttons/custom selected.png').convert_alpha()
        self.custom_expl_orig = pygame.image.load('buttons/custom expl.png').convert_alpha()
        self.expl_height_orig = pygame.image.load('buttons/expl height.png').convert_alpha()
        self.expl_width_orig = pygame.image.load('buttons/expl width.png').convert_alpha()
        self.expl_mines_orig = pygame.image.load('buttons/expl mines.png').convert_alpha()

        self.display_button_orig = pygame.image.load('buttons/display button.png').convert_alpha()
        self.fullscreen_button_orig = pygame.image.load('buttons/fullscreen button.png').convert_alpha()
        self.windowed_button_orig = pygame.image.load('buttons/windowed button.png').convert_alpha()
        self.resolution_button_orig = pygame.image.load('buttons/resolution button.png').convert_alpha()
        self.r640_button_orig = pygame.image.load('buttons/640 button.png').convert_alpha()
        self.r800_button_orig = pygame.image.load('buttons/800 button.png').convert_alpha()
        self.r1024_button_orig = pygame.image.load('buttons/1024 button.png').convert_alpha()
        self.music_button_orig = pygame.image.load('buttons/music button.png').convert_alpha()
        self.sounds_button_orig = pygame.image.load('buttons/sounds button.png').convert_alpha()
        self.volume_button_orig = pygame.image.load('buttons/volume button.png').convert_alpha()
        self.volume_bar_orig = pygame.image.load('buttons/volume bar.png').convert_alpha()
        self.larrow_button_orig = pygame.image.load('buttons/larrow button.png').convert_alpha()
        self.larrow_hover_orig = pygame.image.load('buttons/larrow hover.png').convert_alpha()
        self.larrow_pressed_orig = pygame.image.load('buttons/larrow pressed.png').convert_alpha()
        self.rarrow_button_orig = pygame.image.load('buttons/rarrow button.png').convert_alpha()
        self.rarrow_hover_orig = pygame.image.load('buttons/rarrow hover.png').convert_alpha()
        self.rarrow_pressed_orig = pygame.image.load('buttons/rarrow pressed.png').convert_alpha()

        self.tile_hiddenorig = pygame.image.load('tiles/tile uncovered.png').convert_alpha()
        self.tile_1orig = pygame.image.load('tiles/tile 1.png').convert_alpha()
        self.tile_2orig = pygame.image.load('tiles/tile 2.png').convert_alpha()
        self.tile_3orig = pygame.image.load('tiles/tile 3.png').convert_alpha()
        self.tile_4orig = pygame.image.load('tiles/tile 4.png').convert_alpha()
        self.tile_5orig = pygame.image.load('tiles/tile 5.png').convert_alpha()
        self.tile_6orig = pygame.image.load('tiles/tile 6.png').convert_alpha()
        self.tile_7orig = pygame.image.load('tiles/tile 7.png').convert_alpha()
        self.tile_8orig = pygame.image.load('tiles/tile 8.png').convert_alpha()
        self.tile_9orig = pygame.image.load('tiles/tile 9.png').convert_alpha()
        self.tile_mineorig = pygame.image.load('tiles/tile mine.png').convert_alpha()
        self.tile_explodeorig = pygame.image.load('tiles/tile explode.png').convert_alpha()
        self.tile_flagorig = pygame.image.load('tiles/tile flag.png').convert_alpha()
        self.shadow_filterorig = pygame.image.load('resources/shadow_filter.png').convert_alpha()

        self.scale_everything()

        self.start_x = (self.display_w-(self.nx*self.tile_size))/2
        self.start_y = (self.display_h-(self.ny*self.tile_size))/1.2
        self.is_marked = [[0 for x in range(self.nx)]for y in range(self.ny)]

        self.main_menu = MainMenu(self)
        self.difficulty_menu = DifficultyMenu(self)
        self.settings_menu = SettingsMenu(self)
        self.credits_menu = CreditsMenu(self)
        self.curr_menu = self.main_menu

        self.gen = 0
        self.state = 0
        self.counter = self.nx * self.ny
        self.mine_counter = self.mines
        self.time = 0
        self.show_intro = 1
        
        TIMER = pygame.USEREVENT + 1
        pygame.time.set_timer(TIMER, 1000)


    def game_loop(self):
        while self.playing:
            self.display.blit(self.game_background, (0, 0))
            self.draw_grid(self.nx, self.ny)
            self.display.blit(self.shadow_filter, (self.start_x, self.start_y))
            self.draw_button(self.face_button, self.display_w/2, self.display_h/9.32)
            self.face_rect = self.button_rect
            self.draw_button(self.mainmenu_game, self.display_w/4.75, self.display_h/9)
            self.mainmenu_game_rect = self.button_rect
            self.draw_button(self.mines_game, self.display_w/1.38, self.display_h/15)
            self.draw_button(self.timer_game, self.display_w/1.4, self.display_h/6)
            self.timer()
            self.draw_numbers()
            if self.state == 2:
                self.draw_button(self.face_moon, self.display_w/2, self.display_h/9.32)
            if self.state == 1:
                self.draw_button(self.face_sun, self.display_w/2, self.display_h/9.32)

            self.check_input()
            self.check_events()
            self.window.blit(self.display, (0, 0))
            pygame.display.update()
            
    def check_input(self):
        pos = pygame.mouse.get_pos()
        if self.face_rect.collidepoint(pos):
            click = pygame.mouse.get_pressed()
            if click[0] == True:
                self.draw_button(self.face_pressed, self.display_w/2, self.display_h/9.32)
                if self.play_face_sound == True:
                    self.face_press_sound.play(maxtime=1000)
                    self.play_face_sound = False
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP:
                        self.play_face_sound = True
                        self.reset_game()

        elif self.mainmenu_game_rect.collidepoint(pos):
            self.draw_button(self.mainmenu_game_hover, self.display_w/4.75, self.display_h/9)
            if self.play_hover_sound == True:
                self.button_hover_sound.play()
                self.play_hover_sound = False
            click = pygame.mouse.get_pressed()
            if click[0]:
                self.draw_button(self.mainmenu_game_pressed, self.display_w/4.75, self.display_h/9)
                if self.play_press_sound == True:
                    self.button_press_sound.play(maxtime=1000)
                    self.play_press_sound = False
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP:
                        self.play_press_sound = True
                        self.playing = False
                        self.main_menu.run_display = True

        else: 
            self.play_hover_sound = True
                
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
                self.show_intro = 0
                sys.exit()
                   
            if self.playing == True:
                if event.type == pygame.USEREVENT + 1 and self.state == 0:
                    self.time += 1
           
                if self.state == 0:
                    if event.type == pygame.MOUSEBUTTONDOWN and self.curr_menu.run_display == False:
                        click = pygame.mouse.get_pressed()
                        if click[0]:
                            pos = pygame.mouse.get_pos()
                            if pos[0]>=self.start_x and pos[0]<=self.start_x + self.nx*self.tile_size:
                                if pos[1]>=self.start_y and pos[1]<=self.start_y + self.ny*self.tile_size:
                                    column = int((pos[0] - (self.display_w-self.nx*self.tile_size)/2) / self.tile_size)
                                    row = int((pos[1] - (self.display_h-self.ny*self.tile_size)/1.2) / self.tile_size)

                                    if self.matrix[row][column] > 0 and self.matrix[row][column] < 9 and self.is_marked[row][column] == 0:
                                        self.tile_press_sound.play(maxtime=1000)

                                    if self.matrix[row][column] == 10 and self.gen == 0:
                                        while self.matrix[row][column] == 10:
                                            self.mine_gen()
                                    self.gen = 1

                                    if self.is_marked[row][column] == 0:
                                        if self.matrix[row][column] == 0:
                                            self.tile_reveal_sound.play(maxtime=1000)
                                        self.trans_grid(row,column)
                                        if self.matrix[row][column] == 9:
                                            self.reveal(row,column)              
                                        elif self.matrix[row][column] == 19:
                                            self.mine_explode_sound.play(maxtime=2000)
                                            self.reveal_all()
                                            self.matrix[row][column] = 20
                                            self.state = 2
                                
                        elif click[2]:
                            pos = pygame.mouse.get_pos()
                            if pos[0]>=self.start_x and pos[0]<=self.start_x + self.nx*self.tile_size:
                                if pos[1]>=self.start_y and pos[1]<=self.start_y + self.ny*self.tile_size:
                                    column = int((pos[0] - (self.display_w-self.nx*self.tile_size)/2) / self.tile_size)
                                    row = int((pos[1] - (self.display_h-self.ny*self.tile_size)/1.2) / self.tile_size)

                                    if self.matrix[row][column] < 11 and self.matrix[row][column] != 9:
                                        if self.is_marked[row][column] == 0:
                                            self.tile_flag_sound.play(maxtime=1000)
                                            self.is_marked[row][column] = 1
                                            self.mine_counter -= 1
                                        elif self.is_marked[row][column] == 1:
                                            self.tile_flag_sound.play(maxtime=1000)
                                            self.is_marked[row][column] = 0
                                            self.mine_counter += 1

                if self.counter <= self.mines:
                    if self.play_win_sound == True:
                        self.game_win_sound.play(maxtime=2000)
                        self.play_win_sound = False
                    self.state = 1

            if self.curr_menu == self.difficulty_menu:
                if event.type == pygame.KEYDOWN and self.curr_menu.custom_state == 1:
                    if len(self.curr_menu.height_text) > 0:
                        if event.key == pygame.K_BACKSPACE:
                            self.curr_menu.height_text = self.curr_menu.height_text[:-1]
                    if len(self.curr_menu.height_text) < 2:
                        if event.key == pygame.K_0 and len(self.curr_menu.height_text) > 0:
                            self.curr_menu.height_text += event.unicode
                        elif event.key == pygame.K_1:
                            self.curr_menu.height_text += event.unicode
                        elif event.key == pygame.K_2:
                            self.curr_menu.height_text += event.unicode
                        elif event.key == pygame.K_3:
                            self.curr_menu.height_text += event.unicode
                        elif event.key == pygame.K_4:
                            self.curr_menu.height_text += event.unicode
                        elif event.key == pygame.K_5:
                           self.curr_menu.height_text += event.unicode
                        elif event.key == pygame.K_6:
                           self.curr_menu.height_text += event.unicode
                        elif event.key == pygame.K_7:
                            self.curr_menu.height_text += event.unicode
                        elif event.key == pygame.K_8:
                            self.curr_menu.height_text += event.unicode
                        elif event.key == pygame.K_9:
                            self.curr_menu.height_text += event.unicode
                    if event.key == pygame.K_RETURN:
                        self.curr_menu.custom_state = 0

                if event.type == pygame.KEYDOWN and self.curr_menu.custom_state == 2:
                    if len(self.curr_menu.width_text) > 0:
                        if event.key == pygame.K_BACKSPACE:
                            self.curr_menu.width_text = self.curr_menu.width_text[:-1]
                    if len(self.curr_menu.width_text) < 2:
                        if event.key == pygame.K_0 and len(self.curr_menu.width_text) > 0:
                            self.curr_menu.width_text += event.unicode
                        elif event.key == pygame.K_1:
                            self.curr_menu.width_text += event.unicode
                        elif event.key == pygame.K_2:
                            self.curr_menu.width_text += event.unicode
                        elif event.key == pygame.K_3:
                            self.curr_menu.width_text += event.unicode
                        elif event.key == pygame.K_4:
                            self.curr_menu.width_text += event.unicode
                        elif event.key == pygame.K_5:
                           self.curr_menu.width_text += event.unicode
                        elif event.key == pygame.K_6:
                           self.curr_menu.width_text += event.unicode
                        elif event.key == pygame.K_7:
                            self.curr_menu.width_text += event.unicode
                        elif event.key == pygame.K_8:
                            self.curr_menu.width_text += event.unicode
                        elif event.key == pygame.K_9:
                            self.curr_menu.width_text += event.unicode
                    if event.key == pygame.K_RETURN:
                        self.curr_menu.custom_state = 0

                if event.type == pygame.KEYDOWN and self.curr_menu.custom_state == 3:
                    if len(self.curr_menu.mines_text) > 0:
                        if event.key == pygame.K_BACKSPACE:
                            self.curr_menu.mines_text = self.curr_menu.mines_text[:-1]
                    if len(self.curr_menu.mines_text) < 4:
                        if event.key == pygame.K_0 and len(self.curr_menu.mines_text) > 0:
                            self.curr_menu.mines_text += event.unicode
                        elif event.key == pygame.K_1:
                            self.curr_menu.mines_text += event.unicode
                        elif event.key == pygame.K_2:
                            self.curr_menu.mines_text += event.unicode
                        elif event.key == pygame.K_3:
                            self.curr_menu.mines_text += event.unicode
                        elif event.key == pygame.K_4:
                            self.curr_menu.mines_text += event.unicode
                        elif event.key == pygame.K_5:
                           self.curr_menu.mines_text += event.unicode
                        elif event.key == pygame.K_6:
                           self.curr_menu.mines_text += event.unicode
                        elif event.key == pygame.K_7:
                            self.curr_menu.mines_text += event.unicode
                        elif event.key == pygame.K_8:
                            self.curr_menu.mines_text += event.unicode
                        elif event.key == pygame.K_9:
                            self.curr_menu.mines_text += event.unicode
                    if event.key == pygame.K_RETURN:
                        self.curr_menu.custom_state = 0
            else:
                pass

    def scale_transform(self, button):
        self.button = button
        self.button = pygame.transform.smoothscale(self.button, (int(self.button.get_width()*self.scale_x), int(self.button.get_height()*self.scale_y)))
        return self.button

    def scale_tile(self, tile):
        rx = 45 / self.nx 
        ry = 25 / self.ny
        if rx < ry:
            r = rx
        else:
            r = ry
        self.tile = tile
        self.tile = pygame.transform.smoothscale(self.tile, (int(self.tile.get_width()*self.scale_x*r/2), int(self.tile.get_height()*self.scale_y*r/2)))
        return self.tile

    def scale_alltiles(self):
        self.tile_hidden = self.scale_tile(self.tile_hiddenorig)
        self.tile_1 = self.scale_tile(self.tile_1orig)
        self.tile_2 = self.scale_tile(self.tile_2orig)
        self.tile_3 = self.scale_tile(self.tile_3orig)
        self.tile_4 = self.scale_tile(self.tile_4orig)
        self.tile_5 = self.scale_tile(self.tile_5orig)
        self.tile_6 = self.scale_tile(self.tile_6orig)
        self.tile_7 = self.scale_tile(self.tile_7orig)
        self.tile_8 = self.scale_tile(self.tile_8orig)
        self.tile_9 = self.scale_tile(self.tile_9orig)
        self.tile_mine = self.scale_tile(self.tile_mineorig)
        self.tile_explode = self.scale_tile(self.tile_explodeorig)
        self.tile_flag = self.scale_tile(self.tile_flagorig)
        self.tile_size = self.tile_hidden.get_width()
        self.shadow_filter = pygame.transform.smoothscale(self.shadow_filterorig, (self.nx*self.tile_size, self.ny*self.tile_size))

    def scale_everything(self):
        self.background = pygame.transform.smoothscale(self.background_orig, (self.display_w, self.display_h))
        self.game_background = pygame.transform.smoothscale(self.game_background_orig, (self.display_w, self.display_h))
        self.credits_background = pygame.transform.smoothscale(self.credits_background_orig, (self.display_w, self.display_h))
        self.fade = pygame.transform.smoothscale(self.fade_orig, (self.display_w, self.display_h))

        self.face_button = self.scale_transform(self.face_button_orig)
        self.face_pressed = self.scale_transform(self.face_pressed_orig)
        self.face_sun = self.scale_transform(self.face_sun_orig)
        self.face_moon = self.scale_transform(self.face_moon_orig)

        self.mainmenu_game = self.scale_transform(self.mainmenu_game_orig)
        self.mainmenu_game_hover = self.scale_transform(self.mainmenu_game_hover_orig)
        self.mainmenu_game_pressed = self.scale_transform(self.mainmenu_game_pressed_orig)
        self.mines_game = self.scale_transform(self.mines_game_orig)
        self.timer_game = self.scale_transform(self.timer_game_orig)

        self.no0 = self.scale_transform(self.no0_orig)
        self.no1 = self.scale_transform(self.no1_orig)
        self.no2 = self.scale_transform(self.no2_orig)
        self.no3 = self.scale_transform(self.no3_orig)
        self.no4 = self.scale_transform(self.no4_orig)
        self.no5 = self.scale_transform(self.no5_orig)
        self.no6 = self.scale_transform(self.no6_orig)
        self.no7 = self.scale_transform(self.no7_orig)
        self.no8 = self.scale_transform(self.no8_orig)
        self.no9 = self.scale_transform(self.no9_orig)
        self.sep = self.scale_transform(self.sep_orig)

        self.numbers_convert = {
            0: self.no0,
            1: self.no1,
            2: self.no2,
            3: self.no3,
            4: self.no4,
            5: self.no5,
            6: self.no6,
            7: self.no7,
            8: self.no8,
            9: self.no9,
            10: self.sep,
        }

        self.play_button = self.scale_transform(self.play_button_orig)
        self.play_hover = self.scale_transform(self.play_hover_orig)
        self.play_pressed = self.scale_transform(self.play_pressed_orig)
        self.difficulty_button = self.scale_transform(self.difficulty_button_orig)
        self.difficulty_hover = self.scale_transform(self.difficulty_hover_orig)
        self.difficulty_pressed = self.scale_transform(self.difficulty_pressed_orig)
        self.settings_button = self.scale_transform(self.settings_button_orig)
        self.settings_hover = self.scale_transform(self.settings_hover_orig)
        self.settings_pressed = self.scale_transform(self.settings_pressed_orig)
        self.credits_button = self.scale_transform(self.credits_button_orig)
        self.credits_hover = self.scale_transform(self.credits_hover_orig)
        self.credits_pressed = self.scale_transform(self.credits_pressed_orig)
        self.exit_button = self.scale_transform(self.exit_button_orig)
        self.exit_hover = self.scale_transform(self.exit_hover_orig)
        self.exit_pressed = self.scale_transform(self.exit_pressed_orig)
        self.back_button = self.scale_transform(self.back_button_orig)
        self.back_hover = self.scale_transform(self.back_hover_orig)
        self.back_pressed = self.scale_transform(self.back_pressed_orig)

        self.beginner_button = self.scale_transform(self.beginner_button_orig)
        self.beginner_hover = self.scale_transform(self.beginner_hover_orig)
        self.beginner_pressed = self.scale_transform(self.beginner_pressed_orig)
        self.beginner_selected = self.scale_transform(self.beginner_selected_orig)
        self.beginner_expl = self.scale_transform(self.beginner_expl_orig)
        self.intermediate_button = self.scale_transform(self.intermediate_button_orig)
        self.intermediate_hover = self.scale_transform(self.intermediate_hover_orig)
        self.intermediate_pressed = self.scale_transform(self.intermediate_pressed_orig)
        self.intermediate_selected = self.scale_transform(self.intermediate_selected_orig)
        self.intermediate_expl = self.scale_transform(self.intermediate_expl_orig)
        self.expert_button = self.scale_transform(self.expert_button_orig)
        self.expert_hover = self.scale_transform(self.expert_hover_orig)
        self.expert_pressed = self.scale_transform(self.expert_pressed_orig)
        self.expert_selected = self.scale_transform(self.expert_selected_orig)
        self.expert_expl = self.scale_transform(self.expert_expl_orig)
        self.custom_button = self.scale_transform(self.custom_button_orig)
        self.custom_hover = self.scale_transform(self.custom_hover_orig)
        self.custom_pressed = self.scale_transform(self.custom_pressed_orig)
        self.custom_selected = self.scale_transform(self.custom_selected_orig)
        self.custom_expl = self.scale_transform(self.custom_expl_orig)
        self.expl_height = self.scale_transform(self.expl_height_orig)
        self.expl_width = self.scale_transform(self.expl_width_orig)
        self.expl_mines = self.scale_transform(self.expl_mines_orig)

        self.display_button = self.scale_transform(self.display_button_orig)
        self.fullscreen_button = self.scale_transform(self.fullscreen_button_orig)
        self.windowed_button = self.scale_transform(self.windowed_button_orig)
        self.resolution_button = self.scale_transform(self.resolution_button_orig)
        self.r640_button = self.scale_transform(self.r640_button_orig)
        self.r800_button = self.scale_transform(self.r800_button_orig)
        self.r1024_button = self.scale_transform(self.r1024_button_orig)
        self.music_button = self.scale_transform(self.music_button_orig)
        self.sounds_button = self.scale_transform(self.sounds_button_orig)
        self.volume_button = self.scale_transform(self.volume_button_orig)
        self.volume_bar = self.scale_transform(self.volume_bar_orig)
        self.larrow_button = self.scale_transform(self.larrow_button_orig)
        self.larrow_hover = self.scale_transform(self.larrow_hover_orig)
        self.larrow_pressed = self.scale_transform(self.larrow_pressed_orig)
        self.rarrow_button = self.scale_transform(self.rarrow_button_orig)
        self.rarrow_hover = self.scale_transform(self.rarrow_hover_orig)
        self.rarrow_pressed = self.scale_transform(self.rarrow_pressed_orig)

        self.tile_size = self.tile_hiddenorig.get_width()
        self.scale_alltiles()

    def draw_button(self, button, x, y):
        self.button_surface = button
        self.button_rect = self.button_surface.get_rect()
        self.button_rect.center = (x, y)
        self.display.blit(self.button_surface, self.button_rect)

    def draw_tile(self, tile, x, y):
        self.tile_surface = tile
        self.tile_rect = self.tile_surface.get_rect()
        self.tile_rect.topleft = (x, y)
        self.display.blit(self.tile_surface, self.tile_rect)

    def draw_volume(self, button, x, y, vol_level):
        self.button_surface = button
        self.button_rect = self.button_surface.get_rect()
        self.button_rect.center = (x, y)
        self.display.blit(self.button_surface, self.button_rect,(0,0,(self.volume_bar.get_width()/10)*vol_level, self.volume_bar.get_height()))

    def draw_grid(self, nx, ny):
        for i in range(ny):
            for j in range(nx):
                if self.matrix[i][j] < 9 or self.matrix[i][j] == 10:
                    self.draw_tile(self.tile_hidden, self.start_x + j*self.tile_size, self.start_y + i*self.tile_size)
                if self.is_marked[i][j] == 1:
                    self.draw_tile(self.tile_flag, self.start_x + j*self.tile_size, self.start_y + i*self.tile_size)
                elif self.matrix[i][j] == 9:
                    self.draw_tile(self.tile_9, self.start_x + j*self.tile_size, self.start_y + i*self.tile_size)
                elif self.matrix[i][j] == 11:
                    self.draw_tile(self.tile_1, self.start_x + j*self.tile_size, self.start_y + i*self.tile_size)
                elif self.matrix[i][j] == 12:
                    self.draw_tile(self.tile_2, self.start_x + j*self.tile_size, self.start_y + i*self.tile_size)
                elif self.matrix[i][j] == 13:
                    self.draw_tile(self.tile_3, self.start_x + j*self.tile_size, self.start_y + i*self.tile_size)
                elif self.matrix[i][j] == 14:
                    self.draw_tile(self.tile_4, self.start_x + j*self.tile_size, self.start_y + i*self.tile_size)
                elif self.matrix[i][j] == 15:
                    self.draw_tile(self.tile_5, self.start_x + j*self.tile_size, self.start_y + i*self.tile_size)
                elif self.matrix[i][j] == 16:
                    self.draw_tile(self.tile_6, self.start_x + j*self.tile_size, self.start_y + i*self.tile_size)
                elif self.matrix[i][j] == 17:
                    self.draw_tile(self.tile_7, self.start_x + j*self.tile_size, self.start_y + i*self.tile_size)
                elif self.matrix[i][j] == 18:
                    self.draw_tile(self.tile_8, self.start_x + j*self.tile_size, self.start_y + i*self.tile_size)
                elif self.matrix[i][j] == 19:
                    self.draw_tile(self.tile_mine, self.start_x + j*self.tile_size, self.start_y + i*self.tile_size)
                elif self.matrix[i][j] == 20:
                    self.draw_tile(self.tile_explode, self.start_x + j*self.tile_size, self.start_y + i*self.tile_size)

    def draw_numbers(self):
        if self.mine_counter < 0:
            self.draw_button(self.numbers_convert[0], self.display_w/1.15, self.display_h/15)
        elif self.mine_counter >= 0 and self.mine_counter < 10:
            self.draw_button(self.numbers_convert[self.mine_counter], self.display_w/1.15, self.display_h/15)
        elif self.mine_counter >= 10 and self.mine_counter < 100:
            self.draw_button(self.numbers_convert[self.mine_counter%10], self.display_w/1.136, self.display_h/15)
            self.draw_button(self.numbers_convert[self.mine_counter//10%10], self.display_w/1.170, self.display_h/15)
        elif self.mine_counter >= 100 and self.mine_counter < 1000:
            self.draw_button(self.numbers_convert[self.mine_counter%10], self.display_w/1.126, self.display_h/15)
            self.draw_button(self.numbers_convert[self.mine_counter//10%10], self.display_w/1.158, self.display_h/15)
            self.draw_button(self.numbers_convert[self.mine_counter//100%10], self.display_w/1.191, self.display_h/15)
        elif self.mine_counter >= 1000:
            self.draw_button(self.numbers_convert[self.mine_counter%10], self.display_w/1.111, self.display_h/15)
            self.draw_button(self.numbers_convert[self.mine_counter//10%10], self.display_w/1.144, self.display_h/15)
            self.draw_button(self.numbers_convert[self.mine_counter//100%10], self.display_w/1.179, self.display_h/15)
            self.draw_button(self.numbers_convert[self.mine_counter//1000%10], self.display_w/1.218, self.display_h/15)

    def mine_gen(self):
        self.matrix = [[0 for x in range(self.nx)]for y in range(self.ny)]
        for i in range(self.mines):
            x = randint(0, self.ny-1)
            y = randint(0 ,self.nx-1)
            if self.matrix[x][y] == 10:
                while self.matrix[x][y] == 10:
                    x = randint(0, self.ny-1)
                    y = randint(0, self.nx-1)
            self.matrix[x][y] = 10   
           
            for j in range(x-1, x+2):
                    if j<0:
                        continue
                    elif j>self.ny-1:
                        continue
                  
                    for k in range(y-1, y+2):
                        if k<0:
                            continue
                        elif k>self.nx-1:
                            continue
                        if self.matrix[j][k]<9:
                            self.matrix[j][k] +=1

    def trans_grid(self,i,j):
        if self.matrix[i][j] == 0:
            self.matrix[i][j] = 9
            self.counter -= 1
        elif self.matrix[i][j] == 1:
            self.matrix[i][j] = 11
            self.counter -= 1
        elif self.matrix[i][j] == 2:
            self.matrix[i][j] = 12
            self.counter -= 1
        elif self.matrix[i][j] == 3:
            self.matrix[i][j] = 13
            self.counter -= 1
        elif self.matrix[i][j] == 4:
            self.matrix[i][j] = 14
            self.counter -= 1
        elif self.matrix[i][j] == 5:
            self.matrix[i][j] = 15
            self.counter -= 1
        elif self.matrix[i][j] == 6:
            self.matrix[i][j] = 16
            self.counter -= 1
        elif self.matrix[i][j] == 7:
            self.matrix[i][j] = 17
            self.counter -= 1
        elif self.matrix[i][j] == 8:
            self.matrix[i][j] = 18
            self.counter -= 1
        elif self.matrix[i][j] == 10:
            self.matrix[i][j] = 19
                                              
    def reveal(self,row,col):
        i = row
        j = col
        if i >= 0 and j >= 0 and i < self.ny and j < self.nx:
            for k in range(i-1, i+2):
                if k<0:
                    continue
                elif k>self.ny-1:
                    continue
              
                for l in range(j-1, j+2):
                    if l<0:
                        continue
                    elif l>self.nx-1:
                        continue

                    if self.is_marked[k][l] == 0:
                        if self.matrix[k][l] < 9:
                            self.trans_grid(k,l)
                            if self.matrix[k][l] == 9:
                                self.reveal(k,l)

    def reveal_all(self):
        for i in range(self.ny):
            for j in range(self.nx):
                if self.matrix[i][j] == 10:
                    self.trans_grid(i,j)

    def intro(self):
        for alpha in range(0, 500):
            self.fade.set_alpha(int(alpha/5))
            self.window.blit(self.fade, (0,0))
            if self.show_intro == 0:
                return
            pygame.display.update()

        self.fade.fill((0,0,0))
        for alpha in range(0, 200):
            self.fade.set_alpha(int(alpha/2))
            self.window.blit(self.fade, (0,0))
            if self.show_intro == 0:
                return
            pygame.display.update()
        
        self.show_intro = 0

    def timer(self):
        mins, secs = divmod(self.time, 60)        
        self.draw_button(self.numbers_convert[secs%10], self.display_w/1.104, self.display_h/6)
        self.draw_button(self.numbers_convert[secs//10%10], self.display_w/1.139, self.display_h/6)
        self.draw_button(self.numbers_convert[10], self.display_w/1.167, self.display_h/6)
        self.draw_button(self.numbers_convert[mins%10], self.display_w/1.195, self.display_h/6)
        self.draw_button(self.numbers_convert[mins//10%10], self.display_w/1.234, self.display_h/6)

    def set_sounds_volume(self, vol):
        self.button_hover_sound.set_volume(vol/10)
        self.button_press_sound.set_volume(vol/10)
        self.tile_press_sound.set_volume(vol/10)
        self.tile_flag_sound.set_volume(vol/10)
        self.mine_explode_sound.set_volume(vol/10)
        self.tile_reveal_sound.set_volume(vol/10)
        self.game_win_sound.set_volume(vol/10)
        self.face_press_sound.set_volume(vol/10)

    def reset_game(self):
         self.state = 0
         self.mine_gen()
         self.counter = self.nx*self.ny
         self.mine_counter = self.mines
         self.is_marked = [[0 for x in range(self.nx)]for y in range(self.ny)]
         self.gen = 0
         self.time = 0
         self.play_win_sound = True
