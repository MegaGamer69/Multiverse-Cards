# Module path: mcards.gameplay.core.cards

import pygame

class Cards(pygame.sprite.Sprite):
	"""
	The base game in the game.
	Contains the basic system to summon units and some other stuffs.
	"""
	
	def __init__(self, key_id: str, name: str, level: int, rarity: str,
				cost: int, summons: list[str], blue_team: bool):
		"""
		Initialize the card system.
		"""
		
		super().__init__()
		
		self.__key_id = key_id
		self.__name = name
		self.__level = level
		self.__rarity = rarity
		self.__cost = cost
		self.__summons = summons
		self.__blue_team = blue_team
		
		self.__ready = False
		self.__selected = False
		
		self.__position = pygame.math.Vector2(0, 0)
	
	def update(self, user: Player):
		"""
		Updates the ard's sprite state.
		"""
		
		self.__ready = (user.get_elixir() >= self.__cost)
