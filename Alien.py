import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""A class to represent a single alien"""

	def __init__(self, ai_settings, screen):
		super().__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		# load the alien sprite and set its rect
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()
		
		# start at the top left
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# store the exact position
		self.x = float(self.rect.x)

	def draw(self):
		"""draw the alien at current location"""
		print('Drawing alien')
		self.screen.blit(self.image, self.rect)
