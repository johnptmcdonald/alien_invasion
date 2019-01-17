import pygame

class Ship():
	
	def __init__(self, ai_settings, screen):
		"""initialize the ship and set the starting position"""
		self.screen = screen
		self.ai_settings = ai_settings
		print(self.ai_settings.ship_speed_factor)
		# load the ship image, yo it's down to get_rect()
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# start the ship at the bottom center
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		# store decimal value for ship's center
		# this indirection stops bug of ship moving left faster than right
		self.center = float(self.rect.centerx)

		# movement flags
		self.moving_right = False
		self.moving_left = False

	def update(self):
		"""update position based on movement flag"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor			

		self.rect.centerx = self.center

	def draw(self):
		"""draw the ship"""
		self.screen.blit(self.image, self.rect)




