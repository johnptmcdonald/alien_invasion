import sys
import pygame

from Bullet import Bullet
from Alien import Alien

def check_keydown_events(event, ai_settings, screen, ship, bullets):
	"""respond to keydowns"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	if event.key == pygame.K_LEFT:
		ship.moving_left = True	
	if event.key == pygame.K_SPACE:
		fire_bullet(event, ai_settings, screen, ship, bullets)
	if event.key == pygame.K_q:
		sys.exit()

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

def update_screen(ai_settings, screen, ship, aliens, bullets):
	screen.fill(ai_settings.bg_color)
	
	for bullet in bullets.sprites():
		bullet.draw_bullet()

	ship.draw()

	# aliens is a group in pygame, so calling draw() on the group calls it for every member of the group
	aliens.draw(screen)

	# make most recently drawn screen visible
	pygame.display.flip()


def update_bullets(bullets):
	"""update all bullets and remove old bullets"""
	# calling update() on a group automatically calls update on each member of that group
	bullets.update()

	# remove bullets that have left screen
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

def fire_bullet(event, ai_settings, screen, ship, bullets):
	#create a new bullet and add it to the group
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)

def create_fleet(ai_settings, screen, aliens):
	"""create lots of aliens"""
	alien = Alien(ai_settings, screen)
	
	# maths for number and spacing of aliens
	alien_width = alien.rect.width
	available_space_x = ai_settings.screen_width - 2*alien_width
	number_aliens_x = int(available_space_x / (2*alien_width))

	for alien_number in range(number_aliens_x):
		# create an alien and put it in the row
		alien = Alien(ai_settings, screen)
		alien.x = alien_width + 2*alien_width*alien_number
		alien.rect.x = alien.x
		aliens.add(alien)




