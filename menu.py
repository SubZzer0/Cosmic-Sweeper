
import pygame

class Menu():
    def __init__(self, game):
        self.game = game
        self.run_display = True
        self.res_change = 0

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()

    def resize_screen_w(self,x,y):
        self.game.display_w, self.game.display_h = x, y
        self.game.scale_x = self.game.display_w / 2441
        self.game.scale_y = self.game.display_h / 1827
        self.game.mid_w, self.game.mid_h = self.game.display_w/2, self.game.display_h/2
        self.game.display = pygame.Surface ((self.game.display_w, self.game.display_h))
        self.game.window = pygame.display.set_mode((self.game.display_w, self.game.display_h))
        self.game.scale_everything()
        self.game.start_x = (self.game.display_w-(self.game.nx*self.game.tile_size))/2
        self.game.start_y = (self.game.display_h-(self.game.ny*self.game.tile_size))/1.2

    def resize_screen_f(self,x,y):
        self.game.display_w, self.game.display_h = x, y
        self.game.scale_x = self.game.display_w / 2441
        self.game.scale_y = self.game.display_h / 1827
        self.game.mid_w, self.game.mid_h = self.game.display_w/2, self.game.display_h/2
        self.game.display = pygame.Surface ((self.game.display_w, self.game.display_h))
        self.game.window = pygame.display.set_mode((self.game.display_w, self.game.display_h), pygame.FULLSCREEN)
        self.game.scale_everything()
        self.game.start_x = (self.game.display_w-(self.game.nx*self.game.tile_size))/2
        self.game.start_y = (self.game.display_h-(self.game.ny*self.game.tile_size))/1.2

    def resize_screen_sm(self):
        self.sm_init()

    def resize_screen_dm(self):
        self.dm_init()

    def resize_screen_cm(self):
        self.cm_init()

    def resize_screen_mm(self):
        self.mm_init()   
        

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.mm_init()

    def mm_init(self):
        self.play_x, self.play_y = self.game.mid_w, self.game.mid_h-500*self.game.scale_y
        self.difficulty_x, self.difficulty_y = self.game.mid_w, self.game.mid_h-200*self.game.scale_y
        self.settings_x, self.settings_y = self.game.mid_w, self.game.mid_h+50*self.game.scale_y
        self.credits_x, self.credits_y = self.game.mid_w, self.game.mid_h+300*self.game.scale_y
        self.exit_x, self.exit_y = self.game.mid_w, self.game.mid_h+550*self.game.scale_y

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.display.blit(self.game.background, (0, 0))
            self.game.draw_button(self.game.play_button, self.play_x, self.play_y)
            self.play_rect = self.game.button_rect.inflate(-30,-30)
            self.game.draw_button(self.game.difficulty_button, self.difficulty_x, self.difficulty_y)
            self.difficulty_rect = self.game.button_rect.inflate(-30,-30)
            self.game.draw_button(self.game.settings_button, self.settings_x, self.settings_y)
            self.settings_rect = self.game.button_rect.inflate(-30,-30)
            self.game.draw_button(self.game.credits_button, self.credits_x, self.credits_y)
            self.credits_rect = self.game.button_rect.inflate(-30,-30)
            self.game.draw_button(self.game.exit_button, self.exit_x, self.exit_y)
            self.exit_rect = self.game.button_rect.inflate(-30,-30)

            self.check_input()
            self.game.check_events()
            self.blit_screen()

    def check_input(self):
        pos = pygame.mouse.get_pos()
        if self.play_rect.collidepoint(pos):
            self.game.draw_button(self.game.play_hover, self.play_x, self.play_y)
            if self.game.play_hover_sound == True:
                self.game.button_hover_sound.play()
                self.game.play_hover_sound = False
            click = pygame.mouse.get_pressed()
            if click[0]:
                self.game.draw_button(self.game.play_pressed, self.play_x, self.play_y)
                if self.game.play_press_sound == True:
                    self.game.button_press_sound.play(maxtime=1000)
                    self.game.play_press_sound = False
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP:
                        self.game.play_press_sound = True
                        self.run_display = False
                        self.game.playing = True
                        self.game.reset_game()

        elif self.difficulty_rect.collidepoint(pos):
            self.game.draw_button(self.game.difficulty_hover, self.difficulty_x, self.difficulty_y)
            if self.game.play_hover_sound == True:
                self.game.button_hover_sound.play()
                self.game.play_hover_sound = False
            click = pygame.mouse.get_pressed()
            if click[0]:
                self.game.draw_button(self.game.difficulty_pressed, self.difficulty_x, self.difficulty_y)
                if self.game.play_press_sound == True:
                    self.game.button_press_sound.play(maxtime=1000)
                    self.game.play_press_sound = False
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP:
                        self.game.play_press_sound = True
                        self.game.curr_menu = self.game.difficulty_menu
                        self.run_display = False

        elif self.settings_rect.collidepoint(pos):
            self.game.draw_button(self.game.settings_hover, self.settings_x, self.settings_y)
            if self.game.play_hover_sound == True:
                self.game.button_hover_sound.play()
                self.game.play_hover_sound = False
            click = pygame.mouse.get_pressed()
            if click[0]:
                self.game.draw_button(self.game.settings_pressed, self.settings_x, self.settings_y)
                if self.game.play_press_sound == True:
                    self.game.button_press_sound.play(maxtime=1000)
                    self.game.play_press_sound = False
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP:
                        self.game.play_press_sound = True
                        self.game.curr_menu = self.game.settings_menu
                        self.run_display = False

        elif self.credits_rect.collidepoint(pos):
            self.game.draw_button(self.game.credits_hover, self.credits_x, self.credits_y)
            if self.game.play_hover_sound == True:
                self.game.button_hover_sound.play()
                self.game.play_hover_sound = False
            click = pygame.mouse.get_pressed()
            if click[0]:
                self.game.draw_button(self.game.credits_pressed, self.credits_x, self.credits_y)
                if self.game.play_press_sound == True:
                    self.game.button_press_sound.play(maxtime=1000)
                    self.game.play_press_sound = False
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP:
                        self.game.play_press_sound = True
                        self.game.curr_menu = self.game.credits_menu
                        self.run_display = False             

        elif self.exit_rect.collidepoint(pos):
            self.game.draw_button(self.game.exit_hover, self.exit_x, self.exit_y)
            if self.game.play_hover_sound == True:
                self.game.button_hover_sound.play()
                self.game.play_hover_sound = False
            click = pygame.mouse.get_pressed()
            if click[0]:
                self.game.draw_button(self.game.exit_pressed, self.exit_x, self.exit_y)
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP:
                        self.game.running, self.game.playing = False, False
                        self.run_display = False

        else: 
            self.game.play_hover_sound = True

class DifficultyMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.dm_init()

        self.custom_state = 0
        self.height_text = '20'
        self.width_text = '30'
        self.mines_text = '145'

    def dm_init(self):
        self.beginner_x, self.beginner_y = self.game.display_w/4.45, self.game.mid_h-550*self.game.scale_y
        self.intermediate_x, self.intermediate_y = self.game.display_w/4.45, self.game.mid_h-275*self.game.scale_y
        self.expert_x, self.expert_y = self.game.display_w/4.45, self.game.mid_h+0*self.game.scale_y
        self.custom_x, self.custom_y = self.game.display_w/4.45, self.game.mid_h+275*self.game.scale_y
        self.back_x, self.back_y = self.game.mid_w, self.game.mid_h+600*self.game.scale_y

        self.expl_height_x, self.expl_height_y = self.game.display_w/2.17, self.game.mid_h+275*self.game.scale_y
        self.expl_height_rect = self.game.expl_height.get_rect()
        self.expl_height_rect.center = (self.expl_height_x, self.expl_height_y)

        self.expl_width_x, self.expl_width_y = self.game.display_w/1.75, self.game.mid_h+275*self.game.scale_y
        self.expl_width_rect = self.game.expl_width.get_rect()
        self.expl_width_rect.center = (self.expl_width_x, self.expl_height_y)

        self.expl_mines_x, self.expl_mines_y = self.game.display_w/1.47, self.game.mid_h+275*self.game.scale_y
        self.expl_mines_rect = self.game.expl_mines.get_rect()
        self.expl_mines_rect.center = (self.expl_mines_x, self.expl_mines_y)

        self.beginner2_x, self.beginner2_y = self.game.display_w/1.53, self.game.mid_h-550*self.game.scale_y
        self.intermediate2_x, self.intermediate2_y = self.game.display_w/1.53, self.game.mid_h-275*self.game.scale_y
        self.expert2_x, self.expert2_y = self.game.display_w/1.53, self.game.mid_h+0*self.game.scale_y
        self.custom2_x, self.custom2_y = self.game.display_w/1.53, self.game.mid_h+275*self.game.scale_y

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.display.blit(self.game.background, (0, 0))
            if self.game.difficulty != 0:
                self.game.draw_button(self.game.beginner_button, self.beginner_x, self.beginner_y)
            else:
                self.game.draw_button(self.game.beginner_selected, self.beginner_x, self.beginner_y)
            self.beginner_rect = self.game.button_rect.inflate(-30,-30)
            if self.game.difficulty != 1:
                self.game.draw_button(self.game.intermediate_button, self.intermediate_x, self.intermediate_y)
            else:
                self.game.draw_button(self.game.intermediate_selected, self.intermediate_x, self.intermediate_y)
            self.intermediate_rect = self.game.button_rect.inflate(-30,-30)
            if self.game.difficulty != 2:
                self.game.draw_button(self.game.expert_button, self.expert_x, self.expert_y)
            else:
                self.game.draw_button(self.game.expert_selected, self.expert_x, self.expert_y)
            self.expert_rect = self.game.button_rect.inflate(-30,-30)
            if self.game.difficulty != 3:
                self.game.draw_button(self.game.custom_button, self.custom_x, self.custom_y)
            else:
                self.game.draw_button(self.game.custom_selected, self.custom_x, self.custom_y)
            self.custom_rect = self.game.button_rect.inflate(-30,-30)

            self.game.draw_button(self.game.back_button, self.back_x, self.back_y)
            self.back_rect = self.game.button_rect.inflate(-30,-30)
            self.game.draw_button(self.game.beginner_expl, self.beginner2_x, self.beginner2_y)
            self.game.draw_button(self.game.intermediate_expl, self.intermediate2_x, self.intermediate2_y)
            self.game.draw_button(self.game.expert_expl, self.expert2_x, self.expert2_y)
            self.game.draw_button(self.game.custom_expl, self.custom2_x, self.custom2_y)

            if self.custom_state == 1 and self.game.difficulty == 3:
                self.game.draw_button(self.game.expl_height, self.expl_height_x, self.expl_height_y)
                if len(self.height_text) > 0:
                    if int(self.height_text) > 25:
                        self.height_text = '25'
                    self.game.ny = int(self.height_text)
            if len(self.height_text) == 1:
                self.game.draw_button(self.game.numbers_convert[int(self.height_text[0])], self.expl_height_x, self.expl_height_y)
            if len(self.height_text) == 2:
                self.game.draw_button(self.game.numbers_convert[int(self.height_text[0])], self.expl_height_x/1.035, self.expl_height_y)
                self.game.draw_button(self.game.numbers_convert[int(self.height_text[1])], self.expl_height_x*1.02, self.expl_height_y)
                
            if self.custom_state == 2 and self.game.difficulty == 3:
                self.game.draw_button(self.game.expl_width, self.expl_width_x, self.expl_width_y)
                if len(self.width_text) > 0:
                    if int(self.width_text) > 45:
                        self.width_text = '45'
                    self.game.nx = int(self.width_text)
            if len(self.width_text) == 1:
                self.game.draw_button(self.game.numbers_convert[int(self.width_text[0])], self.expl_width_x, self.expl_width_y)
            if len(self.width_text) == 2:
                self.game.draw_button(self.game.numbers_convert[int(self.width_text[0])], self.expl_width_x/1.03, self.expl_width_y)
                self.game.draw_button(self.game.numbers_convert[int(self.width_text[1])], self.expl_width_x*1.015, self.expl_width_y)

            if self.custom_state == 3 and self.game.difficulty == 3:
                self.game.draw_button(self.game.expl_mines, self.expl_mines_x, self.expl_mines_y)
            if len(self.mines_text) > 0:
                if int(self.mines_text) > self.game.nx * self.game.ny and self.game.difficulty == 3:
                    self.mines_text = str(self.game.nx * self.game.ny - 1)
            if len(self.mines_text) == 1:
                self.game.draw_button(self.game.numbers_convert[int(self.mines_text[0])], self.expl_mines_x, self.expl_mines_y)
            if len(self.mines_text) == 2:
                self.game.draw_button(self.game.numbers_convert[int(self.mines_text[0])], self.expl_mines_x/1.025, self.expl_mines_y)
                self.game.draw_button(self.game.numbers_convert[int(self.mines_text[1])], self.expl_mines_x*1.015, self.expl_mines_y)
            if len(self.mines_text) == 3:
                self.game.draw_button(self.game.numbers_convert[int(self.mines_text[0])], self.expl_mines_x/1.05, self.expl_mines_y)
                self.game.draw_button(self.game.numbers_convert[int(self.mines_text[1])], self.expl_mines_x/1.01, self.expl_mines_y)
                self.game.draw_button(self.game.numbers_convert[int(self.mines_text[2])], self.expl_mines_x*1.03, self.expl_mines_y)
            if len(self.mines_text) == 4:
                self.game.draw_button(self.game.numbers_convert[int(self.mines_text[0])], self.expl_mines_x/1.065, self.expl_mines_y)
                self.game.draw_button(self.game.numbers_convert[int(self.mines_text[1])], self.expl_mines_x/1.025, self.expl_mines_y)
                self.game.draw_button(self.game.numbers_convert[int(self.mines_text[2])], self.expl_mines_x*1.015, self.expl_mines_y)
                self.game.draw_button(self.game.numbers_convert[int(self.mines_text[3])], self.expl_mines_x*1.05, self.expl_mines_y)
            
            self.check_input()
            self.game.check_events()
            self.blit_screen()

    def check_input(self):
        pos = pygame.mouse.get_pos()
        if self.beginner_rect.collidepoint(pos) and self.game.difficulty != 0:
            self.game.draw_button(self.game.beginner_hover, self.beginner_x, self.beginner_y)
            if self.game.play_hover_sound == True:
                self.game.button_hover_sound.play()
                self.game.play_hover_sound = False
            click = pygame.mouse.get_pressed()
            if click[0]:
                self.game.draw_button(self.game.beginner_pressed, self.beginner_x, self.beginner_y)
                if self.game.play_press_sound == True:
                    self.game.button_press_sound.play(maxtime=1000)
                    self.game.play_press_sound = False
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP:
                        self.game.play_press_sound = True
                        self.reset_difficulty(0,9,9,10)

        elif self.intermediate_rect.collidepoint(pos) and self.game.difficulty != 1:
            self.game.draw_button(self.game.intermediate_hover, self.intermediate_x, self.intermediate_y)
            if self.game.play_hover_sound == True:
                self.game.button_hover_sound.play()
                self.game.play_hover_sound = False
            click = pygame.mouse.get_pressed()
            if click[0]:
                self.game.draw_button(self.game.intermediate_pressed, self.intermediate_x, self.intermediate_y)
                if self.game.play_press_sound == True:
                    self.game.button_press_sound.play(maxtime=1000)
                    self.game.play_press_sound = False
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP:
                        self.game.play_press_sound = True
                        self.reset_difficulty(1,16,16,40)

        elif self.expert_rect.collidepoint(pos) and self.game.difficulty != 2:
            self.game.draw_button(self.game.expert_hover, self.expert_x, self.expert_y)
            if self.game.play_hover_sound == True:
                self.game.button_hover_sound.play()
                self.game.play_hover_sound = False
            click = pygame.mouse.get_pressed()
            if click[0]:
                self.game.draw_button(self.game.expert_pressed, self.expert_x, self.expert_y)
                if self.game.play_press_sound == True:
                    self.game.button_press_sound.play(maxtime=1000)
                    self.game.play_press_sound = False
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP:
                        self.game.play_press_sound = True
                        self.reset_difficulty(2,30,16,99)

        elif self.custom_rect.collidepoint(pos) and self.game.difficulty != 3:
            self.game.draw_button(self.game.custom_hover, self.custom_x, self.custom_y)
            if self.game.play_hover_sound == True:
                self.game.button_hover_sound.play()
                self.game.play_hover_sound = False
            click = pygame.mouse.get_pressed()
            if click[0]:
                self.game.draw_button(self.game.custom_pressed, self.custom_x, self.custom_y)
                if self.game.play_press_sound == True:
                    self.game.button_press_sound.play(maxtime=1000)
                    self.game.play_press_sound = False
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP:
                        self.game.play_press_sound = True
                        self.reset_difficulty(3,int(self.width_text),int(self.height_text),int(self.mines_text))

        elif self.expl_height_rect.collidepoint(pos) and self.game.difficulty == 3 and self.custom_state != 1:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.custom_state = 1

        elif self.expl_width_rect.collidepoint(pos) and self.game.difficulty == 3 and self.custom_state != 2:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.custom_state = 2

        elif self.expl_mines_rect.collidepoint(pos) and self.game.difficulty == 3 and self.custom_state != 3:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.custom_state = 3

        elif self.back_rect.collidepoint(pos):
            self.game.draw_button(self.game.back_hover, self.back_x, self.back_y)
            if self.game.play_hover_sound == True:
                self.game.button_hover_sound.play()
                self.game.play_hover_sound = False
            click = pygame.mouse.get_pressed()
            if click[0]:
                self.game.draw_button(self.game.back_pressed, self.back_x, self.back_y)
                if self.game.play_press_sound == True:
                    self.game.button_press_sound.play(maxtime=1000)
                    self.game.play_press_sound = False
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP:
                        self.game.play_press_sound = True
                        if not self.height_text:
                            self.height_text = '9'
                        elif not self.width_text:
                            self.width_text = '9'
                        elif not self.width_text:
                            self.width_text = '1'
                        elif int(self.height_text) == 1 and int(self.width_text) == 1:
                            self.height_text = '9'
                            self.width_text = '9'
                        self.game.curr_menu = self.game.main_menu
                        self.run_display = False
                        if self.game.difficulty == 3:
                            self.reset_difficulty(3,int(self.width_text),int(self.height_text),int(self.mines_text))

        else: 
            self.game.play_hover_sound = True

    def reset_difficulty(self,difficulty,nx,ny,mines):
        self.game.difficulty = difficulty
        self.game.nx = nx
        self.game.ny = ny
        self.game.mines = mines
        self.game.scale_alltiles()
        self.game.start_x = (self.game.display_w-(self.game.nx*self.game.tile_size))/2
        self.game.start_y = (self.game.display_h-(self.game.ny*self.game.tile_size))/1.2
        self.custom_state = 0
        self.game.reset_game()    

class SettingsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.sm_init()

        self.disp_mode = 0
        self.disp_change = 0
        self.res_mode = 1
        self.res_change = 1
        self.music_volume = 10
        self.sounds_volume = 10

    def sm_init(self):
        self.display_x, self.display_y = self.game.display_w/4.45, self.game.mid_h-550*self.game.scale_y
        self.resolution_x, self.resolution_y = self.game.display_w/4.45, self.game.mid_h-275*self.game.scale_y
        self.music_x, self.music_y = self.game.display_w/4.45, self.game.mid_h+0*self.game.scale_y
        self.sounds_x, self.sounds_y = self.game.display_w/4.45, self.game.mid_h+275*self.game.scale_y
        self.back_x, self.back_y = self.game.mid_w, self.game.mid_h+600*self.game.scale_y

        self.display2_x, self.display2_y = self.game.display_w/1.53, self.game.mid_h-550*self.game.scale_y
        self.resolution2_x, self.resolution2_y = self.game.display_w/1.53, self.game.mid_h-275*self.game.scale_y
        self.music2_x, self.music2_y = self.game.display_w/1.53, self.game.mid_h+0*self.game.scale_y
        self.sounds2_x, self.sounds2_y = self.game.display_w/1.53, self.game.mid_h+275*self.game.scale_y
        self.volume_bar_mx, self.volume_bar_my = self.game.display_w/1.99, self.game.mid_h+0*self.game.scale_y
        self.volume_bar_sx, self.volume_bar_sy = self.game.display_w/1.99, self.game.mid_h-275*self.game.scale_y

        self.larrow1_x, self.larrow1_y = self.game.display_w/2.26, self.game.mid_h-550*self.game.scale_y
        self.larrow1_rect = self.game.larrow_button.get_rect()
        self.larrow1_rect = self.larrow1_rect.inflate(-30,-30)
        self.larrow1_rect.center  = (self.larrow1_x, self.larrow1_y)
        self.rarrow1_x, self.rarrow1_y = self.game.display_w/1.156, self.game.mid_h-550*self.game.scale_y
        self.rarrow1_rect = self.game.rarrow_button.get_rect()
        self.rarrow1_rect = self.rarrow1_rect.inflate(-30,-30)
        self.rarrow1_rect.center  = (self.rarrow1_x, self.rarrow1_y)

        self.larrow2_x, self.larrow2_y = self.game.display_w/2.26, self.game.mid_h-275*self.game.scale_y
        self.larrow2_rect = self.game.larrow_button.get_rect()
        self.larrow2_rect = self.larrow2_rect.inflate(-30,-30)
        self.larrow2_rect.center  = (self.larrow2_x, self.larrow2_y)
        self.rarrow2_x, self.rarrow2_y = self.game.display_w/1.156, self.game.mid_h-275*self.game.scale_y
        self.rarrow2_rect = self.game.rarrow_button.get_rect()
        self.rarrow2_rect = self.rarrow2_rect.inflate(-30,-30)
        self.rarrow2_rect.center  = (self.rarrow2_x, self.rarrow2_y)

        self.larrow3_x, self.larrow3_y = self.game.display_w/2.26, self.game.mid_h-0*self.game.scale_y
        self.larrow3_rect = self.game.larrow_button.get_rect()
        self.larrow3_rect = self.larrow3_rect.inflate(-30,-30)
        self.larrow3_rect.center  = (self.larrow3_x, self.larrow3_y)
        self.rarrow3_x, self.rarrow3_y = self.game.display_w/1.156, self.game.mid_h-0*self.game.scale_y
        self.rarrow3_rect = self.game.rarrow_button.get_rect()
        self.rarrow3_rect = self.rarrow3_rect.inflate(-30,-30)
        self.rarrow3_rect.center  = (self.rarrow3_x, self.rarrow3_y)

        self.larrow4_x, self.larrow4_y = self.game.display_w/2.26, self.game.mid_h+275*self.game.scale_y
        self.larrow4_rect = self.game.larrow_button.get_rect()
        self.larrow4_rect = self.larrow4_rect.inflate(-30,-30)
        self.larrow4_rect.center  = (self.larrow4_x, self.larrow4_y)
        self.rarrow4_x, self.rarrow4_y = self.game.display_w/1.156, self.game.mid_h+275*self.game.scale_y
        self.rarrow4_rect = self.game.rarrow_button.get_rect()
        self.rarrow4_rect = self.rarrow4_rect.inflate(-30,-30)
        self.rarrow4_rect.center  = (self.rarrow4_x, self.rarrow4_y)

    def resize_everything(self):
        self.game.settings_menu.resize_screen_sm()
        self.game.difficulty_menu.resize_screen_dm()
        self.game.credits_menu.resize_screen_cm()
        self.game.main_menu.resize_screen_mm()

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.display.blit(self.game.background, (0, 0))
            self.game.draw_button(self.game.display_button, self.display_x, self.display_y)
            self.game.draw_button(self.game.resolution_button, self.resolution_x, self.resolution_y)
            self.game.draw_button(self.game.music_button, self.music_x, self.music_y)
            self.game.draw_button(self.game.sounds_button, self.sounds_x, self.sounds_y)
            self.game.draw_button(self.game.back_button, self.back_x, self.back_y)
            self.back_rect = self.game.button_rect.inflate(-30,-30)

            if self.disp_mode == 0:
                self.game.draw_button(self.game.windowed_button, self.display2_x, self.display2_y)
            elif self.disp_mode == 1:
                self.game.draw_button(self.game.fullscreen_button, self.display2_x, self.display2_y)
            if self.res_mode == 0:
                self.game.draw_button(self.game.r640_button, self.resolution2_x, self.resolution2_y)
            elif self.res_mode == 1:
                self.game.draw_button(self.game.r800_button, self.resolution2_x, self.resolution2_y)
            elif self.res_mode == 2:
                self.game.draw_button(self.game.r1024_button, self.resolution2_x, self.resolution2_y)

            self.game.draw_button(self.game.volume_button, self.music2_x, self.music2_y)
            self.game.draw_button(self.game.volume_button, self.sounds2_x, self.sounds2_y)
            self.game.draw_volume(self.game.volume_bar, self.music2_x, self.music2_y, int(self.music_volume))
            self.game.draw_volume(self.game.volume_bar, self.sounds2_x, self.sounds2_y, self.sounds_volume)

            self.game.draw_button(self.game.larrow_button, self.larrow1_x, self.larrow1_y)
            self.game.draw_button(self.game.rarrow_button, self.rarrow1_x, self.rarrow1_y)
            self.game.draw_button(self.game.larrow_button, self.larrow2_x, self.larrow2_y)
            self.game.draw_button(self.game.rarrow_button, self.rarrow2_x, self.rarrow2_y)
            self.game.draw_button(self.game.larrow_button, self.larrow3_x, self.larrow3_y)
            self.game.draw_button(self.game.rarrow_button, self.rarrow3_x, self.rarrow3_y)
            self.game.draw_button(self.game.larrow_button, self.larrow4_x, self.larrow4_y)
            self.game.draw_button(self.game.rarrow_button, self.rarrow4_x, self.rarrow4_y)

            self.check_input()
            self.game.check_events()
            self.blit_screen()

    def check_input(self):
        pos = pygame.mouse.get_pos()
        if self.larrow1_rect.collidepoint(pos):
            self.game.draw_button(self.game.larrow_hover, self.larrow1_x, self.larrow1_y)
            if self.game.play_hover_sound == True:
                self.game.button_hover_sound.play()
                self.game.play_hover_sound = False
            click = pygame.mouse.get_pressed()
            if click[0]:
                self.game.draw_button(self.game.larrow_pressed, self.larrow1_x, self.larrow1_y)
                if self.game.play_press_sound == True:
                    self.game.button_press_sound.play(maxtime=1000)
                    self.game.play_press_sound = False
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP:
                        self.game.play_press_sound = True
                        if self.disp_mode == 0:
                            self.disp_mode = 1
                        else:
                            self.disp_mode = 0
                        
        elif self.rarrow1_rect.collidepoint(pos):
            self.game.draw_button(self.game.rarrow_hover, self.rarrow1_x, self.rarrow1_y)
            if self.game.play_hover_sound == True:
                self.game.button_hover_sound.play()
                self.game.play_hover_sound = False
            click = pygame.mouse.get_pressed()
            if click[0]:
                self.game.draw_button(self.game.rarrow_pressed, self.rarrow1_x, self.rarrow1_y)
                if self.game.play_press_sound == True:
                    self.game.button_press_sound.play(maxtime=1000)
                    self.game.play_press_sound = False
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP:
                        self.game.play_press_sound = True
                        if self.disp_mode == 0:
                            self.disp_mode = 1
                        else:
                            self.disp_mode = 0

        elif self.larrow2_rect.collidepoint(pos):
            self.game.draw_button(self.game.larrow_hover, self.larrow2_x, self.larrow2_y)
            if self.game.play_hover_sound == True:
                self.game.button_hover_sound.play()
                self.game.play_hover_sound = False
            click = pygame.mouse.get_pressed()
            if click[0]:
                self.game.draw_button(self.game.larrow_pressed, self.larrow2_x, self.larrow2_y)
                if self.game.play_press_sound == True:
                    self.game.button_press_sound.play(maxtime=1000)
                    self.game.play_press_sound = False
                if self.res_mode > 0:
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONUP:
                            self.game.play_press_sound = True
                            self.res_mode -= 1

        elif self.rarrow2_rect.collidepoint(pos):
            self.game.draw_button(self.game.rarrow_hover, self.rarrow2_x, self.rarrow2_y)
            if self.game.play_hover_sound == True:
                self.game.button_hover_sound.play()
                self.game.play_hover_sound = False
            click = pygame.mouse.get_pressed()
            if click[0]:
                self.game.draw_button(self.game.rarrow_pressed, self.rarrow2_x, self.rarrow2_y)
                if self.game.play_press_sound == True:
                    self.game.button_press_sound.play(maxtime=1000)
                    self.game.play_press_sound = False
                if self.res_mode < 2:
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONUP:
                            self.game.play_press_sound = True
                            self.res_mode += 1

        elif self.larrow3_rect.collidepoint(pos):
            self.game.draw_button(self.game.larrow_hover, self.larrow3_x, self.larrow3_y)
            if self.game.play_hover_sound == True:
                self.game.button_hover_sound.play()
                self.game.play_hover_sound = False
            click = pygame.mouse.get_pressed()
            if click[0]:
                self.game.draw_button(self.game.larrow_pressed, self.larrow3_x, self.larrow3_y)
                if self.game.play_press_sound == True:
                    self.game.button_press_sound.play(maxtime=1000)
                    self.game.play_press_sound = False
                if self.music_volume > 0:
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONUP:
                            self.game.play_press_sound = True
                            self.music_volume -= 1
                            pygame.mixer.music.set_volume(self.music_volume/10)

        elif self.rarrow3_rect.collidepoint(pos):
            self.game.draw_button(self.game.rarrow_hover, self.rarrow3_x, self.rarrow3_y)
            if self.game.play_hover_sound == True:
                self.game.button_hover_sound.play()
                self.game.play_hover_sound = False
            click = pygame.mouse.get_pressed()
            if click[0]:
                self.game.draw_button(self.game.rarrow_pressed, self.rarrow3_x, self.rarrow3_y)
                if self.game.play_press_sound == True:
                    self.game.button_press_sound.play(maxtime=1000)
                    self.game.play_press_sound = False
                if self.music_volume < 10:
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONUP:
                            self.game.play_press_sound = True
                            self.music_volume += 1
                            pygame.mixer.music.set_volume(self.music_volume/10)

        elif self.larrow4_rect.collidepoint(pos):
            self.game.draw_button(self.game.larrow_hover, self.larrow4_x, self.larrow4_y)
            if self.game.play_hover_sound == True:
                self.game.button_hover_sound.play()
                self.game.play_hover_sound = False
            click = pygame.mouse.get_pressed()
            if click[0]:
                self.game.draw_button(self.game.larrow_pressed, self.larrow4_x, self.larrow4_y)
                if self.game.play_press_sound == True:
                    self.game.button_press_sound.play(maxtime=1000)
                    self.game.play_press_sound = False
                if self.sounds_volume > 0:
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONUP:
                            self.game.play_press_sound = True
                            self.sounds_volume -= 1
                            self.game.set_sounds_volume(self.sounds_volume)

        elif self.rarrow4_rect.collidepoint(pos):
            self.game.draw_button(self.game.rarrow_hover, self.rarrow4_x, self.rarrow4_y)
            if self.game.play_hover_sound == True:
                self.game.button_hover_sound.play()
                self.game.play_hover_sound = False
            click = pygame.mouse.get_pressed()
            if click[0]:
                self.game.draw_button(self.game.rarrow_pressed, self.rarrow4_x, self.rarrow4_y)
                if self.game.play_press_sound == True:
                    self.game.button_press_sound.play(maxtime=1000)
                    self.game.play_press_sound = False
                if self.sounds_volume < 10:
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONUP:
                            self.game.play_press_sound = True
                            self.sounds_volume += 1
                            self.game.set_sounds_volume(self.sounds_volume)

        elif self.back_rect.collidepoint(pos):
            self.game.draw_button(self.game.back_hover, self.back_x, self.back_y)
            if self.game.play_hover_sound == True:
                self.game.button_hover_sound.play()
                self.game.play_hover_sound = False
            click = pygame.mouse.get_pressed()
            if click[0]:
                self.game.draw_button(self.game.back_pressed, self.back_x, self.back_y)
                if self.game.play_press_sound == True:
                    self.game.button_press_sound.play(maxtime=1000)
                    self.game.play_press_sound = False
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP:
                        self.game.play_press_sound = True
                        if self.disp_change != self.disp_mode or self.res_change != self.res_mode:
                            if self.disp_mode == 0:
                                if self.res_mode == 0:
                                    self.resize_screen_w(640, 480)
                                    self.resize_everything()
                                elif self.res_mode == 1:
                                    self.resize_screen_w(800, 600)
                                    self.resize_everything()
                                elif self.res_mode == 2:
                                    self.resize_screen_w(1024, 768)
                                    self.resize_everything()

                            elif self.disp_mode == 1:
                                if self.res_mode == 0:
                                    self.resize_screen_f(640, 480)
                                    self.resize_everything()
                                elif self.res_mode == 1:
                                    self.resize_screen_f(800, 600)
                                    self.resize_everything()
                                elif self.res_mode == 2:
                                    self.resize_screen_f(1024, 768)
                                    self.resize_everything()

                        self.disp_change = self.disp_mode
                        self.res_change = self.res_mode
                        self.game.curr_menu = self.game.main_menu
                        self.run_display = False

        else: 
            self.game.play_hover_sound = True

class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.cm_init()

    def cm_init(self):
        self.back_x, self.back_y = self.game.mid_w, self.game.mid_h+600*self.game.scale_y

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.display.blit(self.game.credits_background, (0, 0))
            self.game.draw_button(self.game.back_button, self.back_x, self.back_y)
            self.back_rect = self.game.button_rect.inflate(-30,-30)

            self.check_input()
            self.game.check_events()
            self.blit_screen()

    def check_input(self):
        pos = pygame.mouse.get_pos()
        if self.back_rect.collidepoint(pos):
            self.game.draw_button(self.game.back_hover, self.back_x, self.back_y)
            if self.game.play_hover_sound == True:
                self.game.button_hover_sound.play()
                self.game.play_hover_sound = False
            click = pygame.mouse.get_pressed()
            if click[0]:
                self.game.draw_button(self.game.back_pressed, self.back_x, self.back_y)
                if self.game.play_press_sound == True:
                    self.game.button_press_sound.play(maxtime=1000)
                    self.game.play_press_sound = False
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP:
                        self.game.play_press_sound = True
                        self.game.curr_menu = self.game.main_menu
                        self.run_display = False
      
        else: 
            self.game.play_hover_sound = True
