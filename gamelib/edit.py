import data
import graph
import pygame
import cPickle

class editor_data:
    zero = 0

def init_editor():
    editor = editor_data()
    return editor
    
def load_tileset(filename, graphics):
    factor_x = int(graphics.resolution_x/640)
    factor_y = int(graphics.resolution_y/400)
    tile_w = 16*factor_x
    tile_h = 16*factor_y
    img = pygame.image.load(filename)
    buff = pygame.Surface((256*factor_x, 256*factor_y), pygame.HWSURFACE, 32)
    img.convert(32, pygame.HWSURFACE)
    i = 0
    while i < 256*factor_x:
        buff.blit(img, (i, 0), (i/factor_x, 0, 1, 256))
        i += 1
    i = 0
    while i < 256*factor_y:
        graphics.tileset.blit(buff, (0, i), (0, i/factor_y, 256*factor_x, 1))
        i += 1

def load_spriteset(filename, graphics):
    factor_x = int(graphics.resolution_x/640)
    factor_y = int(graphics.resolution_y/400)
    tile_w = 16*factor_x
    tile_h = 16*factor_y
    img = pygame.image.load(filename)
    buff = pygame.Surface((256*factor_x, 256*factor_y), pygame.HWSURFACE, 32)
    img.convert(32, pygame.HWSURFACE)
    i = 0
    while i < 256*factor_x:
        buff.blit(img, (i, 0), (i/factor_x, 0, 1, 256))
        i += 1
    i = 0
    while i < 256*factor_y:
        graphics.spriteset.blit(buff, (0, i), (0, i/factor_y, 256*factor_x, 1))
        i += 1
    
def draw_screen(editor, level, graphics):
    factor_x = int(graphics.resolution_x/640)
    factor_y = int(graphics.resolution_y/400)
    tile_w = 16*factor_x
    tile_h = 16*factor_y
    graphics.screen.fill((32, 0, 64))
    x = 0
    tile_x = int(graphics.scroll_x/16)
    while x < 24:
        y = 0
        tile_y = int(graphics.scroll_y/16)
        while y < 24:
            if tile_x < graphics.tilemap_width \
              and tile_y < graphics.tilemap_height \
              and tile_x >= 0 \
              and tile_y >= 0:
                tile = graphics.tilemap[tile_y * graphics.tilemap_width + tile_x]
                graphics.screen.blit(graphics.tileset, (x*tile_w, y*tile_h), ((tile%16)*tile_w, (tile/16)*tile_h, tile_w, tile_h))
            else:
                tile = 1
                graphics.screen.blit(graphics.tileset, (x*tile_w, y*tile_h), ((tile%16)*tile_w, (tile/16)*tile_h, tile_w, tile_h))
            y += 1
            tile_y += 1
        x += 1
        tile_x += 1
        
    if editor.mode == 1:
        x = 0
        tile_x = int(graphics.scroll_x/16)
        while x < 24:
            y = 0
            tile_y = int(graphics.scroll_y/16)
            while y < 24:
                if tile_x < graphics.tilemap_width \
                  and tile_y < graphics.tilemap_height \
                  and tile_x >= 0 \
                  and tile_y >= 0:
                    tile = level.object_[tile_y * graphics.tilemap_width + tile_x]
                    if tile != 0:
                        graphics.screen.blit(graphics.spriteset, (x*tile_w, y*tile_h), ((tile%16)*tile_w, (tile/16)*tile_h, tile_w, tile_h))
                y += 1
                tile_y += 1
            x += 1
            tile_x += 1
            
    if editor.mode == 2:
        x = 0
        tile_x = int(graphics.scroll_x/16)
        while x < 24:
            y = 0
            tile_y = int(graphics.scroll_y/16)
            while y < 24:
                if tile_x < graphics.tilemap_width \
                  and tile_y < graphics.tilemap_height \
                  and tile_x >= 0 \
                  and tile_y >= 0:
                    tile = level.direction[tile_y * graphics.tilemap_width + tile_x]
                    if tile != 0:
                        graphics.screen.blit(graphics.spriteset, (x*tile_w, y*tile_h), ((tile%16)*tile_w, (tile/16)*tile_h, tile_w, tile_h))
                y += 1
                tile_y += 1
            x += 1
            tile_x += 1
    
    graphics.screen.fill((32, 0, 64), (384*factor_x, 256*factor_x, tile_w, tile_h))
    
    if editor.mode == 0:
        graphics.screen.blit(graphics.tileset, (384*factor_x, 0), (0, 0, 256*factor_x, 256*factor_y))
        tile = editor.tile
        graphics.screen.blit(graphics.tileset, (384*factor_x, 256*factor_y), ((tile%16)*tile_w, (tile/16)*tile_h, tile_w, tile_h))
        
    if editor.mode != 0:
        graphics.screen.blit(graphics.spriteset, (384*factor_x, 0), (0, 0, 256*factor_x, 256*factor_y))
        tile = editor.object_
        graphics.screen.blit(graphics.spriteset, (384*factor_x, 256*factor_y), ((tile%16)*tile_w, (tile/16)*tile_h, tile_w, tile_h))
    
    i=0
    while i < graphics.sprites:
        graphics.screen.blit(graphics.spriteset, ((graphics.sprite_x[i] - int(graphics.scroll_x/16)*16*graphics.sprite_s[i])*factor_x, (graphics.sprite_y[i] - int(graphics.scroll_y/16)*16*graphics.sprite_s[i])*factor_y), ((graphics.sprite_c[i]%16)*tile_w, (graphics.sprite_c[i]/16)*tile_h, tile_w, tile_h))
        i += 1
    graphics.sprites = 0
    
    pygame.display.flip()


def edit(level, graphics):
    factor_x = int(graphics.resolution_x/640)
    factor_y = int(graphics.resolution_y/400)
    tile_w = 16*factor_x
    tile_h = 16*factor_y
    editor = init_editor()
    #graphics.tilemap_width = 1024
    #graphics.tilemap_height = 1024
    #graphics.tilemap = [0 for i in range(graphics.tilemap_width*graphics.tilemap_height)]
    f = data.load("tileset.png")
    load_tileset(f, graphics)
    f = data.load("editor.png")
    load_spriteset(f, graphics)
    
    i=0
    menu_quit = 0
    ticks = pygame.time.get_ticks()
    t = 0
    editor.tile = 1
    editor.mode = 0
    editor.object_ = 0
    while menu_quit == 0:
        pygame.event.pump()
        keys = pygame.key.get_pressed()
        if(keys[pygame.K_ESCAPE] == 1):
            menu_quit = 1
        if(keys[pygame.K_LEFT] == 1):
            graphics.scroll_x -= 0.25*t
        if(keys[pygame.K_RIGHT] == 1):
            graphics.scroll_x += 0.25*t
        if(keys[pygame.K_UP] == 1):
            graphics.scroll_y -= 0.25*t
        if(keys[pygame.K_DOWN] == 1):
            graphics.scroll_y += 0.25*t
        if(keys[pygame.K_TAB] == 1 and tab == 0):
            editor.mode = (editor.mode + 1)%3
            if editor.mode == 2:
                f = data.load("arrows.png")
                load_spriteset(f, graphics)
            if editor.mode == 0:
                f = data.load("editor.png")
                load_spriteset(f, graphics)
                
        tab = keys[pygame.K_TAB]
        
        t = pygame.mouse.get_pos()
        mouse = (float(t[0])/float(factor_x), float(t[1])/float(factor_y))
        graph.draw_sprite_static(0, int(mouse[0]/16)*16, int(mouse[1]/16)*16, graphics)
        graph.draw_sprite_static(1, mouse[0], mouse[1], graphics)
        
        if keys[pygame.K_s]:
            level.start_x = int(mouse[0]/16)*16 + int(graphics.scroll_x/16)*16
            level.start_y = int(mouse[1]/16)*16 + int(graphics.scroll_y/16)*16
        
        if editor.mode == 0:
            mouseb = pygame.mouse.get_pressed()
            if mouseb[2]:
                if mouse[0] >= 384 and mouse[0] < 640 and mouse[1] >= 0 and mouse[1] < 256:
                    editor.tile = (int(mouse[0])-384)/16 + int(mouse[1]/16)*16
                if mouse[0] >= 0 and mouse[0] < 384:
                    tile = int(int(mouse[0]/16) + int(graphics.scroll_x/16) + (int(mouse[1]/16) + int(graphics.scroll_y/16))*graphics.tilemap_width)
                    if tile >= 0 and tile < graphics.tilemap_width*graphics.tilemap_height:
                        editor.tile = graphics.tilemap[tile]
                        
            if mouseb[0]:
                if mouse[0] >= 0 and mouse[0] < 384:
                    tile = int(int(mouse[0]/16) + int(graphics.scroll_x/16) + (int(mouse[1]/16) + int(graphics.scroll_y/16))*graphics.tilemap_width)
                    if tile >= 0 and tile < graphics.tilemap_width*graphics.tilemap_height:
                        graphics.tilemap[tile] = editor.tile
        
        if editor.mode == 1:
            mouseb = pygame.mouse.get_pressed()
            if mouseb[2]:
                if mouse[0] >= 384 and mouse[0] < 640 and mouse[1] >= 0 and mouse[1] < 256:
                    editor.object_ = (int(mouse[0])-384)/16 + int(mouse[1]/16)*16
                if mouse[0] >= 0 and mouse[0] < 384:
                    tile = int(int(mouse[0]/16) + int(graphics.scroll_x/16) + (int(mouse[1]/16) + int(graphics.scroll_y/16))*graphics.tilemap_width)
                    if tile >= 0 and tile < graphics.tilemap_width*graphics.tilemap_height:
                        editor.object_ = level.object_[tile]
                        
            if mouseb[0]:
                if mouse[0] >= 0 and mouse[0] < 384:
                    tile = int(int(mouse[0]/16) + int(graphics.scroll_x/16) + (int(mouse[1]/16) + int(graphics.scroll_y/16))*graphics.tilemap_width)
                    if tile >= 0 and tile < graphics.tilemap_width*graphics.tilemap_height:
                        level.object_[tile] = editor.object_

        if editor.mode == 2:
            mouseb = pygame.mouse.get_pressed()
            if mouseb[2]:
                if mouse[0] >= 384 and mouse[0] < 640 and mouse[1] >= 0 and mouse[1] < 256:
                    editor.object_ = (int(mouse[0])-384)/16 + int(mouse[1]/16)*16
                if mouse[0] >= 0 and mouse[0] < 384:
                    tile = int(int(mouse[0]/16) + int(graphics.scroll_x/16) + (int(mouse[1]/16) + int(graphics.scroll_y/16))*graphics.tilemap_width)
                    if tile >= 0 and tile < graphics.tilemap_width*graphics.tilemap_height:
                        editor.object_ = level.direction[tile]
                        
            if mouseb[0]:
                if mouse[0] >= 0 and mouse[0] < 384:
                    tile = int(int(mouse[0]/16) + int(graphics.scroll_x/16) + (int(mouse[1]/16) + int(graphics.scroll_y/16))*graphics.tilemap_width)
                    if tile >= 0 and tile < graphics.tilemap_width*graphics.tilemap_height:
                        level.direction[tile] = editor.object_
                        
        draw_screen(editor, level, graphics)
        pygame.time.wait(1)
        t = pygame.time.get_ticks() - ticks
        ticks = pygame.time.get_ticks()
        i += 1
    graphics.screen.fill((32, 0, 64))
    pygame.display.flip()
    f = data.load('level.map', 'wb')
    cPickle.dump(level, f)
    f = data.load("tileset.png")
    graph.load_tileset(f, graphics)
    f.close()
