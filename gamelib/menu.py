import gc ; gc.disable()
import data
import graph
import pygame
import game

def main_menu(mygame, level, graphics):
    f = data.load("menu.png")
    graph.load_spriteset(f, graphics)
    
    i=0
    menu_quit = 2
    ticks = pygame.time.get_ticks()
    t = 0
    menu_selection = 0
    key_pressed = 1
    next = "play"
    while menu_quit != 1:
        pygame.event.pump()
        keys = pygame.key.get_pressed()
        if(keys[pygame.K_ESCAPE] == 1 and key_pressed == 0):
            menu_quit = 1
            next = "play"
        if((keys[pygame.K_LEFT] or keys[pygame.K_UP]) and key_pressed == 0):
            menu_selection = (menu_selection+2)%3
            key_pressed = 1
            mygame.sound_11.play()
        if((keys[pygame.K_RIGHT] or keys[pygame.K_DOWN]) and key_pressed == 0):
            menu_selection = (menu_selection+1)%3
            key_pressed = 1
            mygame.sound_11.play()
        if( keys[pygame.K_LEFT] == 0 and keys[pygame.K_RIGHT] == 0 and keys[pygame.K_UP] == 0 and keys[pygame.K_DOWN] == 0 and keys[pygame.K_ESCAPE] == 0 and keys[pygame.K_RETURN] == 0 and keys[pygame.K_1] == 0 and keys[pygame.K_2] == 0 and keys[pygame.K_3] == 0 and keys[pygame.K_LCTRL] == 0):
            key_pressed = 0
        if((keys[pygame.K_RETURN] == 1 or keys[pygame.K_LCTRL] == 1 ) and key_pressed == 0):
            menu_quit = 1
            if menu_selection == 0:
                next = "play"
                mygame.sound_12.play()
            if menu_selection == 1:
                next = "edit"
            if menu_selection == 2:
                next = "quit"
        graph.draw_sprite_static_multi(256+0 + 5*(menu_selection==0), 120, 60, 5, 1, graphics)
        graph.draw_sprite_static_multi(256+16 + 5*(menu_selection==1), 120, 60+32, 5, 1, graphics)
        graph.draw_sprite_static_multi(256+32 + 5*(menu_selection==2), 120, 60+64, 5, 1, graphics)
        graph.draw_screen(graphics)
        pygame.time.wait(1)
        t = pygame.time.get_ticks() - ticks
        ticks = pygame.time.get_ticks()
        i += 1
        
    if next == "play" and mygame.ingame == 0:
        i = 0
        menu_quit = 2
        ticks = pygame.time.get_ticks()
        t = 0
        menu_selection = 0
        key_pressed = 1
        next = "menu"
        while menu_quit != 1:
            pygame.event.pump()
            keys = pygame.key.get_pressed()
            if(keys[pygame.K_ESCAPE] == 1 and key_pressed == 0):
                menu_quit = 1
                next = "menu"
            if((keys[pygame.K_LEFT] or keys[pygame.K_UP]) and key_pressed == 0):
                menu_selection = (menu_selection+1)%2
                key_pressed = 1
                mygame.sound_11.play()
            if((keys[pygame.K_RIGHT] or keys[pygame.K_DOWN]) and key_pressed == 0):
                menu_selection = (menu_selection+1)%2
                key_pressed = 1
                mygame.sound_11.play()
            if( keys[pygame.K_LEFT] == 0 and keys[pygame.K_RIGHT] == 0 and keys[pygame.K_UP] == 0 and keys[pygame.K_DOWN] == 0 and keys[pygame.K_ESCAPE] == 0 and keys[pygame.K_RETURN] == 0 and keys[pygame.K_1] == 0 and keys[pygame.K_2] == 0 and keys[pygame.K_3] == 0 and keys[pygame.K_LCTRL] == 0):
                key_pressed = 0
            if((keys[pygame.K_RETURN] == 1 or keys[pygame.K_LCTRL] == 1 ) and key_pressed == 0):
                menu_quit = 1
                if menu_selection == 0:
                    next = "play"
                    mygame.ingame = 1
                    # SQ - this game crashed if this option was selected with no existing save data..
                    #    So, I made continue_game return immediately if it checked and found no data
                    #    and if we get to the next line that is indeed the case. Instead of crashing,
                    #    we'll now just start a new game by copying the three lines for menu selection
                    #    1 below and pasting them here:
                    #game.continue_game(mygame, level)
                    if not game.continue_game(mygame, level):
                        next = "intro"
                        mygame.ingame = 1
                        game.new_game(mygame, level)
                if menu_selection == 1:
                    next = "intro"
                    mygame.ingame = 1
                    game.new_game(mygame, level)
            graph.draw_sprite_static_multi(256+48 + 3*(menu_selection==0), 136, 60+16, 3, 1, graphics)
            graph.draw_sprite_static_multi(256+64 + 3*(menu_selection==1), 136, 60+48, 3, 1, graphics)
            graph.draw_screen(graphics)
            pygame.time.wait(1)
            t = pygame.time.get_ticks() - ticks
            ticks = pygame.time.get_ticks()
            i += 1
    return next
    
    
    
    
def load_img(file, graphics):
    img = pygame.image.load(file)
    buff = pygame.Surface((320*graphics.factor_x, 200*graphics.factor_y), pygame.SWSURFACE, 32)
    buff2 = pygame.Surface((320*graphics.factor_x, 200*graphics.factor_y), pygame.SWSURFACE, 32)
    img.convert()
    i = 0
    while i < 320*graphics.factor_x:
        buff.blit(img, (i, 0), (i/graphics.factor_x, 0, 1, 200))
        i += 1
    i = 0
    while i < 200*graphics.factor_y:
        buff2.blit(buff, (0, i), (0, i/graphics.factor_y, 320*graphics.factor_x, 1))
        i += 1
    return buff2

def title_screen(graphics):
    f = data.load("img0.png")
    img = load_img(f, graphics)
    
    i=0
    menu_quit = 2
    ticks = pygame.time.get_ticks()
    t = 0
    menu_selection = 0
    key_pressed = 1
    next = "menu"
    while menu_quit != 1:
        pygame.event.pump()
        keys = pygame.key.get_pressed()
        if(keys[pygame.K_ESCAPE] == 1 and key_pressed == 0):
            menu_quit = 1
            next = "menu"
        if( keys[pygame.K_LEFT] == 0 and keys[pygame.K_RIGHT] == 0 and keys[pygame.K_UP] == 0 and keys[pygame.K_DOWN] == 0 and keys[pygame.K_ESCAPE] == 0 and keys[pygame.K_RETURN] == 0 and keys[pygame.K_1] == 0 and keys[pygame.K_2] == 0 and keys[pygame.K_3] == 0 and keys[pygame.K_LCTRL] == 0):
            key_pressed = 0
        if((keys[pygame.K_RETURN] == 1 or keys[pygame.K_LCTRL] == 1) and key_pressed == 0):
            menu_quit = 1
            next = "menu"
            
        graphics.screen.blit(img, (0,0))
        
        pygame.display.flip()
        pygame.time.wait(1)
        
        t = pygame.time.get_ticks() - ticks
        ticks = pygame.time.get_ticks()
        i += 1
    return next
    
    
def intro(graphics):
    f = data.load("img1.png")
    img = load_img(f, graphics)
    
    i=0
    menu_quit = 2
    ticks = pygame.time.get_ticks()
    t = 0
    key_pressed = 1
    next = "play"
    while menu_quit != 1:
        pygame.event.pump()
        keys = pygame.key.get_pressed()
        if(keys[pygame.K_ESCAPE] == 1 and key_pressed == 0):
            menu_quit = 1
        if( keys[pygame.K_LEFT] == 0 and keys[pygame.K_RIGHT] == 0 and keys[pygame.K_UP] == 0 and keys[pygame.K_DOWN] == 0 and keys[pygame.K_ESCAPE] == 0 and keys[pygame.K_RETURN] == 0 and keys[pygame.K_1] == 0 and keys[pygame.K_2] == 0 and keys[pygame.K_3] == 0 and keys[pygame.K_LCTRL] == 0):
            key_pressed = 0
        if((keys[pygame.K_RETURN] == 1 or keys[pygame.K_RIGHT] == 1 or keys[pygame.K_LCTRL] == 1)  and key_pressed == 0):
            menu_quit = 1
            
        graphics.screen.blit(img, (0,0))
        
        pygame.display.flip()
        pygame.time.wait(1)
        
        t = pygame.time.get_ticks() - ticks
        ticks = pygame.time.get_ticks()
        i += 1
        
    menu_quit = 2 
    f = data.load("img2.png")
    img = load_img(f, graphics)
    key_pressed = 1
    while menu_quit != 1:
        pygame.event.pump()
        keys = pygame.key.get_pressed()
        if(keys[pygame.K_ESCAPE] == 1 and key_pressed == 0):
            menu_quit = 1
        if( keys[pygame.K_LEFT] == 0 and keys[pygame.K_RIGHT] == 0 and keys[pygame.K_UP] == 0 and keys[pygame.K_DOWN] == 0 and keys[pygame.K_ESCAPE] == 0 and keys[pygame.K_RETURN] == 0 and keys[pygame.K_1] == 0 and keys[pygame.K_2] == 0 and keys[pygame.K_3] == 0 and keys[pygame.K_LCTRL] == 0):
            key_pressed = 0
        if((keys[pygame.K_RETURN] == 1 or keys[pygame.K_RIGHT] == 1 or keys[pygame.K_LCTRL] == 1) and key_pressed == 0):
            menu_quit = 1
            
        graphics.screen.blit(img, (0,0))
        
        pygame.display.flip()
        pygame.time.wait(1)
        
        t = pygame.time.get_ticks() - ticks
        ticks = pygame.time.get_ticks()
        i += 1
        
    menu_quit = 2 
    f = data.load("img3.png")
    img = load_img(f, graphics)
    key_pressed = 1
    while menu_quit != 1:
        pygame.event.pump()
        keys = pygame.key.get_pressed()
        if(keys[pygame.K_ESCAPE] == 1 and key_pressed == 0):
            menu_quit = 1
        if( keys[pygame.K_LEFT] == 0 and keys[pygame.K_RIGHT] == 0 and keys[pygame.K_UP] == 0 and keys[pygame.K_DOWN] == 0 and keys[pygame.K_ESCAPE] == 0 and keys[pygame.K_RETURN] == 0 and keys[pygame.K_1] == 0 and keys[pygame.K_2] == 0 and keys[pygame.K_3] == 0 and keys[pygame.K_LCTRL] == 0):
            key_pressed = 0
        if((keys[pygame.K_RETURN] == 1 or keys[pygame.K_RIGHT] == 1 or keys[pygame.K_LCTRL] == 1) and key_pressed == 0):
            menu_quit = 1
            
        graphics.screen.blit(img, (0,0))
        
        pygame.display.flip()
        pygame.time.wait(1)
        
        t = pygame.time.get_ticks() - ticks
        ticks = pygame.time.get_ticks()
        i += 1
        
    menu_quit = 2 
    f = data.load("img4.png")
    img = load_img(f, graphics)
    key_pressed = 1
    while menu_quit != 1:
        pygame.event.pump()
        keys = pygame.key.get_pressed()
        if(keys[pygame.K_ESCAPE] == 1 and key_pressed == 0):
            menu_quit = 1
        if( keys[pygame.K_LEFT] == 0 and keys[pygame.K_RIGHT] == 0 and keys[pygame.K_UP] == 0 and keys[pygame.K_DOWN] == 0 and keys[pygame.K_ESCAPE] == 0 and keys[pygame.K_RETURN] == 0 and keys[pygame.K_1] == 0 and keys[pygame.K_2] == 0 and keys[pygame.K_3] == 0 and keys[pygame.K_LCTRL] == 0):
            key_pressed = 0
        if((keys[pygame.K_RETURN] == 1 or keys[pygame.K_RIGHT] == 1 or keys[pygame.K_LCTRL] == 1) and key_pressed == 0):
            menu_quit = 1
            
        graphics.screen.blit(img, (0,0))
        
        pygame.display.flip()
        pygame.time.wait(1)
        
        t = pygame.time.get_ticks() - ticks
        ticks = pygame.time.get_ticks()
        i += 1
        
    menu_quit = 2 
    f = data.load("img5.png")
    img = load_img(f, graphics)
    key_pressed = 1
    while menu_quit != 1:
        pygame.event.pump()
        keys = pygame.key.get_pressed()
        if(keys[pygame.K_ESCAPE] == 1 and key_pressed == 0):
            menu_quit = 1
        if( keys[pygame.K_LEFT] == 0 and keys[pygame.K_RIGHT] == 0 and keys[pygame.K_UP] == 0 and keys[pygame.K_DOWN] == 0 and keys[pygame.K_ESCAPE] == 0 and keys[pygame.K_RETURN] == 0 and keys[pygame.K_1] == 0 and keys[pygame.K_2] == 0 and keys[pygame.K_3] == 0 and keys[pygame.K_LCTRL] == 0):
            key_pressed = 0
        if((keys[pygame.K_RETURN] == 1 or keys[pygame.K_RIGHT] == 1 or keys[pygame.K_LCTRL] == 1) and key_pressed == 0):
            menu_quit = 1
            
        graphics.screen.blit(img, (0,0))
        
        pygame.display.flip()
        pygame.time.wait(1)
        
        t = pygame.time.get_ticks() - ticks
        ticks = pygame.time.get_ticks()
        i += 1
        
    menu_quit = 2 
    f = data.load("img6.png")
    img = load_img(f, graphics)
    key_pressed = 1
    while menu_quit != 1:
        pygame.event.pump()
        keys = pygame.key.get_pressed()
        if(keys[pygame.K_ESCAPE] == 1 and key_pressed == 0):
            menu_quit = 1
        if( keys[pygame.K_LEFT] == 0 and keys[pygame.K_RIGHT] == 0 and keys[pygame.K_UP] == 0 and keys[pygame.K_DOWN] == 0 and keys[pygame.K_ESCAPE] == 0 and keys[pygame.K_RETURN] == 0 and keys[pygame.K_1] == 0 and keys[pygame.K_2] == 0 and keys[pygame.K_3] == 0 and keys[pygame.K_LCTRL] == 0):
            key_pressed = 0
        if((keys[pygame.K_RETURN] == 1 or keys[pygame.K_RIGHT] == 1 or keys[pygame.K_LCTRL] == 1) and key_pressed == 0):
            menu_quit = 1
            
        graphics.screen.blit(img, (0,0))
        
        pygame.display.flip()
        pygame.time.wait(1)
        
        t = pygame.time.get_ticks() - ticks
        ticks = pygame.time.get_ticks()
        i += 1
        
    return next
    
    
def win(graphics):
    f = data.load("img7.png")
    img = load_img(f, graphics)
    
    i=0
    menu_quit = 2
    ticks = pygame.time.get_ticks()
    t = 0
    key_pressed = 1
    next = "quit"
    while menu_quit != 1:
        pygame.event.pump()
        keys = pygame.key.get_pressed()
        if(keys[pygame.K_ESCAPE] == 1 and key_pressed == 0):
            menu_quit = 1
        if( keys[pygame.K_LEFT] == 0 and keys[pygame.K_RIGHT] == 0 and keys[pygame.K_UP] == 0 and keys[pygame.K_DOWN] == 0 and keys[pygame.K_ESCAPE] == 0 and keys[pygame.K_RETURN] == 0 and keys[pygame.K_1] == 0 and keys[pygame.K_2] == 0 and keys[pygame.K_3] == 0 and keys[pygame.K_LCTRL] == 0):
            key_pressed = 0
        if((keys[pygame.K_RETURN] == 1 or keys[pygame.K_RIGHT] == 1 or keys[pygame.K_LCTRL] == 1)  and key_pressed == 0):
            menu_quit = 1
            
        graphics.screen.blit(img, (0,0))
        
        pygame.display.flip()
        pygame.time.wait(1)
        
        t = pygame.time.get_ticks() - ticks
        ticks = pygame.time.get_ticks()
        i += 1
    return next
