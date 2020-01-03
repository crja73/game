import pygame
import os
import random


BLUE = (0, 0, 255)

pygame.init()
size = width, height = 900, 650
screen = pygame.display.set_mode(size)
screen.fill(BLUE)
x = 0
y =550
x2 = 0
y2 = 500

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert_alpha()
    if colorkey is not None:
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image

def load_image2(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert_alpha()
    if colorkey is not None:
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image

class Tile(pygame.sprite.Sprite):
	image = load_image2('препятствие 1.2.png')
	def __init__(self, group):
		super().__init__(group)
		self.image = Tile.image
		self.rect = self.image.get_rect()

	def update(self, event):
		self.rect.x = event[0]

class Bird(pygame.sprite.Sprite):
    image = load_image("new_geralt.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = Bird.image
        self.rect = self.image.get_rect()

    def update(self, event):
        self.rect.x = event[0]
        self.rect.y = event[1]


all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()

Tile(tiles_group)
Bird(all_sprites)
count_jump = 20
jump_flag = False

x_pos = 800
y_pos = 500

running = True
while running:
    all_sprites.update([x, y])
    tiles_group.update([x_pos, y_pos])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    x_pos -= 1
    tiles_group.update([x_pos])
    if event.type == pygame.KEYDOWN:    
        if event.key == pygame.K_SPACE:    # это проверка на нажатие пробела
        	jump_flag = True      #объявляем прыжок и ставим коэфициент ускорения прыжка на максимум
        	count_jump = 20
    if jump_flag == True:   #если флаг истенен, а знчит мы нажали на пробел, то мы совершаем прыжок
    	if count_jump >= -20:
    		y -= count_jump / 2   #эти две строчки описывают прыжок вверх, без возвращения назад
    		count_jump -= 1       #они нужны для того, чтобы прожок был не резким, а поавным и с ускорением
    	else:
    		if y < 550:    #это проверка на положоние спрайта относительно земли
    			y = min(550, (y - count_jump / 2))   #эти строчки возвращают птицу строго на замлю, птица всегда будет стремиться падать на землю
    			count_jump -= 1
    		else:
    			count_jump = 20   #если мы все же приземлились на землю, то коэфициент становится прежним, а режим прыжка отменяется
    			jump_flag = False
 
    screen.fill(BLUE)
    all_sprites.draw(screen)
    tiles_group.draw(screen)
    pygame.display.flip()
    pygame.time.wait(10)   #обновляем экран и ставим подходящую скорость