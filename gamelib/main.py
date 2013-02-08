'''Game main module.

Contains the entry point used by the run_game.py script.

Feel free to put all your game code here, or in other modules in this "gamelib"
package.
'''

import data
import pygame
import graph
import menu
import edit
import game

def main():
    graphics = graph.init_video()
    graphics.screen.fill((32, 0, 64))
    pygame.display.flip()
    level = game.load_level()
    mygame = game.init_game(level)
    graphics.tilemap = level.tilemap
    graphics.tilemap_height = level.height
    graphics.tilemap_width = level.width
    next = "title"
    mygame.ingame = 0
    while next != "quit":
        if next == "menu":
            next = menu.main_menu(mygame, level, graphics)
        if next == "edit":
            next = "menu"
            edit.edit(level, graphics)
        if next == "play":
            next = game.game(mygame, level, graphics)
        if next == "title":
            mygame.sound_12.play()
            next = menu.title_screen(graphics)
        if next == "intro":
            mygame.sound_12.play()
            next = menu.intro(graphics)
        if next == "win":
            mygame.sound_0.play()
            next = menu.win(graphics)
            
    graph.free_video()
