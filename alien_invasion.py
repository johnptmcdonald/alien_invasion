import sys
import pygame
from pygame.sprite import Group

from Settings import Settings
from Ship import Ship
from Alien import Alien

import game_functions as gf

def run_game():
	# initialize game, create screen object
	pygame.init()
	ai_settings = Settings()

	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption(ai_settings.name)

	# make a ship
	ship = Ship(ai_settings, screen)

	# make an alien
	alien = Alien(ai_settings, screen)

	# make a group to store bullets in
	bullets = Group()
	aliens = Group()

	gf.create_fleet(ai_settings, screen, aliens)

	# start main game loop
	while True:
		# watch for keyboard and mouse events
		gf.check_events(ai_settings, screen, ship, bullets)
		
		ship.update()

		gf.update_bullets(bullets)

		gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()


