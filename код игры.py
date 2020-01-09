import pygame
import os
import random


BLUE = (0, 0, 255)

pygame.init()
size = width, height = 450, 650
screen = pygame.display.set_mode(size)
screen.fill(BLUE)
x = 0
y =550


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

def load_image3(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert_alpha()
    if colorkey is not None:
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image

def load_image4(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert_alpha()
    if colorkey is not None:
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def load_level(filename):
    filename = "data/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    # и подсчитываем максимальную длину    
    max_width = max(map(len, level_map))

    # дополняем каждую строку пустыми клетками ('.')    
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


class Tile(pygame.sprite.Sprite):
	image = load_image2('огр.png')

	def __init__(self, group):
		super().__init__(group)
		self.image = Tile.image
		self.rect = self.image.get_rect()
		self.mask = pygame.mask.from_surface(self.image)


	def update(self, event):
		self.rect.x = event[0]
		self.rect.y = event[1]

class Dragon(pygame.sprite.Sprite):
	image = load_image4('дракончик.png')

	def __init__(self, group):
		super().__init__(group)
		self.image = Dragon.image
		self.rect = self.image.get_rect()

	def update(self, event):
		self.rect.x = event[0]
		self.rect.y = event[1]



class Bird(pygame.sprite.Sprite):
    image = load_image("new_geralt.png")

    def __init__(self, group):
        super().__init__(group)
        self.count_jump = 15
        self.jump_flag = False
        self.image = Bird.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)


    def update(self, event):
    	if not pygame.sprite.collide_mask(self, tile):
    		self.rect.x = event[0]
    		self.rect.y = event[1]
    		if self.count_jump >= -15:
    			self.rect.y -= self.count_jump / 2
    			self.count_jump -= 1
    		else: 
    			if self.rect.y < 550:   
    				self.rect.y = min(550, (self.rect.y - self.count_jump / 2))
    				self.count_jump -= 1
    			else:
    				self.count_jump = 15  
    				self.jump_flag = False

    		


class Bullet(pygame.sprite.Sprite):
	image = load_image3('bullet.png')

	def __init__(self, group):
		super().__init__(group)
		self.image = Bullet.image
		self.rect = self.image.get_rect()

	def update(self, event):
		self.rect.x = event[0]
		self.rect.y = event[1]


all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
bullets = pygame.sprite.Group()
dragon_group = pygame.sprite.Group()

Tile(tiles_group)
Bird(all_sprites)
Bullet(bullets)
Dragon(dragon_group)
tile = Tile(tiles_group)



diaposon_of_mob = []
diaposon_of_mob_x = []
for i in range(420, 650):
	diaposon_of_mob.append(i)
for j in range(50, 150):
	diaposon_of_mob_x.append(j)
x_pos = 450
y_pos = 500
xd = 450
yd = 200
height = []
bullet_flag = False
simple_flag = False

x2 = x

running = True
while running: #генрацию препятствий можно сделать с помощью чтения из файла
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	x_pos -= 2    #это движение припятствия
	tiles_group.update([x_pos, y_pos])
	if x_pos < -110:
		x_pos = 400
		y_pos = 500
	xd -= 2
	dragon_group.update([xd, yd])
	if xd < - 220:
		xd = 450
		yd = 200
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_SPACE:    # это проверка на нажатие пробела
		    all_sprites.update([x, y])
		elif event.key == pygame.K_UP:
			y2 = y
			x2 = x + 50
			bullet_flag = True
	



	if bullet_flag:
		x2 += 1
		bullets.update([x2, y2])
		 

	screen.fill(BLUE)
	all_sprites.draw(screen)
	tiles_group.draw(screen)
	bullets.draw(screen)
	dragon_group.draw(screen)
	pygame.display.flip()
	pygame.time.wait(8)   #обновляем экран и ставим подходящую скорость