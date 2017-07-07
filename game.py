import pygame, sys, settings

from colours import *


class Game:

	def __init__(self):
		""" Initialise game window """
		pygame.init()
		pygame.mixer.init()
		self.window = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
		pygame.display.set_caption(settings.TITLE)
		self.clock = pygame.time.Clock()
		self.is_done = False

	def init_start_game(self):
		""" starts the initial game """
		self.show_start_screen()
		while not self.is_done:
			self.new_game()
			self.show_go_screen()

		self.close()

	def new_game(self):
		""" initialise the variables for a new game """
		self.all_sprites = pygame.sprite.Group()
		self.run()

	def run(self):
		""" Defines the overall game loop """

		while not self.is_done:
			""" PROCESSES / LOGIC """
			self.clock.tick(settings.FPS)

			""" EVENTS """
			self.events()

			""" UPDATES """
			self.update()

			""" DRAW/RENDER """
			self.draw()

	def events(self):
		""" process events in the game loop """
		# check for player inputs by polling for events
		for event in pygame.event.get():
			# check for the player closing the window (via the x button)
			if event.type == pygame.QUIT:
				# break out of the loop
				self.is_done = True

	def update(self):
		""" update the game loop """
		self.all_sprites.update()

	def draw(self):
		""" draw objects in the game loop """
		self.window.fill(Black)  # this is the same as window.fill(0, 0, 0)
		self.all_sprites.draw(self.window)

		pygame.display.flip()  # *AFTER* drawing everything, flip the display

	def show_start_screen(self):
		""" splash/start screen """
		pass

	def show_go_screen(self):
		""" game over screen """
		pass

	def close(self):
		""" shut everything down """
		pygame.quit()  # shut down pygame
		sys.exit()  # shut down the game

