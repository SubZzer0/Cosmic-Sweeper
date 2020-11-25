
import pygame
import threading

from game import Game

g = Game()

thread1 = threading.Thread(target = g.intro)
thread1.start()
while g.show_intro == 1:
    g.check_events()

thread1.join()

while g.running:
    g.curr_menu.display_menu()
    g.mine_gen()
    g.game_loop()
