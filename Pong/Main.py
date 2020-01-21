from math import *
from pygame import *
from Classique import *
import pygame

#Background - Load - Initialisation des fonds.

init()

fenetre = display.set_mode((800, 600), RESIZABLE)

fondBlack = image.load("fonds/fondblack.jpg").convert_alpha()
fondMenu = image.load("fonds/fondmenu.jpg").convert_alpha()
fondModes = image.load("fonds/fondmodes.jpg").convert_alpha()

#Global Functions - Fonctions globales.

def clearAll():
	"""
	Fonctions de déboggage, permet d'afficher un écran noir, utile pour savoir si il y a eu réponse ou non.
	Debugging function, displays a black screen. Can be used to detect user interaction in debug mode.
	"""
	fenetre.blit(fondBlack, (0,0))
	display.flip()

#States - États.

state = "menu"
stateOverride = "debug" #Seulement à des fins de déboggage. Only for debugging purposes.

""" 
All different states - Tous les états différents :
- "menu"
- "modes"
- "informations"
- "classique"
- "pouvoirs"
- stateOverride ----> "debug".
"""
class volume:

	def displayFunc():
		"""
		Affiche et lance les fonctions liées le bouton mute du jeu.
		Loads and displays functions linked to the mute button.
		"""
		#Display - Affichage

		volumeRect = image.load("mute.png").convert_alpha()
		fenetre.blit(volumeRect, (0, 0))
	def musicFunc():
		"""
		Active ou désactive toutes les fonctions liées au volume et aux sons du jeu.
		Mute on or off.
		"""
		musique_theme = pygame.mixer.music.load("musique.mp3")
		pygame.mixer.music.play(-1)

	def clickFunc():
		"""
		Joue le son lors d'un click.
		Plays a sound effect when object is clicked.
		"""
		click_sound_effect = pygame.mixer.music.load("click.mp3")
		pygame.mixer.music.play(0)


def menuFunc():
	"""
	Lance l'apparation et les fonctions globales du Menu.
	Run dislay and load mouse events.
	"""
	#Display - Affichage.
	fenetre.blit(fondMenu, (0,0))

	presentationRect = image.load("menu/presentation.jpg").convert_alpha()
	fenetre.blit(presentationRect, (200, 250))
	modesRect = image.load("menu/modes.jpg").convert_alpha()
	fenetre.blit(modesRect, (300, 50))
	informationsRect = image.load("menu/informations.jpg").convert_alpha()
	fenetre.blit(informationsRect, (300, 450))

	#User mouse events - Utilisation de la souris par l'utilisateur. -- onClickEvent.
	mouseCordsX, mouseCordsY = mouse.get_pos()
	if mouse.get_pressed()[0]:
		if 300 <= mouseCordsX <= 500:
			if 450 <= mouseCordsY <= 550:
				volume.clickFunc()
				print("Click informations | ! |")
				stateTransfer = "informations"
				return stateTransfer
			elif 50 <= mouseCordsY <= 150:
				volume.clickFunc()
				print("Click modes | ! |")
				stateTransfer = "modes"
				return stateTransfer

	display.flip()

def modesFunc():
	"""
	Lance l'apparition et les fonctions du menu de sélection des modes.
	Run display and load mouse events of the Modes menu.
	"""
	#Display - Affichage
	fenetre.blit(fondModes, (0,0))

	titleRect = image.load("modes/titre.jpg").convert_alpha()
	fenetre.blit(titleRect, (250, 20))
	classiqueRect = image.load("modes/classique.jpg").convert_alpha()
	fenetre.blit(classiqueRect, (250, 150))
	pouvoirsRect = image.load("modes/pouvoirs.jpg").convert_alpha()
	fenetre.blit(pouvoirsRect, (345, 300))
	retourRect = image.load("modes/retour.jpg").convert_alpha()
	fenetre.blit(retourRect, (250, 450))

	#User mouse events - Utilisation de la souris par l'utilisateur. -- onClickEvent.
	mouseCordsX, mouseCordsY = mouse.get_pos()
	if mouse.get_pressed()[0]:
		if 345 <= mouseCordsX <= 545:
			if 300 <= mouseCordsY <= 400:
				volume.clickFunc()
				print("Click pouvoirs | ! |")
				stateTransfer = "debug"
		if 250 <= mouseCordsX <= 450:
			if 150 <= mouseCordsY <= 250:
				volume.clickFunc()
				print("Click classique | ! |")
				stateTransfer = "classique"
				return stateTransfer
			elif 450 <= mouseCordsY <= 550:
				volume.clickFunc()
				print("Click retour | ! |")
				stateTransfer = "retour"
				return stateTransfer

	display.flip()

def nbplayersFunc():
	"""
	Lance l'apparition et les fonctions de la page de choix de joueurs.
	Run display and loads functions related to the players number.
	"""
	#Display - Affichage
	fenetre.blit(fondModes, (0,0))

	uniqueRect = image.load("players/unique.jpg").convert_alpha()
	fenetre.blit(uniqueRect, (270, 45))
	duoRect = image.load("players/duo.jpg").convert_alpha()
	fenetre.blit(duoRect, (385, 250))
	retourRect = image.load("modes/retour.jpg").convert_alpha()
	fenetre.blit(retourRect, (250, 450))

	#User mouse events - Utilisation de la souris par l'utilisateur. -- onClickEvent.
	mouseCordsX, mouseCordsY = mouse.get_pos()
	if mouse.get_pressed()[0]:
		if 270 <= mouseCordsX <= 470:
			if 45 <= mouseCordsY <= 145:
				volume.clickFunc()
				print("Click unique | ! |")
				stateTransfer = "unique"
				return stateTransfer
		if 385 <= mouseCordsX <= 585:
			if 250 <= mouseCordsY <= 350:
				volume.clickFunc()
				print("Click duo | ! |")
				stateOverride = "duo"
				return stateOverride
		if 250 <= mouseCordsX <= 450:
			if 450 <= mouseCordsY <= 550:
				volume.clickFunc()
				print("Click retour | ! |")
				stateTransfer = "retour"
				return stateTransfer
	
	display.flip()

def informationsFunc():
	"""
	Lance l'apparition et les fonctions de la page informations.
	Run display and loads informations's mouse events.
	""" 
	#Display - Affichage
	fenetre.blit(fondBlack, (0,0))

	presentationRect = image.load("informations/texte.jpg").convert_alpha()
	fenetre.blit(presentationRect,(0,0))
	titleRect = image.load("informations/titre.jpg").convert_alpha()
	fenetre.blit(titleRect, (250,25))
	retourRect  = image.load("informations/retour.jpg").convert_alpha()
	fenetre.blit(retourRect, (570, 475))

	#User mouse events - Utilisation de la souris par l'utilisateur. -- onClickEvent.
	mouseCordsX, mouseCordsY = mouse.get_pos()
	if mouse.get_pressed()[0]:
		if 570 < mouseCordsX < 770:
			if 475 < mouseCordsY < 575:
				volume.clickFunc()
				print("Click Retour | ! |")
				stateTransfer = "retour"
				return stateTransfer

	display.flip()

#Principal Loop - Boucle Principale.

running = True
musique = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			print("Merci d'avoir jouer ! Voici une blague : Que dit Higgs lors d'un concert ? Quel Boson !")
			quit()
			exit()

		if state ==  "menu":
			menuFunc()
			if menuFunc() == "modes":
				state = "modes"
			if menuFunc() == "informations":
				state = "informations"

		if state == "modes":
			modesFunc()
			if modesFunc() == "classique":
				state = "classique"
				if state == "classique":
					state = "players"
			elif modesFunc() == "pouvoirs":
				state = "pouvoirs"
				if state == "pouvoirs":
					state == "players"
			elif modesFunc() == "retour":
				state = "retour"
				if state == "retour":
					state = "menu"

		if state == "informations":
			informationsFunc()
			if informationsFunc() == "retour":
				state = "retour"
				if state == "retour":
					state = "menu"

		if state == "players":
			nbplayersFunc()
			if nbplayersFunc() == "unique":
				state = "start_unique"
				if state == "start_unique":
					unique()
			if nbplayersFunc() == "duo":
				state = "start_duo"
				if state == "start_duo":
					duo()
			elif nbplayersFunc() == "retour":
				state = "menu"