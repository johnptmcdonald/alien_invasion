class Settings():
	"""
	A class to store all settings
	"""

	def __init__(self):
		"""Initialize game settings """
		#screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230,230,230)
		self.name = "Alien Invasion"
		self.ship_speed_factor = 10.5

		# bullet settings
		self.bullet_speed_factor = 1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60,60,60)