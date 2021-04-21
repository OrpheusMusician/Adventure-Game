import os, random, pygame
	

# 0 + [6 координатных позиций с комнатами]
# 
# комната = {'имя': 'x_y', 'поле': (клетки с возможностью передвигаться), 'выходы': }
#

		 # level 00
rules = [[0, {'name': '01_00', 'space': (), 'exits': ()}, 
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
			 {'name': '04_04', 'space': (), 'exits': ()}, # 04
		  0],

		 # level 05
         [0, {'name': '01_05', 'space': (), 'exits': ()}, 
			 {'name': '02_05', 'space': (), 'exits': ()},
			 {'name': '03_05', 'space': (), 'exits': ()},
			 {'name': '04_05', 'space': ({'x': range( 54, 846), 'y': range(475, 572)}, 
			 							 {'x': range(367, 533), 'y': range(572, 630)}, 
			 							 {'x': range( 54, 265), 'y': range(268, 475)}, 
			 							 {'x': range( 54, 220), 'y': range( 58, 268)}, 
			 							 {'x': range(634, 846), 'y': range(268, 475)}, 
			 							 {'x': range(679, 846), 'y': range( 58, 268)}, 
			 							 {'x': range(383, 517), 'y': range(  0, 158)}), 

							   'exits': ({'x': range(367, 533), 'y': range(605, 631), 'room': [4, 6], 'mode': 'down'},
										 {'x': range(383, 517), 'y': range(0, 1), 'room': [4, 4], 'mode': 'up'})},

			 {'name': '05_05', 'space': (), 'exits': ()},
			 {'name': '06_05', 'space': (), 'exits': ()}],
	     
	     # level 06
		 [0, {'name': '01_06', 'space': (), 'exits': ()}, 
			 {'name': '02_06', 'space': (), 'exits': ()},
			 {'name': '03_06', 'space': (), 'exits': ()},
			 {'name': '04_06', 'space': ({'x': range(  0, 900), 'y': range( 57, 571)},
			 							 {'x': range(367, 533), 'y': range(  0,  58)},
			 							 {'x': range(367, 533), 'y': range( 40,  98)}), 

			 				   'exits': ({'x': range(367, 533), 'y': range(  0,   1), 'room': [ 4,  5], 'mode': 'up'},  
			 							 {'x': range(  0,   1), 'y': range( 57, 571), 'room': [ 3,  6], 'mode': 'left'}, 
			 							 {'x': range(875, 876), 'y': range( 57, 571), 'room': [ 5,  6], 'mode': 'right'})},

			 {'name': '05_06', 'space': (), 'exits': ()},
			 {'name': '06_06', 'space': (), 'exits': ()}],

		 # level 07
		 [0, {'name': '01_07', 'space': (), 'exits': ()}, 
			 {'name': '02_07', 'space': (), 'exits': ()},
			 {'name': '03_07', 'space': (), 'exits': ()},
			 {'name': '04_07', 'space': (), 'exits': ()},
			 {'name': '05_07', 'space': (), 'exits': ()},
			 {'name': '06_07', 'space': (), 'exits': ()}],
         
         # level 08
		 [0, {'name': '01_08', 'space': (), 'exits': ()}, 
			 {'name': '02_08', 'space': (), 'exits': ()},
			 {'name': '03_08', 'space': (), 'exits': ()},
			 {'name': '04_08', 'space': (), 'exits': ()},
			 {'name': '05_08', 'space': (), 'exits': ()},
			 {'name': '06_08', 'space': (), 'exits': ()}],

		 # level 09
         [0, {'name': '01_09', 'space': (), 'exits': ()}, 
			 {'name': '02_09', 'space': (), 'exits': ()},
			 {'name': '03_09', 'space': (), 'exits': ()},
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
		 [0, {'name': '01_10', 'space': (), 'exits': ()}, 
			 {'name': '02_10', 'space': (), 'exits': ()},
			 {'name': '03_10', 'space': (), 'exits': ()},
			 {'name': '04_10', 'space': ({'x': range(67, 900), 'y': range(57, 571)}, 
			 	                         {'x': range(368, 533), 'y': range(571, 630)}, 
			 	                         {'x': range(368, 533), 'y': range(0, 58)}), 

								'exits': ({'x': range(368, 533), 'y': range(605, 630), 'room': [4, 11], 'mode': 'down'}, 
										  {'x': range(368, 533), 'y': range(1) , 'room': [4, 9], 'mode': 'up'})},
			 
			 {'name': '05_10', 'space': (), 'exits': ()},
			 {'name': '06_10', 'space': (), 'exits': ()}],

		 # level 11
		 [0, {'name': '01_11', 'space': (), 'exits': []}, 
			 {'name': '02_11', 'space': (), 'exits': ()},
			 {'name': '03_11', 'space': (), 'exits': ()},
			 {'name': '04_11', 'space': ({'x': range(53, 846), 'y': range(57, 572)}, 
			 							 {'x': range(368, 533), 'y': range(0, 88)}), 

			 				   'exits': ({'x': range(368, 532), 'y': range(1), 'room': [4, 10], 'mode': 'up'}, 
			 				   			 {'x': range(-100, -100), 'y': range(-100, -100), 'room': [0, 0], 'mode': 'up'})},
			 				   
			 {'name': '05_11', 'space': (), 'exits': ()},
			 {'name': '06_11', 'space': (), 'exits': ()}]
		]