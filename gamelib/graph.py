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



def init_video():
    graphics = graphics_data()
    pygame.init()
    #graphics.screen = pygame.display.set_mode((graphics.resolution_x,graphics.resolution_y), pygame.FULLSCREEN|pygame.HWSURFACE|pygame.DOUBLEBUF, 32)
    graphics.screen = pygame.display.set_mode((graphics.resolution_x,graphics.resolution_y), pygame.HWSURFACE|pygame.DOUBLEBUF, 32)
    graphics.tileset = pygame.Surface((256*graphics.factor_x, 256*graphics.factor_y), pygame.HWSURFACE, 32)
    graphics.tileset.fill((255, 0, 255))
    graphics.spriteset = pygame.Surface((256*graphics.factor_x, 512*graphics.factor_y), pygame.HWSURFACE, 32)
    graphics.spriteset.fill((255, 0, 255))
    graphics.spriteset.set_colorkey((255, 0, 255, 255))
    f = data.load("tileset.png")
    load_tileset(f, graphics)

    
    return graphics

def load_tileset(file, graphics):
    img = pygame.image.load(file)
    buff = pygame.Surface((256*graphics.factor_x, 256*graphics.factor_y), pygame.HWSURFACE, 32)
    img.convert(32, pygame.HWSURFACE)
    i = 0
    while i < 256*graphics.factor_x:
        buff.blit(img, (i, 0), (i/graphics.factor_x, 0, 1, 256))
        i += 1
    i = 0
    while i < 256*graphics.factor_y:
        graphics.tileset.blit(buff, (0, i), (0, i/graphics.factor_y, 256*graphics.factor_x, 1))
        i += 1

def load_spriteset(file, graphics):
    img = pygame.image.load(file)
    buff = pygame.Surface((256*graphics.factor_x, 512*graphics.factor_y), pygame.HWSURFACE, 32)
    img.convert(32, pygame.HWSURFACE)
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
    #SQ - optimized math and dereferencing extensively:
    x = 0

    lscroll_x = graphics.scroll_x
    lscroll_y = graphics.scroll_y
    liscroll_x = int(lscroll_x)
    liscroll_y = int(lscroll_y)
    tile_x = liscroll_x >> 4
    ltilemap_width = graphics.tilemap_width
    ltilemap_height = graphics.tilemap_height
    ltile_w = graphics.tile_w
    ltile_h = graphics.tile_h

    lscroll_x_mod_16 = lscroll_x%16
    lscroll_y_mod_16 = lscroll_y%16

    gfxtm=graphics.tilemap
    gfxts=graphics.tileset
    gfxss=graphics.spriteset
    gfxspritex = graphics.sprite_x
    gfxspritey = graphics.sprite_y
    gfxsprites = graphics.sprite_s
    gfxspritec = graphics.sprite_c
    gfxblit=graphics.screen.blit

    while x < 21:
        y = 0
        tile_y = liscroll_y >> 4

        while y < 14:
            if tile_x < ltilemap_width \
              and tile_y < ltilemap_height \
              and tile_x >= 0 \
              and tile_y >= 0:
                tile = gfxtm[tile_y * ltilemap_width + tile_x]
                gfxblit(gfxts, \
                        (x*ltile_w-lscroll_x_mod_16, y*ltile_h-lscroll_y_mod_16), 
                        ((tile%16)*ltile_w, (tile>>4)*ltile_h, ltile_w, ltile_h))
            y += 1
            tile_y += 1
        x += 1
        tile_x += 1
    i=0
    while i < graphics.sprites:
        gfxblit(gfxss, ((gfxspritex[i] - lscroll_x*gfxsprites[i]), \
            (gfxspritey[i] - lscroll_y*gfxsprites[i])), \
            ((gfxspritec[i]%16)*ltile_w, (gfxspritec[i]>>4)*ltile_h, ltile_w, ltile_h))
        i += 1
    graphics.sprites = 0
    
    pygame.display.flip()
    
