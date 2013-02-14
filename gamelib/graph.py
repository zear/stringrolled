import gc ; gc.disable()
import data
import pygame

class graphics_data:
    resolution_x = 320
    resolution_y = 200
    factor_x = int(resolution_x/320)
    factor_y = int(resolution_y/200)
    tile_w = 16*factor_x
    tile_h = 16*factor_y
    scroll_x = 0.0
    scroll_y = 0.0
    tilemap_width = 1
    tilemap_height = 1
    tilemap = [0]
    sprite_x = [0 for i in range(256)]
    sprite_y = [0 for i in range(256)]
    sprite_c = [0 for i in range(256)]
    sprite_s = [0 for i in range(256)]
    sprites = 0
    i = 0
    #SQ - had to make the game skip rendering the tileset every other frame because not achieving 60fps broke the physics
    skipped_last_frame = True 



def init_video():
    graphics = graphics_data()
    pygame.init()
    #graphics.screen = pygame.display.set_mode((graphics.resolution_x,graphics.resolution_y), pygame.FULLSCREEN|pygame.HWSURFACE|pygame.DOUBLEBUF, 32)
    #graphics.screen = pygame.display.set_mode((graphics.resolution_x,graphics.resolution_y), pygame.HWSURFACE|pygame.DOUBLEBUF, 32)
    graphics.screen = pygame.display.set_mode((graphics.resolution_x,graphics.resolution_y), pygame.SWSURFACE, 32)
    graphics.tileset = pygame.Surface((256*graphics.factor_x, 256*graphics.factor_y), pygame.SWSURFACE, 32)
    graphics.tileset.fill((255, 0, 255))
    graphics.spriteset = pygame.Surface((256*graphics.factor_x, 512*graphics.factor_y), pygame.SWSURFACE, 32)
    graphics.spriteset.fill((255, 0, 255))
    graphics.spriteset.set_colorkey((255, 0, 255, 255))
    f = data.load("tileset.png")
    load_tileset(f, graphics)

    
    return graphics

def load_tileset(file, graphics):
    img = pygame.image.load(file)
    buff = pygame.Surface((256*graphics.factor_x, 256*graphics.factor_y), pygame.SWSURFACE, 32)
    img.convert()
    i = 0
    while i < 256*graphics.factor_x:
        buff.blit(img, (i, 0), (i/graphics.factor_x, 0, 1, 256))
        i += 1
    i = 0
    while i < 256*graphics.factor_y:
        graphics.tileset.blit(buff, (0, i), (0, i/graphics.factor_y, 256*graphics.factor_x, 1))
        i += 1
    graphics.tileset.convert()

def load_spriteset(file, graphics):
    img = pygame.image.load(file)
    buff = pygame.Surface((256*graphics.factor_x, 512*graphics.factor_y), pygame.SWSURFACE, 32)
    img.convert()
    i = 0
    while i < 256*graphics.factor_x:
        buff.blit(img, (i, 256), (i/graphics.factor_x, 0, 1, 256))
        buff.blit(img, (i, 0), (15 - ((i/graphics.factor_x)%16) + (i/graphics.factor_x/16)*16, 0, 1, 256))
        i += 1
    i = 0
    while i < 256*graphics.factor_y:
        graphics.spriteset.blit(buff, (0, i), (0, i/graphics.factor_y, 256*graphics.factor_x, 1))
        graphics.spriteset.blit(buff, (0, i+256*graphics.factor_y), (0, i/graphics.factor_y + 256, 256*graphics.factor_x, 1))
        i += 1
    graphics.spriteset.convert()


def draw_sprite(c, x, y, graphics):
    if graphics.sprites < 256:
        graphics.sprite_x[graphics.sprites] = x
        graphics.sprite_y[graphics.sprites] = y
        graphics.sprite_c[graphics.sprites] = c
        graphics.sprite_s[graphics.sprites] = 1
        graphics.sprites += 1

def draw_sprite_multi(c, x, y, w, h, graphics):
    i3 = 0
    i2 = 0
    while i2 < h:
        i = 0
        while i < w:
            if graphics.sprites < 256:
                #SQ - optimizing integer math
#                graphics.sprite_x[graphics.sprites] = x + i*16
#                graphics.sprite_y[graphics.sprites] = y + i2*16
                graphics.sprite_x[graphics.sprites] = x + (i<<4)
                graphics.sprite_y[graphics.sprites] = y + (i2<<4)
                graphics.sprite_c[graphics.sprites] = c + i3
                graphics.sprite_s[graphics.sprites] = 1
                graphics.sprites += 1
            i3 += 1
            i += 1
        i2 += 1
        
def draw_sprite_static(c, x, y, graphics):
    if graphics.sprites < 256:
        graphics.sprite_x[graphics.sprites] = x
        graphics.sprite_y[graphics.sprites] = y
        graphics.sprite_c[graphics.sprites] = c
        graphics.sprite_s[graphics.sprites] = 0
        graphics.sprites += 1

def draw_sprite_static_multi(c, x, y, w, h, graphics):
    i3 = 0
    i2 = 0
    while i2 < h:
        i = 0
        while i < w:
            if graphics.sprites < 256:
                #SQ - optimizing integer math
#                graphics.sprite_x[graphics.sprites] = x + i*16
#                graphics.sprite_y[graphics.sprites] = y + i2*16
                graphics.sprite_x[graphics.sprites] = x + (i<<4)
                graphics.sprite_y[graphics.sprites] = y + (i2<<4)
                graphics.sprite_c[graphics.sprites] = c + i3
                graphics.sprite_s[graphics.sprites] = 0
                graphics.sprites += 1
            i3 += 1
            i += 1
        i2 += 1
        
def free_video():
    pygame.display.quit()


def draw_screen(graphics):
    #SQ - optimized math, logic, and dereferencing extensively:
    #SQ - NOTE: the truth is that in this game, the level width is always 512 and height is 256, NO MATTER WHAT,
    #       even the editor does not allow expanding beyond that, and that allows a lot of optimizations here
    #       and elsewhere
    
    #SQ - disabled frame skipping experiment for now:
#    if graphics.skipped_last_frame:
#        graphics.skipped_last_frame = False
#    else:
#        graphics.skipped_last_frame = True
#        graphics.sprites = 0
#        return

    x = 0
    liscroll_x = int(graphics.scroll_x)
    liscroll_y = int(graphics.scroll_y)
    tile_x = liscroll_x >> 4
    gfxtm=graphics.tilemap
    gfxts=graphics.tileset
    gfxss=graphics.spriteset
    gfxspritex = graphics.sprite_x
    gfxspritey = graphics.sprite_y
    gfxsprites = graphics.sprite_s
    gfxspritec = graphics.sprite_c
    gfxblit=graphics.screen.blit
    liscroll_y_div_16 = liscroll_y >> 4
    liscroll_x_mod_16 = liscroll_x & 0xF
    liscroll_y_mod_16 = liscroll_y & 0xF

    while x < 21:
        y = 0
        tile_y = liscroll_y_div_16
        while y < 14:
            if (0 <= tile_y < 256) and (0 <= tile_x < 512):
                tile = gfxtm[(tile_y << 9)+tile_x]
                gfxblit(gfxts, 
                        ((x<<4)-liscroll_x_mod_16, (y<<4)-liscroll_y_mod_16), 
                        ((tile & 0xF)<<4, tile&0xFFF0, 16, 16))
            y += 1
            tile_y += 1
        x += 1
        tile_x += 1
    i=0
    numsprites = graphics.sprites
    while i < numsprites:
        gfxspritec_val=gfxspritec[i];
        if gfxsprites[i]:
            gfxblit(gfxss, 
                    ((gfxspritex[i] - liscroll_x), (gfxspritey[i] - liscroll_y)),
                    ((gfxspritec_val & 0xF)<<4, gfxspritec_val & 0xFFF0, 16, 16))

        else:
            gfxblit(gfxss, ((gfxspritex[i]), 
                    (gfxspritey[i])),
                    ((gfxspritec_val & 0xF)<<4, gfxspritec_val & 0xFFF0, 16, 16))
        i += 1
    graphics.sprites = 0
    
    pygame.display.flip()
    
