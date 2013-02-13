import data
import cPickle
import graph
import pygame
import random
import math
import os

class level_data:
    width = 1
    height = 1
    tilemap = [0]
    object_ = [0]
    direction = [0]
    start_x = 0
    start_y = 0
    spawn_distance_x = 16
    spawn_distance_y = 12
    
class object__data:
    x = 0.0
    y = 0.0
    speed_x = 0.0
    speed_y = 0.0
    max_speed_x = 0.0
    max_speed_y = 0.0
    jump_speed = 0.0
    acceleration_x = 0.0
    acceleration_y = 0.0
    max_acceleration_x = 0.0
    max_acceleration_y = 0.0
    width = 16.0
    height = 16.0
    direction = 0
    airborne = 0
    animation = 0
    type = 0
    id = 0
    dead = 0

class game_data:
    cat = object__data()
    princess = object__data()
    ball = object__data()
    object_ = []
    object_s = 0
    object__on = []
    character = 0
    fill_all = 1
    switch = []
    
class save_data:
    cat_x = 0.0
    cat_y = 0.0
    princess_x = 0.0
    princess_y = 0.0
    ball_x = 0.0
    ball_y = 0.0
    character = 0
    
class gamepad_data:
    left = 0
    right = 0
    up = 0
    down = 0
    jump = 0
    toggle = 0
    throw = 0
    
def load_level():
    #level = level_data()
    #level.width = 512
    #level.height = 256
    #level.tilemap = [0 for i in range(level.width*level.height)]
    #level.object_ = [0 for i in range(level.width*level.height)]
    f = data.load("level.map")
    level = cPickle.load(f)
    f.close()
    level.spawn_distance_x = 16
    level.spawn_distance_y = 12
    #level.direction = [0 for i in range(level.width*level.height)]
    return level
    
def init_game(level):
    mygame = game_data()
    mygame.width = level.width
    mygame.cat.x = level.start_x - 64
    mygame.cat.y = level.start_y + 32
    mygame.cat.max_speed_x = 0.18
    mygame.cat.max_speed_y = 0.35
    mygame.cat.max_acceleration_x = 0.0008
    mygame.cat.max_acceleration_y = 0.001
    mygame.cat.jump_speed = 0.365
    mygame.cat.platform = 0
    mygame.cat.direction = 1
    mygame.cat_dead = 0
    
    mygame.princess.x = level.start_x + 96
    mygame.princess.y = level.start_y - 32
    mygame.princess.max_speed_x = 0.14
    mygame.princess.max_speed_y = 0.2
    mygame.princess.max_acceleration_x = 0.0008
    mygame.princess.max_acceleration_y = 0.0005
    mygame.princess.jump_speed = 0.23
    mygame.princess.height = 32.0
    mygame.princess.platform = 0
    mygame.princess_dead = 0

    mygame.ball.x = level.start_x - 40
    mygame.ball.y = level.start_y + 32
    mygame.ball.max_speed_x = 0.2
    mygame.ball.max_speed_y = 0.2
    mygame.ball.max_acceleration_x = 0.001
    mygame.ball.max_acceleration_y = 0.0005
    mygame.ball.jump_speed = 0.23
    mygame.ball.height = 16
    mygame.ball.platform = 0
    mygame.ball_dead = 0
    
    mygame.character = 0
    mygame.fill_all = 1
    mygame.object_s = 0
    mygame.object_ = [0 for i in range(512)]
    mygame.object__on = [0 for i in range(512)]
    mygame.switch = [i%2 for i in range(10)]
    mygame.time = 0
    mygame.dead = 0
    mygame.sparkle = 0
    mygame.carrying_ball = 0
    mygame.ball_is_deadly = 0
    
    
    pygame.mixer.init()
    f = data.load("Sfx000.ogg")
    mygame.sound_0 = pygame.mixer.Sound(f)
    f = data.load("Sfx001.ogg")
    mygame.sound_1 = pygame.mixer.Sound(f)
    f = data.load("Sfx002.ogg")
    mygame.sound_2 = pygame.mixer.Sound(f)
    f = data.load("Sfx003.ogg")
    mygame.sound_3 = pygame.mixer.Sound(f)
    f = data.load("Sfx004.ogg")
    mygame.sound_4 = pygame.mixer.Sound(f)
    f = data.load("Sfx005.ogg")
    mygame.sound_5 = pygame.mixer.Sound(f)
    f = data.load("Sfx006.ogg")
    mygame.sound_6 = pygame.mixer.Sound(f)
    f = data.load("Sfx007.ogg")
    mygame.sound_7 = pygame.mixer.Sound(f)
    f = data.load("Sfx008.ogg")
    mygame.sound_8 = pygame.mixer.Sound(f)
    f = data.load("son1.ogg")
    mygame.sound_11 = pygame.mixer.Sound(f)
    f = data.load("son2.ogg")
    mygame.sound_12 = pygame.mixer.Sound(f)
    f = data.load("son3.ogg")
    mygame.sound_13 = pygame.mixer.Sound(f)
    f = data.load("son4.ogg")
    mygame.sound_14 = pygame.mixer.Sound(f)
    f = data.load("son5.ogg")
    mygame.sound_15 = pygame.mixer.Sound(f)
    f = data.load("son6.ogg")
    mygame.sound_16 = pygame.mixer.Sound(f)
    f = data.load("son7.ogg")
    mygame.sound_17 = pygame.mixer.Sound(f)
    f = data.load("son8.ogg")
    mygame.sound_18 = pygame.mixer.Sound(f)
    mygame.sound_18.set_volume(0.2)
    f = data.load("son9.ogg")
    mygame.sound_19 = pygame.mixer.Sound(f)
    f = data.load("son10.ogg")
    mygame.sound_20 = pygame.mixer.Sound(f)
    f = data.load("son11.ogg")
    mygame.sound_21 = pygame.mixer.Sound(f)
    f = data.load("son12.ogg")
    mygame.sound_22 = pygame.mixer.Sound(f)
    return mygame
    
def continue_game(mygame, level):
    homepath = os.environ["HOME"] + '/.stringrolled/'
    if not os.path.exists(homepath): os.makedirs(homepath)
    f = data.load(homepath + 'game.sav')
    save = cPickle.load(f)
    f.close()
    mygame.cat.x = save.cat_x
    mygame.cat.y = save.cat_y
    mygame.ball.x = save.ball_x
    mygame.ball.y = save.ball_y
    mygame.princess.x = save.princess_x
    mygame.princess.y = save.princess_y
    mygame.character = save.character
    i = 0
    i2 = 0
    temp = mygame.object_s
    while i < temp:
        while mygame.object__on[i2] != 1:
            i2 += 1   
        remove_object_(i2, mygame)
        i += 1
        i2 += 1
    mygame.fill_all = 1
    return

def new_game(mygame, level):
    return

def save_game(x, y, mygame):
    save  = save_data()
    save.cat_x = x + 24
    save.cat_y = y
    save.princess_x = x - 24
    save.princess_y = y
    save.ball_x = x + 24
    save.ball_y = y + 16
    save.character = mygame.character
    homepath = os.environ["HOME"] + '/.stringrolled/'
    if not os.path.exists(homepath): os.makedirs(homepath)
    f = data.load(homepath + 'game.sav', 'wb')
    cPickle.dump(save, f)
    f.close()
    

def verify_id(id, mygame):
    i = 0
    i2 = 0
    while i < mygame.object_s:
        while mygame.object__on[i2] == 0:
            i2 += 1
        if mygame.object_[i2].id == id:
            return 1
        i += 1
        i2 += 1
    return 0
    
def add_object_(object__type, x, y, map_width, mygame, idcheck):
    if idcheck == 1:
        if verify_id(int(y/16)*map_width + int(x/16), mygame) == 1:
            return
        
    i = 0
    while mygame.object__on[i] == 1:
        i += 1
    mygame.object_[i] = object__data()
    mygame.object_[i].dead = 0
    mygame.object_[i].x = x
    mygame.object_[i].y = y
    mygame.object_[i].width = 15.9
    mygame.object_[i].height = 15.9
    mygame.object_[i].animation = 0
    mygame.object_[i].type = object__type
    mygame.object_[i].id = int(y/16)*map_width + int(x/16)
    
    #=====================================================================  BELL ===============================================================================
    #if object__type == 2:
    
    #=====================================================================  PLATFORM ===============================================================================
    if object__type >=  48 and object__type < 59:
        mygame.object_[i].target_x = x
        mygame.object_[i].target_y = y
        mygame.object_[i].move_x = 0
        mygame.object_[i].move_y = 0
        mygame.object_[i].speed = 0.05
    
    #=====================================================================  BAT ===============================================================================
    if object__type == 128:
        mygame.object_[i].direction = 1
        mygame.object_[i].height = 8.9
        
    #=====================================================================  SPIKES ===============================================================================   
    if mygame.object_[i].type >=  112 and mygame.object_[i].type < 123:
        mygame.object_[i].y = y + 4
    
    mygame.object__on[i] = 1
    mygame.object_s += 1
    return

def touching_player(x, y, w, h, ccball, mygame):
    if x+w > mygame.cat.x and x < mygame.cat.x+mygame.cat.width and y+h > mygame.cat.y and y < mygame.cat.y+mygame.cat.height:
        return 1
    if x+w > mygame.princess.x and x < mygame.princess.x+mygame.princess.width and y+h > mygame.princess.y and y < mygame.princess.y+mygame.princess.height:
        return 2
    if ccball == 1:
        if x+w > mygame.ball.x and x < mygame.ball.x+mygame.ball.width and y+h > mygame.ball.y and y < mygame.ball.y+mygame.ball.height:
            return 3
    return 0

def touching_player_weak(x, y, w, h, ccball, mygame):
    x += 3
    w -= 6
    y += 3
    h -= 6
    if x+w > mygame.cat.x and x < mygame.cat.x+mygame.cat.width and y+h > mygame.cat.y and y < mygame.cat.y+mygame.cat.height:
        return 1
    if x+w > mygame.princess.x and x < mygame.princess.x+mygame.princess.width and y+h > mygame.princess.y and y < mygame.princess.y+mygame.princess.height:
        return 2
    if ccball == 1:
        if x+w > mygame.ball.x and x < mygame.ball.x+mygame.ball.width and y+h > mygame.ball.y and y < mygame.ball.y+mygame.ball.height:
            return 3
    return 0
    
def block_player(x, y, w, h, mygame):
    if x+w > mygame.cat.x and x < mygame.cat.x+mygame.cat.width and y+h > mygame.cat.y and y-0.5 < mygame.cat.y+mygame.cat.height:
        if x > mygame.cat.x:
            hdist = x-mygame.cat.x
        else:
            hdist = mygame.cat.x - x
        if y > mygame.cat.y:
            vdist = y-mygame.cat.y
        else:
            vdist = mygame.cat.y - y
        if hdist > vdist:
            if x > mygame.cat.x:
                mygame.cat.x = x - mygame.cat.width
                mygame.cat.speed_x = 0
            else:
                mygame.cat.x = x + w
                mygame.cat.speed_x = 0
        else:
            if y > mygame.cat.y:
                mygame.cat.y = y - mygame.cat.height
                mygame.cat.platform = 1
                mygame.cat.speed_y = 0
            else:
                mygame.cat.y = y + h
                mygame.cat.speed_y = 0
    if x+w > mygame.princess.x and x < mygame.princess.x+mygame.princess.width and y+h > mygame.princess.y and y-0.5 < mygame.princess.y+mygame.princess.height:
        if x > mygame.princess.x:
            hdist = x-mygame.princess.x
        else:
            hdist = mygame.princess.x - x
        if y > mygame.princess.y+8:
            vdist = y-8-mygame.princess.y
        else:
            vdist = mygame.princess.y+8 - y
        vdist = vdist*0.67
        if hdist > vdist:
            if x > mygame.princess.x:
                mygame.princess.x = x - mygame.princess.width
                mygame.princess.speed_x = 0
            else:
                mygame.princess.x = x + w
                mygame.princess.speed_x = 0
        else:
            if y > mygame.princess.y+8:
                mygame.princess.y = y - mygame.princess.height
                mygame.princess.platform = 1
                mygame.princess.speed_y = 0
            else:
                mygame.princess.y = y + h + 0.1
                mygame.princess.speed_y = 0
    if x+w > mygame.ball.x and x < mygame.ball.x+mygame.ball.width and y+h > mygame.ball.y and y-0.5 < mygame.ball.y+mygame.ball.height:
        if x > mygame.ball.x:
            hdist = x-mygame.ball.x
        else:
            hdist = mygame.ball.x - x
        if y > mygame.ball.y:
            vdist = y-mygame.ball.y
        else:
            vdist = mygame.ball.y - y
        if hdist > vdist:
            if x > mygame.ball.x:
                mygame.ball.x = x - mygame.ball.width
                mygame.ball.speed_x = 0
            else:
                mygame.ball.x = x + w
                mygame.ball.speed_x = 0
        else:
            if y > mygame.ball.y:
                mygame.ball.y = y - mygame.ball.height
                mygame.ball.platform = 1
                mygame.ball.speed_y = 0
            else:
                mygame.ball.y = y + h
                mygame.ball.speed_y = 0
    return

def block_player_platform(x, y, mx, my, w, h, mygame):
    if x+w > mygame.cat.x and x < mygame.cat.x+mygame.cat.width and y+h > mygame.cat.y and y-2.5 < mygame.cat.y+mygame.cat.height:
        if x > mygame.cat.x:
            hdist = x-mygame.cat.x
        else:
            hdist = mygame.cat.x - x
        if y > mygame.cat.y:
            vdist = y-mygame.cat.y
        else:
            vdist = mygame.cat.y - y
        if hdist <= vdist and mygame.cat.speed_y >= 0:
            if y > mygame.cat.y:
                mygame.cat.y = y - mygame.cat.height + 1
                mygame.cat.platform = 1
                mygame.cat.x += mx*mygame.time
                #mygame.cat.y += my*mygame.time
                mygame.cat.speed_y = 0
    if x+w > mygame.princess.x and x < mygame.princess.x+mygame.princess.width and y+h > mygame.princess.y and y-2.5 < mygame.princess.y+mygame.princess.height:
        if x > mygame.princess.x:
            hdist = x-mygame.princess.x
        else:
            hdist = mygame.princess.x - x
        if y > mygame.princess.y+8:
            vdist = y-8-mygame.princess.y
        else:
            vdist = mygame.princess.y+8 - y
        vdist = vdist*0.8
        if hdist <= vdist and mygame.princess.speed_y >= 0:
            if y > mygame.princess.y+8:
                mygame.princess.y = y - mygame.princess.height + 1
                mygame.princess.platform = 1
                mygame.princess.x += mx*mygame.time
                #mygame.princess.y += my*mygame.time
                mygame.princess.speed_y = 0
    return
    
def object__too_far(i, mygame):
    xdist = 640
    ydist = 400
    if mygame.object_[i].type >=  48 and mygame.object_[i].type < 59:
        xdist = 1000
        ydist = 8000
    if mygame.object_[i].type >=  16 and mygame.object_[i].type < 27:
        if mygame.object_[i].type%2 == 0:
            xdist = 1000
            ydist = 800
        else:
            xdist = 500
            ydist = 300
    if mygame.object_[i].type == 2:
        xdist = 1000
        ydist = 800
    x = mygame.object_[i].x
    y = mygame.object_[i].y
    
    if x - mygame.cat.x > xdist or mygame.cat.x - x > xdist or y - mygame.cat.y > ydist or mygame.cat.y - y > ydist:
        if x - mygame.princess.x > xdist or mygame.princess.x - x > xdist or y - mygame.princess.y > ydist or mygame.princess.y - y > ydist:
            return 1
    return 0

def remove_object_(i, mygame):
    mygame.object_[i] = 0
    mygame.object__on[i] = 0
    mygame.object_s -= 1
    
def move_object_(i, time, mygame, level, graphics):
    
    #=====================================================================  BELL ===============================================================================
    if mygame.object_[i].type == 2:
        if mygame.object_[i].animation == 0:
            if touching_player(mygame.object_[i].x, mygame.object_[i].y, mygame.object_[i].width, mygame.object_[i].height, 0, mygame) == mygame.character+1:
                mygame.sound_15.play()
                mygame.object_[i].animation = 1
                i2 = 0
                while i2 < 10:
                    mygame.switch[i2] = i2%2
                    i2 += 1
                if mygame.character == 0:
                    mygame.princess.x = mygame.object_[i].x - 24
                    mygame.princess.y = mygame.object_[i].y
                else:
                    mygame.cat.x = mygame.object_[i].x + 24
                    mygame.cat.y = mygame.object_[i].y
                mygame.ball.x = mygame.object_[i].x + 24
                mygame.ball.y = mygame.object_[i].y + 16
                mygame.sparkle = 1000
                mygame.em = 0
                save_game(mygame.object_[i].x, mygame.object_[i].y, mygame)
            graph.draw_sprite(256 + 32, mygame.object_[i].x, mygame.object_[i].y, graphics)    
        else:
            mygame.object_[i].animation += time
            frame = (mygame.object_[i].animation/100)%6
            if frame < 2:
                graph.draw_sprite(256 + 33, mygame.object_[i].x, mygame.object_[i].y, graphics)
            if (frame >= 2 and frame < 3) or frame == 5:
                graph.draw_sprite(256 + 32, mygame.object_[i].x, mygame.object_[i].y, graphics)
            if frame >= 3 and frame < 5:
                graph.draw_sprite(256 + 34, mygame.object_[i].x, mygame.object_[i].y, graphics)
            if mygame.object_[i].animation > 10000:
                mygame.object_[i].animation = 0
        if object__too_far(i, mygame) == 1:
            remove_object_(i, mygame)
            return

    #===================================================================== DESTRO BLOCKS ===============================================================================
    if mygame.object_[i].type == 3:
        graph.draw_sprite(256 + 45, mygame.object_[i].x, mygame.object_[i].y, graphics)
        if touching_player(mygame.object_[i].x, mygame.object_[i].y, mygame.object_[i].width, mygame.object_[i].height, 1, mygame) == 3 and mygame.ball_is_deadly:
            add_object_(5, (int(mygame.object_[i].x/16))*16, (int(mygame.object_[i].y/16))*16, level.width, mygame, 0)
            remove_object_(i, mygame)
            mygame.sound_7.play()
            return  
        block_player(mygame.object_[i].x, mygame.object_[i].y, mygame.object_[i].width, mygame.object_[i].height, mygame)      
        if object__too_far(i, mygame) == 1:
            remove_object_(i, mygame)
            return
            
    #===================================================================== INVISI HURT ===============================================================================
    if mygame.object_[i].type == 4:
        ccheck = touching_player(mygame.object_[i].x, mygame.object_[i].y, mygame.object_[i].width, mygame.object_[i].height, 0, mygame)
        if ccheck != 0:
            mygame.dead += 1
            if ccheck == 1:
                mygame.cat_dead = 1
            else:
                mygame.princess_dead = 1
        if object__too_far(i, mygame) == 1:
            remove_object_(i, mygame)
            return
            
            

    #=====================================================================  EXPLODE >:(  ===============================================================================
    if mygame.object_[i].type == 5:
        mygame.object_[i].animation += mygame.time  
        frame = mygame.object_[i].animation/100
        if frame < 5:
            graph.draw_sprite(256 + 35 + frame, mygame.object_[i].x, mygame.object_[i].y, graphics)    
        else: 
            remove_object_(i, mygame)
            return

    #=====================================================================  SPARKLE ===============================================================================
    if mygame.object_[i].type == 6:
        mygame.object_[i].animation += mygame.time  
        frame = mygame.object_[i].animation/100
        if frame < 5:
            graph.draw_sprite(256 + 40 + frame, mygame.object_[i].x, mygame.object_[i].y, graphics)    
        else: 
            remove_object_(i, mygame)
            return
            
    #===================================================================== SWITCHES ===============================================================================
    if mygame.object_[i].type >=  16 and mygame.object_[i].type < 27:
        color = ((mygame.object_[i].type - 16)/2)*2
        switch_type = mygame.object_[i].type%2
        if switch_type == 0:
            #TOGGLE
            if mygame.switch[color] == 0:
                if touching_player(mygame.object_[i].x, mygame.object_[i].y, mygame.object_[i].width, mygame.object_[i].height, 1, mygame) != 0:
                    mygame.sound_3.play()
                    mygame.switch[color] = 1
                    mygame.switch[color + 1] = 0
            graph.draw_sprite(256 + 48 + color + mygame.switch[color], mygame.object_[i].x, mygame.object_[i].y, graphics)
        else:
            #PRESS
            if touching_player(mygame.object_[i].x, mygame.object_[i].y, mygame.object_[i].width, mygame.object_[i].height, 1, mygame) != 0:
                if mygame.switch[color] == 0:
                    mygame.sound_3.play()
                mygame.switch[color] = 1
                mygame.switch[color + 1] = 0
            else:
                if mygame.switch[color] == 1:
                    mygame.sound_8.play()
                mygame.switch[color] = 0
                mygame.switch[color + 1] = 1
            graph.draw_sprite(256 + 48 + color + mygame.switch[color], mygame.object_[i].x, mygame.object_[i].y, graphics)
        if object__too_far(i, mygame) == 1:
            remove_object_(i, mygame)
            return

    
    #===================================================================== BLOCKS ===============================================================================
    if mygame.object_[i].type >=  32 and mygame.object_[i].type < 43:
        color = ((mygame.object_[i].type - 32)/2)*2
        active = mygame.switch[mygame.object_[i].type - 32]
        graph.draw_sprite(256 + 65 + color - active, mygame.object_[i].x, mygame.object_[i].y, graphics)
        if active == 1:
            block_player(mygame.object_[i].x, mygame.object_[i].y, mygame.object_[i].width, mygame.object_[i].height, mygame)
        if object__too_far(i, mygame) == 1:
            remove_object_(i, mygame)
            return

    #===================================================================== PLATFORMS ===============================================================================
    if mygame.object_[i].type >=  48 and mygame.object_[i].type < 59:
        color = ((mygame.object_[i].type - 48)/2)*2
        active = mygame.switch[mygame.object_[i].type - 48]
        frame = (mygame.object_[i].animation/50)%2
        mygame.object_[i].animation += mygame.time
        graph.draw_sprite(256 + 80 + color + frame, mygame.object_[i].x, mygame.object_[i].y, graphics)
        move_x = 0
        move_y = 0
        if active == 1:
            move = 0
            if (mygame.object_[i].x + mygame.object_[i].speed * mygame.time) < mygame.object_[i].target_x:
                mygame.object_[i].x += mygame.object_[i].speed * mygame.time
                move = 1
                move_x = mygame.object_[i].speed
            if (mygame.object_[i].x - mygame.object_[i].speed * mygame.time) > mygame.object_[i].target_x:
                move = 1
                mygame.object_[i].x -= mygame.object_[i].speed * mygame.time
                move_x = -mygame.object_[i].speed
            if (mygame.object_[i].y + mygame.object_[i].speed * mygame.time) < mygame.object_[i].target_y:
                move = 1
                mygame.object_[i].y += mygame.object_[i].speed * mygame.time
                move_y = mygame.object_[i].speed
            if (mygame.object_[i].y - mygame.object_[i].speed * mygame.time) > mygame.object_[i].target_y:
                move = 1
                mygame.object_[i].y -= mygame.object_[i].speed * mygame.time
                move_y = -mygame.object_[i].speed
            if move == 0:
                mygame.object_[i].x = mygame.object_[i].target_x
                mygame.object_[i].y = mygame.object_[i].target_y
                tile = int(mygame.object_[i].x/16) + int(mygame.object_[i].y/16)*mygame.width
                tile2 = level.direction[tile]
                if tile2 != 0:
                    mygame.object_[i].move_x = (tile2%16) - 2
                    mygame.object_[i].move_y = (tile2/16) - 1
                mygame.object_[i].target_x = mygame.object_[i].target_x + mygame.object_[i].move_x*16
                mygame.object_[i].target_y = mygame.object_[i].target_y + mygame.object_[i].move_y*16
        block_player_platform(mygame.object_[i].x, mygame.object_[i].y, move_x, move_y, mygame.object_[i].width, mygame.object_[i].height, mygame)
        if object__too_far(i, mygame) == 1:
            remove_object_(i, mygame)
            return
    
    #===================================================================== GUNS ===============================================================================
    if mygame.object_[i].type >=  64 and mygame.object_[i].type < 75:
        color = ((mygame.object_[i].type - 64)/2)*2
        active = mygame.switch[mygame.object_[i].type - 64]
        mygame.object_[i].animation += time
        if active == 1:
            if mygame.object_[i].animation > 2400:
                mygame.object_[i].animation = 0
                add_object_(75, (int(mygame.object_[i].x/16))*16, (int(mygame.object_[i].y/16))*16, level.width, mygame, 0)
                mygame.sound_18.play()
            frame = mygame.object_[i].animation < 250
            if frame == 1:
                graph.draw_sprite(256 + 97 + color, mygame.object_[i].x, mygame.object_[i].y, graphics)
            else:
                graph.draw_sprite(256 + 96 + color, mygame.object_[i].x, mygame.object_[i].y, graphics)
        else:
            graph.draw_sprite(256 + 96 + color, mygame.object_[i].x, mygame.object_[i].y, graphics)
        if object__too_far(i, mygame) == 1:
            remove_object_(i, mygame)
            return
    
    #===================================================================== BULLETRON ===============================================================================
    if mygame.object_[i].type ==  75:
        mygame.object_[i].y -= 0.17 * mygame.time
        graph.draw_sprite(256 + 106, mygame.object_[i].x, mygame.object_[i].y, graphics)
        ccheck = touching_player_weak(mygame.object_[i].x, mygame.object_[i].y, mygame.object_[i].width, mygame.object_[i].height, 0, mygame)
        if ccheck != 0:
            mygame.dead += 1
            if ccheck == 1:
                mygame.cat_dead = 1
            else:
                mygame.princess_dead = 1
        if object__too_far(i, mygame) == 1:
            remove_object_(i, mygame)
            return

    #===================================================================== GUNS 2 ===============================================================================
    if mygame.object_[i].type >=  80 and mygame.object_[i].type < 91:
        color = ((mygame.object_[i].type - 80)/2)*2
        active = mygame.switch[mygame.object_[i].type - 80]
        mygame.object_[i].animation += time
        if active == 1:
            if mygame.object_[i].animation > 2400:
                mygame.object_[i].animation = 0
                add_object_(76, (int(mygame.object_[i].x/16))*16, (int(mygame.object_[i].y/16))*16, level.width, mygame, 0)
                mygame.sound_18.play()
            frame = mygame.object_[i].animation < 250
            if frame == 1:
                graph.draw_sprite(97 + 16 + color, mygame.object_[i].x, mygame.object_[i].y, graphics)
            else:
                graph.draw_sprite(96 + 16 + color, mygame.object_[i].x, mygame.object_[i].y, graphics)
        else:
            graph.draw_sprite(96 + 16 + color, mygame.object_[i].x, mygame.object_[i].y, graphics)
        if object__too_far(i, mygame) == 1:
            remove_object_(i, mygame)
            return

    #===================================================================== GUNS 3 ===============================================================================
    if mygame.object_[i].type >=  96 and mygame.object_[i].type < 107:
        color = ((mygame.object_[i].type - 96)/2)*2
        active = mygame.switch[mygame.object_[i].type - 96]
        mygame.object_[i].animation += time
        if active == 1:
            if mygame.object_[i].animation > 2400:
                mygame.object_[i].animation = 0
                add_object_(77, (int(mygame.object_[i].x/16))*16, (int(mygame.object_[i].y/16))*16, level.width, mygame, 0)
                mygame.sound_18.play()
            frame = mygame.object_[i].animation < 250
            if frame == 1:
                graph.draw_sprite(256 + 97 + 16 + color, mygame.object_[i].x, mygame.object_[i].y, graphics)
            else:
                graph.draw_sprite(256 + 96 + 16 + color, mygame.object_[i].x, mygame.object_[i].y, graphics)
        else:
            graph.draw_sprite(256 + 96 + 16 + color, mygame.object_[i].x, mygame.object_[i].y, graphics)
        if object__too_far(i, mygame) == 1:
            remove_object_(i, mygame)
            return
            
    
    #===================================================================== BULLETRON 2 ===============================================================================
    if mygame.object_[i].type ==  76:
        mygame.object_[i].x -= 0.17 * mygame.time
        graph.draw_sprite(106 + 16, mygame.object_[i].x, mygame.object_[i].y, graphics)
        ccheck = touching_player_weak(mygame.object_[i].x, mygame.object_[i].y, mygame.object_[i].width, mygame.object_[i].height, 0, mygame)
        if ccheck != 0:
            mygame.dead += 1
            if ccheck == 1:
                mygame.cat_dead = 1
            else:
                mygame.princess_dead = 1
        if object__too_far(i, mygame) == 1:
            remove_object_(i, mygame)
            return
    
    #===================================================================== BULLETRON 3 ===============================================================================
    if mygame.object_[i].type ==  77:
        mygame.object_[i].x += 0.17 * mygame.time
        graph.draw_sprite(106 + 16 + 256, mygame.object_[i].x, mygame.object_[i].y, graphics)
        ccheck = touching_player_weak(mygame.object_[i].x, mygame.object_[i].y, mygame.object_[i].width, mygame.object_[i].height, 0, mygame)
        if ccheck != 0:
            mygame.dead += 1
            if ccheck == 1:
                mygame.cat_dead = 1
            else:
                mygame.princess_dead = 1
        if object__too_far(i, mygame) == 1:
            remove_object_(i, mygame)
            return
    
    
    
    
    
    
    
    #===================================================================== SPIKES ===============================================================================
    if mygame.object_[i].type >=  112 and mygame.object_[i].type < 123:
        color = ((mygame.object_[i].type - 112)/2)*2
        active = mygame.switch[mygame.object_[i].type - 112]
        graph.draw_sprite(256 + 129 + color - active, mygame.object_[i].x, mygame.object_[i].y - 4, graphics)
        if active == 1:
            ccheck = touching_player(mygame.object_[i].x, mygame.object_[i].y, mygame.object_[i].width, mygame.object_[i].height, 0, mygame)
            if ccheck != 0:
                mygame.dead += 1
                if ccheck == 1:
                    mygame.cat_dead = 1
                else:
                    mygame.princess_dead = 1
        if object__too_far(i, mygame) == 1:
            remove_object_(i, mygame)
            return
    
    #===================================================================== BAT ===============================================================================
    if mygame.object_[i].type == 128:
        if mygame.object_[i].dead == 0:
            mygame.object_[i].animation += mygame.time
            frame = (mygame.object_[i].animation/100)%4
            frame = frame - (frame==3)*2
            mygame.object_[i].y += math.sin(mygame.object_[i].animation/100.0)
            mygame.object_[i].x += mygame.object_[i].direction * mygame.time * 0.02
            
            tile = int(mygame.object_[i].x/16) + int(mygame.object_[i].y/16)*mygame.width
            tile2 = level.tilemap[tile]
            tile3 = level.tilemap[tile+1]
            if tile2 >= 64 or tile3 >= 64:
                mygame.object_[i].direction *= -1
                mygame.object_[i].x += mygame.object_[i].direction * mygame.time * 0.02
                        
            graph.draw_sprite(256*(mygame.object_[i].direction == 1) + 128 + 16 + frame, mygame.object_[i].x, mygame.object_[i].y, graphics)
            if touching_player(mygame.object_[i].x, mygame.object_[i].y, mygame.object_[i].width, mygame.object_[i].height, 1, mygame) == 3 and mygame.ball_is_deadly:
                add_object_(5, (int(mygame.object_[i].x/16))*16, (int(mygame.object_[i].y/16))*16, level.width, mygame, 0)
                mygame.object_[i].dead = 1
                mygame.sound_7.play()
                return  
            ccheck = touching_player(mygame.object_[i].x, mygame.object_[i].y, mygame.object_[i].width, mygame.object_[i].height, 0, mygame)
            if ccheck != 0:
                mygame.dead += 1
                if ccheck == 1:
                    mygame.cat_dead = 1
                else:
                    mygame.princess_dead = 1     
        if object__too_far(i, mygame) == 1:
            remove_object_(i, mygame)
            return
    
    return
    
def step(time, gamepad, mygame, level, graphics):
    if gamepad.toggle == 1:
        if mygame.character == 0:
            mygame.character = 1
            mygame.sound_16.play()
        else:
            mygame.character = 0
            mygame.sound_17.play()

    if mygame.dead != 0:
        if mygame.dead < 10:
            mygame.sound_20.play()
            if mygame.cat_dead == 1:
                mygame.cat.speed_y -= 1.2
            if mygame.princess_dead == 1:
                mygame.princess.speed_y -= 1.2
            mygame.em = 0
        mygame.dead += mygame.time
        if mygame.cat_dead == 1:
            mygame.cat.x += mygame.cat.speed_x
            mygame.cat.y += mygame.cat.speed_y
            mygame.cat.speed_y += time*mygame.cat.max_acceleration_y*2
        if mygame.princess_dead == 1:
            mygame.princess.x += mygame.princess.speed_x
            mygame.princess.y += mygame.princess.speed_y
            mygame.princess.speed_y += time*mygame.princess.max_acceleration_y*4
        while mygame.em < math.sqrt(mygame.dead/12) + (mygame.dead/100):
            mygame.em += 1
            if mygame.cat_dead == 1:
                add_object_(5, mygame.cat.x - 16 + random.random()*32, mygame.cat.y - 16 + random.random()*32, level.width, mygame, 0)
            if mygame.princess_dead == 1:
                add_object_(5, mygame.princess.x - 16 + random.random()*32, mygame.princess.y - 16 + random.random()*48, level.width, mygame, 0)
        mygame.character = 3
        if mygame.dead > 2000:
            mygame.dead = 0
            mygame.cat_dead = 0
            mygame.princess_dead = 0
            mygame.sparkle = 1000
            mygame.em = 0
            mygame.sound_21.play()
            continue_game(mygame, level)
            
    if mygame.sparkle > 0:
        mygame.sparkle -= mygame.time
        while mygame.em < (1000-mygame.sparkle)/80:
            mygame.em += 1
            add_object_(6, mygame.cat.x - 8 + random.random()*24, mygame.cat.y - 8 + random.random()*24, level.width, mygame, 0)
            add_object_(6, mygame.princess.x - 8 + random.random()*24, mygame.princess.y - 8 + random.random()*32, level.width, mygame, 0)
        
    #=====================================================================  CAT MOVEMENT ===============================================================================
    if(mygame.cat_dead == 0):
        tile1 = int((mygame.cat.x + 0.01)/16) +                        int((mygame.cat.y + mygame.cat.height + 0.1)/16)*level.width
        tile2 = int((mygame.cat.x + mygame.cat.width - 0.01)/16) +     int((mygame.cat.y + mygame.cat.height + 0.1)/16)*level.width
        if tile1 >= 0 and tile2 < level.width*(level.height-1):
            if ((level.tilemap[tile1] >= 32 or level.tilemap[tile2] >= 32) and mygame.cat.speed_y >= 0) or mygame.cat.platform == 1:
                if mygame.cat.airborne == 1:
                    mygame.sound_1.play()
                mygame.cat.airborne = 0
                if mygame.cat.platform == 0:
                    mygame.cat.speed_y = 0
                mygame.cat.y = int(mygame.cat.y)
                mygame.cat.acceleration_y = 0
                if gamepad.jump == 1 and mygame.character == 0:
                    mygame.sound_4.play()
                    mygame.cat.speed_y = -mygame.cat.jump_speed
            else:
                mygame.cat.airborne = 1        
        mygame.cat.platform = 0
        
        if mygame.cat.airborne == 0:
            if mygame.cat.speed_y < mygame.cat.max_speed_y:
                mygame.cat.acceleration_y = mygame.cat.max_acceleration_y
            else:
                mygame.cat.acceleration_y = 0
                mygame.cat.speed_y = mygame.cat.max_speed_y
            mygame.cat.acceleration_x = 0.0
            if mygame.cat.speed_x < -0.05:
                if gamepad.left == 1 and mygame.character == 0:
                    mygame.cat.acceleration_x = -mygame.cat.max_acceleration_x
                else:
                    mygame.cat.acceleration_x = mygame.cat.max_acceleration_x*2

            if mygame.cat.speed_x > 0.05:
                if gamepad.right == 1 and mygame.character == 0:
                    mygame.cat.acceleration_x = mygame.cat.max_acceleration_x
                else:
                    mygame.cat.acceleration_x = -mygame.cat.max_acceleration_x*2
                    
            if mygame.cat.speed_x >= -0.05 and mygame.cat.speed_x <= 0.05:
                if gamepad.left == 1 and mygame.character == 0:
                    mygame.cat.acceleration_x = -mygame.cat.max_acceleration_x
                if gamepad.right == 1 and mygame.character == 0:
                    mygame.cat.acceleration_x = mygame.cat.max_acceleration_x
                if gamepad.left == 0 and gamepad.right == 0:
                    mygame.cat.speed_x = 0

        else:
            if mygame.cat.speed_y < mygame.cat.max_speed_y:
                if gamepad.up == 1 or mygame.cat.speed_y >= 0:
                    mygame.cat.acceleration_y = mygame.cat.max_acceleration_y
                else:
                    mygame.cat.acceleration_y = mygame.cat.max_acceleration_y*3
            else:
                mygame.cat.acceleration_y = 0
                mygame.cat.speed_y = mygame.cat.max_speed_y
            mygame.cat.acceleration_x = 0.0
            if mygame.cat.speed_x < -0.05:
                if gamepad.left == 1 and mygame.character == 0:
                    mygame.cat.acceleration_x = -mygame.cat.max_acceleration_x/3
                else:
                    mygame.cat.acceleration_x = mygame.cat.max_acceleration_x*1.2

            if mygame.cat.speed_x > 0.05:
                if gamepad.right == 1 and mygame.character == 0:
                    mygame.cat.acceleration_x = mygame.cat.max_acceleration_x/3
                else:
                    mygame.cat.acceleration_x = -mygame.cat.max_acceleration_x*1.2
                    
            if mygame.cat.speed_x >= -0.05 and mygame.cat.speed_x <= 0.05:
                if gamepad.left == 1 and mygame.character == 0:
                    mygame.cat.acceleration_x = -mygame.cat.max_acceleration_x/2
                if gamepad.right == 1 and mygame.character == 0:
                    mygame.cat.acceleration_x = mygame.cat.max_acceleration_x/2
                if gamepad.left == 0 and gamepad.right == 0:
                    mygame.cat.speed_x = 0
                    
        walking = 0
        if gamepad.left == 1 and mygame.character == 0:          
            mygame.cat.direction = 0
            walking = 1
        if gamepad.right == 1 and mygame.character == 0:
            mygame.cat.direction = 1    
            walking = 1
        mygame.cat.animation = (mygame.cat.animation + time)*walking
                
                
        move_x = mygame.cat.speed_x + time*mygame.cat.acceleration_x/2.0
        if move_x > mygame.cat.max_speed_x:
            move_x = mygame.cat.max_speed_x
        if move_x < -mygame.cat.max_speed_x:
            move_x = -mygame.cat.max_speed_x        
        mygame.cat.x += time*move_x
        mygame.cat.speed_x += mygame.cat.acceleration_x*time
        if mygame.cat.speed_x > mygame.cat.max_speed_x:
            mygame.cat.speed_x = mygame.cat.max_speed_x     
        if mygame.cat.speed_x < -mygame.cat.max_speed_x:
            mygame.cat.speed_x = -mygame.cat.max_speed_x         
        collision = 1
        reset_speed = 0
        while collision != 0 and collision < 3:
            tile1 = int(mygame.cat.x + 0.01)/16 +                      level.width*(int(mygame.cat.y + 0.2)/16)
            tile2 = int(mygame.cat.x + mygame.cat.width - 0.01)/16 +   level.width*(int(mygame.cat.y + 0.2)/16)
            tile5 = int(mygame.cat.x + 0.01)/16 +                      level.width*(int(mygame.cat.y + mygame.cat.height - 0.01)/16)
            tile6 = int(mygame.cat.x + mygame.cat.width - 0.01)/16 +   level.width*(int(mygame.cat.y + mygame.cat.height - 0.01)/16)
            if tile1 >= 0 and tile6 < level.width*(level.height-1):
                if level.tilemap[tile1] >= 64 or level.tilemap[tile2] >= 64 or level.tilemap[tile5] >= 64 or level.tilemap[tile6] >= 64:
                    collision += 1
                    if(mygame.cat.speed_x > 0):
                        mygame.cat.x = float(int((mygame.cat.x + mygame.cat.width)/16)*16) - mygame.cat.width
                        reset_speed = 1
                    else:
                        if(mygame.cat.speed_x == 0):
                            mygame.cat.x = float(int((mygame.cat.x + 8.0)/16)*16)
                            reset_speed = 1
                        else:
                            mygame.cat.x = float(int((mygame.cat.x + 16)/16)*16)
                            reset_speed = 1
                else:
                    collision = 0
            else:
                collision = 0
        if collision == 3:
            mygame.cat_dead = 1
            mygame.dead = 1
        if reset_speed == 1:
            mygame.cat.speed_x = 0
        
        move_y = mygame.cat.speed_y + time*mygame.cat.acceleration_y/2.0
        if move_y > mygame.cat.max_speed_y:
            move_y = mygame.cat.max_speed_y
        if move_y < -mygame.cat.max_speed_y:
            move_y = -mygame.cat.max_speed_y        
        mygame.cat.y += time*move_y
        mygame.cat.speed_y += mygame.cat.acceleration_y*time

        if mygame.cat.speed_y > mygame.cat.max_speed_y:
            mygame.cat.speed_y = mygame.cat.max_speed_y     
        collision = 1
        reset_speed = 0
        while collision != 0 and collision < 3:
            tile1 = int(mygame.cat.x + 0.01)/16 +                      level.width*(int(mygame.cat.y + 0.2)/16)
            tile2 = int(mygame.cat.x + mygame.cat.width - 0.01)/16 +   level.width*(int(mygame.cat.y + 0.2)/16)
            tile3 = int(mygame.cat.x + 0.01)/16 +                      level.width*(int(mygame.cat.y + mygame.cat.height - 0.01)/16)
            tile4 = int(mygame.cat.x + mygame.cat.width - 0.01)/16 +   level.width*(int(mygame.cat.y + mygame.cat.height - 0.01)/16)
            if tile1 >= 0 and tile6 < level.width*(level.height-1):
                if(mygame.cat.speed_y >= 0):
                    if level.tilemap[tile1] >= 64 or level.tilemap[tile2] >= 64 or level.tilemap[tile3] >= 32 or level.tilemap[tile4] >= 32:
                        collision += 1
                        mygame.cat.y = float(int((mygame.cat.y + mygame.cat.height)/16)*16) - mygame.cat.height
                        reset_speed = 1
                    else:
                        collision = 0
                else:
                    if level.tilemap[tile1] >= 64 or level.tilemap[tile2] >= 64 or level.tilemap[tile3] >= 64 or level.tilemap[tile4] >= 64 or level.tilemap[tile5] >= 64 or level.tilemap[tile6] >= 64:
                        collision += 1
                        mygame.cat.y = float(int((mygame.cat.y + 16)/16)*16)
                        reset_speed = 1
                    else:
                        collision = 0
            else:
                collision = 0
        if collision == 3:
            mygame.cat_dead = 1
            mygame.dead = 1
        if reset_speed == 1:
            mygame.cat.speed_y = 0
            

            
            
    
    #=====================================================================  BALL  THROW ===============================================================================
    if(mygame.ball_dead == 0 and mygame.carrying_ball == 1):
        if gamepad.throw == 1:
            gamepad.throw = 2
            mygame.carrying_ball = 0
            mygame.sound_13.play()
            mygame.ball.x = mygame.princess.x
            mygame.ball.y = mygame.princess.y
            mygame.ball.speed_x = (mygame.princess.direction-0.5)*0.5
            mygame.ball.speed_y = -0.15
            
    if(mygame.ball_dead == 0 and mygame.carrying_ball == 0):
        if mygame.ball.speed_x < -0.12 or mygame.ball.speed_x > 0.12 or mygame.ball.speed_y > 0.12:
            mygame.ball_is_deadly = 1
        else:
            mygame.ball_is_deadly = 0
        
        if gamepad.throw == 1:
            if mygame.ball.x+mygame.ball.width > mygame.princess.x and mygame.ball.x < mygame.princess.x+mygame.princess.width and mygame.ball.y+mygame.ball.height > mygame.princess.y and mygame.ball.y-0.5 < mygame.princess.y+mygame.princess.height:
                mygame.sound_5.play()
                mygame.carrying_ball = 1
                mygame.ball_is_deadly = 0
    #=====================================================================  BALL  MOVEMENT ===============================================================================
    if(mygame.ball_dead == 0 and mygame.carrying_ball == 0):
        tile1 = int((mygame.ball.x + 0.01)/16) +                        int((mygame.ball.y + mygame.ball.height + 0.1)/16)*level.width
        tile2 = int((mygame.ball.x + mygame.ball.width - 0.01)/16) +     int((mygame.ball.y + mygame.ball.height + 0.1)/16)*level.width
        if tile1 >= 0 and tile2 < level.width*(level.height-1):
            if ((level.tilemap[tile1] >= 32 or level.tilemap[tile2] >= 32) and mygame.ball.speed_y >= 0) or mygame.ball.platform == 1:
                mygame.ball.airborne = 0
                if mygame.ball.speed_y < 0.1 and mygame.ball.speed_y > -0.1:
                    mygame.ball.speed_y = 0
                mygame.ball.y = int(mygame.ball.y)
                mygame.ball.acceleration_y = 0
            else:
                mygame.ball.airborne = 1        
        mygame.ball.platform = 0
        
        if mygame.ball.airborne == 0:
            if mygame.ball.speed_y < mygame.ball.max_speed_y:
                mygame.ball.acceleration_y = mygame.ball.max_acceleration_y
            else:
                mygame.ball.acceleration_y = 0
                mygame.ball.speed_y = mygame.ball.max_speed_y
            mygame.ball.acceleration_x = 0.0
            if mygame.ball.speed_x < -0.05:
                    mygame.ball.acceleration_x = mygame.ball.max_acceleration_x

            if mygame.ball.speed_x > 0.05:
                    mygame.ball.acceleration_x = -mygame.ball.max_acceleration_x
                    
            if mygame.ball.speed_x >= -0.05 and mygame.ball.speed_x <= 0.05:
                mygame.ball.speed_x = 0

        else:
            if mygame.ball.speed_y < mygame.ball.max_speed_y:
                mygame.ball.acceleration_y = mygame.ball.max_acceleration_y
            else:
                mygame.ball.acceleration_y = 0
                mygame.ball.speed_y = mygame.ball.max_speed_y
            mygame.ball.acceleration_x = 0.0
            if mygame.ball.speed_x < -0.05:
                mygame.ball.acceleration_x = mygame.ball.max_acceleration_x/6

            if mygame.ball.speed_x > 0.05:
                mygame.ball.acceleration_x = -mygame.ball.max_acceleration_x/6
                    
            if mygame.ball.speed_x >= -0.005 and mygame.ball.speed_x <= 0.005:
                mygame.ball.speed_x = 0
                    
        walking = 0
        if mygame.ball.speed_x < 0.05 or mygame.ball.speed_x > 0.05:          
            walking = 1  
        mygame.ball.animation = mygame.ball.animation + time*walking*1000*mygame.ball.speed_x
                
                
        move_x = mygame.ball.speed_x + time*mygame.ball.acceleration_x/2.0
        if move_x > mygame.ball.max_speed_x:
            move_x = mygame.ball.max_speed_x
        if move_x < -mygame.ball.max_speed_x:
            move_x = -mygame.ball.max_speed_x        
        mygame.ball.x += time*move_x
        mygame.ball.speed_x += mygame.ball.acceleration_x*time
        if mygame.ball.speed_x > mygame.ball.max_speed_x:
            mygame.ball.speed_x = mygame.ball.max_speed_x     
        if mygame.ball.speed_x < -mygame.ball.max_speed_x:
            mygame.ball.speed_x = -mygame.ball.max_speed_x         
        collision = 1
        reset_speed = 0
        while collision != 0 and collision < 100:
            tile1 = int(mygame.ball.x + 0.01)/16 +                      level.width*(int(mygame.ball.y + 0.2)/16)
            tile2 = int(mygame.ball.x + mygame.ball.width - 0.01)/16 +   level.width*(int(mygame.ball.y + 0.2)/16)
            tile5 = int(mygame.ball.x + 0.01)/16 +                      level.width*(int(mygame.ball.y + mygame.ball.height - 0.01)/16)
            tile6 = int(mygame.ball.x + mygame.ball.width - 0.01)/16 +   level.width*(int(mygame.ball.y + mygame.ball.height - 0.01)/16)
            if tile1 >= 0 and tile6 < level.width*(level.height-1):
                if level.tilemap[tile1] >= 64 or level.tilemap[tile2] >= 64 or level.tilemap[tile5] >= 64 or level.tilemap[tile6] >= 64:
                    collision += 1
                    if(mygame.ball.speed_x > 0):
                        mygame.ball.x = float(int((mygame.ball.x + mygame.ball.width)/16)*16) - mygame.ball.width
                        reset_speed = 1
                    else:
                        if(mygame.ball.speed_x == 0):
                            mygame.ball.x = float(int((mygame.ball.x + 8.0)/16)*16)
                            reset_speed = 1
                        else:
                            mygame.ball.x = float(int((mygame.ball.x + 16)/16)*16)
                            reset_speed = 1
                else:
                    collision = 0
            else:
                collision = 0
        if reset_speed == 1:
            if mygame.ball.speed_x < -0.05 or mygame.ball.speed_x > 0.05:
                mygame.sound_14.play()
            mygame.ball.speed_x = 0
        
        move_y = mygame.ball.speed_y + time*mygame.ball.acceleration_y/2.0
        if move_y > mygame.ball.max_speed_y:
            move_y = mygame.ball.max_speed_y
        if move_y < -mygame.ball.max_speed_y:
            move_y = -mygame.ball.max_speed_y        
        mygame.ball.y += time*move_y
        mygame.ball.speed_y += mygame.ball.acceleration_y*time

        if mygame.ball.speed_y > mygame.ball.max_speed_y:
            mygame.ball.speed_y = mygame.ball.max_speed_y     
        collision = 1
        reset_speed = 0
        while collision != 0 and collision < 100:
            tile1 = int(mygame.ball.x + 0.01)/16 +                      level.width*(int(mygame.ball.y + 0.2)/16)
            tile2 = int(mygame.ball.x + mygame.ball.width - 0.01)/16 +   level.width*(int(mygame.ball.y + 0.2)/16)
            tile3 = int(mygame.ball.x + 0.01)/16 +                      level.width*(int(mygame.ball.y + mygame.ball.height - 0.01)/16)
            tile4 = int(mygame.ball.x + mygame.ball.width - 0.01)/16 +   level.width*(int(mygame.ball.y + mygame.ball.height - 0.01)/16)
            if tile1 >= 0 and tile6 < level.width*(level.height-1):
                if(mygame.ball.speed_y >= 0):
                    if level.tilemap[tile1] >= 64 or level.tilemap[tile2] >= 64 or level.tilemap[tile3] >= 32 or level.tilemap[tile4] >= 32:
                        collision += 1
                        mygame.ball.y = float(int((mygame.ball.y + mygame.ball.height)/16)*16) - mygame.ball.height
                        reset_speed = 1
                    else:
                        collision = 0
                else:
                    if level.tilemap[tile1] >= 64 or level.tilemap[tile2] >= 64 or level.tilemap[tile3] >= 64 or level.tilemap[tile4] >= 64 or level.tilemap[tile5] >= 64 or level.tilemap[tile6] >= 64:
                        collision += 1
                        mygame.ball.y = float(int((mygame.ball.y + 16)/16)*16)
                        reset_speed = 1
                    else:
                        collision = 0
            else:
                collision = 0
        if reset_speed == 1:
            if mygame.ball.speed_y > 0.1:
                mygame.ball.speed_y = mygame.ball.speed_y/-1.4
                mygame.sound_22.play()
            else:
                mygame.ball.speed_y = 0
                mygame.ball.speed_x = mygame.ball.speed_x*0.5
        
        x = mygame.ball.x
        y = mygame.ball.y
        w = mygame.ball.width
        h = mygame.ball.height
        
        pcollide = 0
        if x+w > mygame.princess.x and x < mygame.princess.x+mygame.princess.width and y+h > mygame.princess.y and y-0.5 < mygame.princess.y+mygame.princess.height:
            pcollide = 1
            if x > mygame.princess.x:
                hdist = x-mygame.princess.x
            else:
                hdist = mygame.princess.x - x
            if y > mygame.princess.y+8:
                vdist = y-8-mygame.princess.y
            else:
                vdist = mygame.princess.y+8 - y
            vdist = vdist*0.5
            if hdist > vdist:
                if x > mygame.princess.x:
                    mygame.princess.speed_x = mygame.princess.speed_x
                else:
                    mygame.princess.speed_x = mygame.princess.speed_x
            else:
                if y > mygame.princess.y+24:
                    if mygame.princess.speed_y >= 0 and mygame.ball.airborne == 0:
                        mygame.princess.y = y - mygame.princess.height
                        mygame.princess.platform = 1
                        mygame.princess.speed_y = 0
                        mygame.ball.speed_x = mygame.princess.speed_x + 0.5*time*mygame.princess.acceleration_x
                else:
                    mygame.princess.speed_y = mygame.princess.speed_y
        if x+w > mygame.cat.x and x < mygame.cat.x+mygame.cat.width and y+h > mygame.cat.y and y-0.5 < mygame.cat.y+mygame.cat.height:
            if x > mygame.cat.x:
                hdist = x-mygame.cat.x
            else:
                hdist = mygame.cat.x - x
            if y > mygame.cat.y:
                vdist = y-mygame.cat.y
            else:
                vdist = mygame.cat.y - y
            if hdist > vdist:
                if x > mygame.cat.x:
                    if pcollide == 0:
                        mygame.sound_14.play()
                        mygame.ball.speed_y = -0.05 + mygame.cat.speed_y/4.0
                    mygame.ball.speed_x = mygame.cat.speed_x / 4.0 + 0.105
                    mygame.cat.speed_x = mygame.cat.speed_x / 2.0
                    mygame.cat.x = mygame.ball.x - mygame.cat.width
                else:
                    if pcollide == 0:
                        mygame.ball.speed_y = -0.05 + mygame.cat.speed_y/4.0
                        mygame.sound_14.play()
                    mygame.ball.speed_x = mygame.cat.speed_x / 4.0 - 0.105
                    mygame.cat.speed_x = mygame.cat.speed_x / 2.0
                    mygame.cat.x = mygame.ball.x + mygame.ball.width 
            else:
                if y > mygame.cat.y:
                    mygame.cat.y = y - mygame.cat.height
                    mygame.cat.platform = 1
                    mygame.cat.speed_y = 0
                    mygame.ball.speed_x = mygame.cat.speed_x * 0.6
                else:
                    if pcollide == 0:
                        mygame.sound_22.play()
                        mygame.ball.speed_y = mygame.ball.speed_y/-1.5 + mygame.cat.speed_y/3.0 - 0.05
                    mygame.ball.speed_x = (mygame.ball.x - mygame.cat.x)/120.0
                    mygame.cat.speed_y = mygame.cat.speed_y / 4.0
                    if mygame.cat.airborne == 1:
                        mygame.cat.y = mygame.ball.y + mygame.ball.height
                    
                    
    #=====================================================================  PRINCESS MOVEMENT ===============================================================================
    if(mygame.princess_dead == 0):
        if mygame.princess.speed_y < mygame.princess.max_speed_y:
            if gamepad.up == 1 or mygame.princess.speed_y >= 0:
                mygame.princess.acceleration_y = mygame.princess.max_acceleration_y
            else:
                mygame.princess.acceleration_y = mygame.princess.max_acceleration_y*3
        else:
            mygame.princess.acceleration_y = 0
            mygame.princess.speed_y = mygame.princess.max_speed_y
            
        mygame.princess.acceleration_x = 0.0
        if mygame.princess.speed_x < -0.05:
            if gamepad.left == 1 and mygame.character == 1:
                mygame.princess.acceleration_x = -mygame.princess.max_acceleration_x
            else:
                mygame.princess.acceleration_x = mygame.princess.max_acceleration_x

        if mygame.princess.speed_x > 0.05:
            if gamepad.right == 1 and mygame.character == 1:
                mygame.princess.acceleration_x = mygame.princess.max_acceleration_x
            else:
                mygame.princess.acceleration_x = -mygame.princess.max_acceleration_x
                
        if mygame.princess.speed_x >= -0.05 and mygame.princess.speed_x <= 0.05:
            if gamepad.left == 1 and mygame.character == 1:
                mygame.princess.acceleration_x = -mygame.princess.max_acceleration_x
            if gamepad.right == 1 and mygame.character == 1:
                mygame.princess.acceleration_x = mygame.princess.max_acceleration_x
            if gamepad.left == 0 and gamepad.right == 0:
                mygame.princess.speed_x = 0
        
        walking = 0
        if gamepad.left == 1 and mygame.character == 1:          
            mygame.princess.direction = 0
            walking = 1
        if gamepad.right == 1 and mygame.character == 1:
            mygame.princess.direction = 1    
            walking = 1
        mygame.princess.animation = (mygame.princess.animation + time)*walking
            
        tile1 = int((mygame.princess.x + 0.01)/16) +                           int((mygame.princess.y + mygame.princess.height + 0.1)/16)*level.width
        tile2 = int((mygame.princess.x + mygame.princess.width - 0.01)/16) +   int((mygame.princess.y + mygame.princess.height + 0.1)/16)*level.width
        if tile1 >= 0 and tile2 < level.width*(level.height-1):
            if ((level.tilemap[tile1] >= 32 or level.tilemap[tile2] >= 32) and mygame.princess.speed_y >= 0) or mygame.princess.platform == 1:
                if mygame.princess.airborne == 1:
                    mygame.sound_19.play()
                mygame.princess.airborne = 0
                if mygame.princess.platform == 0:
                    mygame.princess.speed_y = 0
                mygame.princess.acceleration_y = 0
                mygame.princess.y = int(mygame.princess.y)
                if gamepad.jump == 1 and mygame.character == 1:
                    mygame.sound_5.play()
                    mygame.princess.speed_y = -mygame.princess.jump_speed
            else:
                mygame.princess.airborne = 1
        mygame.princess.platform = 0
                
        move_x = mygame.princess.speed_x + time*mygame.princess.acceleration_x/2.0
        if move_x > mygame.princess.max_speed_x:
            move_x = mygame.princess.max_speed_x
        if move_x < -mygame.princess.max_speed_x:
            move_x = -mygame.princess.max_speed_x        
        mygame.princess.x += time*move_x
        mygame.princess.speed_x += mygame.princess.acceleration_x*time
        if mygame.princess.speed_x > mygame.princess.max_speed_x:
            mygame.princess.speed_x = mygame.princess.max_speed_x  
        if mygame.princess.speed_x < -mygame.princess.max_speed_x:
            mygame.princess.speed_x = -mygame.princess.max_speed_x  
        collision = 1
        reset_speed = 0
        while collision != 0 and collision < 3:
            tile1 = int(mygame.princess.x + 0.01)/16 +                           level.width*(int(mygame.princess.y + 0.5)/16)
            tile2 = int(mygame.princess.x + mygame.princess.width - 0.01)/16 +   level.width*(int(mygame.princess.y + 0.5)/16)
            tile3 = int(mygame.princess.x + 0.01)/16 +                           level.width*(int(mygame.princess.y + 16)/16)
            tile4 = int(mygame.princess.x + mygame.princess.width - 0.01)/16 +   level.width*(int(mygame.princess.y + 16)/16)
            tile5 = int(mygame.princess.x + 0.01)/16 +                           level.width*(int(mygame.princess.y + mygame.princess.height - 0.01)/16)
            tile6 = int(mygame.princess.x + mygame.princess.width - 0.01)/16 +   level.width*(int(mygame.princess.y + mygame.princess.height - 0.01)/16)
            if tile1 >= 0 and tile6 < level.width*(level.height-1):
                if level.tilemap[tile1] >= 64 or level.tilemap[tile2] >= 64 or level.tilemap[tile3] >= 64 or level.tilemap[tile4] >= 64  or level.tilemap[tile5] >= 64 or level.tilemap[tile6] >= 64:
                    collision += 1
                    if(mygame.princess.speed_x > 0):
                        mygame.princess.x = float(int((mygame.princess.x + mygame.princess.width)/16)*16) - mygame.princess.width
                        reset_speed = 1
                    else:
                        if(mygame.princess.speed_x == 0):
                            mygame.princess.x = float(int((mygame.princess.x + 8.0)/16)*16)
                            reset_speed = 1
                        else:
                            mygame.princess.x = float(int((mygame.princess.x + 16)/16)*16)
                            reset_speed = 1
                else:
                    collision = 0
            else:
                collision = 0
        if collision == 3:
            mygame.princess_dead = 1
            mygame.dead = 1
        if reset_speed == 1:
            mygame.princess.speed_x = 0
        
        move_y = mygame.princess.speed_y + time*mygame.princess.acceleration_y/2.0
        if move_y > mygame.princess.max_speed_y:
            move_y = mygame.princess.max_speed_y     
        mygame.princess.y += time*move_y
        mygame.princess.speed_y += mygame.princess.acceleration_y*time
        if mygame.princess.speed_y > mygame.princess.max_speed_y:
            mygame.princess.speed_y = mygame.princess.max_speed_y    
        collision = 1
        reset_speed = 0
        while collision != 0 and collision < 3:
            tile1 = int(mygame.princess.x + 0.01)/16 +                           level.width*(int(mygame.princess.y + 0.5)/16)
            tile2 = int(mygame.princess.x + mygame.princess.width - 0.01)/16 +   level.width*(int(mygame.princess.y + 0.5)/16)
            tile3 = int(mygame.princess.x + 0.01)/16 +                           level.width*(int(mygame.princess.y + 16)/16)
            tile4 = int(mygame.princess.x + mygame.princess.width - 0.01)/16 +   level.width*(int(mygame.princess.y + 16)/16)
            tile5 = int(mygame.princess.x + 0.01)/16 +                           level.width*(int(mygame.princess.y + mygame.princess.height - 0.01)/16)
            tile6 = int(mygame.princess.x + mygame.princess.width - 0.01)/16 +   level.width*(int(mygame.princess.y + mygame.princess.height - 0.01)/16)
            if tile1 >= 0 and tile6 < level.width*(level.height-1):
                if(mygame.princess.speed_y >= 0):
                    if level.tilemap[tile1] >= 64 or level.tilemap[tile2] >= 64 or level.tilemap[tile3] >= 64 or level.tilemap[tile4] >= 64 or level.tilemap[tile5] >= 32 or level.tilemap[tile6] >= 32:
                        collision += 1
                        mygame.princess.y = float(int((mygame.princess.y + mygame.princess.height)/16)*16) - mygame.princess.height
                        reset_speed = 1
                    else:
                        collision = 0
                else:
                    if level.tilemap[tile1] >= 64 or level.tilemap[tile2] >= 64 or level.tilemap[tile3] >= 64 or level.tilemap[tile4] >= 64 or level.tilemap[tile5] >= 64 or level.tilemap[tile6] >= 64:
                        collision += 1
                        mygame.princess.y = (int(mygame.princess.y + 16)/16)*16
                        reset_speed = 1
                    else:
                        collision = 0
            else:
                collision = 0
        if collision == 3:
            mygame.princess_dead = 1
            mygame.dead = 1
        if reset_speed == 1:
            mygame.princess.speed_y = 0
    
    
    
    #=====================================================================  DRAW PRINCESS  ===============================================================================
    if(mygame.princess_dead == 0):
        if mygame.princess.airborne == 1:
            graph.draw_sprite_multi(mygame.princess.direction*256 + mygame.carrying_ball*8 + 22, mygame.princess.x, mygame.princess.y, 1, 2, graphics)
        else:
            if mygame.princess.animation == 0:
                graph.draw_sprite_multi(mygame.princess.direction*256 + mygame.carrying_ball*8 + 16, mygame.princess.x, mygame.princess.y, 1, 2, graphics)
            else:
                graph.draw_sprite_multi(mygame.princess.direction*256 + mygame.carrying_ball*8 + 18 + (int(mygame.princess.animation/100)%2)*2, mygame.princess.x, mygame.princess.y, 1, 2, graphics)
          
     
    #=====================================================================  DRAW CAT ===============================================================================
    if(mygame.cat_dead == 0):
        if mygame.cat.airborne == 1:
            graph.draw_sprite(mygame.cat.direction*256 + 3, mygame.cat.x, mygame.cat.y, graphics)
        else:
            mygame.cat.y = int(mygame.cat.y)
            if mygame.cat.animation == 0:
                graph.draw_sprite(mygame.cat.direction*256 + 0, mygame.cat.x, mygame.cat.y, graphics)
            else:
                graph.draw_sprite(mygame.cat.direction*256 + 1 + (int(mygame.cat.animation/100)%2), mygame.cat.x, mygame.cat.y, graphics)          
    
    #=====================================================================  DRAW BALL ===============================================================================
    if mygame.carrying_ball == 1:
        mygame.ball.x = mygame.princess.x
        mygame.ball.y = mygame.princess.y - 8
    frame = int((mygame.ball.animation + 1000)/12000)%3
    graph.draw_sprite(256 + 4 + frame, mygame.ball.x, mygame.ball.y, graphics)
    
    #=====================================================================  CAMERA MOVEMENT ===============================================================================
    if(1):
        if mygame.character == 0:
            if ((mygame.cat.x-152) - graphics.scroll_x ) > 1000:
                graphics.scroll_x = mygame.cat.x-152
                graphics.scroll_y = mygame.cat.y-92
            graphics.scroll_x = (graphics.scroll_x*100 + (mygame.cat.x - 152)*time)/(time + 100)
            if graphics.scroll_x < 0:
                graphics.scroll_x = 0
            graphics.scroll_y = (graphics.scroll_y*100 + (mygame.cat.y - 92)*time)/(time + 100)
            if graphics.scroll_y < 0:
                graphics.scroll_y = 0
        if mygame.character == 1:
            if ((mygame.princess.x-152) - graphics.scroll_x ) > 1000:
                graphics.scroll_x = mygame.princess.x-152
                graphics.scroll_y = mygame.princess.y-92
            graphics.scroll_x = (graphics.scroll_x*100 + (mygame.princess.x - 152)*time)/(time + 100)
            if graphics.scroll_x < 0:
                graphics.scroll_x = 0
            graphics.scroll_y = (graphics.scroll_y*100 + (mygame.princess.y - 92)*time)/(time + 100)
            if graphics.scroll_y < 0:
                graphics.scroll_y = 0
    
    #=====================================================================  object_ SPAWN, CAT ===============================================================================
    if(1):
        if mygame.fill_all == 1:
            i = -level.spawn_distance_x
            while i <= level.spawn_distance_x:
                i2 = -level.spawn_distance_y
                while i2 <= level.spawn_distance_y:
                    tile =  i + int(mygame.cat.x/16) + level.width*(int(mygame.cat.y/16) + i2)
                    if tile >= 0 and tile < level.width*level.height:
                        object__type = level.object_[tile]
                        if object__type != 0:
                            add_object_(object__type, (i + int(mygame.cat.x/16))*16, (int(mygame.cat.y/16) + i2)*16, level.width, mygame, 1)
                    i2 += 1
                i += 1
        else:
            if mygame.cat.speed_y < 0:
                i = -level.spawn_distance_x
                i2 = -level.spawn_distance_y
                while i <= level.spawn_distance_x:
                    tile =  i + int(mygame.cat.x/16) + level.width*(int(mygame.cat.y/16) + i2)
                    if tile >= 0 and tile < level.width*level.height:
                        object__type = level.object_[tile]
                        if object__type != 0:
                            add_object_(object__type, (i + int(mygame.cat.x/16))*16, (int(mygame.cat.y/16) + i2)*16, level.width, mygame, 1)
                    i += 1
            if mygame.cat.speed_y > 0:
                i = -level.spawn_distance_x
                i2 = level.spawn_distance_y
                while i <= level.spawn_distance_x:
                    tile =  i + int(mygame.cat.x/16) + level.width*(int(mygame.cat.y/16) + i2)
                    if tile >= 0 and tile < level.width*level.height:
                        object__type = level.object_[tile]
                        if object__type != 0:
                            add_object_(object__type, (i + int(mygame.cat.x/16))*16, (int(mygame.cat.y/16) + i2)*16, level.width, mygame, 1)
                    i += 1
            if mygame.cat.speed_x < 0:
                i = -level.spawn_distance_x
                i2 = -level.spawn_distance_y
                while i2 <= level.spawn_distance_y:
                    tile =  i + int(mygame.cat.x/16) + level.width*(int(mygame.cat.y/16) + i2)
                    if tile >= 0 and tile < level.width*level.height:
                        object__type = level.object_[tile]
                        if object__type != 0:
                            add_object_(object__type, (i + int(mygame.cat.x/16))*16, (int(mygame.cat.y/16) + i2)*16, level.width, mygame, 1)
                    i2 += 1
            if mygame.cat.speed_x > 0:
                i = level.spawn_distance_x
                i2 = -level.spawn_distance_y
                while i2 <= level.spawn_distance_y:
                    tile =  i + int(mygame.cat.x/16) + level.width*(int(mygame.cat.y/16) + i2)
                    if tile >= 0 and tile < level.width*level.height:
                        object__type = level.object_[tile]
                        if object__type != 0:
                            add_object_(object__type, (i + int(mygame.cat.x/16))*16, (int(mygame.cat.y/16) + i2)*16, level.width, mygame, 1)
                    i2 += 1
                
    
    #=====================================================================  object_ SPAWN, PRINCESS ===============================================================================
    if(1):
        if mygame.fill_all == 1:
            i = -level.spawn_distance_x
            while i <= level.spawn_distance_x:
                i2 = -level.spawn_distance_y
                while i2 <= level.spawn_distance_y:
                    tile =  i + int(mygame.princess.x/16) + level.width*(int(mygame.princess.y/16) + i2)
                    if tile >= 0 and tile < level.width*level.height:
                        object__type = level.object_[tile]
                        if object__type != 0:
                            add_object_(object__type, (i + int(mygame.princess.x/16))*16, (int(mygame.princess.y/16) + i2)*16, level.width, mygame, 1)
                    i2 += 1
                i += 1
        else:
            if mygame.princess.speed_y < 0:
                i = -level.spawn_distance_x
                i2 = -level.spawn_distance_y
                while i <= level.spawn_distance_x:
                    tile =  i + int(mygame.princess.x/16) + level.width*(int(mygame.princess.y/16) + i2)
                    if tile >= 0 and tile < level.width*level.height:
                        object__type = level.object_[tile]
                        if object__type != 0:
                            add_object_(object__type, (i + int(mygame.princess.x/16))*16, (int(mygame.princess.y/16) + i2)*16, level.width, mygame, 1)
                    i += 1
            if mygame.princess.speed_y > 0:
                i = -level.spawn_distance_x
                i2 = level.spawn_distance_y
                while i <= level.spawn_distance_x:
                    tile =  i + int(mygame.princess.x/16) + level.width*(int(mygame.princess.y/16) + i2)
                    if tile >= 0 and tile < level.width*level.height:
                        object__type = level.object_[tile]
                        if object__type != 0:
                            add_object_(object__type, (i + int(mygame.princess.x/16))*16, (int(mygame.princess.y/16) + i2)*16, level.width, mygame, 1)
                    i += 1
            if mygame.princess.speed_x < 0:
                i = -level.spawn_distance_x
                i2 = -level.spawn_distance_y
                while i2 <= level.spawn_distance_y:
                    tile =  i + int(mygame.princess.x/16) + level.width*(int(mygame.princess.y/16) + i2)
                    if tile >= 0 and tile < level.width*level.height:
                        object__type = level.object_[tile]
                        if object__type != 0:
                            add_object_(object__type, (i + int(mygame.princess.x/16))*16, (int(mygame.princess.y/16) + i2)*16, level.width, mygame, 1)
                    i2 += 1
            if mygame.princess.speed_x > 0:
                i = level.spawn_distance_x
                i2 = -level.spawn_distance_y
                while i2 <= level.spawn_distance_y:
                    tile =  i + int(mygame.princess.x/16) + level.width*(int(mygame.princess.y/16) + i2)
                    if tile >= 0 and tile < level.width*level.height:
                        object__type = level.object_[tile]
                        if object__type != 0:
                            add_object_(object__type, (i + int(mygame.princess.x/16))*16, (int(mygame.princess.y/16) + i2)*16, level.width, mygame, 1)
                    i2 += 1

    mygame.fill_all = 0
    
    #=====================================================================  object_S ===============================================================================
    if(1):
        i = 0
        i2 = 0
        temp = mygame.object_s
        while i < temp:
            while mygame.object__on[i2] == 0:
                i2 += 1
            move_object_(i2, time, mygame, level, graphics)
            i += 1
            i2 += 1
    
def game(mygame, level, graphics):
    clock = pygame.time.Clock()
    f = data.load("sprites.png")
    graph.load_spriteset(f, graphics)
    path = data.filepath("prismtrap.it")
    pygame.mixer.music.load(path)
    pygame.mixer.music.play(-1, 0)
    
    i=0
    game_quit = 0
    gamepad = gamepad_data()
    mygame.fill_all = 1
    ticks = pygame.time.get_ticks()
    random.seed()
    next = "menu"
    while game_quit == 0:
        clock.tick() #SQ-parameter should be 60 when not optimizing, changed to 0 for now
        print clock.get_fps() # FPS computed by averaging the last few calls to Clock.tick
        time = pygame.time.get_ticks() - ticks
        if time > 50:
            time = 50
        mygame.time = time
        ticks = pygame.time.get_ticks()
        pygame.event.pump()
        keys = pygame.key.get_pressed()
        if(keys[pygame.K_ESCAPE] == 1):
            game_quit = 1
        gamepad.left = keys[pygame.K_LEFT]
        if gamepad.left == 0:
            gamepad.right = keys[pygame.K_RIGHT]
        else:
            gamepad.right = 0;
        gamepad.up = keys[pygame.K_UP] or keys[pygame.K_LCTRL]
        gamepad.down = keys[pygame.K_DOWN]
        if keys[pygame.K_SPACE] and gamepad.toggle != 0:
            gamepad.toggle = 2
        else:
            gamepad.toggle = keys[pygame.K_SPACE]
        if (keys[pygame.K_UP] or keys[pygame.K_LCTRL]) and gamepad.jump != 0:
            gamepad.jump = 2
        else:
            gamepad.jump = keys[pygame.K_UP] or keys[pygame.K_LCTRL]

        if (keys[pygame.K_LALT] or keys[pygame.K_x]) and gamepad.throw != 0:
            gamepad.throw = 2
        else:
            gamepad.throw = keys[pygame.K_LALT] or keys[pygame.K_x]      

        if mygame.cat.x < 256 or mygame.princess.x < 256:
            game_quit = 1
            next = "win"
            
        step(time, gamepad, mygame, level, graphics)

        graph.draw_screen(graphics)
        pygame.time.wait(1)
        i += 1
    pygame.mixer.music.stop()
    return next
