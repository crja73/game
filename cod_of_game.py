import pygame
import os
import random
from os import path
import sys
import PyQt5
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from random import randrange

playing = False
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
snd_dir = path.join(path.dirname(__file__), 'data')
shoot_sound = pygame.mixer.Sound(path.join(snd_dir, 'pew.wav'))
shoot_sound2 = pygame.mixer.Sound(path.join(snd_dir, 'pew paw.wav'))
shoot_sound3 = pygame.mixer.Sound(path.join(snd_dir, 'the_vagabond.wav'))
health = 100
black = [0, 0, 0]


class MyWidget(QMainWindow):

	def __init__(self):
		super().__init__()
		uic.loadUi('меню.ui', self)
		self.pixmap = QPixmap('лул3.jpg')
		self.back.setPixmap(self.pixmap)

		shoot_sound3.play()
		self.pushButton.clicked.connect(self.Ruls)
		self.pushButton_2.clicked.connect(self.play)
		self.pushButton_3.clicked.connect(self.results)
		self.pushButton_4.clicked.connect(self.lvl)
		self.pushButton_5.clicked.connect(self.end)


		self.present_coin()

	def present_coin(self):
		self.pixmap = QPixmap('moneyka.png')
		self.label_coin.setPixmap(self.pixmap)
		self.pushButton_2.setStyleSheet('QPushButton {background-color: #31adff}')
		self.pushButton_3.setStyleSheet('QPushButton {background-color: #31adff}')
		self.pushButton.setStyleSheet('QPushButton {background-color: #31adff}')
		self.pushButton_4.setStyleSheet('QPushButton {background-color: #31adff}')
		self.pushButton_5.setStyleSheet('QPushButton {background-color: #31adff}')
		with open('монеты.txt', 'r') as lines:
			for o in lines:
				self.coinss = int(o)
				self.label_coin2.setText(str(self.coinss))


	def Ruls(self):
		self.second_form = SecondForm()
		self.second_form.show()

	def lvl(self):
		self.fifth_form = FifthForm()
		self.fifth_form.show()

	def play(self):
		playing = True
		print(playing)
		self.fourth_form = FourthForm(playing)
		self.fourth_form.show()

	def results(self):
		self.third_form = ThirdForm()
		self.third_form.show()

	def end(self):
		sys.exit()


class SecondForm(QMainWindow):
	def __init__(self):
		super().__init__()
		uic.loadUi('правила.ui', self)

class FifthForm(QMainWindow):
	def __init__(self):
		super().__init__()
		uic.loadUi('levels.ui', self)
		self.pushButton_h.setStyleSheet('QPushButton {background-color: #b32828}')
		self.pushButton_s.setStyleSheet('QPushButton {background-color: #b32828}')
		self.pushButton_n.setStyleSheet('QPushButton {background-color: #b32828}')

		self.pushButton_h.clicked.connect(self.lvvl)
		self.pushButton_s.clicked.connect(self.lvvl)
		self.pushButton_n.clicked.connect(self.lvvl)
	
	def lvvl(self):
		global health
		heath = 0
		level = self.sender().text()
		if level == 'SIMPLE':
			health = 100
		elif level == 'NORMAL':
			health = 50
		elif level == 'HARD':
			health = 10


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

		health2 = health
		print(health2)
		if playing == True:
			BLUE = (0, 0, 0)
			pygame.init()
			size = width, height = 550, 650
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
					

			all_sprites = pygame.sprite.Group()
			tiles_group = pygame.sprite.Group()
			dragon_group = pygame.sprite.Group()


			Tile(tiles_group)
			Bird(all_sprites)
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
			star_list = []

			for i in range(500):
				xs = random.randrange(0, 550)
				ys = random.randrange(0, 650)
				star_list.append([xs, ys, 2])
			clock = pygame.time.Clock()



			running = True
			while running:

				font = pygame.font.Font(None, 60)
				all_sprites.update([x, y])  

				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						shoot_sound3.play()
						running = False
						playing = False
				
				x_pos -= 5
				tiles_group.update([x_pos, y_pos])
				if x_pos < -110:
					x_pos = 550
					y_pos = 500
				
				xd -= 4
				dragon_group.update([xd, yd])
				if xd < - 220:
					xd = 550
					yd = 200


				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE:    # это проверка на нажатие пробела
					    jump_flag = True      
					    count_jump = 15
					    shoot_sound.play()
					if event.key == pygame.K_UP:
						pygame.draw.rect(screen, (255, 150, 0), [230, 280, 20, 100], 0)
						pygame.draw.rect(screen, (255, 150, 0), [270, 280, 20, 100], 0)
						pygame.display.flip()
						pause = True
						while pause:
							for event in pygame.event.get():
								if event.type == pygame.QUIT:
									pause = False
							if event.type == pygame.KEYDOWN:
								if event.key == pygame.K_RETURN:
									pause = False
						
	

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
					health2 -= 1
				if y in diaposon_of_mob2 and (x + 65 >= xd and x <= (xd + 100)):
					health2 -= 1
				if y == 550:
					health2 -= 1
				if y < -100:
					health2 -= 1



				if x == x_pos or x == x_pos + 1 or x == x_pos - 1:
					count_coins += 1

				if health2 <= 0:
					running = False

				screen.fill(BLUE)

				for star in star_list:
					pygame.draw.circle(screen, (255, 255, 255), star[0:2], 2)
					star[0] -= star[2]
					if star[0] < 0:
					 	star[0] = random.randrange(width, width + 200)
					 	star[1] = random.randrange(0, 650)

				screen.blit(font.render('Coins: {}'.format(count_coins), 1, (180, 180, 0)), (20, 20))
				screen.blit(font.render('Health: {}'.format(health2), 1, (180, 180, 0)), (320, 20))
				all_sprites.draw(screen)
				tiles_group.draw(screen)
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