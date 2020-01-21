from math import *
import pygame
from pygame import * 
import random

#Programme de Menu, affiche les différents modes et les menus crédits et informations.

#!!!!!! PATHS !!!!!!#

path_menu = "menu.py"
path_modes = "modes.py"
path_informations = "informations.py"

#------ Fonds ------#
init()

fenetre = display.set_mode((800, 600), RESIZABLE)

fond = image.load("fonds/fondmenu.jpg").convert()
fondblack = image.load("fonds/fondblack.jpg").convert_alpha()
fondmodes = image.load("fonds/fondmodes.jpg").convert_alpha()
end = image.load("end/OverClassique.jpg").convert_alpha()
end_gagnant_joueur_1 = image.load("end/OverClassiquePlayerOne.jpg")
end_gagnant_joueur_2 = image.load("end/OverClassiquePlayerTwo.jpg")

retourRectGame = image.load("modes/retour.jpg").convert_alpha()

""" Initialisation de la police"""

font = font.SysFont("consolas", 60, bold = False, italic = False)

#------ Fonds - Affichage - JEU ------#

def mainFonds():
	"""
	Affiche le fond principal, dans ce cas, noir avec tirets blancs sur côtés.
	"""
	fenetre.blit(fondblack, (0,0))

	display.flip()

#------ Personnage - User - Set ------#

player = image.load("classique/bar.jpg").convert_alpha()
player2 = image.load("classique/bar.jpg").convert_alpha()

#------ Personnage - Balle - Set ------#

balle = image.load("classique/ball.png").convert_alpha()

#------ Main ------#

def unique():
	mouseCordsXGame, mouseCordsYGame = mouse.get_pos()

	classique = True

	y_player = 295
	y_player2 = 295
	limitmin = 10
	limitmax = 530

	vecteur_balle_x = 3
	vecteur_balle_y = 1

	cord_balle_x = 400
	cord_balle_y = 300

	score_player = 0
	score_player_2 = 0

	pause = 0

	mainFonds()

	while classique:
		time.Clock().tick(800)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
				quit()
				exit()

		key_alpha = key.get_pressed()
		key_alpha_2 = key.get_pressed()
		key_alpha_3 = key.get_pressed()


		#CONTROLS - MOUVEMENTS
		#Player 1
		if key_alpha[K_UP]:
			y_player -= 3.5
		if key_alpha[K_DOWN]:
			y_player += 3.5
		
		#Player 2
		#Marge d'erreur
		erreur = random.randint(1, 696969)
		if cord_balle_y - 20 > y_player2:
			if erreur > 695475:
				y_player2 -= 140
			else:
				y_player2 += 1.4
		else:
			y_player2 -= 1.4

		#LIMITS - LIMITES HAUT / BAS --> PLAYERS
		#Player 1
		if y_player < limitmin:
			y_player = limitmin
		if y_player > limitmax:
			y_player = limitmax

		#Player 2
		if y_player2 < limitmin:
			y_player2 = limitmin
		if y_player2 > limitmax:
			y_player2 = limitmax

		fenetre.blit(fondblack, (0,0))
		fenetre.blit(player, (775, y_player))
		fenetre.blit(player2, (15, y_player2))

		cord_balle_x += vecteur_balle_x
		cord_balle_y += vecteur_balle_y

		#Gain de point.
		if cord_balle_x > 780:
			print("Joueur 2 (gauche) --> Point Gagné !")
			score_player_2 += 1
			cord_balle_x = 400
			cord_balle_y = 300
			print(score_player_2, score_player)
		if cord_balle_x < 10:
			print("Joueur 1 (droite) --> Point Gagné !")
			score_player += 1
			cord_balle_x = 400
			cord_balle_y = 300
			print(score_player_2, score_player)

		#Collisions.
		if cord_balle_y >= 580:
			vecteur_balle_y = 0 - vecteur_balle_y
		if cord_balle_y <= 5:
			vecteur_balle_y = 0 - vecteur_balle_y
		if Rect((775, y_player), (7, 60)).colliderect(Rect((cord_balle_x, cord_balle_y), (15, 15))):
			vecteur_balle_x = 0 - vecteur_balle_x
			print(vecteur_balle_x)
		if Rect((15, y_player2), (7, 60)).colliderect(Rect((cord_balle_x, cord_balle_y), (15, 15))):
			vecteur_balle_x = 0 - vecteur_balle_x
			print(vecteur_balle_x, vecteur_balle_y)

		score = str(score_player_2) + " : " + str(score_player)
		score_render = font.render(score, 1, (255, 255, 255))

		fenetre.blit(balle, (cord_balle_x, cord_balle_y))
		fenetre.blit(score_render, (325,25))

		if score_player_2 > 9:
			fenetre.blit(fondblack, (0,0))
			fenetre.blit(end, (200, 150))
			fenetre.blit(end_gagnant_joueur_1, (200, 350))
		elif score_player > 9:
			fenetre.blit(fondblack, (0,0))
			fenetre.blit(end, (200, 150))
			fenetre.blit(end_gagnant_joueur_2, (200, 350))

		display.flip()

def duo():
	mouseCordsXGame, mouseCordsYGame = mouse.get_pos()

	classique = True

	y_player = 295
	y_player2 = 295
	limitmin = 10
	limitmax = 530

	vecteur_balle_x = 3
	vecteur_balle_y = 1

	cord_balle_x = 400
	cord_balle_y = 300

	score_player = 0
	score_player_2 = 0

	pause = 0

	mainFonds()

	while classique:
		time.Clock().tick(800)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
				quit()
				exit()

		key_alpha = key.get_pressed()
		key_alpha_2 = key.get_pressed()
		key_alpha_3 = key.get_pressed()


		#CONTROLS - MOUVEMENTS
		#Player 1
		if key_alpha[K_UP]:
			y_player -= 3.5
		if key_alpha[K_DOWN]:
			y_player += 3.5
		
		#Player 2
		if key_alpha_3[K_w]:
			y_player2 -= 3.5
		if key_alpha_2[K_s]:
			y_player2 += 3.5

		#LIMITS - LIMITES HAUT / BAS --> PLAYERS
		#Player 1
		if y_player < limitmin:
			y_player = limitmin
		if y_player > limitmax:
			y_player = limitmax

		#Player 2
		if y_player2 < limitmin:
			y_player2 = limitmin
		if y_player2 > limitmax:
			y_player2 = limitmax

		fenetre.blit(fondblack, (0,0))
		fenetre.blit(player, (775, y_player))
		fenetre.blit(player2, (15, y_player2))

		cord_balle_x += vecteur_balle_x
		cord_balle_y += vecteur_balle_y

		#Gain de point.
		if cord_balle_x > 780:
			print("Joueur 2 (gauche) --> Point Gagné !")
			score_player_2 += 1
			cord_balle_x = 400
			cord_balle_y = 300
			print(score_player_2, score_player)
		if cord_balle_x < 10:
			print("Joueur 1 (droite) --> Point Gagné !")
			score_player += 1
			cord_balle_x = 400
			cord_balle_y = 300
			print(score_player_2, score_player)

		#Collisions.
		if cord_balle_y >= 580:
			vecteur_balle_y = 0 - vecteur_balle_y
		if cord_balle_y <= 5:
			vecteur_balle_y = 0 - vecteur_balle_y
		if Rect((775, y_player), (7, 60)).colliderect(Rect((cord_balle_x, cord_balle_y), (15, 15))):
			vecteur_balle_x = 0 - vecteur_balle_x
			vecteur_balle_x -= 0.07
			print(vecteur_balle_x)
		if Rect((15, y_player2), (7, 60)).colliderect(Rect((cord_balle_x, cord_balle_y), (15, 15))):
			vecteur_balle_x = 0 - vecteur_balle_x
			print(vecteur_balle_x, vecteur_balle_y)

		score = str(score_player_2) + " : " + str(score_player)
		score_render = font.render(score, 1, (255, 255, 255))

		fenetre.blit(balle, (cord_balle_x, cord_balle_y))
		fenetre.blit(score_render, (325,25))

		if score_player_2 > 9:
			fenetre.blit(fondblack, (0,0))
			fenetre.blit(end, (200, 150))
			fenetre.blit(end_gagnant_joueur_1, (200, 350))
		elif score_player > 9:
			fenetre.blit(fondblack, (0,0))
			fenetre.blit(end, (200, 150))
			fenetre.blit(end_gagnant_joueur_2, (200, 350))

		display.flip()
