import sys
import pygame

def run_game():
	# initialize game, create screen object
	pygame.init()
	screen = pygame.display.set_mode((1200,800))
	pygame.display.set_caption("Alien Invasion")

	# start main game loop
	while True:
		# watch for keyboard and mouse events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		# make most recently drawn screen visible
		pygame.display.flip()

run_game()


