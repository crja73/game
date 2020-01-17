import pygame
import os
import random
from os import path
import sys
import PyQt5
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from PyQt5.QtGui import QPixmap


playing = False

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
snd_dir = path.join(path.dirname(__file__), 'data')
shoot_sound = pygame.mixer.Sound(path.join(snd_dir, 'pew.wav'))
shoot_sound2 = pygame.mixer.Sound(path.join(snd_dir, 'pew paw.wav'))

class MyWidget(QMainWindow):
	def __init__(self):
		super().__init__()
		uic.loadUi('меню.ui', self)

		self.pushButton.clicked.connect(self.Ruls)
		self.pushButton_2.clicked.connect(self.play)
		self.pushButton_3.clicked.connect(self.results)

		self.present_coin()

	def present_coin(self):
		self.pixmap = QPixmap('wolf2.png')
		self.back.setPixmap(self.pixmap)
		self.pixmap = QPixmap('moneyka.png')
		self.label_coin.setPixmap(self.pixmap)
		self.pushButton_2.setStyleSheet('QPushButton {background-color: #b32828}')
		self.pushButton_3.setStyleSheet('QPushButton {background-color: #b32828}')
		self.pushButton.setStyleSheet('QPushButton {background-color: #b32828}')
		with open('монеты.txt', 'r') as lines:
			for o in lines:
				self.coinss = int(o)
				self.label_coin2.setText(str(self.coinss))


	def Ruls(self):
		self.second_form = SecondForm()
		self.second_form.show()

	def play(self):
		playing = True
		print(playing)
		self.fourth_form = FourthForm(playing)
		self.fourth_form.show()

	def results(self):
		self.third_form = ThirdForm()
		self.third_form.show()

class SecondForm(QMainWindow):
	def __init__(self):
		super().__init__()
		uic.loadUi('правила.ui', self)

class ThirdForm(QMainWindow):
	def __init__(self):
		super().__init__()
		uic.loadUi('results.ui', self)
		w = open('результаты.txt', 'r')
		lines = w.readlines()
		self.label.setText('\n'.join(lines))

class FourthForm(QMainWindow):
	def __init__(self, arg):
		super().__init__()
		playing = arg

		if playing == True:
			BLUE = (0, 0, 255)
			pygame.init()
			size = width, height = 450, 650
			screen = pygame.display.set_mode(size)
			screen.fill(BLUE)
			x = 0
			y =549

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
			   

			class Bird(pygame.sprite.Sprite):
			    image = load_image("new_geralt.png")
			    
			    def __init__(self, group):
			    	super().__init__(group)
			    	self.image = Bird.image
			    	self.rect = self.image.get_rect()
			    	self.mask = pygame.mask.from_surface(self.image)


			    def update(self, event):
			    	self.rect.x = event[0]
			    	self.rect.y = event[1]

			all_sprites = pygame.sprite.Group()
			bird = Bird(all_sprites)

			class Dragon(pygame.sprite.Sprite):
				image = load_image4('дракон.png')

				def __init__(self, group):
					super().__init__(group)
					self.image = Dragon.image
					self.rect = self.image.get_rect()
					self.mask = pygame.mask.from_surface(self.image)

				def update(self, event):
					self.rect.x = event[0]
					self.rect.y = event[1]
					

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
			count_jump = 15
			jump_flag = False
			diaposon_of_mob = []
			for i in range(420, 650):
				diaposon_of_mob.append(i)
			diaposon_of_mob2 = []
			for i in range(140, 300):
				diaposon_of_mob2.append(i)
			x_pos = 450
			y_pos = 500
			xd = 450
			yd = 200
			height = []
			bullet_flag = False
			simple_flag = False
			count_coins = 0

 

			running = True
			while running:
				all_sprites.update([x, y])  #генрацию препятствий можно сделать с помощью чтения из файла
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						running = False
				x_pos -= 3    #это движение припятствия
				tiles_group.update([x_pos, y_pos])
				if x_pos < -110:
					x_pos = 400
					y_pos = 500
				xd -= 4
				dragon_group.update([xd, yd])
				if xd < - 220:
					xd = 450
					yd = 200
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE:    # это проверка на нажатие пробела
					    jump_flag = True      
					    count_jump = 15
					    shoot_sound.play()
					if event.key == pygame.K_UP:
						bullet_flag = True
						y2 = y + 50
						x2 = x + 50
						shoot_sound2.play()
	

				if jump_flag == True:
					if count_jump >= -15:
						y -= count_jump / 2
						count_jump -= 1
					else: 
						if y < 550:   
							y = min(550, (y - count_jump / 2))
							count_jump -= 1
						else:
							count_jump = 15  
							jump_flag = False
							shoot_sound.play()

				if y in diaposon_of_mob and (x + 90 >= x_pos and x <= (x_pos + 75)):
					running = False
					print('game over')
				if y in diaposon_of_mob2 and (x + 65 >= xd and x <= (xd + 100)):
					running = False
				if y == 550:
					running = False
				if y < -100:
					running = False

				if bullet_flag:
					x2 += 1 
					bullets.update([x2, y2])


				if x == x_pos or x == x_pos + 1 or x == x_pos - 1:
					count_coins += 1
					 

				screen.fill(BLUE)
				all_sprites.draw(screen)
				tiles_group.draw(screen)
				bullets.draw(screen)
				dragon_group.draw(screen)
				pygame.display.flip()
				pygame.time.wait(8)   #обновляем экран и ставим подходящую скорость

			coins2 = 0
			with open('монеты.txt', 'r') as lines:
				for o in lines:
					coins2 = int(o)

			g = open('результаты.txt', 'a') 
			g.write('очков за игру: {} \n'.format(str(count_coins)))

			f = open('монеты.txt', 'r+')
			f.truncate()
			f = open('монеты.txt', 'a')
			count_coins += coins2
			f.write(str(count_coins))
			f.close()
			pygame.quit()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = MyWidget()
	ex.show()
	sys.exit(app.exec())