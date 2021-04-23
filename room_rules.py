import os, random, pygame
	

# загрузка карты по плану [room_pic, color_of_walls]
#         0  1   2   3   4   5   6

# 		# =========== [y = 00] ===========  
rooms = [
		
		[0, 
		 [pygame.image.load('assets/rooms/01_00.png'), (245, 146,  48)], 
		 [pygame.image.load('assets/rooms/02_00.png'), (245, 146,  48)], 
		 0, 0, 0, 0
		], 

		# =========== [y = 01] ===========  
		[0, 
		 [pygame.image.load('assets/rooms/01_01.png'), (245, 146,  48)], 
		 [pygame.image.load('assets/rooms/02_01.png'), (245, 146,  48)], 
		 0, 0, 0, 0
		],  

		# =========== [y = 02] ===========  
		[
		 0, 
		 0, 
		 [pygame.image.load('assets/rooms/02_02.png'), (245,  97,  48)], 
		 0, 0, 0, 0
		], 

		# =========== [y = 03] ===========  
		[
		 0, 
		 0, 
		 [pygame.image.load('assets/rooms/02_03.png'), ( 21,  17,  21)], 
		 0, 0, 0, 0
		], 

		# =========== [y = 04] ===========  
		[
		 0, 
		 0, 
		 [pygame.image.load('assets/rooms/02_04.png'), ( 80,  92, 192)], 
		 [pygame.image.load('assets/rooms/03_04.png'), ( 80,  92, 192)], 
		 [pygame.image.load('assets/rooms/04_04.png'), (192, 204,  13)], 
		 0, 0
		], 
		 
		# =========== [y = 05] ===========  
		[
		 0, 
		 [], 
		 [pygame.image.load('assets/rooms/02_05.png'), ( 80,  92, 192)], 
		 [pygame.image.load('assets/rooms/03_05.png'), ( 80,  92, 192)], 
		 [pygame.image.load('assets/rooms/04_05.png'), (192, 204,  13)], 
		 [], 
		 []
		],

		# =========== [y = 06] ===========  
		[
		 0, 
		 [pygame.image.load('assets/rooms/03_04.png'), ( 80,  92, 192)], 
		 [pygame.image.load('assets/rooms/02_06.png'), ( 80,  92, 192)], 
		 [pygame.image.load('assets/rooms/03_06.png'), (131, 180,  22)], 
		 [pygame.image.load('assets/rooms/04_06.png'), ( 73, 183,  16)], 
		 [pygame.image.load('assets/rooms/05_06.png'), (197, 141,  17)], 
		 [pygame.image.load('assets/rooms/06_06.png'), (138,  52, 179)]
		],

		# =========== [y = 07] ===========  
		[
		 0, 
		 [], 
		 [], 
		 [], 
		 [pygame.image.load('assets/rooms/04_07.png'), (237,  72,  45)], 
		 [], 
		 []
		],

		# =========== [y = 08] ===========  
		[
		 0, 
		 [], 
		 [], 
		 [], 
		 [pygame.image.load('assets/rooms/04_08.png'), (237,  72,  45)], 
		 [], 
		 []
		],

		# =========== [y = 09] ===========  
		[
		 0, 0, 0, 0, 
		 [pygame.image.load('assets/rooms/04_09.png'), (223, 222, 228)], 
		 0, 
		 [pygame.image.load('assets/rooms/06_09.png'), (140,  88, 184)]
		], 
		
		# =========== [y = 10] ===========  
		[
		 0, 
		 [], 
		 [], 
		 [], 
		 [pygame.image.load('assets/rooms/04_10.png'), ( 73, 183,  16)], 
		 [], 
		 [pygame.image.load('assets/rooms/06_10.png'), (104, 136, 204)]
		],
		
		# =========== [y = 11] ===========  
		[
		 0, 0, 0, 0, 
		 [pygame.image.load('assets/rooms/04_11.png'), (  9, 181, 137)], 
		 0, 
		 [pygame.image.load('assets/rooms/06_11.png'), (192, 104,  72)]
		]]


# 0 + [6 координатных позиций с комнатами]
# 
# комната = {'имя': 'x_y', 'поле': (клетки с возможностью передвигаться), 'выходы': }
#

y_down = range(605, 631)
y_up = range(0, 1)
x_right = range(875, 876)
x_left = range(0, 1)

rules = [

		 # level 00
		 [0, {'name': '01_00', 'space': (), 'exits': ()}, 
			 {'name': '02_00', 'space': (), 'exits': ()},
			 0, 0, 0, 0],
         
         # level 01
         [0, {'name': '01_01', 'space': (), 'exits': ()}, 
			 {'name': '02_01', 'space': (), 'exits': ()},
			 0, 0, 0, 0],
	     
	     # level 02
		 [0, 
		  0, {'name': '02_02', 'space': (), 'exits': ()}, # 02
		  0, 0, 0, 0],

		 # level 03
		 [0, 
		  0, {'name': '02_03', 'space': (), 'exits': ()}, # 02
		  0, 0, 0, 0],
         
         # level 04
		 [0, 
		  0, {'name': '02_04', 'space': (), 'exits': ()}, # 02
		     {'name': '03_04', 'space': (), 'exits': ()}, # 03
			 {'name': '04_04', 'space': ({'x': range( 54, 846), 'y': range( 58, 572)},
			 							 {'x': range(382, 517), 'y': range( 58, 630)}), 

			 				   'exits': ({'x': range(382, 517), 'y': y_down, 'room': [ 4,  5], 'mode': 'down'},
			 				   			 {'x': range(-10, -10), 'y': y_down, 'room': [ 0,  0], 'mode': 'up'})}, # 04
		  0],

		 # level 05
         [0, 0, 
			 {'name': '02_05', 'space': (), 'exits': ()},
			 {'name': '03_05', 'space': ({'x': range(367, 533), 'y': range(473, 630)}, 
			 							 {'x': range(  0, 900), 'y': range(473, 572)}, 
			 							 {'x': range(180, 227), 'y': range(  0, 572)}, 
			 							 {'x': range(673, 720), 'y': range(  0, 572)}, 
			 							 {'x': range(270, 630), 'y': range(263, 370)},
			 							 {'x': range(270, 316), 'y': range(  0, 370)},
			 							 {'x': range(584, 630), 'y': range(  0, 370)},

			 							 {'x': range(359, 541), 'y': range( 54, 161)},
			 							 {'x': range(359, 407), 'y': range(  0, 161)},
			 							 {'x': range(493, 541), 'y': range(  0, 161)},
			 							 
			 							 # left
			 							 {'x': range(  0, 137), 'y': range( 54, 161)},
			 							 {'x': range(  0, 137), 'y': range(263, 370)},
			 							 {'x': range( 89, 137), 'y': range( 54, 370)},

			 							 # right
			 							 {'x': range(763, 900), 'y': range( 54, 161)},
			 							 {'x': range(763, 900), 'y': range(263, 370)},
			 							 {'x': range(763, 811), 'y': range( 54, 370)}),

			 				   'exits': ({'x': range(367, 533), 'y': y_down, 'room': [ 3,  6], 'mode': 'down'},
			 				   			 
			 				   			 # right
			 				   			 {'x': x_right, 'y': range(473, 572), 'room': [ 2,  5], 'mode': 'right'},
			 				   			 {'x': x_right, 'y': range(263, 370), 'room': [ 2,  5], 'mode': 'right'},
			 				   			 {'x': x_right, 'y': range( 54, 161), 'room': [ 2,  5], 'mode': 'right'},
			 				   			 
			 				   			 # left
			 				   			 {'x': x_left, 'y': range(473, 572), 'room': [ 2,  5], 'mode': 'left'},
			 				   			 {'x': x_left, 'y': range(263, 370), 'room': [ 2,  5], 'mode': 'left'},
			 				   			 {'x': x_left, 'y': range( 54, 161), 'room': [ 2,  5], 'mode': 'left'},
			 				   			 
			 				   			 # up
			 				   			 {'x': range(180, 227), 'y': y_up, 'room': [ 3,  4], 'mode': 'up'},
			 				   			 {'x': range(270, 316), 'y': y_up, 'room': [ 3,  4], 'mode': 'up'},
			 				   			 {'x': range(359, 407), 'y': y_up, 'room': [ 3,  4], 'mode': 'up'},
			 				   			 {'x': range(493, 541), 'y': y_up, 'room': [ 3,  4], 'mode': 'up'},
			 				   			 {'x': range(584, 630), 'y': y_up, 'room': [ 3,  4], 'mode': 'up'},
			 				   			 {'x': range(673, 720), 'y': y_up, 'room': [ 3,  4], 'mode': 'up'},
			 				   			 )},

			 {'name': '04_05', 'space': [{'x': range( 54, 846), 'y': range(475, 572)}, 
			 							 {'x': range(367, 533), 'y': range(572, 630)}, 
			 							 {'x': range( 54, 265), 'y': range(268, 475)}, 
			 							 {'x': range( 54, 220), 'y': range( 58, 268)}, 
			 							 {'x': range(634, 846), 'y': range(268, 475)}, 
			 							 {'x': range(679, 846), 'y': range( 58, 268)}, 
			 							 {'x': range(383, 517), 'y': range(  0, 158)}], 

							   'exits': ({'x': range(367, 533), 'y': y_down, 'room': [ 4,  6], 'mode': 'down'},
										 {'x': range(383, 517), 'y': y_up  , 'room': [ 4,  4], 'mode': 'up'})},
		 0, 0],
	     
	     # level 06
		 [0, {'name': '01_06', 'space': (), 'exits': ()}, 
			 {'name': '02_06', 'space': (), 'exits': ()},
			 {'name': '03_06', 'space': ({'x': range( 68, 900), 'y': range( 58, 572)}, 
			 							 {'x': range(367, 533), 'y': range(  0, 90)}), 
			 				   
			 				   'exits': ({'x': range(367, 533), 'y': range(  0,   1), 'room': [ 3,  5], 'mode': 'up'}, 
			 				   			 {'x': x_right, 'y': range( 58, 572), 'room': [ 4,  6], 'mode': 'right'})},
			 
			 {'name': '04_06', 'space': ({'x': range(  0, 900), 'y': range( 57, 571)},
			 							 {'x': range(367, 533), 'y': range(  0,  98)}), 

			 				   'exits': ({'x': range(367, 533), 'y': range(  0,   1), 'room': [ 4,  5], 'mode': 'up'},  
			 							 {'x': range(  0,   1), 'y': range( 57, 571), 'room': [ 3,  6], 'mode': 'left'}, 
			 							 {'x': range(875, 876), 'y': range( 57, 571), 'room': [ 5,  6], 'mode': 'right'})},

			 {'name': '05_06', 'space': [{'x': range(  0, 832), 'y': range( 57, 572)}, 
			 							 {'x': range(367, 533), 'y': range(572, 630)}, 
			 							 {'x': range(367, 533), 'y': range(540, 608)}], 
			 				   
			 				   'exits': ({'x': range(  0,   1), 'y': range( 57, 572), 'room': [ 4,  6], 'mode': 'left'},
			 				   			 {'x': range(367, 533), 'y': range(605, 631), 'room': [ 5,  7], 'mode': 'down'},
			 				   			 {'x': x_right, 'y': range( 58, 572), 'room': [6,  6], 'mode': 'right'})},

			 {'name': '06_06', 'space': ({'x': range(  0, 445), 'y': range( 57, 571)}, 
			 							 {'x': range(368, 445), 'y': range(  0, 571)}), 

			 				   'exits': ({'x': x_left, 'y': range( 58, 572), 'room': [5,  6], 'mode': 'left'}, 
			 				   			 {'x': range(-10, -10), 'y': range(-10, -10), 'room': [ 0,  0], 'mode': 'up'})}],

		 # level 07
		 [0, 0, 0,
			 {'name': '03_07', 'space': (), 'exits': ()},
			 {'name': '04_07', 'space': (), 'exits': ()},
			 {'name': '05_07', 'space': (), 'exits': ()},
			 0],
         
         # level 08
		 [0, 0, 0,
			 {'name': '03_08', 'space': (), 'exits': ()},
			 {'name': '04_08', 'space': (), 'exits': ()},
			 {'name': '05_08', 'space': (), 'exits': ()},
			 0],

		 # level 09
         [0, 0, 0, 0,
			 {'name': '04_09', 'space': ({'x': range(54, 846), 'y': range(475, 572)}, 
			 							 {'x': range(367, 533), 'y': range(572, 630)}, 
			 							 {'x': range(54, 265), 'y': range(268, 475)}, 
			 							 {'x': range(54, 220), 'y': range(58, 268)}, 
			 							 {'x': range(634, 846), 'y': range(268, 475)}, 
			 							 {'x': range(679, 846), 'y': range(58, 268)}, 
			 							 {'x': range(383, 517), 'y': range(0, 158)}), 

							   'exits': ({'x': range(367, 533), 'y': range(605, 631), 'room': [4, 10], 'mode': 'down'},
										 {'x': range(383, 517), 'y': range(0, 1), 'room': [4, 8], 'mode': 'up'})},

			 {'name': '05_09', 'space': (), 'exits': ()},
			 {'name': '06_09', 'space': (), 'exits': ()}],
	     
	     # level 10
		 [0, 0, 0, 0,
			 {'name': '04_10', 'space': ({'x': range(67, 900), 'y': range(57, 571)}, 
			 	                         {'x': range(368, 533), 'y': range(571, 630)}, 
			 	                         {'x': range(368, 533), 'y': range(0, 58)}), 

								'exits': ({'x': range(368, 533), 'y': range(605, 630), 'room': [4, 11], 'mode': 'down'}, 
										  {'x': range(368, 533), 'y': range(1) , 'room': [4, 9], 'mode': 'up'})},
			 
			 {'name': '05_10', 'space': (), 'exits': ()},
			 {'name': '06_10', 'space': (), 'exits': ()}],

		 # level 11
		 [0, 0, 0, 0,
			 {'name': '04_11', 'space': ({'x': range( 53, 846), 'y': range( 57, 572)}, 
			 							 {'x': range(368, 533), 'y': range(  0,  88)}), 

			 				   'exits': ({'x': range(368, 532), 'y': range(  0,   1), 'room': [ 4, 10], 'mode': 'up'}, 
			 				   			 {'x': range(-10, -10), 'y': range(-10, -10), 'room': [ 0,  0], 'mode': 'up'})},
			 				   
			 0,
			 {'name': '06_11', 'space': ({'x': range( 53, 846), 'y': range( 57, 572)}, 
			 							 {'x': range(368, 533), 'y': range(  0,  88)}), 

			 				   'exits': ({'x': range(368, 532), 'y': range(  0,   1), 'room': [ 6, 10], 'mode': 'up'}, 
			 				   			 {'x': range(-10, -10), 'y': range(-10, -10), 'room': [ 0,  0], 'mode': 'up'})}]]