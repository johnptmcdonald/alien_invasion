import sys
import pygame

from Bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
	"""respond to keydowns"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	if event.key == pygame.K_LEFT:
		ship.moving_left = True	
	if event.key == pygame.K_SPACE:
		#create a new bullet and add it to the group
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)


def check_keyup_events(event, ai_settings, screen, ship, bullets):
	"""respond to keyups"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	if event.key == pygame.K_LEFT:
		ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
	# respond to key and mouse events
	for event in pygame.event.get():
		
		if event.type == pygame.QUIT:
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets)

		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ai_settings, screen, ship, bullets)

def update_screen(ai_settings, screen, ship, bullets):
	screen.fill(ai_settings.bg_color)
	
	for bullet in bullets.sprites():
		bullet.draw_bullet()

	ship.draw_ship()

	# make most recently drawn screen visible
	pygame.display.flip()