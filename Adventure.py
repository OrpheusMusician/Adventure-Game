import pygame
import random, os

pygame.init()

RES = 900, 630
sc = pygame.display.set_mode(RES)
pygame.display.set_caption('Adventure Atari 2600')

icon = pygame.image.load('logo.png')
pygame.display.set_icon(icon)


fps = pygame.time.Clock()

# [room_pic, color_of_walls]
#         0  1   2   3   4   5   6
rooms = [[0, [], [], [], [], [], []], #  0 
		 [0, [], [], [], [], [], []], #  1
		 [0, [], [], [], [], [], []], #  2
		 [0, [], [], [], [], [], []], #  3
		 [0, [], [], [], [], [], []], #  4
		 [0, [], [], [], [pygame.image.load('assets/rooms/04_05.png'), (255, 255, 255)], [], []], #  5
		 [0, [], [], [], [], [], []], #  6
		 [0, [], [], [], [], [], []], #  7
		 [0, [], [], [], [], [], []], #  8
		 [0, [], [], [], [], [], []], #  9 
		 [0, [], [], [], [], [], []], # 10
		 [0, [], [], [], [pygame.image.load('assets/rooms/04_11.png'), (  9, 181, 137)], [], []]] # 11

main_room = pygame.image.load('assets/rooms/04_05.png')

# игрок
class MainCharacter:
	# добавить правила положения в данной комнате 
	def __init__(self, scene, x = 450, y = 420, room = [0, 1]):
		self.scene = scene
		self.x = x
		self.y = y
		self.room = room

		self.size = (25, 25) 

	def check_color(self):
		pass

	def draw_room(self):
		self.scene.blit(rooms[self.room[1]][self.room[0]][0], (0, 0))
		pygame.draw.rect(self.scene, rooms[self.room[1]][self.room[0]][1], (self.x, self.y, self.size[0], self.size[1]))

		sw = pygame.image.load('assets/textures/sword.png')
		self.scene.blit(sw, (0, 0))

	def move(self):
		speed = 3
		
		keys = pygame.key.get_pressed()
		if keys[pygame.K_a]:
			self.x -= speed

		if keys[pygame.K_d]:
			self.x += speed

		if keys[pygame.K_w]:
			self.y -= speed

		if keys[pygame.K_s]:
			self.y += speed

	def control(self):
		pass

	def inventory(self):
		pass

# оружие игрока
class Sword:
	def __init__(self, scene, texture, x, y, room):
		pass

def run_game():
	global sc
	game = True

	# изменить на комнату с тройкой
	start_screen = pygame.image.load('logo.png')
	sc.blit(start_screen, (0, 0))

	# создание персонажа
	cube = MainCharacter(sc, 435, 500, [4, 5])

	while game:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()

		sc.blit(main_room, (0, 0))
		
		# print(cube.room)
		cube.draw_room()
		cube.move()

		print(cube.x, cube.y)
		

		fps.tick(100)
		pygame.display.update()

run_game()