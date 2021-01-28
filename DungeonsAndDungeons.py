# Code created by Xndraftica
# coding: utf-8

import random
import time
from PIL import  Image

time = int(time.time())
random.seed(time)

cache = 0
lives = 100


print("Здравствуй Герой.")

while (True):
	print("Готов ли ты войти в подземелье?")
	img= Image.open("Door.jpg")  
	img.show()
	start = int(input("1) Да" + '\n' + "2) Нет" + '\n' + "(Введи число)" + '\n'))
	if(start == 2):
		print("Что же, это твой выбор. Прощай путник.")
		break
	elif(start != 1 and start != 2):
		print("Я не понимаю речей твоих. Способен ли ты глаголить на едином со мной языке? Если да то ответь мне.")
	elif(start == 1):
		print("Это смелый шаг, Герой. Если ты действительно готов, то можешь проходить. И да помогут тебе Боги.")
		print("#Ты входишь в подземелье.")
		while(start == 1):
			print("#Впереди три пути, куда ты пойдёшь?")
			img= Image.open("Way.png")  
			img.show()
			way = int(input("1) На лево" + '\n' + "2) На право" + '\n' + "3) Прямо" + '\n'))
			if(way == 1):
				enemy = random.randint(1, 6)
				if(enemy == 1):
					print("#Перед вами огромный паук.")
					choice = int(input("1) Сражаться" + '\n' + "2) Бежать" + '\n' + "(Введи число)" + '\n'))
					print("#Впереди три пути, куда ты пойдёшь?")
					img= Image.open("Pavuk.jpeg") 
					img.show() 
					if(choice == 1):
						iflives = lives - 20
						if(iflives > 0):
							lives = lives - 10
							cache = cache + 5
							print("Вы победили.")
							print("Счёт: " + str(cache))
							print("Жизни: " + str(lives))
						else:
							print("Вы погибли.")
							start = 2
					elif(choice == 2):
						iflives = lives - 5
						if(iflives > 0):
							lives = lives - 5
							print("Вы сбежали")
							print("Счёт: " + str(cache))
							print("Жизни: " + str(lives))
						else:
							print("Вы погибли.")
							start = 2
				elif(enemy == 2):
					img= Image.open("Heal.jpeg")  
					img.show()
					print("#Вы нашли лечебное зелье.")
					lives = lives + 20
					print("Счёт: " + str(cache))
					print("Жизни: " + str(lives))
				elif(enemy == 3):
					print("#Перед вами мумия.")
					img= Image.open("Heal.jpeg")  
					img.show()
					choice = int(input("1) Сражаться" + '\n' + "2) Бежать" + '\n' + "(Введи число)" + '\n'))
					if(choice == 1):
						iflives = lives - 30
						if(iflives > 0):
							lives = lives - 15
							cache = cache + 10
							print("Вы победили.")
							print("Счёт: " + str(cache))
							print("Жизни: " + str(lives))
						else:
							print("Вы погибли.")
							start = 2
					elif(choice == 2):
						iflives = lives - 7
						if(iflives > 0):
							lives = lives - 7
							print("Вы сбежали")
							print("Счёт: " + str(cache))
							print("Жизни: " + str(lives))
						else:
							print("Вы погибли.")
							start = 2
				elif(enemy == 4):
					print("#Перед вами сундук.")
					img= Image.open("Mimik.jpeg")  
					img.show()
					choice = int(input("1) Открыть" + '\n' + "2) Не открывать" + '\n' + "(Введи число)" + '\n'))
					if(choice == 1):
						mimik = random.randint(1, 2)
						if(mimik == 1):
							print("#Сундук оказался мимиком.")
							iflives = lives - 50	
							if(iflives > 0):
								lives = lives - 15
								cache = cache + 20
								print("Вы победили.")
								print("Счёт: " + str(cache))
								print("Жизни: " + str(lives))
							else:
								print("Вы погибли.")
								start = 2
						else:
							cache = cache + 100
							print("#Вы открыли сундук.")
							print("Счёт: " + str(cache))
							print("Жизни: " + str(lives))
					elif(choice == 2):
						lives = lives - 0
						print("Вы не открыли сундук.")
						print("Счёт: " + str(cache))
						print("Жизни: " + str(lives))
				elif(enemy == 5):
					print("#Перед вами крипер.")
					img= Image.open("Mine.jpeg")  
					img.show()
					choice = int(input("1) Сражаться" + '\n' + "2) Бежать" + '\n' + "(Введи число)" + '\n'))
					if(choice == 1):
						iflives = lives - 100
						if(iflives > 0):
							lives = lives - 25
							cache = cache + 1000
							print("Вы победили.")
							print("Счёт: " + str(cache))
							print("Жизни: " + str(lives))
						else:
							print("Вы погибли.")
							start = 2
					elif(choice == 2):
						iflives = lives - 10
						if(iflives > 0):
							lives = lives - 10
							print("Вы сбежали")
							print("Счёт: " + str(cache))
							print("Жизни: " + str(lives))
						else:
							print("Вы погибли.")
							start = 2
				elif(enemy == 6):
					print("#Перед вами скелет.")
					img= Image.open("Skelet.jpeg")  
					img.show()
					choice = int(input("1) Сражаться" + '\n' + "2) Бежать" + '\n' + "(Введи число)" + '\n'))
					if(choice == 1):
						iflives = lives - 80
						if(iflives > 0):
							lives = lives - 40
							cache = cache + 40
							print("Вы победили.")
							print("Счёт: " + str(cache))
							print("Жизни: " + str(lives))
						else:
							print("Вы погибли.")
							start = 2
					elif(choice == 2):
						iflives = lives - 20
						if(iflives > 0):
							lives = lives - 20
							print("Вы сбежали")
							print("Счёт: " + str(cache))
							print("Жизни: " + str(lives))
						else:
							print("Вы погибли.")
							start = 2
				elif(enemy == 1):
					print("#Перед вами бешеная крыса.")
					img= Image.open("Maus.jpeg")  
					img.show()
					choice = int(input("1) Сражаться" + '\n' + "2) Бежать" + '\n' + "(Введи число)" + '\n'))
					if(choice == 1):
						iflives = lives - 10
						if(iflives > 0):
							lives = lives - 5
							cache = cache + 5
							print("Вы победили.")
							print("Счёт: " + str(cache))
							print("Жизни: " + str(lives))
						else:
							print("Вы погибли.")
							start = 2
					elif(choice == 2):
						iflives = lives - 1
						if(iflives > 0):
							lives = lives - 1
							print("Вы сбежали")
							print("Счёт: " + str(cache))
							print("Жизни: " + str(lives))
						else:
							print("Вы погибли.")
							start = 2
			elif(way == 2):
				enemy = random.randint(1, 6)
				if(enemy == 1):
					print("#Перед вами огромный паук.")
					choice = int(input("1) Сражаться" + '\n' + "2) Бежать" + '\n' + "(Введи число)" + '\n'))
					print("#Впереди три пути, куда ты пойдёшь?")
					img= Image.open("Pavuk.jpeg") 
					img.show() 
					if(choice == 1):
						iflives = lives - 20
						if(iflives > 0):
							lives = lives - 10
							cache = cache + 5
							print("Вы победили.")
							print("Счёт: " + str(cache))
							print("Жизни: " + str(lives))
						else:
							print("Вы погибли.")
							start = 2
					elif(choice == 2):
						iflives = lives - 5
						if(iflives > 0):
							lives = lives - 5
							print("Вы сбежали")
							print("Счёт: " + str(cache))
							print("Жизни: " + str(lives))
						else:
							print("Вы погибли.")
							start = 2
				elif(enemy == 2):
					img= Image.open("Heal.jpeg")  
					img.show()
					print("#Вы нашли лечебное зелье.")
					lives = lives + 20
					print("Счёт: " + str(cache))
					print("Жизни: " + str(lives))
				elif(enemy == 3):
					print("#Перед вами мумия.")
					img= Image.open("Heal.jpeg")  
					img.show()
					choice = int(input("1) Сражаться" + '\n' + "2) Бежать" + '\n' + "(Введи число)" + '\n'))
					if(choice == 1):
						iflives = lives - 30
						if(iflives > 0):
							lives = lives - 15
							cache = cache + 10
							print("Вы победили.")
							print("Счёт: " + str(cache))
							print("Жизни: " + str(lives))
						else:
							print("Вы погибли.")
							start = 2
					elif(choice == 2):
						iflives = lives - 7
						if(iflives > 0):
							lives = lives - 7
							print("Вы сбежали")
							print("Счёт: " + str(cache))
							print("Жизни: " + str(lives))
						else:
							print("Вы погибли.")
							start = 2
				elif(enemy == 4):
					print("#Перед вами сундук.")
					img= Image.open("Mimik.jpeg")  
					img.show()
					choice = int(input("1) Открыть" + '\n' + "2) Не открывать" + '\n' + "(Введи число)" + '\n'))
					if(choice == 1):
						mimik = random.randint(1, 2)
						if(mimik == 1):
							print("#Сундук оказался мимиком.")
							iflives = lives - 50	
							if(iflives > 0):
								lives = lives - 15
								cache = cache + 20
								print("Вы победили.")
								print("Счёт: " + str(cache))
								print("Жизни: " + str(lives))
							else:
								print("Вы погибли.")
								start = 2
						else:
							cache = cache + 100
							print("#Вы открыли сундук.")
							print("Счёт: " + str(cache))
							print("Жизни: " + str(lives))
					elif(choice == 2):
						lives = lives - 0
						print("Вы не открыли сундук.")
						print("Счёт: " + str(cache))
						print("Жизни: " + str(lives))
				elif(enemy == 5):
					print("#Перед вами крипер.")
					img= Image.open("Mine.jpeg")  
					img.show()
					choice = int(input("1) Сражаться" + '\n' + "2) Бежать" + '\n' + "(Введи число)" + '\n'))
					if(choice == 1):
						iflives = lives - 100
						if(iflives > 0):
							lives = lives - 25
							cache = cache + 1000
							print("Вы победили.")
							print("Счёт: " + str(cache))
							print("Жизни: " + str(lives))
						else:
							print("Вы погибли.")
							start = 2
					elif(choice == 2):
						iflives = lives - 10
						if(iflives > 0):
							lives = lives - 10
							print("Вы сбежали")
							print("Счёт: " + str(cache))
							print("Жизни: " + str(lives))
						else:
							print("Вы погибли.")
							start = 2
				elif(enemy == 6):
					print("#Перед вами скелет.")
					img= Image.open("Skelet.jpeg")  
					img.show()
					choice = int(input("1) Сражаться" + '\n' + "2) Бежать" + '\n' + "(Введи число)" + '\n'))
					if(choice == 1):
						iflives = lives - 80
						if(iflives > 0):
							lives = lives - 40
							cache = cache + 40
							print("Вы победили.")
							print("Счёт: " + str(cache))
							print("Жизни: " + str(lives))
						else:
							print("Вы погибли.")
							start = 2
					elif(choice == 2):
						iflives = lives - 20
						if(iflives > 0):
							lives = lives - 20
							print("Вы сбежали")
							print("Счёт: " + str(cache))
							print("Жизни: " + str(lives))
						else:
							print("Вы погибли.")
							start = 2
				elif(enemy == 1):
					print("#Перед вами бешеная крыса.")
					img= Image.open("Maus.jpeg")  
					img.show()
					choice = int(input("1) Сражаться" + '\n' + "2) Бежать" + '\n' + "(Введи число)" + '\n'))
					if(choice == 1):
						iflives = lives - 10
						if(iflives > 0):
							lives = lives - 5
							cache = cache + 5
							print("Вы победили.")
							print("Счёт: " + str(cache))
							print("Жизни: " + str(lives))
						else:
							print("Вы погибли.")
							start = 2
					elif(choice == 2):
						iflives = lives - 1
						if(iflives > 0):
							lives = lives - 1
							print("Вы сбежали")
							print("Счёт: " + str(cache))
							print("Жизни: " + str(lives))
						else:
							print("Вы погибли.")
							start = 2
			if(way == 3):
				enemy = random.randint(1, 6)
				if(enemy == 1):
					print("#Перед вами огромный паук.")
					choice = int(input("1) Сражаться" + '\n' + "2) Бежать" + '\n' + "(Введи число)" + '\n'))
					print("#Впереди три пути, куда ты пойдёшь?")
					img= Image.open("Pavuk.jpeg") 
					img.show() 
					if(choice == 1):
						iflives = lives - 20
						if(iflives > 0):
							lives = lives - 10
							cache = cache + 5
							print("Вы победили.")
							print("Счёт: " + str(cache))
							print("Жизни: " + str(lives))
						else:
							print("Вы погибли.")
							start = 2
					elif(choice == 2):
						iflives = lives - 5
						if(iflives > 0):
							lives = lives - 5
							print("Вы сбежали")
							print("Счёт: " + str(cache))
							print("Жизни: " + str(lives))
						else:
							print("Вы погибли.")
							start = 2
				elif(enemy == 2):
					img= Image.open("Heal.jpeg")  
					img.show()
					print("#Вы нашли лечебное зелье.")
					lives = lives + 20
					print("Счёт: " + str(cache))
					print("Жизни: " + str(lives))
				elif(enemy == 3):
					print("#Перед вами мумия.")
					img= Image.open("Heal.jpeg")  
					img.show()
					choice = int(input("1) Сражаться" + '\n' + "2) Бежать" + '\n' + "(Введи число)" + '\n'))
					if(choice == 1):
						iflives = lives - 30
						if(iflives > 0):
							lives = lives - 15
							cache = cache + 10
							print("Вы победили.")
							print("Счёт: " + str(cache))
							print("Жизни: " + str(lives))
						else:
							print("Вы погибли.")
							start = 2
					elif(choice == 2):
						iflives = lives - 7
						if(iflives > 0):
							lives = lives - 7
							print("Вы сбежали")
							print("Счёт: " + str(cache))
							print("Жизни: " + str(lives))
						else:
							print("Вы погибли.")
							start = 2
				elif(enemy == 4):
					print("#Перед вами сундук.")
					img= Image.open("Mimik.jpeg")  
					img.show()
					choice = int(input("1) Открыть" + '\n' + "2) Не открывать" + '\n' + "(Введи число)" + '\n'))
					if(choice == 1):
						mimik = random.randint(1, 2)
						if(mimik == 1):
							print("#Сундук оказался мимиком.")
							iflives = lives - 50	
							if(iflives > 0):
								lives = lives - 15
								cache = cache + 20
								print("Вы победили.")
								print("Счёт: " + str(cache))
								print("Жизни: " + str(lives))
							else:
								print("Вы погибли.")
								start = 2
						else:
							cache = cache + 100
							print("#Вы открыли сундук.")
							print("Счёт: " + str(cache))
							print("Жизни: " + str(lives))
					elif(choice == 2):
						lives = lives - 0
						print("Вы не открыли сундук.")
						print("Счёт: " + str(cache))
						print("Жизни: " + str(lives))
				elif(enemy == 5):
					print("#Перед вами крипер.")
					img= Image.open("Mine.jpeg")  
					img.show()
					choice = int(input("1) Сражаться" + '\n' + "2) Бежать" + '\n' + "(Введи число)" + '\n'))
					if(choice == 1):
						iflives = lives - 100
						if(iflives > 0):
							lives = lives - 25
							cache = cache + 1000
							print("Вы победили.")
							print("Счёт: " + str(cache))
							print("Жизни: " + str(lives))
						else:
							print("Вы погибли.")
							start = 2
					elif(choice == 2):
						iflives = lives - 10
						if(iflives > 0):
							lives = lives - 10
							print("Вы сбежали")
							print("Счёт: " + str(cache))
							print("Жизни: " + str(lives))
						else:
							print("Вы погибли.")
							start = 2
				elif(enemy == 6):
					print("#Перед вами скелет.")
					img= Image.open("Skelet.jpeg")  
					img.show()
					choice = int(input("1) Сражаться" + '\n' + "2) Бежать" + '\n' + "(Введи число)" + '\n'))
					if(choice == 1):
						iflives = lives - 80
						if(iflives > 0):
							lives = lives - 40
							cache = cache + 40
							print("Вы победили.")
							print("Счёт: " + str(cache))
							print("Жизни: " + str(lives))
						else:
							print("Вы погибли.")
							start = 2
					elif(choice == 2):
						iflives = lives - 20
						if(iflives > 0):
							lives = lives - 20
							print("Вы сбежали")
							print("Счёт: " + str(cache))
							print("Жизни: " + str(lives))
						else:
							print("Вы погибли.")
							start = 2
				elif(enemy == 1):
					print("#Перед вами бешеная крыса.")
					img= Image.open("Maus.jpeg")  
					img.show()
					choice = int(input("1) Сражаться" + '\n' + "2) Бежать" + '\n' + "(Введи число)" + '\n'))
					if(choice == 1):
						iflives = lives - 10
						if(iflives > 0):
							lives = lives - 5
							cache = cache + 5
							print("Вы победили.")
							print("Счёт: " + str(cache))
							print("Жизни: " + str(lives))
						else:
							print("Вы погибли.")
							start = 2
					elif(choice == 2):
						iflives = lives - 1
						if(iflives > 0):
							lives = lives - 1
							print("Вы сбежали")
							print("Счёт: " + str(cache))
							print("Жизни: " + str(lives))
						else:
							print("Вы погибли.")
							start = 2
	img= Image.open("Over.jpeg")  
	img.show()
	print("Игра окончена...")
	print("Ваш результат: " + str(cache))
