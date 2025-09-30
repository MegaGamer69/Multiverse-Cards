# Module path: mcards.engine

import pygame

from .gameplay.core.units import Hero, Troop, Spell, Building
from .gameplay.core.cards import Card

from .gvars import *

from .gameplay.game_state import GameManager
from .gameplay.player import Player

class Engine:
	"""
	The main gameplay Engine.
	Contains every needed functions to handle stuffs.
	
	Fields:
	---------------------------------------------------------------------
	1. __cards (dict[str, Card]) - the card dictionary.
	2. __heroes (dict[str, Hero]) - the hero dictionary.
	2. __troops (dict[str, Troop]) - the troop dictionary.
	3. __spells (dict[str, Spell]) - the spell dictionary.
	4. __buildings (dict[str, Building]) - the building dictionary.
	----------------------------------------------------------------------
	"""
	def __init__(self):
		"""
		Initialize the Engine module.
		"""
		
		self.__cards: dict[str, Type[Card]] = {}
		self.__heroes: dict[str, Type[Hero]] = {}
		self.__troops: dict[str, Type[Troop]] = {}
		self.__spells: dict[str, Type[Spell]] = {}
		self.__buildings: dict[str, Type[Building]] = {}
		
	def register_card(self, name: str, card: Type[Card]):
		"""
		Register the card to the dictionary.
		"""
		
		self.__cards.update({name: card})
		
	def register_hero(self, name: str, hero: Type[Hero]):
		"""
		Register the spell to the dictionary.
		"""
		
		self.__heroes.update({name: hero})
	
	def register_troop(self, name: str, troop: Type[Troop]):
		"""
		Register the troop to the dictionary.
		"""
		
		self.__troops.update({name: troop})
	
	def register_spell(self, name: str, spell: Type[Spell]):
		"""
		Register the spell to the dictionary.
		"""
		
		self.__spells.update({name: spell})
	
	def register_building(self, name: str, building: Type[Building]):
		"""
		Register the building to the dictionary.
		"""
		
		self.__buildings.update({name: building})
	
	def initialize(self, mobile):
		"""
		Initializes the engine functions.
		"""
		
		pygame.init()
		
		player = Player()
		game_manager = GameManager(player)
		running = True
		clock = pygame.time.Clock()
		
		if mobile:
			# Fixed size if the OS is a Android or iOS system.
			
			WINDOW_SIZE = (720, 1280)
		
		window = pygame.display.set_mode(WINDOW_SIZE)
		
		while running:
			# Difines the delta time.
			
			delta_time = clock.tick(60)
			
			for e in pygame.event.get():
				# When the QUIT event is called:
				
				if e.type == pygame.QUIT:
					running = False
			
			window.fill(pygame.Color(255, 255, 255))
			game_manager.draw(window)
			
			pygame.display.flip()
		
		pygame.quit()

engine = Engine()
