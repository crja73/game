import pygame
import os
import random


BLUE = (0, 0, 255)

pygame.init()
size = width, height = 900, 650
screen = pygame.display.set_mode(size)
screen.fill(BLUE)
x = 300
y = 300

def load_image(name, colorkey=None, color_key=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


class Bird(pygame.sprite.Sprite):
    image = load_image("new_bird.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = Bird.image
        self.rect = self.image.get_rect()
        self.speed = -10.5
        self.count = 0

    def update(self, event):
        self.rect.x = event[0]
        self.rect.y = event[1]



all_sprites = pygame.sprite.Group()
Bird(all_sprites)
count_jump = 10
jump_flag = False

keys = pygame.key.get_pressed()
running = True
while running:
    all_sprites.update([x, y])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if jump_flag == False:
        if event.type == pygame.KEYDOWN:
        	if event.key == pygame.K_SPACE:
        		jump_flag = True
    else:
    	if count_jump >= -10:
    		if count_jump < 0:
    			y += ((count_jump ** 2) / 2)
    		else:
    		    y -= (count_jump ** 2) / 2
    		count_jump -= 1
    		all_sprites.update([x, y])
    	else:
    		jump_flag = False
    		count_jump = 10

        
            
    screen.fill(BLUE)
    all_sprites.draw(screen)
    pygame.display.flip()
    pygame.time.wait(20)