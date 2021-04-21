# LIBRARIES
import pygame
import random, os

# FILES
import room_rules

# PYGAME PATTERN 
pygame.init()

# параметры окна программы
RES = 900, 630
sc = pygame.display.set_mode(RES)
pygame.display.set_caption('Adventure Atari 2600')

# логотип и fps
icon = pygame.image.load('logo.png')
pygame.display.set_icon(icon)
fps = pygame.time.Clock()

# загрузка карты по плану [room_pic, color_of_walls]
#         0  1   2   3   4   5   6
rooms = [[0, [], [], [], [], [], []], #  0 
		 [0, [], [], [], [], [], []], #  1
		 [0, [], [], [], [], [], []], #  2
		 [0, [], [], [], [], [], []], #  3
		 [0, [], [], [], [], [], []], #  4
		 [0, [], [], [], [pygame.image.load('assets/rooms/04_05.png'), (192, 204,  13)], [], []], #  5
		 [0, [], [], [], [pygame.image.load('assets/rooms/04_06.png'), ( 73, 183,  16)], [pygame.image.load('assets/rooms/05_06.png'), (197, 141,  17)], []], #  6
		 [0, [], [], [], [pygame.image.load('assets/rooms/04_07.png'), (237,  72,  45)], [], []], #  7
		 [0, [], [], [], [pygame.image.load('assets/rooms/04_08.png'), (237,  72,  45)], [], []], #  8
		 [0, [], [], [], [pygame.image.load('assets/rooms/04_09.png'), (223, 222, 228)], [], []], #  9 
		 [0, [], [], [], [pygame.image.load('assets/rooms/04_10.png'), ( 73, 183,  16)], [], []], # 10
		 [0, [], [], [], [pygame.image.load('assets/rooms/04_11.png'), (  9, 181, 137)], [], []]] # 11


rules = room_rules.rules
sounds = {'pick_up': pygame.mixer.music.load('assets/sounds/pick-up.mp3'),
		  'put_down': pygame.mixer.music.load('assets/sounds/put-down.mp3'),
		  'moving_down': pygame.mixer.music.load('assets/sounds/moving_down.mp3'),
		  'boom': pygame.mixer.music.load('assets/sounds/boom.mp3'),
		  'final': pygame.mixer.music.load('assets/sounds/final_theme.mp3')}

# оружие игрока
class Weapon:
	def __init__(self, scene, texture, x, y, room):
		self.scene, self.texture, self.x, self.y, self.room = scene, texture, x, y, room

		# в инвентаре / расстояние по х / расстояние по у
		self.taken = [False, 0, 0]

# ключ от ворот
class Key:
	def __init__(self, scene, texture, x, y, room):
		pass

# мост сквозь стены
class Bridge:
	def __init__(self, scene, texture, x, y, room):
		pass

# монстр-дракон
class Dragon:
	def __init__(self, scene, texture, x, y, room):
		pass
# монстр - мышь
class Bat:
	def __init__(self, scene, texture, x, y, room):
		pass

# игрок
class MainCharacter: 
	def __init__(self, scene, x, y, room):
		self.scene = scene
		self.x = x
		self.y = y
		self.room = room
		self.size = (25, 25)

		self.inventory = []

		# создание меча
		sword_texture = pygame.image.load('assets/textures/sword.png')
		self.sword = Weapon(sc, sword_texture, 150, 490, [4, 5])

	# отрисовка комнаты, персонажа, мобов и предметов
	def draw_env(self):
		# комната
		self.scene.blit(rooms[self.room[1]][self.room[0]][0], (0, 0))

		# меч
		if (self.sword.taken[0]):
			self.scene.blit(self.sword.texture, (self.x + self.sword.taken[1], self.y + self.sword.taken[2]))

		else:
			if (self.sword.room == self.room):
				self.scene.blit(self.sword.texture, (self.sword.x, self.sword.y))

		# персонаж
		pygame.draw.rect(self.scene, rooms[self.room[1]][self.room[0]][1], (self.x, self.y, self.size[0], self.size[1]))


	def move(self):
		"""ПЕРЕМЕЩЕНИЕ ПО ПОЛЮ КОМНАТЫ"""

		speed = 2    
		keys = pygame.key.get_pressed()

		# если передвижение на 2 невозможно, двигаемся на 1
		if keys[pygame.K_a]:
			for element in rules[self.room[1]][self.room[0]]['space']:
				if (self.x - 2 in element['x']):
					if (self.y in element['y']) and (self.y + 24 in element['y']):
						self.x -= speed
						break

				elif (self.x - 1 in element['x']):
					if (self.y in element['y']) and (self.y + 24 in element['y']):
						self.x -= (speed - 1)
						break

		if keys[pygame.K_d]:
			for element in rules[self.room[1]][self.room[0]]['space']:
				if (self.x + 26 in element['x']):
					if (self.y in element['y']) and (self.y + 24 in element['y']):
						self.x += speed
						break

				elif (self.x + 25 in element['x']):
					if (self.y in element['y']) and (self.y + 24 in element['y']):
						self.x += (speed - 1)
						break

		if keys[pygame.K_w]:
			for element in rules[self.room[1]][self.room[0]]['space']:
				if (self.y - 2 in element['y']):
					if (self.x in element['x']) and (self.x + 24 in element['x']):
						self.y -= speed
						break

				elif (self.y - 1 in element['y']):
					if (self.x in element['x']) and (self.x + 24 in element['x']):
						self.y -= (speed - 1)
						break

		if keys[pygame.K_s]:
			for element in rules[self.room[1]][self.room[0]]['space']:
				if (self.y + 26 in element['y']):
					if (self.x in element['x']) and (self.x + 24 in element['x']):
						self.y += speed
						break

				elif (self.y + 25 in element['y']):
					if (self.x in element['x']) and (self.x + 24 in element['x']):
						self.y += (speed - 1)
						break


	def check_new_room(self):
		"""ПРОВЕРКА НА ПЕРЕХОД В НОВУЮ КОМНАТУ"""

		# появление на новых координатах в новой комнате, исходя из типа перемещения
		self.teleport = {'up':    {'x': self.x, 'y': 600}, 
						 'down':  {'x': self.x, 'y': 5}, 
						 'left':  {'x': 975,    'y': self.y}, 
						 'right': {'x': 5,      'y': self.y}}

		for element in rules[self.room[1]][self.room[0]]['exits']:
			if (self.x in element['x']) and (self.y in element['y']):
				self.room = element['room']
				self.x, self.y = self.teleport[element['mode']]['x'], self.teleport[element['mode']]['y']
				print(self.x, self.y)


	def control(self):
		pass

	def using_inventory(self):
		keys = pygame.key.get_pressed()
		# print(keys)
		if (keys[pygame.K_SPACE]):

			# если меч взят в руки
			if (self.sword.taken[0]):
				sounds['put_down'].play()
				self.sword.x = self.x + self.sword.taken[1]
				self.sword.y = self.y + self.sword.taken[2]
				self.sword.taken = [False, 0, 0]
				self.sword.room = self.room
				pygame.time.delay(300)

			# если меч не взят, но хотим взять
			else:
				if (self.sword.room == self.room):
					if (self.x in range(self.sword.x - 35, self.sword.x + 100)) and (self.y in range(self.sword.y - 35, self.sword.y + 75)):
						self.sword.taken = [True, self.sword.x - self.x, self.sword.y - self.y]
						pygame.time.delay(300)


# ============== #
#  ГЛАВНЫЙ ЦИКЛ  #
# ============== #
def run_game():
	global sc
	game = True

	# начальный экран с цифрой "3" <--------------- изменить на комнату с тройкой
	start_screen = pygame.image.load('logo.png')
	sc.blit(start_screen, (0, 0))
	pygame.time.delay(2000)

	# создание персонажа
	cube = MainCharacter(sc, 435, 500, [4, 5])

	while game:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()

		# sc.blit(main_room, (0, 0))
		
		cube.draw_env()
		cube.move()
		cube.check_new_room()
		cube.using_inventory()

		print(cube.x, cube.y, cube.room)
		
		fps.tick(1000)
		pygame.display.update()

run_game()